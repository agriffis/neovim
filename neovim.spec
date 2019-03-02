%bcond_with jemalloc

Name:           neovim
Version:        0.3.3
Release:        1%{?dist}

License:        ASL 2.0
Summary:        Vim-fork focused on extensibility and agility
Url:            http://neovim.io

Source0:        https://github.com/neovim/neovim/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        sysinit.vim
Source2:        spec-template
Patch0:         neovim-0.1.7-bitop.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  lua-lpeg
BuildRequires:  lua-mpack
%if %{with jemalloc}
BuildRequires:  jemalloc-devel
%endif
BuildRequires:  msgpack-devel >= 1.2.0
BuildRequires:  libtermkey-devel
BuildRequires:  libuv-devel
BuildRequires:  libvterm-devel
BuildRequires:  unibilium-devel
%if 0%{?el7}
BuildRequires:  lua-bit32
Requires:       lua-bit32
%else
Suggests:       (python2-neovim if python2)
Suggests:       (python3-neovim if python3)
# XSel provides access to the system clipboard
Recommends:     xsel
# Needed to run nvim with the desktop file
Recommends:     xterm
%endif

%description
Neovim is a refactor - and sometimes redactor - in the tradition of
Vim, which itself derives from Stevie. It is not a rewrite, but a
continuation and extension of Vim. Many rewrites, clones, emulators
and imitators exist; some are very clever, but none are Vim. Neovim
strives to be a superset of Vim, notwithstanding some intentionally
removed misfeatures; excepting those few and carefully-considered
excisions, Neovim is Vim. It is built for users who want the good
parts of Vim, without compromise, and more.

%prep
%autosetup -p1

%build
mkdir -p build
pushd build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DPREFER_LUA=ON \
       -DLUA_PRG=%{_bindir}/lua \
       -DENABLE_JEMALLOC=%{?with_jemalloc:ON}%{!?with_jemalloc:OFF} \
       ..

%make_build VERBOSE=1
popd

%install
pushd build
%make_install
popd

install -p -m 644 %SOURCE1 %{buildroot}%{_datadir}/nvim/sysinit.vim
install -p -m 644 %SOURCE2 %{buildroot}%{_datadir}/nvim/template.spec

desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    runtime/nvim.desktop
install -d -m0755 %{buildroot}%{_datadir}/pixmaps
install -m0644 runtime/nvim.png %{buildroot}%{_datadir}/pixmaps/nvim.png

%fdupes %{buildroot}%{_datadir}/
%find_lang nvim

%files -f nvim.lang
%license LICENSE
%doc BACKERS.md CONTRIBUTING.md README.md
%{_bindir}/nvim

%{_mandir}/man1/nvim.1*
%{_datadir}/applications/nvim.desktop
%{_datadir}/pixmaps/nvim.png

%dir %{_datadir}/nvim
%{_datadir}/nvim/sysinit.vim
%{_datadir}/nvim/template.spec

%dir %{_datadir}/nvim/runtime
%{_datadir}/nvim/runtime/bugreport.vim
%{_datadir}/nvim/runtime/delmenu.vim
%{_datadir}/nvim/runtime/filetype.vim
%{_datadir}/nvim/runtime/ftoff.vim
%{_datadir}/nvim/runtime/ftplugin.vim
%{_datadir}/nvim/runtime/ftplugof.vim
%{_datadir}/nvim/runtime/indent.vim
%{_datadir}/nvim/runtime/indoff.vim
%{_datadir}/nvim/runtime/macmap.vim
%{_datadir}/nvim/runtime/makemenu.vim
%{_datadir}/nvim/runtime/menu.vim
%{_datadir}/nvim/runtime/mswin.vim
%{_datadir}/nvim/runtime/optwin.vim
%{_datadir}/nvim/runtime/rgb.txt
%{_datadir}/nvim/runtime/scripts.vim
%{_datadir}/nvim/runtime/synmenu.vim

%dir %{_datadir}/nvim/runtime/autoload
%{_datadir}/nvim/runtime/autoload/RstFold.vim
%{_datadir}/nvim/runtime/autoload/ada.vim
%{_datadir}/nvim/runtime/autoload/adacomplete.vim
%{_datadir}/nvim/runtime/autoload/ccomplete.vim
%{_datadir}/nvim/runtime/autoload/clojurecomplete.vim
%{_datadir}/nvim/runtime/autoload/context.vim
%{_datadir}/nvim/runtime/autoload/contextcomplete.vim
%{_datadir}/nvim/runtime/autoload/csscomplete.vim
%{_datadir}/nvim/runtime/autoload/decada.vim
%{_datadir}/nvim/runtime/autoload/gnat.vim
%{_datadir}/nvim/runtime/autoload/gzip.vim
%{_datadir}/nvim/runtime/autoload/haskellcomplete.vim
%{_datadir}/nvim/runtime/autoload/health.vim
%{_datadir}/nvim/runtime/autoload/health/nvim.vim
%{_datadir}/nvim/runtime/autoload/health/provider.vim
%{_datadir}/nvim/runtime/autoload/htmlcomplete.vim
%{_datadir}/nvim/runtime/autoload/javascriptcomplete.vim
%{_datadir}/nvim/runtime/autoload/man.vim
%{_datadir}/nvim/runtime/autoload/msgpack.vim
%{_datadir}/nvim/runtime/autoload/netrw.vim
%{_datadir}/nvim/runtime/autoload/netrwFileHandlers.vim
%{_datadir}/nvim/runtime/autoload/netrwSettings.vim
%{_datadir}/nvim/runtime/autoload/netrw_gitignore.vim
%{_datadir}/nvim/runtime/autoload/paste.vim
%{_datadir}/nvim/runtime/autoload/phpcomplete.vim
%{_datadir}/nvim/runtime/autoload/provider.vim
%{_datadir}/nvim/runtime/autoload/python3complete.vim
%{_datadir}/nvim/runtime/autoload/pythoncomplete.vim
%{_datadir}/nvim/runtime/autoload/rubycomplete.vim
%{_datadir}/nvim/runtime/autoload/rust.vim
%{_datadir}/nvim/runtime/autoload/rustfmt.vim
%{_datadir}/nvim/runtime/autoload/shada.vim
%{_datadir}/nvim/runtime/autoload/spellfile.vim
%{_datadir}/nvim/runtime/autoload/sqlcomplete.vim
%{_datadir}/nvim/runtime/autoload/syntaxcomplete.vim
%{_datadir}/nvim/runtime/autoload/tar.vim
%{_datadir}/nvim/runtime/autoload/tohtml.vim
%{_datadir}/nvim/runtime/autoload/tutor.vim
%{_datadir}/nvim/runtime/autoload/vimexpect.vim
%{_datadir}/nvim/runtime/autoload/xmlcomplete.vim
%{_datadir}/nvim/runtime/autoload/xmlformat.vim
%{_datadir}/nvim/runtime/autoload/zip.vim

%dir %{_datadir}/nvim/runtime/autoload/dist
%{_datadir}/nvim/runtime/autoload/dist/ft.vim

%dir %{_datadir}/nvim/runtime/autoload/provider
%{_datadir}/nvim/runtime/autoload/provider/clipboard.vim
%{_datadir}/nvim/runtime/autoload/provider/node.vim
%{_datadir}/nvim/runtime/autoload/provider/python.vim
%{_datadir}/nvim/runtime/autoload/provider/python3.vim
%{_datadir}/nvim/runtime/autoload/provider/pythonx.vim
%{_datadir}/nvim/runtime/autoload/provider/ruby.vim
%{_datadir}/nvim/runtime/autoload/provider/script_host.rb

%dir %{_datadir}/nvim/runtime/autoload/remote
%{_datadir}/nvim/runtime/autoload/remote/define.vim
%{_datadir}/nvim/runtime/autoload/remote/host.vim

%dir %{_datadir}/nvim/runtime/autoload/xml
%{_datadir}/nvim/runtime/autoload/xml/xsl.vim
%{_datadir}/nvim/runtime/autoload/xml/xhtml10f.vim
%{_datadir}/nvim/runtime/autoload/xml/html40s.vim
%{_datadir}/nvim/runtime/autoload/xml/html401s.vim
%{_datadir}/nvim/runtime/autoload/xml/xsd.vim
%{_datadir}/nvim/runtime/autoload/xml/html32.vim
%{_datadir}/nvim/runtime/autoload/xml/html40f.vim
%{_datadir}/nvim/runtime/autoload/xml/html401t.vim
%{_datadir}/nvim/runtime/autoload/xml/xhtml10t.vim
%{_datadir}/nvim/runtime/autoload/xml/xhtml10s.vim
%{_datadir}/nvim/runtime/autoload/xml/xhtml11.vim
%{_datadir}/nvim/runtime/autoload/xml/html40t.vim
%{_datadir}/nvim/runtime/autoload/xml/html401f.vim

%dir %{_datadir}/nvim/runtime/colors
%{_datadir}/nvim/runtime/colors/blue.vim
%{_datadir}/nvim/runtime/colors/darkblue.vim
%{_datadir}/nvim/runtime/colors/default.vim
%{_datadir}/nvim/runtime/colors/delek.vim
%{_datadir}/nvim/runtime/colors/desert.vim
%{_datadir}/nvim/runtime/colors/elflord.vim
%{_datadir}/nvim/runtime/colors/evening.vim
%{_datadir}/nvim/runtime/colors/industry.vim
%{_datadir}/nvim/runtime/colors/koehler.vim
%{_datadir}/nvim/runtime/colors/morning.vim
%{_datadir}/nvim/runtime/colors/murphy.vim
%{_datadir}/nvim/runtime/colors/pablo.vim
%{_datadir}/nvim/runtime/colors/peachpuff.vim
%{_datadir}/nvim/runtime/colors/ron.vim
%{_datadir}/nvim/runtime/colors/shine.vim
%{_datadir}/nvim/runtime/colors/slate.vim
%{_datadir}/nvim/runtime/colors/torte.vim
%{_datadir}/nvim/runtime/colors/zellner.vim

%dir %{_datadir}/nvim/runtime/compiler
%{_datadir}/nvim/runtime/compiler/ant.vim
%{_datadir}/nvim/runtime/compiler/bcc.vim
%{_datadir}/nvim/runtime/compiler/bdf.vim
%{_datadir}/nvim/runtime/compiler/cargo.vim
%{_datadir}/nvim/runtime/compiler/checkstyle.vim
%{_datadir}/nvim/runtime/compiler/context.vim
%{_datadir}/nvim/runtime/compiler/cs.vim
%{_datadir}/nvim/runtime/compiler/csslint.vim
%{_datadir}/nvim/runtime/compiler/cucumber.vim
%{_datadir}/nvim/runtime/compiler/decada.vim
%{_datadir}/nvim/runtime/compiler/dot.vim
%{_datadir}/nvim/runtime/compiler/erlang.vim
%{_datadir}/nvim/runtime/compiler/eruby.vim
%{_datadir}/nvim/runtime/compiler/fortran_F.vim
%{_datadir}/nvim/runtime/compiler/fortran_cv.vim
%{_datadir}/nvim/runtime/compiler/fortran_elf90.vim
%{_datadir}/nvim/runtime/compiler/fortran_g77.vim
%{_datadir}/nvim/runtime/compiler/fortran_lf95.vim
%{_datadir}/nvim/runtime/compiler/fpc.vim
%{_datadir}/nvim/runtime/compiler/g95.vim
%{_datadir}/nvim/runtime/compiler/gcc.vim
%{_datadir}/nvim/runtime/compiler/gfortran.vim
%{_datadir}/nvim/runtime/compiler/ghc.vim
%{_datadir}/nvim/runtime/compiler/gnat.vim
%{_datadir}/nvim/runtime/compiler/go.vim
%{_datadir}/nvim/runtime/compiler/haml.vim
%{_datadir}/nvim/runtime/compiler/hp_acc.vim
%{_datadir}/nvim/runtime/compiler/icc.vim
%{_datadir}/nvim/runtime/compiler/ifort.vim
%{_datadir}/nvim/runtime/compiler/intel.vim
%{_datadir}/nvim/runtime/compiler/irix5_c.vim
%{_datadir}/nvim/runtime/compiler/irix5_cpp.vim
%{_datadir}/nvim/runtime/compiler/javac.vim
%{_datadir}/nvim/runtime/compiler/jikes.vim
%{_datadir}/nvim/runtime/compiler/mcs.vim
%{_datadir}/nvim/runtime/compiler/mips_c.vim
%{_datadir}/nvim/runtime/compiler/mipspro_c89.vim
%{_datadir}/nvim/runtime/compiler/mipspro_cpp.vim
%{_datadir}/nvim/runtime/compiler/modelsim_vcom.vim
%{_datadir}/nvim/runtime/compiler/msbuild.vim
%{_datadir}/nvim/runtime/compiler/msvc.vim
%{_datadir}/nvim/runtime/compiler/neato.vim
%{_datadir}/nvim/runtime/compiler/ocaml.vim
%{_datadir}/nvim/runtime/compiler/onsgmls.vim
%{_datadir}/nvim/runtime/compiler/pbx.vim
%{_datadir}/nvim/runtime/compiler/perl.vim
%{_datadir}/nvim/runtime/compiler/php.vim
%{_datadir}/nvim/runtime/compiler/pylint.vim
%{_datadir}/nvim/runtime/compiler/pyunit.vim
%{_datadir}/nvim/runtime/compiler/rake.vim
%{_datadir}/nvim/runtime/compiler/rspec.vim
%{_datadir}/nvim/runtime/compiler/rst.vim
%{_datadir}/nvim/runtime/compiler/ruby.vim
%{_datadir}/nvim/runtime/compiler/rubyunit.vim
%{_datadir}/nvim/runtime/compiler/rustc.vim
%{_datadir}/nvim/runtime/compiler/sass.vim
%{_datadir}/nvim/runtime/compiler/se.vim
%{_datadir}/nvim/runtime/compiler/splint.vim
%{_datadir}/nvim/runtime/compiler/stack.vim
%{_datadir}/nvim/runtime/compiler/tcl.vim
%{_datadir}/nvim/runtime/compiler/tex.vim
%{_datadir}/nvim/runtime/compiler/tidy.vim
%{_datadir}/nvim/runtime/compiler/xbuild.vim
%{_datadir}/nvim/runtime/compiler/xmllint.vim
%{_datadir}/nvim/runtime/compiler/xmlwf.vim

