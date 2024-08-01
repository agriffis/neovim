" Name:         darkblue
" Description:  For those who prefer dark background
" Author:       Original author Bohdan Vlasyuk <bohdan@vstu.edu.ua>
" Maintainer:   Original author Bohdan Vlasyuk <bohdan@vstu.edu.ua>
" Website:      https://github.com/vim/colorschemes
" License:      Same as Vim
" Last Updated: Wed 10 Jul 2024 17:25:49

" Generated by Colortemplate v2.2.3

set background=dark

" hi clear
source $VIMRUNTIME/colors/vim.lua " Nvim: revert to Vim default color scheme
let g:colors_name = 'darkblue'

let s:t_Co = &t_Co

if (has('termguicolors') && &termguicolors) || has('gui_running')
  let g:terminal_ansi_colors = ['#000000', '#8b0000', '#90f020', '#ffa500', '#00008b', '#8b008b', '#008b8b', '#c0c0c0', '#808080', '#ffa0a0', '#90f020', '#ffff60', '#0030ff', '#ff00ff', '#90fff0', '#ffffff']
  " Nvim uses g:terminal_color_{0-15} instead
  for i in range(g:terminal_ansi_colors->len())
    let g:terminal_color_{i} = g:terminal_ansi_colors[i]
  endfor
