let g:python_host_prog = '/usr/bin/python2'
let g:python3_host_prog = '/usr/bin/python3'

augroup Fedora
  autocmd!
  " RPM spec file template
  autocmd BufNewFile *.spec silent! 0read /usr/share/nvim/template.spec
augroup END

" vim: et ts=2 sw=2