%dir %{_datadir}/nvim/runtime/doc
%{_datadir}/nvim/runtime/doc/api.txt
%{_datadir}/nvim/runtime/doc/arabic.txt
%{_datadir}/nvim/runtime/doc/autocmd.txt
%{_datadir}/nvim/runtime/doc/change.txt
%{_datadir}/nvim/runtime/doc/channel.txt
%{_datadir}/nvim/runtime/doc/cmdline.txt
%{_datadir}/nvim/runtime/doc/debug.txt
%{_datadir}/nvim/runtime/doc/deprecated.txt
%{_datadir}/nvim/runtime/doc/develop.txt
%{_datadir}/nvim/runtime/doc/diff.txt
%{_datadir}/nvim/runtime/doc/digraph.txt
%{_datadir}/nvim/runtime/doc/editing.txt
%{_datadir}/nvim/runtime/doc/eval.txt
%{_datadir}/nvim/runtime/doc/farsi.txt
%{_datadir}/nvim/runtime/doc/filetype.txt
%{_datadir}/nvim/runtime/doc/fold.txt
%{_datadir}/nvim/runtime/doc/ft_ada.txt
%{_datadir}/nvim/runtime/doc/ft_rust.txt
%{_datadir}/nvim/runtime/doc/ft_sql.txt
%{_datadir}/nvim/runtime/doc/gui.txt
%{_datadir}/nvim/runtime/doc/hebrew.txt
%{_datadir}/nvim/runtime/doc/help.txt
%{_datadir}/nvim/runtime/doc/helphelp.txt
%{_datadir}/nvim/runtime/doc/if_cscop.txt
%{_datadir}/nvim/runtime/doc/if_lua.txt
%{_datadir}/nvim/runtime/doc/if_pyth.txt
%{_datadir}/nvim/runtime/doc/if_ruby.txt
%{_datadir}/nvim/runtime/doc/indent.txt
%{_datadir}/nvim/runtime/doc/index.txt
%{_datadir}/nvim/runtime/doc/insert.txt
%{_datadir}/nvim/runtime/doc/intro.txt
%{_datadir}/nvim/runtime/doc/job_control.txt
%{_datadir}/nvim/runtime/doc/makehtml.awk
%{_datadir}/nvim/runtime/doc/maketags.awk
%{_datadir}/nvim/runtime/doc/map.txt
%{_datadir}/nvim/runtime/doc/mbyte.txt
%{_datadir}/nvim/runtime/doc/message.txt
%{_datadir}/nvim/runtime/doc/mlang.txt
%{_datadir}/nvim/runtime/doc/motion.txt
%{_datadir}/nvim/runtime/doc/msgpack_rpc.txt
%{_datadir}/nvim/runtime/doc/nvim.txt
%{_datadir}/nvim/runtime/doc/nvim_terminal_emulator.txt
%{_datadir}/nvim/runtime/doc/options.txt
%{_datadir}/nvim/runtime/doc/pattern.txt
%{_datadir}/nvim/runtime/doc/pi_gzip.txt
%{_datadir}/nvim/runtime/doc/pi_health.txt
%{_datadir}/nvim/runtime/doc/pi_matchit.txt
%{_datadir}/nvim/runtime/doc/pi_msgpack.txt
%{_datadir}/nvim/runtime/doc/pi_netrw.txt
%{_datadir}/nvim/runtime/doc/pi_paren.txt
%{_datadir}/nvim/runtime/doc/pi_spec.txt
%{_datadir}/nvim/runtime/doc/pi_tar.txt
%{_datadir}/nvim/runtime/doc/pi_tutor.txt
%{_datadir}/nvim/runtime/doc/pi_zip.txt
%{_datadir}/nvim/runtime/doc/print.txt
%{_datadir}/nvim/runtime/doc/provider.txt
%{_datadir}/nvim/runtime/doc/quickfix.txt
%{_datadir}/nvim/runtime/doc/quickref.txt
%{_datadir}/nvim/runtime/doc/recover.txt
%{_datadir}/nvim/runtime/doc/remote.txt
%{_datadir}/nvim/runtime/doc/remote_plugin.txt
%{_datadir}/nvim/runtime/doc/repeat.txt
%{_datadir}/nvim/runtime/doc/rileft.txt
%{_datadir}/nvim/runtime/doc/russian.txt
%{_datadir}/nvim/runtime/doc/scroll.txt
%{_datadir}/nvim/runtime/doc/sign.txt
%{_datadir}/nvim/runtime/doc/spell.txt
%{_datadir}/nvim/runtime/doc/starting.txt
%{_datadir}/nvim/runtime/doc/syntax.txt
%{_datadir}/nvim/runtime/doc/tabpage.txt
%{_datadir}/nvim/runtime/doc/tags
%{_datadir}/nvim/runtime/doc/tagsrch.txt
%{_datadir}/nvim/runtime/doc/term.txt
%{_datadir}/nvim/runtime/doc/tips.txt
%{_datadir}/nvim/runtime/doc/uganda.txt
%{_datadir}/nvim/runtime/doc/ui.txt
%{_datadir}/nvim/runtime/doc/undo.txt
%{_datadir}/nvim/runtime/doc/usr_01.txt
%{_datadir}/nvim/runtime/doc/usr_02.txt
%{_datadir}/nvim/runtime/doc/usr_03.txt
%{_datadir}/nvim/runtime/doc/usr_04.txt
%{_datadir}/nvim/runtime/doc/usr_05.txt
%{_datadir}/nvim/runtime/doc/usr_06.txt
%{_datadir}/nvim/runtime/doc/usr_07.txt
%{_datadir}/nvim/runtime/doc/usr_08.txt
%{_datadir}/nvim/runtime/doc/usr_09.txt
%{_datadir}/nvim/runtime/doc/usr_10.txt
%{_datadir}/nvim/runtime/doc/usr_11.txt
%{_datadir}/nvim/runtime/doc/usr_12.txt
%{_datadir}/nvim/runtime/doc/usr_20.txt
%{_datadir}/nvim/runtime/doc/usr_21.txt
%{_datadir}/nvim/runtime/doc/usr_22.txt
%{_datadir}/nvim/runtime/doc/usr_23.txt
%{_datadir}/nvim/runtime/doc/usr_24.txt
%{_datadir}/nvim/runtime/doc/usr_25.txt
%{_datadir}/nvim/runtime/doc/usr_26.txt
%{_datadir}/nvim/runtime/doc/usr_27.txt
%{_datadir}/nvim/runtime/doc/usr_28.txt
%{_datadir}/nvim/runtime/doc/usr_29.txt
%{_datadir}/nvim/runtime/doc/usr_30.txt
%{_datadir}/nvim/runtime/doc/usr_31.txt
%{_datadir}/nvim/runtime/doc/usr_32.txt
%{_datadir}/nvim/runtime/doc/usr_40.txt
%{_datadir}/nvim/runtime/doc/usr_41.txt
%{_datadir}/nvim/runtime/doc/usr_42.txt
%{_datadir}/nvim/runtime/doc/usr_43.txt
%{_datadir}/nvim/runtime/doc/usr_44.txt
%{_datadir}/nvim/runtime/doc/usr_45.txt
%{_datadir}/nvim/runtime/doc/usr_toc.txt
%{_datadir}/nvim/runtime/doc/various.txt
%{_datadir}/nvim/runtime/doc/vi_diff.txt
%{_datadir}/nvim/runtime/doc/vim_diff.txt
%{_datadir}/nvim/runtime/doc/visual.txt
%{_datadir}/nvim/runtime/doc/windows.txt