endif
hi! link Terminal Normal
hi! link CursorColumn CursorLine
hi! link CursorIM Cursor
hi! link EndOfBuffer NonText
hi! link ErrorMsg Error
hi! link LineNrAbove LineNr
hi! link LineNrBelow LineNr
hi! link StatusLineTerm StatusLine
hi! link StatusLineTermNC StatusLineNC
hi! link CursorLineFold CursorLine
hi! link CursorLineSign CursorLine
hi! link TabLineFill TabLine
hi! link Boolean Constant
hi! link Character Constant
hi! link Conditional Statement
hi! link Define PreProc
hi! link Delimiter Special
hi! link Exception Statement
hi! link Float Constant
hi! link Function Identifier
hi! link Include PreProc
hi! link Keyword Statement
hi! link Label Statement
hi! link Macro PreProc
hi! link Number Constant
hi! link Operator Statement
hi! link PreCondit PreProc
hi! link Repeat Statement
hi! link SpecialChar Special
hi! link SpecialComment Special
hi! link StorageClass Type
hi! link String Constant
hi! link Structure Type
hi! link Tag Special
hi! link Typedef Type
hi! link Debug Special
hi! link Added String
hi! link Removed WarningMsg
hi! link diffOnly WarningMsg
hi! link diffNoEOL WarningMsg
hi! link diffIsA WarningMsg
hi! link diffIdentical WarningMsg
hi! link diffDiffer WarningMsg
hi! link diffCommon WarningMsg
hi! link diffBDiffer WarningMsg
hi! link lCursor Cursor
hi! link CurSearch Search
hi! link MessageWindow Pmenu
hi! link PopupNotification Todo
hi Normal guifg=#c0c0c0 guibg=#000040 gui=NONE cterm=NONE
hi Conceal guifg=#008b8b guibg=NONE gui=NONE cterm=NONE
hi ColorColumn guifg=#c0c0c0 guibg=#8b0000 gui=NONE cterm=NONE
hi Cursor guifg=#000000 guibg=#ffff60 gui=NONE cterm=NONE
hi QuickFixLine guifg=#000000 guibg=#ff80ff gui=NONE cterm=NONE
hi Error guifg=#ffa0a0 guibg=NONE gui=reverse cterm=reverse
hi FoldColumn guifg=#808080 guibg=NONE gui=bold cterm=NONE
hi Folded guifg=#808080 guibg=NONE gui=bold cterm=NONE
hi IncSearch guifg=#ffffff guibg=#0030ff gui=reverse cterm=reverse
hi LineNr guifg=#90f020 guibg=NONE gui=NONE cterm=NONE
hi MatchParen guifg=NONE guibg=NONE gui=reverse ctermfg=NONE ctermbg=NONE cterm=reverse
hi ModeMsg guifg=#90fff0 guibg=NONE gui=NONE cterm=NONE
hi MoreMsg guifg=#006400 guibg=NONE gui=NONE cterm=NONE
hi NonText guifg=#0030ff guibg=NONE gui=NONE cterm=NONE
hi Pmenu guifg=#ffffff guibg=#0030ff gui=NONE cterm=NONE
hi PmenuSbar guifg=NONE guibg=NONE gui=NONE ctermfg=NONE ctermbg=NONE cterm=NONE
hi PmenuSel guifg=#0030ff guibg=#ffffff gui=NONE cterm=NONE
hi PmenuThumb guifg=NONE guibg=#ffffff gui=NONE cterm=NONE
hi PmenuMatch guifg=#ff80ff guibg=#0030ff gui=NONE cterm=NONE
hi PmenuMatchSel guifg=#ff00ff guibg=#ffffff gui=NONE cterm=NONE
hi Question guifg=#90f020 guibg=NONE gui=NONE cterm=NONE
hi SignColumn guifg=#808080 guibg=NONE gui=NONE cterm=NONE
hi SpecialKey guifg=#008b8b guibg=NONE gui=NONE cterm=NONE
hi SpellBad guifg=#ff0000 guibg=NONE guisp=#ff0000 gui=undercurl cterm=underline
hi SpellCap guifg=#90f020 guibg=NONE guisp=#90f020 gui=undercurl cterm=underline
hi SpellLocal guifg=#90fff0 guibg=NONE guisp=#90fff0 gui=undercurl cterm=underline
hi SpellRare guifg=#ff00ff guibg=NONE guisp=#ff00ff gui=undercurl cterm=underline
hi StatusLine guifg=#000040 guibg=#c0c0c0 gui=NONE cterm=NONE
hi StatusLineNC guifg=#000000 guibg=#808080 gui=NONE cterm=NONE
hi TabLine guifg=#000000 guibg=#808080 gui=NONE cterm=NONE
hi ToolbarButton guifg=#ffffff guibg=#0030ff gui=NONE cterm=NONE
hi ToolbarLine guifg=NONE guibg=NONE gui=NONE ctermfg=NONE ctermbg=NONE cterm=NONE
hi VertSplit guifg=#000000 guibg=#808080 gui=NONE cterm=NONE
hi Visual guifg=#8080ff guibg=#ffffff gui=reverse cterm=reverse
hi VisualNOS guifg=#8080ff guibg=#c0c0c0 gui=reverse,underline cterm=reverse,underline
hi WarningMsg guifg=#ff0000 guibg=NONE gui=NONE cterm=NONE
hi WildMenu guifg=#ffff60 guibg=#000000 gui=NONE cterm=NONE
hi debugBreakpoint guifg=#90f020 guibg=#00008b gui=reverse cterm=reverse
hi debugPC guifg=#90fff0 guibg=#00008b gui=reverse cterm=reverse
hi Directory guifg=#008b8b guibg=NONE gui=NONE cterm=NONE
hi Title guifg=#ff00ff guibg=NONE gui=NONE cterm=NONE
hi Comment guifg=#80a0ff guibg=NONE gui=NONE cterm=NONE
hi Constant guifg=#ffa0a0 guibg=NONE gui=NONE cterm=NONE
hi Identifier guifg=#90fff0 guibg=NONE gui=NONE cterm=NONE
hi Ignore guifg=#000040 guibg=#c0c0c0 gui=NONE cterm=NONE
hi PreProc guifg=#ff80ff guibg=NONE gui=NONE cterm=NONE
hi Special guifg=#ffa500 guibg=NONE gui=NONE cterm=NONE
hi Statement guifg=#ffff60 guibg=NONE gui=NONE cterm=NONE
hi Todo guifg=NONE guibg=NONE gui=reverse ctermfg=NONE ctermbg=NONE cterm=reverse
hi Type guifg=#90f020 guibg=NONE gui=NONE cterm=NONE
hi Underlined guifg=#80a0ff guibg=NONE gui=underline cterm=underline
hi TabLineSel guifg=#000040 guibg=#c0c0c0 gui=NONE cterm=NONE
hi CursorLine guifg=NONE guibg=#666666 gui=NONE cterm=NONE
hi CursorLineNr guifg=#ffff60 guibg=#666666 gui=NONE cterm=NONE
hi Search guifg=#90fff0 guibg=#0030ff gui=NONE cterm=NONE
hi DiffAdd guifg=#ffffff guibg=#5f875f gui=NONE cterm=NONE
hi DiffChange guifg=#ffffff guibg=#5f87af gui=NONE cterm=NONE
hi DiffText guifg=#000000 guibg=#c6c6c6 gui=NONE cterm=NONE
hi DiffDelete guifg=#ffffff guibg=#af5faf gui=NONE cterm=NONE

