local t = require('test.testutil')
local n = require('test.functional.testnvim')()
local Screen = require('test.functional.ui.screen')

local tt = require('test.functional.testterm')
local feed_data = tt.feed_data
local feed_csi = tt.feed_csi
local feed, clear = n.feed, n.clear
local poke_eventloop = n.poke_eventloop
local command = n.command
local retry = t.retry
local eq = t.eq
local eval = n.eval
local skip = t.skip
local is_os = t.is_os

describe(':terminal window', function()
  before_each(clear)

  it('sets local values of window options #29325', function()
    command('setglobal wrap list')
    command('terminal')
    eq({ 0, 0, 1 }, eval('[&l:wrap, &wrap, &g:wrap]'))
    eq({ 0, 0, 1 }, eval('[&l:list, &list, &g:list]'))
    command('enew')
    eq({ 1, 1, 1 }, eval('[&l:wrap, &wrap, &g:wrap]'))
    eq({ 1, 1, 1 }, eval('[&l:list, &list, &g:list]'))
    command('buffer #')
    eq({ 0, 0, 1 }, eval('[&l:wrap, &wrap, &g:wrap]'))
    eq({ 0, 0, 1 }, eval('[&l:list, &list, &g:list]'))
    command('new')
    eq({ 1, 1, 1 }, eval('[&l:wrap, &wrap, &g:wrap]'))
    eq({ 1, 1, 1 }, eval('[&l:list, &list, &g:list]'))
  end)
end)