%dir %{_datadir}/nvim/runtime/ftplugin
%{_datadir}/nvim/runtime/ftplugin/a2ps.vim
%{_datadir}/nvim/runtime/ftplugin/aap.vim
%{_datadir}/nvim/runtime/ftplugin/abap.vim
%{_datadir}/nvim/runtime/ftplugin/abaqus.vim
%{_datadir}/nvim/runtime/ftplugin/ada.vim
%{_datadir}/nvim/runtime/ftplugin/alsaconf.vim
%{_datadir}/nvim/runtime/ftplugin/ant.vim
%{_datadir}/nvim/runtime/ftplugin/arch.vim
%{_datadir}/nvim/runtime/ftplugin/art.vim
%{_datadir}/nvim/runtime/ftplugin/aspvbs.vim
%{_datadir}/nvim/runtime/ftplugin/automake.vim
%{_datadir}/nvim/runtime/ftplugin/awk.vim
%{_datadir}/nvim/runtime/ftplugin/bdf.vim
%{_datadir}/nvim/runtime/ftplugin/bst.vim
%{_datadir}/nvim/runtime/ftplugin/btm.vim
%{_datadir}/nvim/runtime/ftplugin/bzl.vim
%{_datadir}/nvim/runtime/ftplugin/c.vim
%{_datadir}/nvim/runtime/ftplugin/calendar.vim
%{_datadir}/nvim/runtime/ftplugin/cdrdaoconf.vim
%{_datadir}/nvim/runtime/ftplugin/ch.vim
%{_datadir}/nvim/runtime/ftplugin/changelog.vim
%{_datadir}/nvim/runtime/ftplugin/chicken.vim
%{_datadir}/nvim/runtime/ftplugin/clojure.vim
%{_datadir}/nvim/runtime/ftplugin/cmake.vim
%{_datadir}/nvim/runtime/ftplugin/cobol.vim
%{_datadir}/nvim/runtime/ftplugin/conf.vim
%{_datadir}/nvim/runtime/ftplugin/config.vim
%{_datadir}/nvim/runtime/ftplugin/context.vim
%{_datadir}/nvim/runtime/ftplugin/cpp.vim
%{_datadir}/nvim/runtime/ftplugin/crm.vim
%{_datadir}/nvim/runtime/ftplugin/cs.vim
%{_datadir}/nvim/runtime/ftplugin/csc.vim
%{_datadir}/nvim/runtime/ftplugin/csh.vim
%{_datadir}/nvim/runtime/ftplugin/css.vim
%{_datadir}/nvim/runtime/ftplugin/cucumber.vim
%{_datadir}/nvim/runtime/ftplugin/cvsrc.vim
%{_datadir}/nvim/runtime/ftplugin/debchangelog.vim
%{_datadir}/nvim/runtime/ftplugin/debcontrol.vim
%{_datadir}/nvim/runtime/ftplugin/denyhosts.vim
%{_datadir}/nvim/runtime/ftplugin/dictconf.vim
%{_datadir}/nvim/runtime/ftplugin/dictdconf.vim
%{_datadir}/nvim/runtime/ftplugin/diff.vim
%{_datadir}/nvim/runtime/ftplugin/dircolors.vim
%{_datadir}/nvim/runtime/ftplugin/docbk.vim
%{_datadir}/nvim/runtime/ftplugin/dockerfile.vim
%{_datadir}/nvim/runtime/ftplugin/dosbatch.vim
%{_datadir}/nvim/runtime/ftplugin/dosini.vim
%{_datadir}/nvim/runtime/ftplugin/dtd.vim
%{_datadir}/nvim/runtime/ftplugin/dtrace.vim
%{_datadir}/nvim/runtime/ftplugin/eiffel.vim
%{_datadir}/nvim/runtime/ftplugin/elinks.vim
%{_datadir}/nvim/runtime/ftplugin/erlang.vim
%{_datadir}/nvim/runtime/ftplugin/eruby.vim
%{_datadir}/nvim/runtime/ftplugin/eterm.vim
%{_datadir}/nvim/runtime/ftplugin/falcon.vim
%{_datadir}/nvim/runtime/ftplugin/fetchmail.vim
%{_datadir}/nvim/runtime/ftplugin/flexwiki.vim
%{_datadir}/nvim/runtime/ftplugin/fortran.vim
%{_datadir}/nvim/runtime/ftplugin/framescript.vim
%{_datadir}/nvim/runtime/ftplugin/fvwm.vim
%{_datadir}/nvim/runtime/ftplugin/gdb.vim
%{_datadir}/nvim/runtime/ftplugin/git.vim
%{_datadir}/nvim/runtime/ftplugin/gitcommit.vim
%{_datadir}/nvim/runtime/ftplugin/gitconfig.vim
%{_datadir}/nvim/runtime/ftplugin/gitrebase.vim
%{_datadir}/nvim/runtime/ftplugin/gitsendemail.vim
%{_datadir}/nvim/runtime/ftplugin/go.vim
%{_datadir}/nvim/runtime/ftplugin/gpg.vim
%{_datadir}/nvim/runtime/ftplugin/gprof.vim
%{_datadir}/nvim/runtime/ftplugin/groovy.vim
%{_datadir}/nvim/runtime/ftplugin/group.vim
%{_datadir}/nvim/runtime/ftplugin/grub.vim
%{_datadir}/nvim/runtime/ftplugin/haml.vim
%{_datadir}/nvim/runtime/ftplugin/hamster.vim
%{_datadir}/nvim/runtime/ftplugin/haskell.vim
%{_datadir}/nvim/runtime/ftplugin/help.vim
%{_datadir}/nvim/runtime/ftplugin/hgcommit.vim
%{_datadir}/nvim/runtime/ftplugin/hog.vim
%{_datadir}/nvim/runtime/ftplugin/hostconf.vim
%{_datadir}/nvim/runtime/ftplugin/hostsaccess.vim
%{_datadir}/nvim/runtime/ftplugin/html.vim
%{_datadir}/nvim/runtime/ftplugin/htmldjango.vim
%{_datadir}/nvim/runtime/ftplugin/indent.vim
%{_datadir}/nvim/runtime/ftplugin/initex.vim
%{_datadir}/nvim/runtime/ftplugin/ishd.vim
%{_datadir}/nvim/runtime/ftplugin/j.vim
%{_datadir}/nvim/runtime/ftplugin/java.vim
%{_datadir}/nvim/runtime/ftplugin/javascript.vim
%{_datadir}/nvim/runtime/ftplugin/jproperties.vim
%{_datadir}/nvim/runtime/ftplugin/json.vim
%{_datadir}/nvim/runtime/ftplugin/jsp.vim
%{_datadir}/nvim/runtime/ftplugin/kconfig.vim
%{_datadir}/nvim/runtime/ftplugin/kwt.vim
%{_datadir}/nvim/runtime/ftplugin/ld.vim
%{_datadir}/nvim/runtime/ftplugin/less.vim
%{_datadir}/nvim/runtime/ftplugin/lftp.vim
%{_datadir}/nvim/runtime/ftplugin/libao.vim
%{_datadir}/nvim/runtime/ftplugin/limits.vim
%{_datadir}/nvim/runtime/ftplugin/liquid.vim
%{_datadir}/nvim/runtime/ftplugin/lisp.vim
%{_datadir}/nvim/runtime/ftplugin/logcheck.vim
%{_datadir}/nvim/runtime/ftplugin/loginaccess.vim
%{_datadir}/nvim/runtime/ftplugin/logindefs.vim
%{_datadir}/nvim/runtime/ftplugin/logtalk.dict
%{_datadir}/nvim/runtime/ftplugin/logtalk.vim
%{_datadir}/nvim/runtime/ftplugin/lprolog.vim
%{_datadir}/nvim/runtime/ftplugin/lua.vim
%{_datadir}/nvim/runtime/ftplugin/m4.vim
%{_datadir}/nvim/runtime/ftplugin/mail.vim
%{_datadir}/nvim/runtime/ftplugin/mailaliases.vim
%{_datadir}/nvim/runtime/ftplugin/mailcap.vim
%{_datadir}/nvim/runtime/ftplugin/make.vim
%{_datadir}/nvim/runtime/ftplugin/man.vim
%{_datadir}/nvim/runtime/ftplugin/manconf.vim
%{_datadir}/nvim/runtime/ftplugin/markdown.vim
%{_datadir}/nvim/runtime/ftplugin/matlab.vim
%{_datadir}/nvim/runtime/ftplugin/mf.vim
%{_datadir}/nvim/runtime/ftplugin/modconf.vim
%{_datadir}/nvim/runtime/ftplugin/mp.vim
%{_datadir}/nvim/runtime/ftplugin/mplayerconf.vim
%{_datadir}/nvim/runtime/ftplugin/mrxvtrc.vim
%{_datadir}/nvim/runtime/ftplugin/msmessages.vim
%{_datadir}/nvim/runtime/ftplugin/muttrc.vim
%{_datadir}/nvim/runtime/ftplugin/nanorc.vim
%{_datadir}/nvim/runtime/ftplugin/neomuttrc.vim
%{_datadir}/nvim/runtime/ftplugin/netrc.vim
%{_datadir}/nvim/runtime/ftplugin/nsis.vim
%{_datadir}/nvim/runtime/ftplugin/objc.vim
%{_datadir}/nvim/runtime/ftplugin/ocaml.vim
%{_datadir}/nvim/runtime/ftplugin/occam.vim
%{_datadir}/nvim/runtime/ftplugin/pamconf.vim
%{_datadir}/nvim/runtime/ftplugin/pascal.vim
%{_datadir}/nvim/runtime/ftplugin/passwd.vim
%{_datadir}/nvim/runtime/ftplugin/pdf.vim
%{_datadir}/nvim/runtime/ftplugin/perl.vim
%{_datadir}/nvim/runtime/ftplugin/perl6.vim
%{_datadir}/nvim/runtime/ftplugin/php.vim
%{_datadir}/nvim/runtime/ftplugin/pinfo.vim
%{_datadir}/nvim/runtime/ftplugin/plaintex.vim
%{_datadir}/nvim/runtime/ftplugin/postscr.vim
%{_datadir}/nvim/runtime/ftplugin/procmail.vim
%{_datadir}/nvim/runtime/ftplugin/prolog.vim
%{_datadir}/nvim/runtime/ftplugin/protocols.vim
%{_datadir}/nvim/runtime/ftplugin/pyrex.vim
%{_datadir}/nvim/runtime/ftplugin/python.vim
%{_datadir}/nvim/runtime/ftplugin/qf.vim
%{_datadir}/nvim/runtime/ftplugin/quake.vim
%{_datadir}/nvim/runtime/ftplugin/r.vim
%{_datadir}/nvim/runtime/ftplugin/racc.vim
%{_datadir}/nvim/runtime/ftplugin/readline.vim
%{_datadir}/nvim/runtime/ftplugin/registry.vim
%{_datadir}/nvim/runtime/ftplugin/reva.vim
%{_datadir}/nvim/runtime/ftplugin/rhelp.vim
%{_datadir}/nvim/runtime/ftplugin/rmd.vim
%{_datadir}/nvim/runtime/ftplugin/rnc.vim
%{_datadir}/nvim/runtime/ftplugin/rnoweb.vim
%{_datadir}/nvim/runtime/ftplugin/rpl.vim
%{_datadir}/nvim/runtime/ftplugin/rrst.vim
%{_datadir}/nvim/runtime/ftplugin/rst.vim
%{_datadir}/nvim/runtime/ftplugin/ruby.vim
%{_datadir}/nvim/runtime/ftplugin/rust.vim
%{_datadir}/nvim/runtime/ftplugin/sass.vim
%{_datadir}/nvim/runtime/ftplugin/sbt.vim
%{_datadir}/nvim/runtime/ftplugin/scala.vim
%{_datadir}/nvim/runtime/ftplugin/scheme.vim
%{_datadir}/nvim/runtime/ftplugin/screen.vim
%{_datadir}/nvim/runtime/ftplugin/scss.vim
%{_datadir}/nvim/runtime/ftplugin/sensors.vim
%{_datadir}/nvim/runtime/ftplugin/services.vim
%{_datadir}/nvim/runtime/ftplugin/setserial.vim
%{_datadir}/nvim/runtime/ftplugin/sgml.vim
%{_datadir}/nvim/runtime/ftplugin/sh.vim
%{_datadir}/nvim/runtime/ftplugin/shada.vim
%{_datadir}/nvim/runtime/ftplugin/sieve.vim
%{_datadir}/nvim/runtime/ftplugin/slpconf.vim
%{_datadir}/nvim/runtime/ftplugin/slpreg.vim
%{_datadir}/nvim/runtime/ftplugin/slpspi.vim
%{_datadir}/nvim/runtime/ftplugin/spec.vim
%{_datadir}/nvim/runtime/ftplugin/sql.vim
%{_datadir}/nvim/runtime/ftplugin/sshconfig.vim
%{_datadir}/nvim/runtime/ftplugin/sudoers.vim
%{_datadir}/nvim/runtime/ftplugin/svg.vim
%{_datadir}/nvim/runtime/ftplugin/sysctl.vim
%{_datadir}/nvim/runtime/ftplugin/systemd.vim
%{_datadir}/nvim/runtime/ftplugin/systemverilog.vim
%{_datadir}/nvim/runtime/ftplugin/tcl.vim
%{_datadir}/nvim/runtime/ftplugin/tcsh.vim
%{_datadir}/nvim/runtime/ftplugin/terminfo.vim
%{_datadir}/nvim/runtime/ftplugin/tex.vim
%{_datadir}/nvim/runtime/ftplugin/text.vim
%{_datadir}/nvim/runtime/ftplugin/tmux.vim
%{_datadir}/nvim/runtime/ftplugin/treetop.vim
%{_datadir}/nvim/runtime/ftplugin/tt2html.vim
%{_datadir}/nvim/runtime/ftplugin/tutor.vim
%{_datadir}/nvim/runtime/ftplugin/udevconf.vim
%{_datadir}/nvim/runtime/ftplugin/udevperm.vim
%{_datadir}/nvim/runtime/ftplugin/udevrules.vim
%{_datadir}/nvim/runtime/ftplugin/updatedb.vim
%{_datadir}/nvim/runtime/ftplugin/vb.vim
%{_datadir}/nvim/runtime/ftplugin/verilog.vim
%{_datadir}/nvim/runtime/ftplugin/vhdl.vim
%{_datadir}/nvim/runtime/ftplugin/vim.vim
%{_datadir}/nvim/runtime/ftplugin/vroom.vim
%{_datadir}/nvim/runtime/ftplugin/wast.vim
%{_datadir}/nvim/runtime/ftplugin/xdefaults.vim
%{_datadir}/nvim/runtime/ftplugin/xf86conf.vim
%{_datadir}/nvim/runtime/ftplugin/xhtml.vim
%{_datadir}/nvim/runtime/ftplugin/xinetd.vim
%{_datadir}/nvim/runtime/ftplugin/xml.vim
%{_datadir}/nvim/runtime/ftplugin/xmodmap.vim
%{_datadir}/nvim/runtime/ftplugin/xs.vim
%{_datadir}/nvim/runtime/ftplugin/xsd.vim
%{_datadir}/nvim/runtime/ftplugin/xslt.vim
%{_datadir}/nvim/runtime/ftplugin/yaml.vim
%{_datadir}/nvim/runtime/ftplugin/zimbu.vim
%{_datadir}/nvim/runtime/ftplugin/zsh.vim