if s:t_Co >= 256
  hi! link Terminal Normal
  hi! link CursorColumn CursorLine
  hi! link CursorIM Cursor
  hi! link EndOfBuffer NonText
  hi! link ErrorMsg Error
  hi! link LineNrAbove LineNr
  hi! link LineNrBelow LineNr
  hi! link StatusLineTerm StatusLine
  hi! link StatusLineTermNC StatusLineNC
  hi! link CursorLineFold CursorLine
  hi! link CursorLineSign CursorLine
  hi! link TabLineFill TabLine
  hi! link Boolean Constant
  hi! link Character Constant
  hi! link Conditional Statement
  hi! link Define PreProc
  hi! link Delimiter Special
  hi! link Exception Statement
  hi! link Float Constant
  hi! link Function Identifier
  hi! link Include PreProc
  hi! link Keyword Statement
  hi! link Label Statement
  hi! link Macro PreProc
  hi! link Number Constant
  hi! link Operator Statement
  hi! link PreCondit PreProc
  hi! link Repeat Statement
  hi! link SpecialChar Special
  hi! link SpecialComment Special
  hi! link StorageClass Type
  hi! link String Constant
  hi! link Structure Type
  hi! link Tag Special
  hi! link Typedef Type
  hi! link Debug Special
  hi! link Added String
  hi! link Removed WarningMsg
  hi! link diffOnly WarningMsg
  hi! link diffNoEOL WarningMsg
  hi! link diffIsA WarningMsg
  hi! link diffIdentical WarningMsg
  hi! link diffDiffer WarningMsg
  hi! link diffCommon WarningMsg
  hi! link diffBDiffer WarningMsg
  hi! link lCursor Cursor
  hi! link CurSearch Search
  hi! link MessageWindow Pmenu
  hi! link PopupNotification Todo
  hi Normal ctermfg=252 ctermbg=17 cterm=NONE
  hi Conceal ctermfg=30 ctermbg=NONE cterm=NONE
  hi ColorColumn ctermfg=252 ctermbg=88 cterm=NONE
  hi Cursor ctermfg=16 ctermbg=227 cterm=NONE
  hi QuickFixLine ctermfg=16 ctermbg=213 cterm=NONE
  hi Error ctermfg=217 ctermbg=NONE cterm=reverse
  hi FoldColumn ctermfg=102 ctermbg=NONE cterm=NONE
  hi Folded ctermfg=102 ctermbg=NONE cterm=NONE
  hi IncSearch ctermfg=231 ctermbg=27 cterm=reverse
  hi LineNr ctermfg=118 ctermbg=NONE cterm=NONE
  hi MatchParen ctermfg=NONE ctermbg=NONE cterm=reverse
  hi ModeMsg ctermfg=123 ctermbg=NONE cterm=NONE
  hi MoreMsg ctermfg=22 ctermbg=NONE cterm=NONE
  hi NonText ctermfg=27 ctermbg=NONE cterm=NONE
  hi Pmenu ctermfg=231 ctermbg=27 cterm=NONE
  hi PmenuSbar ctermfg=NONE ctermbg=NONE cterm=NONE
  hi PmenuSel ctermfg=27 ctermbg=231 cterm=NONE
  hi PmenuThumb ctermfg=NONE ctermbg=231 cterm=NONE
  hi PmenuMatch ctermfg=213 ctermbg=27 cterm=NONE
  hi PmenuMatchSel ctermfg=201 ctermbg=231 cterm=NONE
  hi Question ctermfg=118 ctermbg=NONE cterm=NONE
  hi SignColumn ctermfg=102 ctermbg=NONE cterm=NONE
  hi SpecialKey ctermfg=30 ctermbg=NONE cterm=NONE
  hi SpellBad ctermfg=196 ctermbg=NONE cterm=underline
  hi SpellCap ctermfg=118 ctermbg=NONE cterm=underline
  hi SpellLocal ctermfg=123 ctermbg=NONE cterm=underline
  hi SpellRare ctermfg=201 ctermbg=NONE cterm=underline
  hi StatusLine ctermfg=17 ctermbg=252 cterm=NONE
  hi StatusLineNC ctermfg=16 ctermbg=102 cterm=NONE
  hi TabLine ctermfg=16 ctermbg=102 cterm=NONE
  hi ToolbarButton ctermfg=231 ctermbg=27 cterm=NONE
  hi ToolbarLine ctermfg=NONE ctermbg=NONE cterm=NONE
  hi VertSplit ctermfg=16 ctermbg=102 cterm=NONE
  hi Visual ctermfg=105 ctermbg=231 cterm=reverse
  hi VisualNOS ctermfg=105 ctermbg=252 cterm=reverse,underline
  hi WarningMsg ctermfg=196 ctermbg=NONE cterm=NONE
  hi WildMenu ctermfg=227 ctermbg=16 cterm=NONE
  hi debugBreakpoint ctermfg=118 ctermbg=18 cterm=reverse
  hi debugPC ctermfg=123 ctermbg=18 cterm=reverse
  hi Directory ctermfg=30 ctermbg=NONE cterm=NONE
  hi Title ctermfg=201 ctermbg=NONE cterm=NONE
  hi Comment ctermfg=111 ctermbg=NONE cterm=NONE
  hi Constant ctermfg=217 ctermbg=NONE cterm=NONE
  hi Identifier ctermfg=123 ctermbg=NONE cterm=NONE
  hi Ignore ctermfg=17 ctermbg=252 cterm=NONE
  hi PreProc ctermfg=213 ctermbg=NONE cterm=NONE
  hi Special ctermfg=214 ctermbg=NONE cterm=NONE
  hi Statement ctermfg=227 ctermbg=NONE cterm=NONE
  hi Todo ctermfg=NONE ctermbg=NONE cterm=reverse
  hi Type ctermfg=118 ctermbg=NONE cterm=NONE
  hi Underlined ctermfg=111 ctermbg=NONE cterm=underline
  hi TabLineSel ctermfg=17 ctermbg=252 cterm=NONE
  hi CursorLine ctermfg=NONE ctermbg=59 cterm=NONE
  hi CursorLineNr ctermfg=227 ctermbg=59 cterm=NONE
  hi Search ctermfg=123 ctermbg=27 cterm=NONE
  hi DiffAdd ctermfg=231 ctermbg=65 cterm=NONE
  hi DiffChange ctermfg=231 ctermbg=67 cterm=NONE
  hi DiffText ctermfg=16 ctermbg=251 cterm=NONE
  hi DiffDelete ctermfg=231 ctermbg=133 cterm=NONE
  unlet s:t_Co
  finish
