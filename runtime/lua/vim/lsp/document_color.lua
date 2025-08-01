--- @brief This module provides LSP support for highlighting color references in a document.
--- Highlighting is enabled by default.

local api = vim.api
local lsp = vim.lsp
local util = lsp.util
local ms = lsp.protocol.Methods
local Range = vim.treesitter._range

local document_color_ns = api.nvim_create_namespace('nvim.lsp.document_color')
local document_color_augroup = api.nvim_create_augroup('nvim.lsp.document_color', {})

local M = {}

--- @class (private) vim.lsp.document_color.HighlightInfo
--- @field lsp_info lsp.ColorInformation Unprocessed LSP color information
--- @field hex_code string Resolved HEX color
--- @field range Range4 Range of the highlight
--- @field hl_group? string Highlight group name. Won't be present if the style is a custom function.

--- @class (private) vim.lsp.document_color.BufState
--- @field enabled boolean Whether document_color is enabled for the current buffer
--- @field processed_version table<integer, integer?> (client_id -> buffer version) Buffer version for which the color ranges correspond to
--- @field applied_version table<integer, integer?> (client_id -> buffer version) Last buffer version for which we applied color ranges
--- @field hl_info table<integer, vim.lsp.document_color.HighlightInfo[]?> (client_id -> color highlights) Processed highlight information

--- @type table<integer, vim.lsp.document_color.BufState?>
local bufstates = {}

--- @type table<integer, integer> (client_id -> namespace ID) documentColor namespace ID for each client.
local client_ns = {}

--- @inlinedoc
--- @class vim.lsp.document_color.enable.Opts
---
--- Highlight style. It can be one of the pre-defined styles, a string to be used as virtual text, or a
--- function that receives the buffer handle, the range (start line, start col, end line, end col) and
--- the resolved hex color. (default: `'background'`)
--- @field style? 'background'|'foreground'|'virtual'|string|fun(bufnr: integer, range: Range4, hex_code: string)

-- Default options.
--- @type vim.lsp.document_color.enable.Opts
local document_color_opts = { style = 'background' }

--- @param color string
local function get_contrast_color(color)
  local r_s, g_s, b_s = color:match('^#(%x%x)(%x%x)(%x%x)$')
  if not (r_s and g_s and b_s) then
    error('Invalid color format: ' .. color)
  end
  local r, g, b = tonumber(r_s, 16), tonumber(g_s, 16), tonumber(b_s, 16)
  if not (r and g and b) then
    error('Invalid color format: ' .. color)
  end

  -- Source: https://www.w3.org/TR/WCAG21/#dfn-relative-luminance
  -- Using power 2.2 is a close approximation to full piecewise transform
  local R, G, B = (r / 255) ^ 2.2, (g / 255) ^ 2.2, (b / 255) ^ 2.2
  local is_bright = (0.2126 * R + 0.7152 * G + 0.0722 * B) > 0.5
  return is_bright and '#000000' or '#ffffff'
end

--- Returns the hex string representing the given LSP color.
--- @param color lsp.Color
--- @return string
local function get_hex_code(color)
  -- The RGB values in lsp.Color are in the [0-1] range, but we want them to be in the [0-255] range instead.
  --- @param n number
  color = vim.tbl_map(function(n)
    return math.floor((n * 255) + 0.5)
  end, color)

  return ('#%02x%02x%02x'):format(color.red, color.green, color.blue):lower()
end

--- Cache of the highlight groups that we've already created.
--- @type table<string, true>
local color_cache = {}

--- Gets or creates the highlight group for the given LSP color information.
---
--- @param hex_code string
--- @param style string
--- @return string
local function get_hl_group(hex_code, style)
  if style ~= 'background' then
    style = 'foreground'
  end

  local hl_name = ('LspDocumentColor_%s_%s'):format(hex_code:sub(2), style)

  if not color_cache[hl_name] then
    if style == 'background' then
      api.nvim_set_hl(0, hl_name, { bg = hex_code, fg = get_contrast_color(hex_code) })
    else
      api.nvim_set_hl(0, hl_name, { fg = hex_code })
    end

    color_cache[hl_name] = true
  end

  return hl_name
end

--- @param bufnr integer
--- @param enabled boolean
local function reset_bufstate(bufnr, enabled)
  bufstates[bufnr] = {
    enabled = enabled,
    processed_version = {},
    applied_version = {},
    hl_info = {},
  }
end