%dir %{_datadir}/nvim/runtime/indent
%{_datadir}/nvim/runtime/indent/aap.vim
%{_datadir}/nvim/runtime/indent/ada.vim
%{_datadir}/nvim/runtime/indent/ant.vim
%{_datadir}/nvim/runtime/indent/automake.vim
%{_datadir}/nvim/runtime/indent/awk.vim
%{_datadir}/nvim/runtime/indent/bib.vim
%{_datadir}/nvim/runtime/indent/bst.vim
%{_datadir}/nvim/runtime/indent/bzl.vim
%{_datadir}/nvim/runtime/indent/c.vim
%{_datadir}/nvim/runtime/indent/cdl.vim
%{_datadir}/nvim/runtime/indent/ch.vim
%{_datadir}/nvim/runtime/indent/chaiscript.vim
%{_datadir}/nvim/runtime/indent/changelog.vim
%{_datadir}/nvim/runtime/indent/clojure.vim
%{_datadir}/nvim/runtime/indent/cmake.vim
%{_datadir}/nvim/runtime/indent/cobol.vim
%{_datadir}/nvim/runtime/indent/config.vim
%{_datadir}/nvim/runtime/indent/context.vim
%{_datadir}/nvim/runtime/indent/cpp.vim
%{_datadir}/nvim/runtime/indent/cs.vim
%{_datadir}/nvim/runtime/indent/css.vim
%{_datadir}/nvim/runtime/indent/cucumber.vim
%{_datadir}/nvim/runtime/indent/cuda.vim
%{_datadir}/nvim/runtime/indent/d.vim
%{_datadir}/nvim/runtime/indent/dictconf.vim
%{_datadir}/nvim/runtime/indent/dictdconf.vim
%{_datadir}/nvim/runtime/indent/docbk.vim
%{_datadir}/nvim/runtime/indent/dosbatch.vim
%{_datadir}/nvim/runtime/indent/dtd.vim
%{_datadir}/nvim/runtime/indent/dtrace.vim
%{_datadir}/nvim/runtime/indent/dylan.vim
%{_datadir}/nvim/runtime/indent/eiffel.vim
%{_datadir}/nvim/runtime/indent/erlang.vim
%{_datadir}/nvim/runtime/indent/eruby.vim
%{_datadir}/nvim/runtime/indent/eterm.vim
%{_datadir}/nvim/runtime/indent/falcon.vim
%{_datadir}/nvim/runtime/indent/fortran.vim
%{_datadir}/nvim/runtime/indent/framescript.vim
%{_datadir}/nvim/runtime/indent/gitconfig.vim
%{_datadir}/nvim/runtime/indent/gitolite.vim
%{_datadir}/nvim/runtime/indent/go.vim
%{_datadir}/nvim/runtime/indent/haml.vim
%{_datadir}/nvim/runtime/indent/hamster.vim
%{_datadir}/nvim/runtime/indent/hog.vim
%{_datadir}/nvim/runtime/indent/html.vim
%{_datadir}/nvim/runtime/indent/htmldjango.vim
%{_datadir}/nvim/runtime/indent/idlang.vim
%{_datadir}/nvim/runtime/indent/ishd.vim
%{_datadir}/nvim/runtime/indent/j.vim
%{_datadir}/nvim/runtime/indent/java.vim
%{_datadir}/nvim/runtime/indent/javascript.vim
%{_datadir}/nvim/runtime/indent/json.vim
%{_datadir}/nvim/runtime/indent/jsp.vim
%{_datadir}/nvim/runtime/indent/ld.vim
%{_datadir}/nvim/runtime/indent/less.vim
%{_datadir}/nvim/runtime/indent/lifelines.vim
%{_datadir}/nvim/runtime/indent/liquid.vim
%{_datadir}/nvim/runtime/indent/lisp.vim
%{_datadir}/nvim/runtime/indent/logtalk.vim
%{_datadir}/nvim/runtime/indent/lua.vim
%{_datadir}/nvim/runtime/indent/mail.vim
%{_datadir}/nvim/runtime/indent/make.vim
%{_datadir}/nvim/runtime/indent/matlab.vim
%{_datadir}/nvim/runtime/indent/mf.vim
%{_datadir}/nvim/runtime/indent/mma.vim
%{_datadir}/nvim/runtime/indent/mp.vim
%{_datadir}/nvim/runtime/indent/nsis.vim
%{_datadir}/nvim/runtime/indent/objc.vim
%{_datadir}/nvim/runtime/indent/ocaml.vim
%{_datadir}/nvim/runtime/indent/occam.vim
%{_datadir}/nvim/runtime/indent/pascal.vim
%{_datadir}/nvim/runtime/indent/perl.vim
%{_datadir}/nvim/runtime/indent/perl6.vim
%{_datadir}/nvim/runtime/indent/php.vim
%{_datadir}/nvim/runtime/indent/postscr.vim
%{_datadir}/nvim/runtime/indent/pov.vim
%{_datadir}/nvim/runtime/indent/prolog.vim
%{_datadir}/nvim/runtime/indent/pyrex.vim
%{_datadir}/nvim/runtime/indent/python.vim
%{_datadir}/nvim/runtime/indent/r.vim
%{_datadir}/nvim/runtime/indent/readline.vim
%{_datadir}/nvim/runtime/indent/rhelp.vim
%{_datadir}/nvim/runtime/indent/rmd.vim
%{_datadir}/nvim/runtime/indent/rnoweb.vim
%{_datadir}/nvim/runtime/indent/rpl.vim
%{_datadir}/nvim/runtime/indent/rrst.vim
%{_datadir}/nvim/runtime/indent/rst.vim
%{_datadir}/nvim/runtime/indent/ruby.vim
%{_datadir}/nvim/runtime/indent/rust.vim
%{_datadir}/nvim/runtime/indent/sas.vim
%{_datadir}/nvim/runtime/indent/sass.vim
%{_datadir}/nvim/runtime/indent/scala.vim
%{_datadir}/nvim/runtime/indent/scheme.vim
%{_datadir}/nvim/runtime/indent/scss.vim
%{_datadir}/nvim/runtime/indent/sdl.vim
%{_datadir}/nvim/runtime/indent/sh.vim
%{_datadir}/nvim/runtime/indent/sml.vim
%{_datadir}/nvim/runtime/indent/sql.vim
%{_datadir}/nvim/runtime/indent/sqlanywhere.vim
%{_datadir}/nvim/runtime/indent/systemd.vim
%{_datadir}/nvim/runtime/indent/systemverilog.vim
%{_datadir}/nvim/runtime/indent/tcl.vim
%{_datadir}/nvim/runtime/indent/tcsh.vim
%{_datadir}/nvim/runtime/indent/teraterm.vim
%{_datadir}/nvim/runtime/indent/tex.vim
%{_datadir}/nvim/runtime/indent/tf.vim
%{_datadir}/nvim/runtime/indent/tilde.vim
%{_datadir}/nvim/runtime/indent/treetop.vim
%{_datadir}/nvim/runtime/indent/vb.vim
%{_datadir}/nvim/runtime/indent/verilog.vim
%{_datadir}/nvim/runtime/indent/vhdl.vim
%{_datadir}/nvim/runtime/indent/vim.vim
%{_datadir}/nvim/runtime/indent/vroom.vim
%{_datadir}/nvim/runtime/indent/wast.vim
%{_datadir}/nvim/runtime/indent/xf86conf.vim
%{_datadir}/nvim/runtime/indent/xhtml.vim
%{_datadir}/nvim/runtime/indent/xinetd.vim
%{_datadir}/nvim/runtime/indent/xml.vim
%{_datadir}/nvim/runtime/indent/xsd.vim
%{_datadir}/nvim/runtime/indent/xslt.vim
%{_datadir}/nvim/runtime/indent/yacc.vim
%{_datadir}/nvim/runtime/indent/yaml.vim
%{_datadir}/nvim/runtime/indent/zimbu.vim
%{_datadir}/nvim/runtime/indent/zsh.vim

%dir %{_datadir}/nvim/runtime/keymap
%{_datadir}/nvim/runtime/keymap/accents.vim
%{_datadir}/nvim/runtime/keymap/arabic.vim
%{_datadir}/nvim/runtime/keymap/arabic_utf-8.vim
%{_datadir}/nvim/runtime/keymap/armenian-eastern_utf-8.vim
%{_datadir}/nvim/runtime/keymap/armenian-western_utf-8.vim
%{_datadir}/nvim/runtime/keymap/belarusian-jcuken.vim
%{_datadir}/nvim/runtime/keymap/bulgarian-bds.vim
%{_datadir}/nvim/runtime/keymap/bulgarian-phonetic.vim
%{_datadir}/nvim/runtime/keymap/canfr-win.vim
%{_datadir}/nvim/runtime/keymap/croatian.vim
%{_datadir}/nvim/runtime/keymap/croatian_cp1250.vim
%{_datadir}/nvim/runtime/keymap/croatian_iso-8859-2.vim
%{_datadir}/nvim/runtime/keymap/croatian_utf-8.vim
%{_datadir}/nvim/runtime/keymap/czech.vim
%{_datadir}/nvim/runtime/keymap/czech_utf-8.vim
%{_datadir}/nvim/runtime/keymap/dvorak.vim
%{_datadir}/nvim/runtime/keymap/esperanto.vim
%{_datadir}/nvim/runtime/keymap/esperanto_utf-8.vim
%{_datadir}/nvim/runtime/keymap/greek.vim
%{_datadir}/nvim/runtime/keymap/greek_cp1253.vim
%{_datadir}/nvim/runtime/keymap/greek_cp737.vim
%{_datadir}/nvim/runtime/keymap/greek_iso-8859-7.vim
%{_datadir}/nvim/runtime/keymap/greek_utf-8.vim
%{_datadir}/nvim/runtime/keymap/hebrew.vim
%{_datadir}/nvim/runtime/keymap/hebrew_cp1255.vim
%{_datadir}/nvim/runtime/keymap/hebrew_iso-8859-8.vim
%{_datadir}/nvim/runtime/keymap/hebrew_utf-8.vim
%{_datadir}/nvim/runtime/keymap/hebrewp.vim
%{_datadir}/nvim/runtime/keymap/hebrewp_cp1255.vim
%{_datadir}/nvim/runtime/keymap/hebrewp_iso-8859-8.vim
%{_datadir}/nvim/runtime/keymap/hebrewp_utf-8.vim
%{_datadir}/nvim/runtime/keymap/kana.vim
%{_datadir}/nvim/runtime/keymap/kazakh-jcuken.vim
%{_datadir}/nvim/runtime/keymap/lithuanian-baltic.vim
%{_datadir}/nvim/runtime/keymap/magyar_utf-8.vim
%{_datadir}/nvim/runtime/keymap/mongolian_utf-8.vim
%{_datadir}/nvim/runtime/keymap/oldturkic-orkhon_utf-8.vim
%{_datadir}/nvim/runtime/keymap/oldturkic-yenisei_utf-8.vim
%{_datadir}/nvim/runtime/keymap/persian-iranian_utf-8.vim
%{_datadir}/nvim/runtime/keymap/persian.vim
%{_datadir}/nvim/runtime/keymap/pinyin.vim
%{_datadir}/nvim/runtime/keymap/polish-slash.vim
%{_datadir}/nvim/runtime/keymap/polish-slash_cp1250.vim
%{_datadir}/nvim/runtime/keymap/polish-slash_cp852.vim
%{_datadir}/nvim/runtime/keymap/polish-slash_iso-8859-2.vim
%{_datadir}/nvim/runtime/keymap/polish-slash_utf-8.vim
%{_datadir}/nvim/runtime/keymap/russian-dvorak.vim
%{_datadir}/nvim/runtime/keymap/russian-jcuken.vim
%{_datadir}/nvim/runtime/keymap/russian-jcukenmac.vim
%{_datadir}/nvim/runtime/keymap/russian-jcukenwin.vim
%{_datadir}/nvim/runtime/keymap/russian-yawerty.vim
%{_datadir}/nvim/runtime/keymap/serbian-latin.vim
%{_datadir}/nvim/runtime/keymap/serbian-latin_utf-8.vim
%{_datadir}/nvim/runtime/keymap/serbian.vim
%{_datadir}/nvim/runtime/keymap/serbian_cp1250.vim
%{_datadir}/nvim/runtime/keymap/serbian_cp1251.vim
%{_datadir}/nvim/runtime/keymap/serbian_iso-8859-2.vim
%{_datadir}/nvim/runtime/keymap/serbian_iso-8859-5.vim
%{_datadir}/nvim/runtime/keymap/serbian_utf-8.vim
%{_datadir}/nvim/runtime/keymap/sinhala-phonetic_utf-8.vim
%{_datadir}/nvim/runtime/keymap/sinhala.vim
%{_datadir}/nvim/runtime/keymap/slovak.vim
%{_datadir}/nvim/runtime/keymap/slovak_cp1250.vim
%{_datadir}/nvim/runtime/keymap/slovak_iso-8859-2.vim
%{_datadir}/nvim/runtime/keymap/slovak_utf-8.vim
%{_datadir}/nvim/runtime/keymap/tamil_tscii.vim
%{_datadir}/nvim/runtime/keymap/thaana-phonetic_utf-8.vim
%{_datadir}/nvim/runtime/keymap/thaana.vim
%{_datadir}/nvim/runtime/keymap/ukrainian-dvorak.vim
%{_datadir}/nvim/runtime/keymap/ukrainian-jcuken.vim
%{_datadir}/nvim/runtime/keymap/vietnamese-telex_utf-8.vim
%{_datadir}/nvim/runtime/keymap/vietnamese-viqr_utf-8.vim
%{_datadir}/nvim/runtime/keymap/vietnamese-vni_utf-8.vim

