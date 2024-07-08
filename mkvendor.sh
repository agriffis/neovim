 #!/usr/bin/bash -x

set -euo pipefail

main() {
  rm -rf vendor
  cmake -S cmake.deps -B vendor -G Ninja -DUSE_BUNDLED=OFF -DUSE_BUNDLED_TS_PARSERS=ON
  targets=$(basename -a vendor/build/downloads/treesitter_* | xargs -I {} echo build/src/{}-stamp/{}-download)
  ninja -C vendor ${targets}
  tar czf vendor.tar.gz -H pax --numeric-owner --owner=0:0 vendor/build/downloads
  exit # https://arongriffis.com/2023-11-18-bash-main
}

main "$@"