endif

if s:t_Co >= 16
  hi Normal ctermfg=grey ctermbg=black cterm=NONE
  hi Conceal ctermfg=darkcyan ctermbg=NONE cterm=NONE
  hi ColorColumn ctermfg=grey ctermbg=darkred cterm=NONE
  hi Cursor ctermfg=black ctermbg=yellow cterm=NONE
  hi QuickFixLine ctermfg=black ctermbg=magenta cterm=NONE
  hi Error ctermfg=red ctermbg=NONE cterm=reverse
  hi FoldColumn ctermfg=darkgrey ctermbg=NONE cterm=NONE
  hi Folded ctermfg=darkgrey ctermbg=NONE cterm=NONE
  hi IncSearch ctermfg=white ctermbg=blue cterm=reverse
  hi LineNr ctermfg=green ctermbg=NONE cterm=NONE
  hi MatchParen ctermfg=NONE ctermbg=NONE cterm=reverse
  hi ModeMsg ctermfg=cyan ctermbg=NONE cterm=NONE
  hi MoreMsg ctermfg=darkgreen ctermbg=NONE cterm=NONE
  hi NonText ctermfg=blue ctermbg=NONE cterm=NONE
  hi Pmenu ctermfg=white ctermbg=blue cterm=NONE
  hi PmenuSbar ctermfg=NONE ctermbg=NONE cterm=NONE
  hi PmenuSel ctermfg=blue ctermbg=white cterm=NONE
  hi PmenuThumb ctermfg=NONE ctermbg=white cterm=NONE
  hi PmenuMatch ctermfg=magenta ctermbg=blue cterm=NONE
  hi PmenuMatchSel ctermfg=darkmagenta ctermbg=white cterm=NONE
  hi Question ctermfg=green ctermbg=NONE cterm=NONE
  hi SignColumn ctermfg=darkgrey ctermbg=NONE cterm=NONE
  hi SpecialKey ctermfg=darkcyan ctermbg=NONE cterm=NONE
  hi SpellBad ctermfg=red ctermbg=NONE cterm=underline
  hi SpellCap ctermfg=green ctermbg=NONE cterm=underline
  hi SpellLocal ctermfg=cyan ctermbg=NONE cterm=underline
  hi SpellRare ctermfg=darkmagenta ctermbg=NONE cterm=underline
  hi StatusLine ctermfg=black ctermbg=grey cterm=NONE
  hi StatusLineNC ctermfg=black ctermbg=darkgrey cterm=NONE
  hi TabLine ctermfg=black ctermbg=darkgrey cterm=NONE
  hi ToolbarButton ctermfg=white ctermbg=blue cterm=NONE
  hi ToolbarLine ctermfg=NONE ctermbg=NONE cterm=NONE
  hi VertSplit ctermfg=black ctermbg=darkgrey cterm=NONE
  hi Visual ctermfg=blue ctermbg=white cterm=reverse
  hi VisualNOS ctermfg=blue ctermbg=grey cterm=reverse,underline
  hi WarningMsg ctermfg=red ctermbg=NONE cterm=NONE
  hi WildMenu ctermfg=yellow ctermbg=black cterm=NONE
  hi debugBreakpoint ctermfg=green ctermbg=darkblue cterm=reverse
  hi debugPC ctermfg=cyan ctermbg=darkblue cterm=reverse
  hi Directory ctermfg=darkcyan ctermbg=NONE cterm=NONE
  hi Title ctermfg=darkmagenta ctermbg=NONE cterm=NONE
  hi Comment ctermfg=blue ctermbg=NONE cterm=NONE
  hi Constant ctermfg=red ctermbg=NONE cterm=NONE
  hi Identifier ctermfg=cyan ctermbg=NONE cterm=NONE
  hi Ignore ctermfg=black ctermbg=grey cterm=NONE
  hi PreProc ctermfg=magenta ctermbg=NONE cterm=NONE
  hi Special ctermfg=darkyellow ctermbg=NONE cterm=NONE
  hi Statement ctermfg=yellow ctermbg=NONE cterm=NONE
  hi Todo ctermfg=NONE ctermbg=NONE cterm=reverse
  hi Type ctermfg=green ctermbg=NONE cterm=NONE
  hi Underlined ctermfg=blue ctermbg=NONE cterm=underline
  hi TabLineSel ctermfg=white ctermbg=black cterm=NONE
  hi CursorLine ctermfg=NONE ctermbg=NONE cterm=underline
  hi CursorLineNr ctermfg=yellow ctermbg=NONE cterm=underline
  hi Search ctermfg=white ctermbg=blue cterm=NONE
  hi DiffAdd ctermfg=white ctermbg=darkgreen cterm=NONE
  hi DiffChange ctermfg=white ctermbg=blue cterm=NONE
  hi DiffText ctermfg=black ctermbg=grey cterm=NONE
  hi DiffDelete ctermfg=white ctermbg=magenta cterm=NONE
  unlet s:t_Co
  finish