%dir %{_datadir}/nvim/runtime/lua
%{_datadir}/nvim/runtime/lua/man.lua

%dir %{_datadir}/nvim/runtime/lua/vim
%{_datadir}/nvim/runtime/lua/vim/compat.lua

%dir %{_datadir}/nvim/runtime/macros
%{_datadir}/nvim/runtime/macros/editexisting.vim
%{_datadir}/nvim/runtime/macros/justify.vim
%{_datadir}/nvim/runtime/macros/less.bat
%{_datadir}/nvim/runtime/macros/less.sh
%{_datadir}/nvim/runtime/macros/less.vim
%{_datadir}/nvim/runtime/macros/matchit.vim
%{_datadir}/nvim/runtime/macros/shellmenu.vim
%{_datadir}/nvim/runtime/macros/swapmous.vim

%dir %{_datadir}/nvim/runtime/pack
%dir %{_datadir}/nvim/runtime/pack/dist
%dir %{_datadir}/nvim/runtime/pack/dist/opt

%dir %{_datadir}/nvim/runtime/pack/dist/opt/cfilter
%dir %{_datadir}/nvim/runtime/pack/dist/opt/cfilter/plugin
%{_datadir}/nvim/runtime/pack/dist/opt/cfilter/plugin/cfilter.vim

%dir %{_datadir}/nvim/runtime/pack/dist/opt/justify
%dir %{_datadir}/nvim/runtime/pack/dist/opt/justify/plugin
%{_datadir}/nvim/runtime/pack/dist/opt/justify/plugin/justify.vim

%dir %{_datadir}/nvim/runtime/pack/dist/opt/shellmenu
%dir %{_datadir}/nvim/runtime/pack/dist/opt/shellmenu/plugin
%{_datadir}/nvim/runtime/pack/dist/opt/shellmenu/plugin/shellmenu.vim

%dir %{_datadir}/nvim/runtime/pack/dist/opt/swapmouse
%dir %{_datadir}/nvim/runtime/pack/dist/opt/swapmouse/plugin
%{_datadir}/nvim/runtime/pack/dist/opt/swapmouse/plugin/swapmouse.vim

%dir %{_datadir}/nvim/runtime/pack/dist/opt/termdebug
%dir %{_datadir}/nvim/runtime/pack/dist/opt/termdebug/plugin
%{_datadir}/nvim/runtime/pack/dist/opt/termdebug/plugin/termdebug.vim

%dir %{_datadir}/nvim/runtime/pack/dist/opt/vimball
%dir %{_datadir}/nvim/runtime/pack/dist/opt/vimball/plugin
%{_datadir}/nvim/runtime/pack/dist/opt/vimball/plugin/vimballPlugin.vim

%dir %{_datadir}/nvim/runtime/pack/dist/opt/vimball/autoload
%{_datadir}/nvim/runtime/pack/dist/opt/vimball/autoload/vimball.vim

%dir %{_datadir}/nvim/runtime/pack/dist/opt/vimball/doc
%{_datadir}/nvim/runtime/pack/dist/opt/vimball/doc/tags
%{_datadir}/nvim/runtime/pack/dist/opt/vimball/doc/vimball.txt

%dir %{_datadir}/nvim/runtime/plugin
%{_datadir}/nvim/runtime/plugin/gzip.vim
%{_datadir}/nvim/runtime/plugin/health.vim
%{_datadir}/nvim/runtime/plugin/man.vim
%{_datadir}/nvim/runtime/plugin/matchit.vim
%{_datadir}/nvim/runtime/plugin/matchparen.vim
%{_datadir}/nvim/runtime/plugin/netrwPlugin.vim
%{_datadir}/nvim/runtime/plugin/rplugin.vim
%{_datadir}/nvim/runtime/plugin/shada.vim
%{_datadir}/nvim/runtime/plugin/spellfile.vim
%{_datadir}/nvim/runtime/plugin/tarPlugin.vim
%{_datadir}/nvim/runtime/plugin/tohtml.vim
%{_datadir}/nvim/runtime/plugin/tutor.vim
%{_datadir}/nvim/runtime/plugin/zipPlugin.vim

%dir %{_datadir}/nvim/runtime/print
%{_datadir}/nvim/runtime/print/ascii.ps
%{_datadir}/nvim/runtime/print/cidfont.ps
%{_datadir}/nvim/runtime/print/cns_roman.ps
%{_datadir}/nvim/runtime/print/cp1250.ps
%{_datadir}/nvim/runtime/print/cp1251.ps
%{_datadir}/nvim/runtime/print/cp1252.ps
%{_datadir}/nvim/runtime/print/cp1253.ps
%{_datadir}/nvim/runtime/print/cp1254.ps
%{_datadir}/nvim/runtime/print/cp1255.ps
%{_datadir}/nvim/runtime/print/cp1257.ps
%{_datadir}/nvim/runtime/print/gb_roman.ps
%{_datadir}/nvim/runtime/print/hp-roman8.ps
%{_datadir}/nvim/runtime/print/iso-8859-10.ps
%{_datadir}/nvim/runtime/print/iso-8859-11.ps
%{_datadir}/nvim/runtime/print/iso-8859-13.ps
%{_datadir}/nvim/runtime/print/iso-8859-14.ps
%{_datadir}/nvim/runtime/print/iso-8859-15.ps
%{_datadir}/nvim/runtime/print/iso-8859-2.ps
%{_datadir}/nvim/runtime/print/iso-8859-3.ps
%{_datadir}/nvim/runtime/print/iso-8859-4.ps
%{_datadir}/nvim/runtime/print/iso-8859-5.ps
%{_datadir}/nvim/runtime/print/iso-8859-7.ps
%{_datadir}/nvim/runtime/print/iso-8859-8.ps
%{_datadir}/nvim/runtime/print/iso-8859-9.ps
%{_datadir}/nvim/runtime/print/jis_roman.ps
%{_datadir}/nvim/runtime/print/koi8-r.ps
%{_datadir}/nvim/runtime/print/koi8-u.ps
%{_datadir}/nvim/runtime/print/ks_roman.ps
%{_datadir}/nvim/runtime/print/latin1.ps
%{_datadir}/nvim/runtime/print/mac-roman.ps
%{_datadir}/nvim/runtime/print/prolog.ps

%dir %{_datadir}/nvim/runtime/spell
%{_datadir}/nvim/runtime/spell/en.utf-8.spl

