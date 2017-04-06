PATCHELF_VERSION="0.6"
PATCHELF_TGZ_URL="https://github.com/NixOS/patchelf/archive/${PATCHELF_VERSION}.tar.gz"
PATCHELF_BASE='/tmp/patchelf'
PATCHELF_TGZ_LOCAL="${PATCHELF_BASE}/patchelf-${PATCHELF_VERSION}.tgz"
PATCHELF_SRC_LOCAL="${PATCHELF_BASE}/patchelf-${PATCHELF_VERSION}"

patchelf_git(){
  shout "installing PatchElf from Git"
  _CURR_DIR=`pwd`
  mkdir -p $PATCHELF_BASE
  cd $PATCHELF_BASE
  wget -c -O "${PATCHELF_TGZ_LOCAL}" "${PATCHELF_TGZ_URL}"
  tar zxvf "${PATCHELF_TGZ_LOCAL}"

  cd $PATCHELF_SRC_LOCAL
  sh bootstrap.sh
  ./configure
  make
  make install
  cd $_CURR_DIR
}

patchelf_git