endif

if s:t_Co >= 8
  hi Normal ctermfg=grey ctermbg=black cterm=NONE
  hi Conceal ctermfg=NONE ctermbg=NONE cterm=NONE
  hi ColorColumn ctermfg=grey ctermbg=darkred cterm=NONE
  hi CursorLine ctermfg=NONE ctermbg=NONE cterm=underline
  hi CursorLineNr ctermfg=darkyellow ctermbg=NONE cterm=bold
  hi QuickFixLine ctermfg=grey ctermbg=darkmagenta cterm=NONE
  hi Error ctermfg=darkred ctermbg=grey cterm=reverse
  hi FoldColumn ctermfg=NONE ctermbg=NONE cterm=NONE
  hi Folded ctermfg=darkblue ctermbg=NONE cterm=bold,reverse
  hi IncSearch ctermfg=grey ctermbg=darkblue cterm=reverse
  hi LineNr ctermfg=green ctermbg=NONE cterm=bold
  hi MatchParen ctermfg=NONE ctermbg=NONE cterm=reverse
  hi ModeMsg ctermfg=darkcyan ctermbg=NONE cterm=NONE
  hi MoreMsg ctermfg=darkgreen ctermbg=NONE cterm=NONE
  hi NonText ctermfg=blue ctermbg=NONE cterm=NONE
  hi Pmenu ctermfg=grey ctermbg=blue cterm=NONE
  hi PmenuSbar ctermfg=NONE ctermbg=NONE cterm=NONE
  hi PmenuSel ctermfg=blue ctermbg=grey cterm=NONE
  hi PmenuThumb ctermfg=NONE ctermbg=grey cterm=NONE
  hi Question ctermfg=darkgreen ctermbg=NONE cterm=bold
  hi Search ctermfg=darkcyan ctermbg=blue cterm=NONE
  hi SignColumn ctermfg=grey ctermbg=NONE cterm=NONE
  hi SpecialKey ctermfg=darkcyan ctermbg=NONE cterm=NONE
  hi SpellBad ctermfg=darkred ctermbg=darkyellow cterm=reverse
  hi SpellCap ctermfg=darkgreen ctermbg=NONE cterm=reverse
  hi SpellLocal ctermfg=darkcyan ctermbg=NONE cterm=reverse
  hi SpellRare ctermfg=darkmagenta ctermbg=darkyellow cterm=reverse
  hi StatusLine ctermfg=darkblue ctermbg=grey cterm=bold,reverse
  hi StatusLineNC ctermfg=grey ctermbg=black cterm=reverse
  hi VertSplit ctermfg=grey ctermbg=black cterm=reverse
  hi TabLine ctermfg=grey ctermbg=black cterm=reverse
  hi TabLineSel ctermfg=darkblue ctermbg=grey cterm=bold,reverse
  hi ToolbarButton ctermfg=darkblue ctermbg=grey cterm=bold,reverse
  hi ToolbarLine ctermfg=NONE ctermbg=NONE cterm=NONE
  hi Visual ctermfg=blue ctermbg=grey cterm=reverse
  hi VisualNOS ctermfg=blue ctermbg=grey cterm=reverse,underline
  hi WarningMsg ctermfg=darkred ctermbg=NONE cterm=NONE
  hi WildMenu ctermfg=yellow ctermbg=black cterm=NONE
  hi debugBreakpoint ctermfg=darkgreen ctermbg=darkblue cterm=reverse
  hi debugPC ctermfg=darkcyan ctermbg=darkblue cterm=reverse
  hi Directory ctermfg=darkcyan ctermbg=NONE cterm=NONE
  hi Title ctermfg=darkmagenta ctermbg=NONE cterm=NONE
  hi Comment ctermfg=darkblue ctermbg=NONE cterm=bold
  hi Constant ctermfg=darkred ctermbg=NONE cterm=bold
  hi Identifier ctermfg=darkcyan ctermbg=NONE cterm=NONE
  hi Ignore ctermfg=NONE ctermbg=NONE cterm=NONE
  hi PreProc ctermfg=darkmagenta ctermbg=NONE cterm=bold
  hi Special ctermfg=darkyellow ctermbg=NONE cterm=NONE
  hi Statement ctermfg=darkyellow ctermbg=NONE cterm=bold
  hi Todo ctermfg=NONE ctermbg=NONE cterm=reverse
  hi Type ctermfg=darkgreen ctermbg=NONE cterm=NONE
  hi Underlined ctermfg=NONE ctermbg=NONE cterm=underline
  hi DiffAdd ctermfg=white ctermbg=darkgreen cterm=NONE
  hi DiffChange ctermfg=white ctermbg=darkblue cterm=NONE
  hi DiffText ctermfg=black ctermbg=grey cterm=NONE
  hi DiffDelete ctermfg=white ctermbg=darkmagenta cterm=NONE
  unlet s:t_Co
  finish