describe(':terminal window', function()
  local screen

  before_each(function()
    clear()
    screen = tt.setup_screen()
  end)

  it('sets topline correctly #8556', function()
    skip(is_os('win'))
    -- Test has hardcoded assumptions of dimensions.
    eq(7, eval('&lines'))
    feed_data('\n\n\n') -- Add blank lines.
    -- Terminal/shell contents must exceed the height of this window.
    command('topleft 1split')
    eq('terminal', eval('&buftype'))
    feed([[i<cr>]])
    -- Check topline _while_ in terminal-mode.
    retry(nil, nil, function()
      eq(6, eval('winsaveview()["topline"]'))
    end)
  end)

  describe("with 'number'", function()
    it('wraps text', function()
      feed([[<C-\><C-N>]])
      feed([[:set numberwidth=1 number<CR>i]])
      screen:expect([[
        {7:1 }tty ready                                       |
        {7:2 }rows: 6, cols: 48                               |
        {7:3 }^                                                |
        {7:4 }                                                |
        {7:5 }                                                |
        {7:6 }                                                |
        {3:-- TERMINAL --}                                    |
      ]])
      feed_data('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
      screen:expect([[
        {7:1 }tty ready                                       |
        {7:2 }rows: 6, cols: 48                               |
        {7:3 }abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV|
        {7:4 }WXYZ^                                            |
        {7:5 }                                                |
        {7:6 }                                                |
        {3:-- TERMINAL --}                                    |
      ]])

      -- numberwidth=9
      feed([[<C-\><C-N>]])
      feed([[:set numberwidth=9 number<CR>i]])
      screen:expect([[
        {7:       1 }tty ready                                |
        {7:       2 }rows: 6, cols: 48                        |
        {7:       3 }abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO|
        {7:       4 }PQRSTUVWXYZrows: 6, cols: 41             |
        {7:       5 }^                                         |
        {7:       6 }                                         |
        {3:-- TERMINAL --}                                    |
      ]])
      feed_data(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
      screen:expect([[
        {7:       1 }tty ready                                |
        {7:       2 }rows: 6, cols: 48                        |
        {7:       3 }abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO|
        {7:       4 }PQRSTUVWXYZrows: 6, cols: 41             |
        {7:       5 } abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN|
        {7:       6 }OPQRSTUVWXYZ^                             |
        {3:-- TERMINAL --}                                    |
      ]])
    end)
  end)

  describe("with 'statuscolumn'", function()
    it('wraps text', function()
      command([[set number statuscolumn=++%l\ \ ]])
      screen:expect([[
        {7:++1  }tty ready                                    |
        {7:++2  }rows: 6, cols: 45                            |
        {7:++3  }^                                             |
        {7:++4  }                                             |
        {7:++5  }                                             |
        {7:++6  }                                             |
        {3:-- TERMINAL --}                                    |
      ]])
      feed_data('\n\n\n\n\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
      screen:expect([[
        {7:++4  }                                             |
        {7:++5  }                                             |
        {7:++6  }                                             |
        {7:++7  }                                             |
        {7:++8  }abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS|
        {7:++9  }TUVWXYZ^                                      |
        {3:-- TERMINAL --}                                    |
      ]])
      feed_data('\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
      screen:expect([[
        {7:++ 7  }                                            |
        {7:++ 8  }abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR|
        {7:++ 9  }STUVWXYZ                                    |
        {7:++10  }abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR|
        {7:++11  }STUVWXYZrows: 6, cols: 44                   |
        {7:++12  }^                                            |
        {3:-- TERMINAL --}                                    |
      ]])
    end)
  end)

  describe("with 'colorcolumn'", function()
    before_each(function()
      feed([[<C-\><C-N>]])
      screen:expect([[
        tty ready                                         |
        ^                                                  |
                                                          |*5
      ]])
      feed(':set colorcolumn=20<CR>i')
    end)

    it('wont show the color column', function()
      screen:expect([[
        tty ready                                         |
        ^                                                  |
                                                          |*4
        {3:-- TERMINAL --}                                    |
      ]])
    end)
  end)

  describe('with fold set', function()
    before_each(function()
      feed([[<C-\><C-N>:set foldenable foldmethod=manual<CR>i]])
      feed_data({ 'line1', 'line2', 'line3', 'line4', '' })
      screen:expect([[
        tty ready                                         |
        line1                                             |
        line2                                             |
        line3                                             |
        line4                                             |
        ^                                                  |
        {3:-- TERMINAL --}                                    |
      ]])
    end)

    it('wont show any folds', function()
      feed([[<C-\><C-N>ggvGzf]])
      poke_eventloop()
      screen:expect([[
        ^tty ready                                         |
        line1                                             |
        line2                                             |
        line3                                             |
        line4                                             |
                                                          |
                                                          |
      ]])
    end)
  end)

  it('redrawn when restoring cursorline/column', function()
    screen:set_default_attr_ids({
      [1] = { bold = true },
      [2] = { foreground = 130 },
      [3] = { foreground = 130, underline = true },
      [12] = { underline = true },
      [19] = { background = 7 },
    })

    feed([[<C-\><C-N>]])
    command('setlocal cursorline')
    screen:expect([[
      tty ready                                         |
      {12:^                                                  }|
                                                        |*5
    ]])
    feed('i')
    screen:expect([[
      tty ready                                         |
      ^                                                  |
                                                        |*4
      {1:-- TERMINAL --}                                    |
    ]])
    feed([[<C-\><C-N>]])
    screen:expect([[
      tty ready                                         |
      {12:^                                                  }|
                                                        |*5
    ]])

    command('setlocal number')
    screen:expect([[
      {2:  1 }tty ready                                     |
      {3:  2 }{12:^rows: 6, cols: 46                             }|
      {2:  3 }                                              |
      {2:  4 }                                              |
      {2:  5 }                                              |
      {2:  6 }                                              |
                                                        |
    ]])
    feed('i')
    screen:expect([[
      {2:  1 }tty ready                                     |
      {2:  2 }rows: 6, cols: 46                             |
      {3:  3 }^                                              |
      {2:  4 }                                              |
      {2:  5 }                                              |
      {2:  6 }                                              |
      {1:-- TERMINAL --}                                    |
    ]])
    feed([[<C-\><C-N>]])
    screen:expect([[
      {2:  1 }tty ready                                     |
      {2:  2 }rows: 6, cols: 46                             |
      {3:  3 }{12:^                                              }|
      {2:  4 }                                              |
      {2:  5 }                                              |
      {2:  6 }                                              |
                                                        |
    ]])

    command('setlocal nonumber nocursorline cursorcolumn')
    screen:expect([[
      {19:t}ty ready                                         |
      {19:r}ows: 6, cols: 46                                 |
      ^rows: 6, cols: 50                                 |
      {19: }                                                 |*3
                                                        |
    ]])
    feed('i')
    screen:expect([[
      tty ready                                         |
      rows: 6, cols: 46                                 |
      rows: 6, cols: 50                                 |
      ^                                                  |
                                                        |*2
      {1:-- TERMINAL --}                                    |
    ]])
    feed([[<C-\><C-N>]])
    screen:expect([[
      {19:t}ty ready                                         |
      {19:r}ows: 6, cols: 46                                 |
      {19:r}ows: 6, cols: 50                                 |
      ^                                                  |
      {19: }                                                 |*2
                                                        |
    ]])
  end)

  it('redraws cursor info in terminal mode', function()
    skip(is_os('win'), '#31587')
    command('file AMOGUS | set laststatus=2 ruler')
    -- Expect column shown as "1" on an empty line, not "0-1" in terminal mode.
    screen:expect([[
      tty ready                                         |
      rows: 5, cols: 50                                 |
      ^                                                  |
                                                        |*2
      {17:AMOGUS                          3,1            All}|
      {3:-- TERMINAL --}                                    |
    ]])
    feed_data('you are the imposter')
    screen:expect([[
      tty ready                                         |
      rows: 5, cols: 50                                 |
      you are the imposter^                              |
                                                        |*2
      {17:AMOGUS                          3,21           All}|
      {3:-- TERMINAL --}                                    |
    ]])
    feed([[<C-\><C-N>]])
    screen:expect([[
      tty ready                                         |
      rows: 5, cols: 50                                 |
      you are the imposte^r                              |
                                                        |*2
      {17:AMOGUS                          3,20           All}|
                                                        |
    ]])

    feed_csi('2J') -- Clear screen
    feed_csi('1;1H') -- Cursor to 1,1
    command('set laststatus=3')
    feed('gg')
    screen:expect([[
      ^                                                  |
                                                        |*4
      {17:AMOGUS                          1,0-1          All}|
                                                        |
    ]])
    -- Check statuslines don't show "0-1" in terminal mode.
    feed('i')
    screen:expect([[
      ^                                                  |
                                                        |*4
      {17:AMOGUS                          1,1            All}|
      {3:-- TERMINAL --}                                    |
    ]])
    -- Custom statusline...
    command([[set statusline=byte:%c\ virt:%v\ virtdash:%V]])
    screen:expect([[
      ^                                                  |
                                                        |*4
      {17:byte:1 virt:1 virtdash:                           }|
      {3:-- TERMINAL --}                                    |
    ]])
    feed([[<C-\><C-N>]]) -- Back to normal mode
    screen:expect([[
      ^                                                  |
                                                        |*4
      {17:byte:0 virt:1 virtdash:-1                         }|
                                                        |
    ]])
  end)

  it('redraws stale statuslines and mode when not updating screen', function()
    command('file foo | set ruler | vsplit')
    screen:expect([[
      tty ready                │tty ready               |
      rows: 5, cols: 25        │rows: 5, cols: 25       |
      ^                         │                        |
                               │                        |*2
      {17:foo          3,1      All }{18:foo         2,1      Top}|
      {3:-- TERMINAL --}                                    |
    ]])
    command("call win_execute(win_getid(winnr('#')), 'call cursor(1, 1)')")
    screen:expect([[
      tty ready                │tty ready               |
      rows: 5, cols: 25        │rows: 5, cols: 25       |
      ^                         │                        |
                               │                        |*2
      {17:foo          3,1      All }{18:foo         1,1      All}|
      {3:-- TERMINAL --}                                    |
    ]])
    command('echo ""')
    screen:expect_unchanged()
  end)

  it('has correct topline if scrolled by events', function()
    skip(is_os('win'), '#31587')
    local lines = {}
    for i = 1, 10 do
      lines[#lines + 1] = 'cool line ' .. i
    end
    feed_data(lines)
    feed_csi('1;1H') -- Cursor to 1,1 (after any scrollback)

    -- :sleep (with leeway) until the refresh_terminal uv timer event triggers before we move the
    -- cursor. Check that the next terminal_check tails topline correctly.
    command('set ruler | sleep 20m | call nvim_win_set_cursor(0, [1, 0])')
    screen:expect([[
      ^cool line 5                                       |
      cool line 6                                       |
      cool line 7                                       |
      cool line 8                                       |
      cool line 9                                       |
      cool line 10                                      |
      {3:-- TERMINAL --}                  6,1           Bot |
    ]])
    command('call nvim_win_set_cursor(0, [1, 0])')
    screen:expect_unchanged()

    feed_csi('2;5H') -- Cursor to 2,5 (after any scrollback)
    screen:expect([[
      cool line 5                                       |
      cool^ line 6                                       |
      cool line 7                                       |
      cool line 8                                       |
      cool line 9                                       |
      cool line 10                                      |
      {3:-- TERMINAL --}                  7,5           Bot |
    ]])
    -- Check topline correct after leaving terminal mode.
    -- The new cursor position is one column left of the terminal's actual cursor position.
    command('stopinsert | call nvim_win_set_cursor(0, [1, 0])')
    screen:expect([[
      cool line 5                                       |
      coo^l line 6                                       |
      cool line 7                                       |
      cool line 8                                       |
      cool line 9                                       |
      cool line 10                                      |
                                      7,4           Bot |
    ]])
  end)

  it('in new tabpage has correct terminal size', function()
    screen:set_default_attr_ids({
      [1] = { reverse = true },
      [3] = { bold = true },
      [17] = { background = 2, foreground = Screen.colors.Grey0 },
      [18] = { background = 2, foreground = 8 },
      [19] = { underline = true, foreground = Screen.colors.Grey0, background = 7 },
      [20] = { underline = true, foreground = 5, background = 7 },
    })

    command('file foo | vsplit')
    screen:expect([[
      tty ready                │tty ready               |
      rows: 5, cols: 25        │rows: 5, cols: 25       |
      ^                         │                        |
                               │                        |*2
      {17:foo                       }{18:foo                     }|
      {3:-- TERMINAL --}                                    |
    ]])
    command('tab split')
    screen:expect([[
      {19: }{20:2}{19: foo }{3: foo }{1:                                     }{19:X}|
      tty ready                                         |
      rows: 5, cols: 25                                 |
      rows: 5, cols: 50                                 |
      ^                                                  |
                                                        |
      {3:-- TERMINAL --}                                    |
    ]])
  end)

  it('restores window options when switching terminals', function()
    -- Make this a screen test to also check for proper redrawing.
    screen:set_default_attr_ids({
      [1] = { bold = true },
      [2] = { foreground = Screen.colors.Gray0, background = 7, underline = true },
      [3] = { foreground = 5, background = 7, underline = true },
      [4] = { reverse = true },
      [5] = { bold = true, foreground = 5 },
      [12] = { underline = true },
      [17] = { foreground = Screen.colors.Gray0, background = 2 },
      [18] = { foreground = 8, background = 2 },
      [19] = { background = 7 },
    })

    feed([[<C-\><C-N>]])
    command([[
      file foo
      setlocal cursorline
      vsplit
      setlocal nocursorline cursorcolumn
    ]])
    screen:expect([[
      {19:t}ty ready                │tty ready               |
      ^rows: 5, cols: 25        │{12:rows: 5, cols: 25       }|
      {19: }                        │                        |*3
      {17:foo                       }{18:foo                     }|
                                                        |
    ]])

    feed('i')
    screen:expect([[
      tty ready                │tty ready               |
      rows: 5, cols: 25        │{12:rows: 5, cols: 25       }|
      ^                         │                        |
                               │                        |*2
      {17:foo                       }{18:foo                     }|
      {1:-- TERMINAL --}                                    |
    ]])
    command('wincmd p')
    screen:expect([[
      {19:t}ty ready                │tty ready               |
      {19:r}ows: 5, cols: 25        │rows: 5, cols: 25       |
                               │^                        |
      {19: }                        │                        |*2
      {18:foo                       }{17:foo                     }|
      {1:-- TERMINAL --}                                    |
    ]])
    feed([[<C-\><C-N>]])
    screen:expect([[
      {19:t}ty ready                │tty ready               |
      {19:r}ows: 5, cols: 25        │rows: 5, cols: 25       |
                               │{12:^                        }|
      {19: }                        │                        |*2
      {18:foo                       }{17:foo                     }|
                                                        |
    ]])

    -- Ensure things work when switching tabpages.
    command('tab split | setlocal cursorline cursorcolumn')
    screen:expect([[
      {2: }{3:2}{2: foo }{1: foo }{4:                                     }{2:X}|
      {19:t}ty ready                                         |
      {19:r}ows: 5, cols: 25                                 |
      {12:^rows: 5, cols: 50                                 }|
      {19: }                                                 |*2
                                                        |
    ]])
    feed('i')
    screen:expect([[
      {2: }{3:2}{2: foo }{1: foo }{4:                                     }{2:X}|
      tty ready                                         |
      rows: 5, cols: 25                                 |
      rows: 5, cols: 50                                 |
      ^                                                  |
                                                        |
      {1:-- TERMINAL --}                                    |
    ]])
    command('tabprevious')
    screen:expect([[
      {1: }{5:2}{1: foo }{2: foo }{4:                                     }{2:X}|
      {19:r}ows: 5, cols: 25        │rows: 5, cols: 25       |
      rows: 5, cols: 50        │rows: 5, cols: 50       |
      {19: }                        │^                        |
      {19: }                        │                        |
      {18:foo                       }{17:foo                     }|
      {1:-- TERMINAL --}                                    |
    ]])
    feed([[<C-\><C-N>]])
    screen:expect([[
      {1: }{5:2}{1: foo }{2: foo }{4:                                     }{2:X}|
      {19:r}ows: 5, cols: 25        │rows: 5, cols: 25       |
      rows: 5, cols: 50        │rows: 5, cols: 50       |
      {19: }                        │{12:                        }|
      {19: }                        │^                        |
      {18:foo                       }{17:foo                     }|
                                                        |
    ]])
    command('tabnext')
    screen:expect([[
      {2: }{3:2}{2: foo }{1: foo }{4:                                     }{2:X}|
      {19:t}ty ready                                         |
      {19:r}ows: 5, cols: 25                                 |
      {19:r}ows: 5, cols: 50                                 |
      {12:^                                                  }|
      {19: }                                                 |
                                                        |
    ]])

    -- Closing windows shouldn't break things.
    command('tabprevious')
    feed('i')
    screen:expect([[
      {1: }{5:2}{1: foo }{2: foo }{4:                                     }{2:X}|
      {19:r}ows: 5, cols: 25        │rows: 5, cols: 25       |
      rows: 5, cols: 50        │rows: 5, cols: 50       |
      {19: }                        │                        |
      {19: }                        │^                        |
      {18:foo                       }{17:foo                     }|
      {1:-- TERMINAL --}                                    |
    ]])
    command('quit')
    screen:expect([[
      {1: foo }{2: foo }{4:                                       }{2:X}|
      tty ready                                         |
      rows: 5, cols: 25                                 |
      rows: 5, cols: 50                                 |
      ^                                                  |
                                                        |
      {1:-- TERMINAL --}                                    |
    ]])
    feed([[<C-\><C-N>]])
    screen:expect([[
      {1: foo }{2: foo }{4:                                       }{2:X}|
      {19:t}ty ready                                         |
      {19:r}ows: 5, cols: 25                                 |
      {19:r}ows: 5, cols: 50                                 |
      ^                                                  |
      {19: }                                                 |
                                                        |
    ]])
  end)
end)

describe(':terminal with multigrid', function()
  local screen

  before_each(function()
    clear()
    screen = tt.setup_screen(0, nil, 50, nil, { ext_multigrid = true })
  end)

  it('resizes to requested size', function()
    screen:expect([[
    ## grid 1
      [2:--------------------------------------------------]|*6
      [3:--------------------------------------------------]|
    ## grid 2
      tty ready                                         |
      ^                                                  |
                                                        |*4
    ## grid 3
      {3:-- TERMINAL --}                                    |
    ]])

    screen:try_resize_grid(2, 20, 10)
    if is_os('win') then
      screen:expect { any = 'rows: 10, cols: 20' }
    else
      screen:expect([[
      ## grid 1
        [2:--------------------------------------------------]|*6
        [3:--------------------------------------------------]|
      ## grid 2
        tty ready           |
        rows: 10, cols: 20  |
        ^                    |
                            |*7
      ## grid 3
        {3:-- TERMINAL --}                                    |
      ]])
    end

    screen:try_resize_grid(2, 70, 3)
    if is_os('win') then
      screen:expect { any = 'rows: 3, cols: 70' }
    else
      screen:expect([[
      ## grid 1
        [2:--------------------------------------------------]|*6
        [3:--------------------------------------------------]|
      ## grid 2
        rows: 10, cols: 20                                                    |
        rows: 3, cols: 70                                                     |
        ^                                                                      |
      ## grid 3
        {3:-- TERMINAL --}                                    |
      ]])
    end

    screen:try_resize_grid(2, 0, 0)
    if is_os('win') then
      screen:expect { any = 'rows: 6, cols: 50' }
    else
      screen:expect([[
      ## grid 1
        [2:--------------------------------------------------]|*6
        [3:--------------------------------------------------]|
      ## grid 2
        tty ready                                         |
        rows: 10, cols: 20                                |
        rows: 3, cols: 70                                 |
        rows: 6, cols: 50                                 |
        ^                                                  |
                                                          |
      ## grid 3
        {3:-- TERMINAL --}                                    |
      ]])
    end
  end)
end)