%dir %{_datadir}/nvim/runtime/syntax
%{_datadir}/nvim/runtime/syntax/2html.vim
%{_datadir}/nvim/runtime/syntax/a2ps.vim
%{_datadir}/nvim/runtime/syntax/a65.vim
%{_datadir}/nvim/runtime/syntax/aap.vim
%{_datadir}/nvim/runtime/syntax/abap.vim
%{_datadir}/nvim/runtime/syntax/abaqus.vim
%{_datadir}/nvim/runtime/syntax/abc.vim
%{_datadir}/nvim/runtime/syntax/abel.vim
%{_datadir}/nvim/runtime/syntax/acedb.vim
%{_datadir}/nvim/runtime/syntax/ada.vim
%{_datadir}/nvim/runtime/syntax/aflex.vim
%{_datadir}/nvim/runtime/syntax/ahdl.vim
%{_datadir}/nvim/runtime/syntax/alsaconf.vim
%{_datadir}/nvim/runtime/syntax/amiga.vim
%{_datadir}/nvim/runtime/syntax/aml.vim
%{_datadir}/nvim/runtime/syntax/ampl.vim
%{_datadir}/nvim/runtime/syntax/ant.vim
%{_datadir}/nvim/runtime/syntax/antlr.vim
%{_datadir}/nvim/runtime/syntax/apache.vim
%{_datadir}/nvim/runtime/syntax/apachestyle.vim
%{_datadir}/nvim/runtime/syntax/aptconf.vim
%{_datadir}/nvim/runtime/syntax/arch.vim
%{_datadir}/nvim/runtime/syntax/arduino.vim
%{_datadir}/nvim/runtime/syntax/art.vim
%{_datadir}/nvim/runtime/syntax/asciidoc.vim
%{_datadir}/nvim/runtime/syntax/asm.vim
%{_datadir}/nvim/runtime/syntax/asm68k.vim
%{_datadir}/nvim/runtime/syntax/asmh8300.vim
%{_datadir}/nvim/runtime/syntax/asn.vim
%{_datadir}/nvim/runtime/syntax/aspperl.vim
%{_datadir}/nvim/runtime/syntax/aspvbs.vim
%{_datadir}/nvim/runtime/syntax/asterisk.vim
%{_datadir}/nvim/runtime/syntax/asteriskvm.vim
%{_datadir}/nvim/runtime/syntax/atlas.vim
%{_datadir}/nvim/runtime/syntax/autodoc.vim
%{_datadir}/nvim/runtime/syntax/autohotkey.vim
%{_datadir}/nvim/runtime/syntax/autoit.vim
%{_datadir}/nvim/runtime/syntax/automake.vim
%{_datadir}/nvim/runtime/syntax/ave.vim
%{_datadir}/nvim/runtime/syntax/avra.vim
%{_datadir}/nvim/runtime/syntax/awk.vim
%{_datadir}/nvim/runtime/syntax/ayacc.vim
%{_datadir}/nvim/runtime/syntax/b.vim
%{_datadir}/nvim/runtime/syntax/baan.vim
%{_datadir}/nvim/runtime/syntax/basic.vim
%{_datadir}/nvim/runtime/syntax/bc.vim
%{_datadir}/nvim/runtime/syntax/bdf.vim
%{_datadir}/nvim/runtime/syntax/bib.vim
%{_datadir}/nvim/runtime/syntax/bindzone.vim
%{_datadir}/nvim/runtime/syntax/blank.vim
%{_datadir}/nvim/runtime/syntax/bst.vim
%{_datadir}/nvim/runtime/syntax/btm.vim
%{_datadir}/nvim/runtime/syntax/bzl.vim
%{_datadir}/nvim/runtime/syntax/bzr.vim
%{_datadir}/nvim/runtime/syntax/c.vim
%{_datadir}/nvim/runtime/syntax/cabal.vim
%{_datadir}/nvim/runtime/syntax/calendar.vim
%{_datadir}/nvim/runtime/syntax/catalog.vim
%{_datadir}/nvim/runtime/syntax/cdl.vim
%{_datadir}/nvim/runtime/syntax/cdrdaoconf.vim
%{_datadir}/nvim/runtime/syntax/cdrtoc.vim
%{_datadir}/nvim/runtime/syntax/cf.vim
%{_datadir}/nvim/runtime/syntax/cfg.vim
%{_datadir}/nvim/runtime/syntax/ch.vim
%{_datadir}/nvim/runtime/syntax/chaiscript.vim
%{_datadir}/nvim/runtime/syntax/change.vim
%{_datadir}/nvim/runtime/syntax/changelog.vim
%{_datadir}/nvim/runtime/syntax/chaskell.vim
%{_datadir}/nvim/runtime/syntax/cheetah.vim
%{_datadir}/nvim/runtime/syntax/chicken.vim
%{_datadir}/nvim/runtime/syntax/chill.vim
%{_datadir}/nvim/runtime/syntax/chordpro.vim
%{_datadir}/nvim/runtime/syntax/cl.vim
%{_datadir}/nvim/runtime/syntax/clean.vim
%{_datadir}/nvim/runtime/syntax/clipper.vim
%{_datadir}/nvim/runtime/syntax/clojure.vim
%{_datadir}/nvim/runtime/syntax/cmake.vim
%{_datadir}/nvim/runtime/syntax/cmod.vim
%{_datadir}/nvim/runtime/syntax/cmusrc.vim
%{_datadir}/nvim/runtime/syntax/cobol.vim
%{_datadir}/nvim/runtime/syntax/coco.vim
%{_datadir}/nvim/runtime/syntax/colortest.vim
%{_datadir}/nvim/runtime/syntax/conaryrecipe.vim
%{_datadir}/nvim/runtime/syntax/conf.vim
%{_datadir}/nvim/runtime/syntax/config.vim
%{_datadir}/nvim/runtime/syntax/context.vim
%{_datadir}/nvim/runtime/syntax/cpp.vim
%{_datadir}/nvim/runtime/syntax/crm.vim
%{_datadir}/nvim/runtime/syntax/crontab.vim
%{_datadir}/nvim/runtime/syntax/cs.vim
%{_datadir}/nvim/runtime/syntax/csc.vim
%{_datadir}/nvim/runtime/syntax/csdl.vim
%{_datadir}/nvim/runtime/syntax/csh.vim
%{_datadir}/nvim/runtime/syntax/csp.vim
%{_datadir}/nvim/runtime/syntax/css.vim
%{_datadir}/nvim/runtime/syntax/cterm.vim
%{_datadir}/nvim/runtime/syntax/ctrlh.vim
%{_datadir}/nvim/runtime/syntax/cucumber.vim
%{_datadir}/nvim/runtime/syntax/cuda.vim
%{_datadir}/nvim/runtime/syntax/cupl.vim
%{_datadir}/nvim/runtime/syntax/cuplsim.vim
%{_datadir}/nvim/runtime/syntax/cvs.vim
%{_datadir}/nvim/runtime/syntax/cvsrc.vim
%{_datadir}/nvim/runtime/syntax/cweb.vim
%{_datadir}/nvim/runtime/syntax/cynlib.vim
%{_datadir}/nvim/runtime/syntax/cynpp.vim
%{_datadir}/nvim/runtime/syntax/d.vim
%{_datadir}/nvim/runtime/syntax/datascript.vim
%{_datadir}/nvim/runtime/syntax/dcd.vim
%{_datadir}/nvim/runtime/syntax/dcl.vim
%{_datadir}/nvim/runtime/syntax/debchangelog.vim
%{_datadir}/nvim/runtime/syntax/debcontrol.vim
%{_datadir}/nvim/runtime/syntax/debcopyright.vim
%{_datadir}/nvim/runtime/syntax/debsources.vim
%{_datadir}/nvim/runtime/syntax/def.vim
%{_datadir}/nvim/runtime/syntax/denyhosts.vim
%{_datadir}/nvim/runtime/syntax/desc.vim
%{_datadir}/nvim/runtime/syntax/desktop.vim
%{_datadir}/nvim/runtime/syntax/dictconf.vim
%{_datadir}/nvim/runtime/syntax/dictdconf.vim
%{_datadir}/nvim/runtime/syntax/diff.vim
%{_datadir}/nvim/runtime/syntax/dircolors.vim
%{_datadir}/nvim/runtime/syntax/dirpager.vim
%{_datadir}/nvim/runtime/syntax/diva.vim
%{_datadir}/nvim/runtime/syntax/django.vim
%{_datadir}/nvim/runtime/syntax/dns.vim
%{_datadir}/nvim/runtime/syntax/dnsmasq.vim
%{_datadir}/nvim/runtime/syntax/docbk.vim
%{_datadir}/nvim/runtime/syntax/docbksgml.vim
%{_datadir}/nvim/runtime/syntax/docbkxml.vim
%{_datadir}/nvim/runtime/syntax/dockerfile.vim
%{_datadir}/nvim/runtime/syntax/dosbatch.vim
%{_datadir}/nvim/runtime/syntax/dosini.vim
%{_datadir}/nvim/runtime/syntax/dot.vim
%{_datadir}/nvim/runtime/syntax/doxygen.vim
%{_datadir}/nvim/runtime/syntax/dracula.vim
%{_datadir}/nvim/runtime/syntax/dsl.vim
%{_datadir}/nvim/runtime/syntax/dtd.vim
%{_datadir}/nvim/runtime/syntax/dtml.vim
%{_datadir}/nvim/runtime/syntax/dtrace.vim
%{_datadir}/nvim/runtime/syntax/dts.vim
%{_datadir}/nvim/runtime/syntax/dylan.vim
%{_datadir}/nvim/runtime/syntax/dylanintr.vim
%{_datadir}/nvim/runtime/syntax/dylanlid.vim
%{_datadir}/nvim/runtime/syntax/ecd.vim
%{_datadir}/nvim/runtime/syntax/edif.vim
%{_datadir}/nvim/runtime/syntax/eiffel.vim
%{_datadir}/nvim/runtime/syntax/elf.vim
%{_datadir}/nvim/runtime/syntax/elinks.vim
%{_datadir}/nvim/runtime/syntax/elmfilt.vim
%{_datadir}/nvim/runtime/syntax/erlang.vim
%{_datadir}/nvim/runtime/syntax/eruby.vim
%{_datadir}/nvim/runtime/syntax/esmtprc.vim
%{_datadir}/nvim/runtime/syntax/esqlc.vim
%{_datadir}/nvim/runtime/syntax/esterel.vim
%{_datadir}/nvim/runtime/syntax/eterm.vim
%{_datadir}/nvim/runtime/syntax/euphoria3.vim
%{_datadir}/nvim/runtime/syntax/euphoria4.vim
%{_datadir}/nvim/runtime/syntax/eviews.vim
%{_datadir}/nvim/runtime/syntax/exim.vim
%{_datadir}/nvim/runtime/syntax/expect.vim
%{_datadir}/nvim/runtime/syntax/exports.vim
%{_datadir}/nvim/runtime/syntax/falcon.vim
%{_datadir}/nvim/runtime/syntax/fan.vim
%{_datadir}/nvim/runtime/syntax/fasm.vim
%{_datadir}/nvim/runtime/syntax/fdcc.vim
%{_datadir}/nvim/runtime/syntax/fetchmail.vim
%{_datadir}/nvim/runtime/syntax/fgl.vim
%{_datadir}/nvim/runtime/syntax/flexwiki.vim
%{_datadir}/nvim/runtime/syntax/focexec.vim
%{_datadir}/nvim/runtime/syntax/form.vim
%{_datadir}/nvim/runtime/syntax/forth.vim
%{_datadir}/nvim/runtime/syntax/fortran.vim
%{_datadir}/nvim/runtime/syntax/foxpro.vim
%{_datadir}/nvim/runtime/syntax/framescript.vim
%{_datadir}/nvim/runtime/syntax/freebasic.vim
%{_datadir}/nvim/runtime/syntax/fstab.vim
%{_datadir}/nvim/runtime/syntax/fvwm.vim
%{_datadir}/nvim/runtime/syntax/fvwm2m4.vim
%{_datadir}/nvim/runtime/syntax/gdb.vim
%{_datadir}/nvim/runtime/syntax/gdmo.vim
%{_datadir}/nvim/runtime/syntax/gedcom.vim
%{_datadir}/nvim/runtime/syntax/git.vim
%{_datadir}/nvim/runtime/syntax/gitcommit.vim
%{_datadir}/nvim/runtime/syntax/gitconfig.vim
%{_datadir}/nvim/runtime/syntax/gitolite.vim
%{_datadir}/nvim/runtime/syntax/gitrebase.vim
%{_datadir}/nvim/runtime/syntax/gitsendemail.vim
%{_datadir}/nvim/runtime/syntax/gkrellmrc.vim
%{_datadir}/nvim/runtime/syntax/gnash.vim
%{_datadir}/nvim/runtime/syntax/gnuplot.vim
%{_datadir}/nvim/runtime/syntax/go.vim
%{_datadir}/nvim/runtime/syntax/godoc.vim
%{_datadir}/nvim/runtime/syntax/gp.vim
%{_datadir}/nvim/runtime/syntax/gpg.vim
%{_datadir}/nvim/runtime/syntax/gprof.vim
%{_datadir}/nvim/runtime/syntax/grads.vim
%{_datadir}/nvim/runtime/syntax/gretl.vim
%{_datadir}/nvim/runtime/syntax/groff.vim
%{_datadir}/nvim/runtime/syntax/groovy.vim
%{_datadir}/nvim/runtime/syntax/group.vim
%{_datadir}/nvim/runtime/syntax/grub.vim
%{_datadir}/nvim/runtime/syntax/gsp.vim
%{_datadir}/nvim/runtime/syntax/gtkrc.vim
%{_datadir}/nvim/runtime/syntax/haml.vim
%{_datadir}/nvim/runtime/syntax/hamster.vim
%{_datadir}/nvim/runtime/syntax/haskell.vim
%{_datadir}/nvim/runtime/syntax/haste.vim
%{_datadir}/nvim/runtime/syntax/hastepreproc.vim
%{_datadir}/nvim/runtime/syntax/hb.vim
%{_datadir}/nvim/runtime/syntax/help.vim
%{_datadir}/nvim/runtime/syntax/hercules.vim
%{_datadir}/nvim/runtime/syntax/hex.vim
%{_datadir}/nvim/runtime/syntax/hgcommit.vim
%{_datadir}/nvim/runtime/syntax/hitest.vim
%{_datadir}/nvim/runtime/syntax/hog.vim
%{_datadir}/nvim/runtime/syntax/hostconf.vim
%{_datadir}/nvim/runtime/syntax/hostsaccess.vim
%{_datadir}/nvim/runtime/syntax/html.vim
%{_datadir}/nvim/runtime/syntax/htmlcheetah.vim
%{_datadir}/nvim/runtime/syntax/htmldjango.vim
%{_datadir}/nvim/runtime/syntax/htmlm4.vim
%{_datadir}/nvim/runtime/syntax/htmlos.vim
%{_datadir}/nvim/runtime/syntax/ia64.vim
%{_datadir}/nvim/runtime/syntax/ibasic.vim
%{_datadir}/nvim/runtime/syntax/icemenu.vim
%{_datadir}/nvim/runtime/syntax/icon.vim
%{_datadir}/nvim/runtime/syntax/idl.vim
%{_datadir}/nvim/runtime/syntax/idlang.vim
%{_datadir}/nvim/runtime/syntax/indent.vim
%{_datadir}/nvim/runtime/syntax/inform.vim
%{_datadir}/nvim/runtime/syntax/initex.vim
%{_datadir}/nvim/runtime/syntax/initng.vim
%{_datadir}/nvim/runtime/syntax/inittab.vim
%{_datadir}/nvim/runtime/syntax/ipfilter.vim
%{_datadir}/nvim/runtime/syntax/ishd.vim
%{_datadir}/nvim/runtime/syntax/iss.vim
%{_datadir}/nvim/runtime/syntax/ist.vim
%{_datadir}/nvim/runtime/syntax/j.vim
%{_datadir}/nvim/runtime/syntax/jal.vim
%{_datadir}/nvim/runtime/syntax/jam.vim
%{_datadir}/nvim/runtime/syntax/jargon.vim
%{_datadir}/nvim/runtime/syntax/java.vim
%{_datadir}/nvim/runtime/syntax/javacc.vim
%{_datadir}/nvim/runtime/syntax/javascript.vim
%{_datadir}/nvim/runtime/syntax/jess.vim
%{_datadir}/nvim/runtime/syntax/jgraph.vim
%{_datadir}/nvim/runtime/syntax/jovial.vim
%{_datadir}/nvim/runtime/syntax/jproperties.vim
%{_datadir}/nvim/runtime/syntax/json.vim
%{_datadir}/nvim/runtime/syntax/jsp.vim
%{_datadir}/nvim/runtime/syntax/kconfig.vim
%{_datadir}/nvim/runtime/syntax/kivy.vim
%{_datadir}/nvim/runtime/syntax/kix.vim
%{_datadir}/nvim/runtime/syntax/kscript.vim
%{_datadir}/nvim/runtime/syntax/kwt.vim
%{_datadir}/nvim/runtime/syntax/lace.vim
%{_datadir}/nvim/runtime/syntax/latte.vim
%{_datadir}/nvim/runtime/syntax/ld.vim
%{_datadir}/nvim/runtime/syntax/ldapconf.vim
%{_datadir}/nvim/runtime/syntax/ldif.vim
%{_datadir}/nvim/runtime/syntax/less.vim
%{_datadir}/nvim/runtime/syntax/lex.vim
%{_datadir}/nvim/runtime/syntax/lftp.vim
%{_datadir}/nvim/runtime/syntax/lhaskell.vim
%{_datadir}/nvim/runtime/syntax/libao.vim
%{_datadir}/nvim/runtime/syntax/lifelines.vim
%{_datadir}/nvim/runtime/syntax/lilo.vim
%{_datadir}/nvim/runtime/syntax/limits.vim
%{_datadir}/nvim/runtime/syntax/liquid.vim
%{_datadir}/nvim/runtime/syntax/lisp.vim
%{_datadir}/nvim/runtime/syntax/lite.vim
%{_datadir}/nvim/runtime/syntax/litestep.vim
%{_datadir}/nvim/runtime/syntax/loginaccess.vim
%{_datadir}/nvim/runtime/syntax/logindefs.vim
%{_datadir}/nvim/runtime/syntax/logtalk.vim
%{_datadir}/nvim/runtime/syntax/lotos.vim
%{_datadir}/nvim/runtime/syntax/lout.vim
%{_datadir}/nvim/runtime/syntax/lpc.vim
%{_datadir}/nvim/runtime/syntax/lprolog.vim
%{_datadir}/nvim/runtime/syntax/lscript.vim
%{_datadir}/nvim/runtime/syntax/lsl.vim
%{_datadir}/nvim/runtime/syntax/lss.vim
%{_datadir}/nvim/runtime/syntax/lua.vim
%{_datadir}/nvim/runtime/syntax/lynx.vim
%{_datadir}/nvim/runtime/syntax/m4.vim
%{_datadir}/nvim/runtime/syntax/mail.vim
%{_datadir}/nvim/runtime/syntax/mailaliases.vim
%{_datadir}/nvim/runtime/syntax/mailcap.vim
%{_datadir}/nvim/runtime/syntax/make.vim
%{_datadir}/nvim/runtime/syntax/mallard.vim
%{_datadir}/nvim/runtime/syntax/man.vim
%{_datadir}/nvim/runtime/syntax/manconf.vim
%{_datadir}/nvim/runtime/syntax/manual.vim
%{_datadir}/nvim/runtime/syntax/maple.vim
%{_datadir}/nvim/runtime/syntax/markdown.vim
%{_datadir}/nvim/runtime/syntax/masm.vim
%{_datadir}/nvim/runtime/syntax/mason.vim
%{_datadir}/nvim/runtime/syntax/master.vim
%{_datadir}/nvim/runtime/syntax/matlab.vim
%{_datadir}/nvim/runtime/syntax/maxima.vim
%{_datadir}/nvim/runtime/syntax/mel.vim
%{_datadir}/nvim/runtime/syntax/messages.vim
%{_datadir}/nvim/runtime/syntax/mf.vim
%{_datadir}/nvim/runtime/syntax/mgl.vim
%{_datadir}/nvim/runtime/syntax/mgp.vim
%{_datadir}/nvim/runtime/syntax/mib.vim
%{_datadir}/nvim/runtime/syntax/mix.vim
%{_datadir}/nvim/runtime/syntax/mma.vim
%{_datadir}/nvim/runtime/syntax/mmix.vim
%{_datadir}/nvim/runtime/syntax/mmp.vim
%{_datadir}/nvim/runtime/syntax/modconf.vim
%{_datadir}/nvim/runtime/syntax/model.vim
%{_datadir}/nvim/runtime/syntax/modsim3.vim
%{_datadir}/nvim/runtime/syntax/modula2.vim
%{_datadir}/nvim/runtime/syntax/modula3.vim
%{_datadir}/nvim/runtime/syntax/monk.vim
%{_datadir}/nvim/runtime/syntax/moo.vim
%{_datadir}/nvim/runtime/syntax/mp.vim
%{_datadir}/nvim/runtime/syntax/mplayerconf.vim
%{_datadir}/nvim/runtime/syntax/mrxvtrc.vim
%{_datadir}/nvim/runtime/syntax/msidl.vim
%{_datadir}/nvim/runtime/syntax/msmessages.vim
%{_datadir}/nvim/runtime/syntax/msql.vim
%{_datadir}/nvim/runtime/syntax/mupad.vim
%{_datadir}/nvim/runtime/syntax/murphi.vim
%{_datadir}/nvim/runtime/syntax/mush.vim
%{_datadir}/nvim/runtime/syntax/muttrc.vim
%{_datadir}/nvim/runtime/syntax/mysql.vim
%{_datadir}/nvim/runtime/syntax/n1ql.vim
%{_datadir}/nvim/runtime/syntax/named.vim
%{_datadir}/nvim/runtime/syntax/nanorc.vim
%{_datadir}/nvim/runtime/syntax/nasm.vim
%{_datadir}/nvim/runtime/syntax/nastran.vim
%{_datadir}/nvim/runtime/syntax/natural.vim
%{_datadir}/nvim/runtime/syntax/ncf.vim
%{_datadir}/nvim/runtime/syntax/neomuttrc.vim
%{_datadir}/nvim/runtime/syntax/netrc.vim
%{_datadir}/nvim/runtime/syntax/netrw.vim
%{_datadir}/nvim/runtime/syntax/ninja.vim
%{_datadir}/nvim/runtime/syntax/nosyntax.vim
%{_datadir}/nvim/runtime/syntax/nqc.vim
%{_datadir}/nvim/runtime/syntax/nroff.vim
%{_datadir}/nvim/runtime/syntax/nsis.vim
%{_datadir}/nvim/runtime/syntax/obj.vim
%{_datadir}/nvim/runtime/syntax/objc.vim
%{_datadir}/nvim/runtime/syntax/objcpp.vim
%{_datadir}/nvim/runtime/syntax/ocaml.vim
%{_datadir}/nvim/runtime/syntax/occam.vim
%{_datadir}/nvim/runtime/syntax/omnimark.vim
%{_datadir}/nvim/runtime/syntax/openroad.vim
%{_datadir}/nvim/runtime/syntax/opl.vim
%{_datadir}/nvim/runtime/syntax/ora.vim
%{_datadir}/nvim/runtime/syntax/pamconf.vim
%{_datadir}/nvim/runtime/syntax/papp.vim
%{_datadir}/nvim/runtime/syntax/pascal.vim
%{_datadir}/nvim/runtime/syntax/passwd.vim
%{_datadir}/nvim/runtime/syntax/pcap.vim
%{_datadir}/nvim/runtime/syntax/pccts.vim
%{_datadir}/nvim/runtime/syntax/pdf.vim
%{_datadir}/nvim/runtime/syntax/perl.vim
%{_datadir}/nvim/runtime/syntax/perl6.vim
%{_datadir}/nvim/runtime/syntax/pf.vim
%{_datadir}/nvim/runtime/syntax/pfmain.vim
%{_datadir}/nvim/runtime/syntax/php.vim
%{_datadir}/nvim/runtime/syntax/phtml.vim
%{_datadir}/nvim/runtime/syntax/pic.vim
%{_datadir}/nvim/runtime/syntax/pike.vim
%{_datadir}/nvim/runtime/syntax/pilrc.vim
%{_datadir}/nvim/runtime/syntax/pine.vim
%{_datadir}/nvim/runtime/syntax/pinfo.vim
%{_datadir}/nvim/runtime/syntax/plaintex.vim
%{_datadir}/nvim/runtime/syntax/pli.vim
%{_datadir}/nvim/runtime/syntax/plm.vim
%{_datadir}/nvim/runtime/syntax/plp.vim
%{_datadir}/nvim/runtime/syntax/plsql.vim
%{_datadir}/nvim/runtime/syntax/po.vim
%{_datadir}/nvim/runtime/syntax/pod.vim
%{_datadir}/nvim/runtime/syntax/postscr.vim
%{_datadir}/nvim/runtime/syntax/pov.vim
%{_datadir}/nvim/runtime/syntax/povini.vim
%{_datadir}/nvim/runtime/syntax/ppd.vim
%{_datadir}/nvim/runtime/syntax/ppwiz.vim
%{_datadir}/nvim/runtime/syntax/prescribe.vim
%{_datadir}/nvim/runtime/syntax/privoxy.vim
%{_datadir}/nvim/runtime/syntax/procmail.vim
%{_datadir}/nvim/runtime/syntax/progress.vim
%{_datadir}/nvim/runtime/syntax/prolog.vim
%{_datadir}/nvim/runtime/syntax/promela.vim
%{_datadir}/nvim/runtime/syntax/proto.vim
%{_datadir}/nvim/runtime/syntax/protocols.vim
%{_datadir}/nvim/runtime/syntax/psf.vim
%{_datadir}/nvim/runtime/syntax/ptcap.vim
%{_datadir}/nvim/runtime/syntax/purifylog.vim
%{_datadir}/nvim/runtime/syntax/pyrex.vim
%{_datadir}/nvim/runtime/syntax/python.vim
%{_datadir}/nvim/runtime/syntax/qf.vim
%{_datadir}/nvim/runtime/syntax/quake.vim
%{_datadir}/nvim/runtime/syntax/r.vim
%{_datadir}/nvim/runtime/syntax/racc.vim
%{_datadir}/nvim/runtime/syntax/radiance.vim
%{_datadir}/nvim/runtime/syntax/ratpoison.vim
%{_datadir}/nvim/runtime/syntax/rc.vim
%{_datadir}/nvim/runtime/syntax/rcs.vim
%{_datadir}/nvim/runtime/syntax/rcslog.vim
%{_datadir}/nvim/runtime/syntax/readline.vim
%{_datadir}/nvim/runtime/syntax/rebol.vim
%{_datadir}/nvim/runtime/syntax/redif.vim
%{_datadir}/nvim/runtime/syntax/registry.vim
%{_datadir}/nvim/runtime/syntax/remind.vim
%{_datadir}/nvim/runtime/syntax/resolv.vim
%{_datadir}/nvim/runtime/syntax/reva.vim
%{_datadir}/nvim/runtime/syntax/rexx.vim
%{_datadir}/nvim/runtime/syntax/rhelp.vim
%{_datadir}/nvim/runtime/syntax/rib.vim
%{_datadir}/nvim/runtime/syntax/rmd.vim
%{_datadir}/nvim/runtime/syntax/rnc.vim
%{_datadir}/nvim/runtime/syntax/rng.vim
%{_datadir}/nvim/runtime/syntax/rnoweb.vim
%{_datadir}/nvim/runtime/syntax/robots.vim
%{_datadir}/nvim/runtime/syntax/rpcgen.vim
%{_datadir}/nvim/runtime/syntax/rpl.vim
%{_datadir}/nvim/runtime/syntax/rrst.vim
%{_datadir}/nvim/runtime/syntax/rst.vim
%{_datadir}/nvim/runtime/syntax/rtf.vim
%{_datadir}/nvim/runtime/syntax/ruby.vim
%{_datadir}/nvim/runtime/syntax/rust.vim
%{_datadir}/nvim/runtime/syntax/samba.vim
%{_datadir}/nvim/runtime/syntax/sas.vim
%{_datadir}/nvim/runtime/syntax/sass.vim
%{_datadir}/nvim/runtime/syntax/sather.vim
%{_datadir}/nvim/runtime/syntax/sbt.vim
%{_datadir}/nvim/runtime/syntax/scala.vim
%{_datadir}/nvim/runtime/syntax/scheme.vim
%{_datadir}/nvim/runtime/syntax/scilab.vim
%{_datadir}/nvim/runtime/syntax/screen.vim
%{_datadir}/nvim/runtime/syntax/scss.vim
%{_datadir}/nvim/runtime/syntax/sd.vim
%{_datadir}/nvim/runtime/syntax/sdc.vim
%{_datadir}/nvim/runtime/syntax/sdl.vim
%{_datadir}/nvim/runtime/syntax/sed.vim
%{_datadir}/nvim/runtime/syntax/sendpr.vim
%{_datadir}/nvim/runtime/syntax/sensors.vim
%{_datadir}/nvim/runtime/syntax/services.vim
%{_datadir}/nvim/runtime/syntax/setserial.vim
%{_datadir}/nvim/runtime/syntax/sgml.vim
%{_datadir}/nvim/runtime/syntax/sgmldecl.vim
%{_datadir}/nvim/runtime/syntax/sgmllnx.vim
%{_datadir}/nvim/runtime/syntax/sh.vim
%{_datadir}/nvim/runtime/syntax/shada.vim
%{_datadir}/nvim/runtime/syntax/sicad.vim
%{_datadir}/nvim/runtime/syntax/sieve.vim
%{_datadir}/nvim/runtime/syntax/simula.vim
%{_datadir}/nvim/runtime/syntax/sinda.vim
%{_datadir}/nvim/runtime/syntax/sindacmp.vim
%{_datadir}/nvim/runtime/syntax/sindaout.vim
%{_datadir}/nvim/runtime/syntax/sisu.vim
%{_datadir}/nvim/runtime/syntax/skill.vim
%{_datadir}/nvim/runtime/syntax/sl.vim
%{_datadir}/nvim/runtime/syntax/slang.vim
%{_datadir}/nvim/runtime/syntax/slice.vim
%{_datadir}/nvim/runtime/syntax/slpconf.vim
%{_datadir}/nvim/runtime/syntax/slpreg.vim
%{_datadir}/nvim/runtime/syntax/slpspi.vim
%{_datadir}/nvim/runtime/syntax/slrnrc.vim
%{_datadir}/nvim/runtime/syntax/slrnsc.vim
%{_datadir}/nvim/runtime/syntax/sm.vim
%{_datadir}/nvim/runtime/syntax/smarty.vim
%{_datadir}/nvim/runtime/syntax/smcl.vim
%{_datadir}/nvim/runtime/syntax/smil.vim
%{_datadir}/nvim/runtime/syntax/smith.vim
%{_datadir}/nvim/runtime/syntax/sml.vim
%{_datadir}/nvim/runtime/syntax/snnsnet.vim
%{_datadir}/nvim/runtime/syntax/snnspat.vim
%{_datadir}/nvim/runtime/syntax/snnsres.vim
%{_datadir}/nvim/runtime/syntax/snobol4.vim
%{_datadir}/nvim/runtime/syntax/spec.vim
%{_datadir}/nvim/runtime/syntax/specman.vim
%{_datadir}/nvim/runtime/syntax/spice.vim
%{_datadir}/nvim/runtime/syntax/splint.vim
%{_datadir}/nvim/runtime/syntax/spup.vim
%{_datadir}/nvim/runtime/syntax/spyce.vim
%{_datadir}/nvim/runtime/syntax/sql.vim
%{_datadir}/nvim/runtime/syntax/sqlanywhere.vim
%{_datadir}/nvim/runtime/syntax/sqlforms.vim
%{_datadir}/nvim/runtime/syntax/sqlhana.vim
%{_datadir}/nvim/runtime/syntax/sqlinformix.vim
%{_datadir}/nvim/runtime/syntax/sqlj.vim
%{_datadir}/nvim/runtime/syntax/sqloracle.vim
%{_datadir}/nvim/runtime/syntax/sqr.vim
%{_datadir}/nvim/runtime/syntax/squid.vim
%{_datadir}/nvim/runtime/syntax/srec.vim
%{_datadir}/nvim/runtime/syntax/sshconfig.vim
%{_datadir}/nvim/runtime/syntax/sshdconfig.vim
%{_datadir}/nvim/runtime/syntax/st.vim
%{_datadir}/nvim/runtime/syntax/stata.vim
%{_datadir}/nvim/runtime/syntax/stp.vim
%{_datadir}/nvim/runtime/syntax/strace.vim
%{_datadir}/nvim/runtime/syntax/sudoers.vim
%{_datadir}/nvim/runtime/syntax/svg.vim
%{_datadir}/nvim/runtime/syntax/svn.vim
%{_datadir}/nvim/runtime/syntax/syncolor.vim
%{_datadir}/nvim/runtime/syntax/synload.vim
%{_datadir}/nvim/runtime/syntax/syntax.vim
%{_datadir}/nvim/runtime/syntax/sysctl.vim
%{_datadir}/nvim/runtime/syntax/systemd.vim
%{_datadir}/nvim/runtime/syntax/systemverilog.vim
%{_datadir}/nvim/runtime/syntax/tads.vim
%{_datadir}/nvim/runtime/syntax/tags.vim
%{_datadir}/nvim/runtime/syntax/tak.vim
%{_datadir}/nvim/runtime/syntax/takcmp.vim
%{_datadir}/nvim/runtime/syntax/takout.vim
%{_datadir}/nvim/runtime/syntax/tap.vim
%{_datadir}/nvim/runtime/syntax/tar.vim
%{_datadir}/nvim/runtime/syntax/taskdata.vim
%{_datadir}/nvim/runtime/syntax/taskedit.vim
%{_datadir}/nvim/runtime/syntax/tasm.vim
%{_datadir}/nvim/runtime/syntax/tcl.vim
%{_datadir}/nvim/runtime/syntax/tcsh.vim
%{_datadir}/nvim/runtime/syntax/teraterm.vim
%{_datadir}/nvim/runtime/syntax/terminfo.vim
%{_datadir}/nvim/runtime/syntax/tex.vim
%{_datadir}/nvim/runtime/syntax/texinfo.vim
%{_datadir}/nvim/runtime/syntax/texmf.vim
%{_datadir}/nvim/runtime/syntax/tf.vim
%{_datadir}/nvim/runtime/syntax/tidy.vim
%{_datadir}/nvim/runtime/syntax/tilde.vim
%{_datadir}/nvim/runtime/syntax/tli.vim
%{_datadir}/nvim/runtime/syntax/tmux.vim
%{_datadir}/nvim/runtime/syntax/tpp.vim
%{_datadir}/nvim/runtime/syntax/trasys.vim
%{_datadir}/nvim/runtime/syntax/treetop.vim
%{_datadir}/nvim/runtime/syntax/trustees.vim
%{_datadir}/nvim/runtime/syntax/tsalt.vim
%{_datadir}/nvim/runtime/syntax/tsscl.vim
%{_datadir}/nvim/runtime/syntax/tssgm.vim
%{_datadir}/nvim/runtime/syntax/tssop.vim
%{_datadir}/nvim/runtime/syntax/tt2.vim
%{_datadir}/nvim/runtime/syntax/tt2html.vim
%{_datadir}/nvim/runtime/syntax/tt2js.vim
%{_datadir}/nvim/runtime/syntax/tutor.vim
%{_datadir}/nvim/runtime/syntax/uc.vim
%{_datadir}/nvim/runtime/syntax/udevconf.vim
%{_datadir}/nvim/runtime/syntax/udevperm.vim
%{_datadir}/nvim/runtime/syntax/udevrules.vim
%{_datadir}/nvim/runtime/syntax/uil.vim
%{_datadir}/nvim/runtime/syntax/updatedb.vim
%{_datadir}/nvim/runtime/syntax/upstart.vim
%{_datadir}/nvim/runtime/syntax/upstreamdat.vim
%{_datadir}/nvim/runtime/syntax/upstreaminstalllog.vim
%{_datadir}/nvim/runtime/syntax/upstreamlog.vim
%{_datadir}/nvim/runtime/syntax/upstreamrpt.vim
%{_datadir}/nvim/runtime/syntax/usserverlog.vim
%{_datadir}/nvim/runtime/syntax/usw2kagtlog.vim
%{_datadir}/nvim/runtime/syntax/valgrind.vim
%{_datadir}/nvim/runtime/syntax/vb.vim
%{_datadir}/nvim/runtime/syntax/vera.vim
%{_datadir}/nvim/runtime/syntax/verilog.vim
%{_datadir}/nvim/runtime/syntax/verilogams.vim
%{_datadir}/nvim/runtime/syntax/vgrindefs.vim
%{_datadir}/nvim/runtime/syntax/vhdl.vim
%{_datadir}/nvim/runtime/syntax/vim.vim
%{_datadir}/nvim/runtime/syntax/viminfo.vim
%{_datadir}/nvim/runtime/syntax/vimnormal.vim
%{_datadir}/nvim/runtime/syntax/virata.vim
%{_datadir}/nvim/runtime/syntax/vmasm.vim
%{_datadir}/nvim/runtime/syntax/voscm.vim
%{_datadir}/nvim/runtime/syntax/vrml.vim
%{_datadir}/nvim/runtime/syntax/vroom.vim
%{_datadir}/nvim/runtime/syntax/vsejcl.vim
%{_datadir}/nvim/runtime/syntax/wast.vim
%{_datadir}/nvim/runtime/syntax/wdiff.vim
%{_datadir}/nvim/runtime/syntax/web.vim
%{_datadir}/nvim/runtime/syntax/webmacro.vim
%{_datadir}/nvim/runtime/syntax/wget.vim
%{_datadir}/nvim/runtime/syntax/whitespace.vim
%{_datadir}/nvim/runtime/syntax/winbatch.vim
%{_datadir}/nvim/runtime/syntax/wml.vim
%{_datadir}/nvim/runtime/syntax/wsh.vim
%{_datadir}/nvim/runtime/syntax/wsml.vim
%{_datadir}/nvim/runtime/syntax/wvdial.vim
%{_datadir}/nvim/runtime/syntax/xbl.vim
%{_datadir}/nvim/runtime/syntax/xdefaults.vim
%{_datadir}/nvim/runtime/syntax/xf86conf.vim
%{_datadir}/nvim/runtime/syntax/xhtml.vim
%{_datadir}/nvim/runtime/syntax/xinetd.vim
%{_datadir}/nvim/runtime/syntax/xkb.vim
%{_datadir}/nvim/runtime/syntax/xmath.vim
%{_datadir}/nvim/runtime/syntax/xml.vim
%{_datadir}/nvim/runtime/syntax/xmodmap.vim
%{_datadir}/nvim/runtime/syntax/xpm.vim
%{_datadir}/nvim/runtime/syntax/xpm2.vim
%{_datadir}/nvim/runtime/syntax/xquery.vim
%{_datadir}/nvim/runtime/syntax/xs.vim
%{_datadir}/nvim/runtime/syntax/xsd.vim
%{_datadir}/nvim/runtime/syntax/xslt.vim
%{_datadir}/nvim/runtime/syntax/xxd.vim
%{_datadir}/nvim/runtime/syntax/yacc.vim
%{_datadir}/nvim/runtime/syntax/yaml.vim
%{_datadir}/nvim/runtime/syntax/z8a.vim
%{_datadir}/nvim/runtime/syntax/zimbu.vim
%{_datadir}/nvim/runtime/syntax/zsh.vim