--- |lsp-handler| for the `textDocument/documentColor` method.
---
--- @param err? lsp.ResponseError
--- @param result? lsp.ColorInformation[]
--- @param ctx lsp.HandlerContext
local function on_document_color(err, result, ctx)
  if err then
    lsp.log.error('document_color', err)
    return
  end

  local bufnr = assert(ctx.bufnr)
  local bufstate = assert(bufstates[bufnr])
  local client_id = ctx.client_id

  if
    util.buf_versions[bufnr] ~= ctx.version
    or not result
    or not api.nvim_buf_is_loaded(bufnr)
    or not bufstate.enabled
  then
    return
  end

  if not client_ns[client_id] then
    client_ns[client_id] = api.nvim_create_namespace('nvim.lsp.document_color.client_' .. client_id)
  end

  local hl_infos = {} --- @type vim.lsp.document_color.HighlightInfo[]
  local style = document_color_opts.style
  local position_encoding = assert(lsp.get_client_by_id(client_id)).offset_encoding
  for _, res in ipairs(result) do
    local range = {
      res.range.start.line,
      util._get_line_byte_from_position(bufnr, res.range.start, position_encoding),
      res.range['end'].line,
      util._get_line_byte_from_position(bufnr, res.range['end'], position_encoding),
    }
    local hex_code = get_hex_code(res.color)
    --- @type vim.lsp.document_color.HighlightInfo
    local hl_info = { range = range, hex_code = hex_code, lsp_info = res }

    if type(style) == 'string' then
      hl_info.hl_group = get_hl_group(hex_code, style)
    end

    table.insert(hl_infos, hl_info)
  end

  bufstate.hl_info[client_id] = hl_infos
  bufstate.processed_version[client_id] = ctx.version

  api.nvim__redraw({ buf = bufnr, valid = true, flush = false })
end

--- @param bufnr integer
local function buf_clear(bufnr)
  local bufstate = bufstates[bufnr]
  if not bufstate then
    return
  end

  local client_ids = vim.tbl_keys(bufstate.hl_info) --- @type integer[]

  for _, client_id in ipairs(client_ids) do
    bufstate.hl_info[client_id] = {}
    api.nvim_buf_clear_namespace(bufnr, client_ns[client_id], 0, -1)
  end

  api.nvim__redraw({ buf = bufnr, valid = true, flush = false })
end

--- @param bufnr integer
local function buf_disable(bufnr)
  buf_clear(bufnr)
  reset_bufstate(bufnr, false)
  api.nvim_clear_autocmds({
    buffer = bufnr,
    group = document_color_augroup,
  })
end

--- @param bufnr integer
local function buf_enable(bufnr)
  reset_bufstate(bufnr, true)
  api.nvim_clear_autocmds({
    buffer = bufnr,
    group = document_color_augroup,
  })

  api.nvim_buf_attach(bufnr, false, {
    on_reload = function(_, buf)
      buf_clear(buf)
      if assert(bufstates[buf]).enabled then
        M._buf_refresh(buf)
      end
    end,
    on_detach = function(_, buf)
      buf_disable(buf)
    end,
  })

  api.nvim_create_autocmd('LspNotify', {
    buffer = bufnr,
    group = document_color_augroup,
    desc = 'Refresh document_color on document changes',
    callback = function(args)
      local method = args.data.method --- @type string

      if
        (method == ms.textDocument_didChange or method == ms.textDocument_didOpen)
        and assert(bufstates[args.buf]).enabled
      then
        M._buf_refresh(args.buf, args.data.client_id)
      end
    end,
  })

  api.nvim_create_autocmd('LspDetach', {
    buffer = bufnr,
    group = document_color_augroup,
    desc = 'Disable document_color if all supporting clients detach',
    callback = function(args)
      local clients = lsp.get_clients({ bufnr = args.buf, method = ms.textDocument_documentColor })

      if
        not vim.iter(clients):any(function(c)
          return c.id ~= args.data.client_id
        end)
      then
        -- There are no clients left in the buffer that support document color, so turn it off.
        buf_disable(args.buf)
      end
    end,
  })

  M._buf_refresh(bufnr)
end

--- @param bufnr integer
--- @param client_id? integer
function M._buf_refresh(bufnr, client_id)
  for _, client in
    ipairs(lsp.get_clients({
      bufnr = bufnr,
      id = client_id,
      method = ms.textDocument_documentColor,
    }))
  do
    ---@type lsp.DocumentColorParams
    local params = { textDocument = util.make_text_document_params(bufnr) }
    client:request(ms.textDocument_documentColor, params, on_document_color)
  end
end

--- Query whether document colors are enabled in the given buffer.
---
--- @param bufnr? integer Buffer handle, or 0 for current. (default: 0)
--- @return boolean
function M.is_enabled(bufnr)
  vim.validate('bufnr', bufnr, 'number', true)

  bufnr = vim._resolve_bufnr(bufnr)

  if not bufstates[bufnr] then
    reset_bufstate(bufnr, false)
  end

  return assert(bufstates[bufnr]).enabled
end

--- Enables document highlighting from the given language client in the given buffer.
---
--- You can enable document highlighting when a client attaches to a buffer as follows:
--- ```lua
--- vim.api.nvim_create_autocmd('LspAttach', {
---   callback = function(args)
---     vim.lsp.document_color.enable(true, args.buf)
---   end
--- })
--- ```
---
--- To "toggle", pass the inverse of `is_enabled()`:
---
--- ```lua
--- vim.lsp.document_color.enable(not vim.lsp.document_color.is_enabled())
--- ```
---
--- @param enable? boolean True to enable, false to disable. (default: `true`)
--- @param bufnr? integer Buffer handle, or 0 for current. (default: 0)
--- @param opts? vim.lsp.document_color.enable.Opts
function M.enable(enable, bufnr, opts)
  vim.validate('enable', enable, 'boolean', true)
  vim.validate('bufnr', bufnr, 'number', true)
  vim.validate('opts', opts, 'table', true)

  enable = enable == nil or enable
  bufnr = vim._resolve_bufnr(bufnr)
  document_color_opts = vim.tbl_extend('keep', opts or {}, document_color_opts)

  if enable then
    buf_enable(bufnr)
  else
    buf_disable(bufnr)
  end