endif

if s:t_Co >= 0
  hi Normal term=NONE
  hi ColorColumn term=reverse
  hi Conceal term=NONE
  hi Cursor term=reverse
  hi CursorColumn term=NONE
  hi CursorLine term=underline
  hi CursorLineNr term=bold
  hi DiffAdd term=reverse
  hi DiffChange term=NONE
  hi DiffDelete term=reverse
  hi DiffText term=reverse
  hi Directory term=NONE
  hi EndOfBuffer term=NONE
  hi ErrorMsg term=bold,reverse
  hi FoldColumn term=NONE
  hi Folded term=NONE
  hi IncSearch term=bold,reverse,underline
  hi LineNr term=NONE
  hi MatchParen term=bold,underline
  hi ModeMsg term=bold
  hi MoreMsg term=NONE
  hi NonText term=NONE
  hi Pmenu term=reverse
  hi PmenuSbar term=reverse
  hi PmenuSel term=bold
  hi PmenuThumb term=NONE
  hi Question term=standout
  hi Search term=reverse
  hi SignColumn term=reverse
  hi SpecialKey term=bold
  hi SpellBad term=underline
  hi SpellCap term=underline
  hi SpellLocal term=underline
  hi SpellRare term=underline
  hi StatusLine term=bold,reverse
  hi StatusLineNC term=bold,underline
  hi TabLine term=bold,underline
  hi TabLineFill term=NONE
  hi Terminal term=NONE
  hi TabLineSel term=bold,reverse
  hi Title term=NONE
  hi VertSplit term=NONE
  hi Visual term=reverse
  hi VisualNOS term=NONE
  hi WarningMsg term=standout
  hi WildMenu term=bold
  hi CursorIM term=NONE
  hi ToolbarLine term=reverse
  hi ToolbarButton term=bold,reverse
  hi CurSearch term=reverse
  hi CursorLineFold term=underline
  hi CursorLineSign term=underline
  hi Comment term=bold
  hi Constant term=NONE
  hi Error term=bold,reverse
  hi Identifier term=NONE
  hi Ignore term=NONE
  hi PreProc term=NONE
  hi Special term=NONE
  hi Statement term=NONE
  hi Todo term=bold,reverse
  hi Type term=NONE
  hi Underlined term=underline
  unlet s:t_Co
  finish