%dir %{_datadir}/nvim/runtime/syntax/vim
%{_datadir}/nvim/runtime/syntax/vim/generated.vim

%dir %{_datadir}/nvim/runtime/tools
%{_datadir}/nvim/runtime/tools/check_colors.vim

%dir %{_datadir}/nvim/runtime/tutor
%{_datadir}/nvim/runtime/tutor/tutor.tutor
%{_datadir}/nvim/runtime/tutor/tutor.tutor.json

%dir %{_datadir}/nvim/runtime/tutor/en
%{_datadir}/nvim/runtime/tutor/en/vim-01-beginner.tutor
%{_datadir}/nvim/runtime/tutor/en/vim-01-beginner.tutor.json

%changelog
* Sun Jan 06 2019 Andreas Schneider <asn@redhat.com> - 0.3.3-1
- Update to version 0.3.3

* Wed Jan 02 2019 Andreas Schneider <asn@redhat.com> - 0.3.2-1
- Update to version 0.3.2

* Fri Aug 10 2018 Andreas Schneider <asn@redhat.com> - 0.3.1-1
- Update to version 0.3.1

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.3.0-6
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-5
- Rebuild for new binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-4
- Disable jemalloc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Andreas Schneider <asn@redhat.com> - 0.3.0-2
- resolves: #1592474 - Add jemalloc as a requirement