end

api.nvim_create_autocmd('ColorScheme', {
  pattern = '*',
  group = document_color_augroup,
  desc = 'Refresh document_color',
  callback = function()
    color_cache = {}

    for _, bufnr in ipairs(api.nvim_list_bufs()) do
      buf_clear(bufnr)
      if api.nvim_buf_is_loaded(bufnr) and vim.tbl_get(bufstates, bufnr, 'enabled') then
        M._buf_refresh(bufnr)
      else
        reset_bufstate(bufnr, false)
      end
    end
  end,
})

api.nvim_set_decoration_provider(document_color_ns, {
  on_win = function(_, _, bufnr)
    if not bufstates[bufnr] then
      reset_bufstate(bufnr, false)
    end
    local bufstate = assert(bufstates[bufnr])

    local style = document_color_opts.style

    for client_id, client_hls in pairs(bufstate.hl_info) do
      if
        bufstate.processed_version[client_id] == util.buf_versions[bufnr]
        and bufstate.processed_version[client_id] ~= bufstate.applied_version[client_id]
      then
        api.nvim_buf_clear_namespace(bufnr, client_ns[client_id], 0, -1)

        for _, hl in ipairs(client_hls) do
          if type(style) == 'function' then
            style(bufnr, hl.range, hl.hex_code)
          elseif style == 'foreground' or style == 'background' then
            api.nvim_buf_set_extmark(bufnr, client_ns[client_id], hl.range[1], hl.range[2], {
              end_row = hl.range[3],
              end_col = hl.range[4],
              hl_group = hl.hl_group,
              strict = false,
            })
          else
            -- Default swatch: \uf0c8
            local swatch = style == 'virtual' and ' ' or style
            api.nvim_buf_set_extmark(bufnr, client_ns[client_id], hl.range[1], hl.range[2], {
              virt_text = { { swatch, hl.hl_group } },
              virt_text_pos = 'inline',
            })
          end
        end

        bufstate.applied_version[client_id] = bufstate.processed_version[client_id]
      end
    end
  end,
})

--- @param bufstate vim.lsp.document_color.BufState
--- @return vim.lsp.document_color.HighlightInfo?, integer?
local function get_hl_info_under_cursor(bufstate)
  local cursor_row, cursor_col = unpack(api.nvim_win_get_cursor(0)) --- @type integer, integer
  cursor_row = cursor_row - 1 -- Convert to 0-based index
  local cursor_range = { cursor_row, cursor_col, cursor_row, cursor_col } --- @type Range4

  for client_id, hls in pairs(bufstate.hl_info) do
    for _, hl in ipairs(hls) do
      if Range.contains(hl.range, cursor_range) then
        return hl, client_id
      end
    end
  end
end

--- Select from a list of presentations for the color under the cursor.
function M.color_presentation()
  local bufnr = api.nvim_get_current_buf()
  local bufstate = bufstates[bufnr]
  if not bufstate then
    vim.notify('documentColor is not enabled for this buffer.', vim.log.levels.WARN)
    return
  end

  local hl_info, client_id = get_hl_info_under_cursor(bufstate)
  if not hl_info or not client_id then
    vim.notify('No color information under cursor.', vim.log.levels.WARN)
    return
  end

  local uri = vim.uri_from_bufnr(bufnr)
  local client = assert(lsp.get_client_by_id(client_id))

  --- @type lsp.ColorPresentationParams
  local params = {
    textDocument = { uri = uri },
    color = hl_info.lsp_info.color,
    range = {
      start = { line = hl_info.range[1], character = hl_info.range[2] },
      ['end'] = { line = hl_info.range[3], character = hl_info.range[4] },
    },
  }

  --- @param result lsp.ColorPresentation[]
  client:request(ms.textDocument_colorPresentation, params, function(err, result, ctx)
    if err then
      lsp.log.error('color_presentation', err)
      return
    end

    if
      util.buf_versions[bufnr] ~= ctx.version
      or not next(result)
      or not api.nvim_buf_is_loaded(bufnr)
      or not bufstate.enabled
    then
      return
    end

    vim.ui.select(result, {
      kind = 'color_presentation',
      format_item = function(item)
        return item.label
      end,
    }, function(choice)
      if not choice then
        return
      end

      local text_edits = {} --- @type lsp.TextEdit[]
      if choice.textEdit then
        text_edits[#text_edits + 1] = choice.textEdit
      else
        -- If there's no textEdit, we should insert the label.
        text_edits[#text_edits + 1] = { range = params.range, newText = choice.label }
      end
      vim.list_extend(text_edits, choice.additionalTextEdits or {})

      lsp.util.apply_text_edits(text_edits, bufnr, client.offset_encoding)
    end)
  end)
end

return M
