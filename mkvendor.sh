 #!/usr/bin/bash -x

set -euo pipefail

main() {
  rm -rf .deps
  cmake -S cmake.deps -B .deps -G Ninja -DUSE_BUNDLED=OFF -DUSE_BUNDLED_TS_PARSERS=ON
  targets=$(basename -a .deps/build/downloads/treesitter_* | xargs -I {} echo build/src/{}-stamp/{}-download)
  ninja -C .deps ${targets}
  rm -rf vendor
  mkdir -p vendor/build
  cp -a --reflink=always .deps/build/downloads vendor/build
  exit # https://arongriffis.com/2023-11-18-bash-main
}

main "$@"