endif

" Background: dark
" Color: white         #FFFFFF           231               white
" Color: black         #000000           16                black
" Color: diffc         #0087af           31                darkcyan
" Color: difft         #005f87           24                cyan
" Color: cursorl       #666666           59                darkgrey
" Color: ogDeepBlue    #000040           17                black
" Color: ogDarkBlue    #00008b           18                darkblue
" Color: ogBlue        #0030ff           27                blue
" Color: ogLightBlue   #287eff           33                blue
" Color: ogDarkGrey    #a9a9a9           248               grey
" Color: ogGrey        #808080           102               darkgrey
" Color: ogLightGrey   #c0c0c0           252               grey
" Color: ogDarkViolet  #404080           61                darkblue
" Color: ogViolet      #8080ff           105               blue
" Color: ogLightViolet #80a0ff           111               blue
" Color: ogDarkGreen   #006400           22                darkgreen
" Color: ogGreen       #90f020           118               green
" Color: ogDarkCyan    #008b8b           30                darkcyan
" Color: ogCyan        #90fff0           123               cyan
" Color: ogLightCyan   #b0ffff           159               cyan
" Color: ogDarkerRed   #8b0000           88                darkred
" Color: ogDarkRed     #d14a14           166               darkred
" Color: ogRed         #ff0000           196               red
" Color: ogLightRed    #ffa0a0           217               red
" Color: ogDarkMag     #8b008b           90                darkmagenta
" Color: ogMagenta     #ff00ff           201               darkmagenta
" Color: ogLightMag    #ff80ff           213               magenta
" Color: ogOrange      #ffa500           214               darkyellow
" Color: ogYellow      #ffff60           227               yellow
" Term colors: black  ogDarkerRed ogGreen ogOrange ogDarkBlue ogDarkMag ogDarkCyan ogLightGrey
" Term colors: ogGrey ogLightRed  ogGreen ogYellow ogBlue     ogMagenta    ogCyan     white
" Color: bgDiffA     #5F875F        65             darkgreen
" Color: bgDiffC     #5F87AF        67             blue
" Color: bgDiffD     #AF5FAF        133            magenta
" Color: bgDiffT     #C6C6C6        251            grey
" Color: fgDiffW     #FFFFFF        231            white
" Color: fgDiffB     #000000        16             black
" Color: bgDiffC8    #5F87AF        67             darkblue
" Color: bgDiffD8    #AF5FAF        133            darkmagenta
" vim: et ts=8 sw=2 sts=2