* Mon Jun 11 2018 Andreas Schneider <asn@redhat.com> - 0.3.0-1
- Update to version 0.3.0
- resolves: #1450624 - Set default python_host_prog

* Sat May 26 2018 Andreas Schneider <asn@redhat.com> - 0.2.2-3
- Rebuild against unibilium-2.0.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 23 2017 Andreas Schneider <asn@redhat.com> - 0.2.2-1
- resolves: #1510899 - Update to version 0.2.2

* Wed Nov 08 2017 Andreas Schneider <asn@redhat.com> - 0.2.1-1
- resolves: #1510762 - Update to version 0.2.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Than Ngo <than@redhat.com> 0.2.0-3
- fixed bz#1451143, ppc64/le build failure

* Mon May 15 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.2.0-2
- Adjust spec for building on epel7

* Mon May 08 2017 Andreas Schneider <asn@redhat.com> - 0.2.0-1
- resolves: #1447481 - Update to 0.2.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 0.1.7-6
- Add RPM spec file template

* Thu Dec 08 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 0.1.7-5
- Add recommends for python2-neovim and xsel
- Remove unused CMake options
- Use %%make_build and %%make_install macros
- Remove unnecessary %%defattr directive

* Mon Dec 05 2016 Andreas Schneider <asn@redhat.com> - 0.1.7-4
- Set license file correctly

* Mon Dec 05 2016 Andreas Schneider <asn@redhat.com> - 0.1.7-3
- Update build requires

* Mon Dec 05 2016 Andreas Schneider <asn@redhat.com> - 0.1.7-2
- Add Recommends for python3-neovim
- Use 'bit32' from lua 5.3

* Mon Nov 28 2016 Andreas Schneider <asn@redhat.com> - 0.1.7-1
- Update to version 0.1.7

* Tue Nov 15 2016 Andreas Schneider <asn@redhat.com> - 0.1.6-2
- Removed Group:
- Removed BuildRoot:

* Thu Nov 10 2016 Andreas Schneider <asn@redhat.com> - 0.1.6-1
- Initial version 0.1.6
