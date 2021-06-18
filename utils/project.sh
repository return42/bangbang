#!/usr/bin/env bash
# -*- coding: utf-8; mode: sh indent-tabs-mode: nil -*-
# SPDX-License-Identifier: AGPL-3.0-or-later

# shellcheck source=utils/lib.sh
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

# apt packages
PROD_PACKAGES_debian="\
python3-dev python3-venv git build-essential shellcheck"

BUILD_PACKAGES_debian="\
graphviz imagemagick texlive-xetex librsvg2-bin
texlive-latex-recommended texlive-extra-utils fonts-dejavu
latexmk"

case $DIST_ID-$DIST_VERS in
    ubuntu-*|debian-*)
        PROD_PACKAGES="${PROD_PACKAGES_debian}"
        BUILD_PACKAGES="${BUILD_PACKAGES_debian}"
        ;;
    *)
        die 42 "$DIST_ID-$DIST_VERS: not yet implemented"
        ;;
esac

usage() {
    cat <<EOF
usage::
  $(basename "$0") install    [packages|buildhost]

install:
  :packages:   install needed packages from OS package manager
  :buildhost:  install packages from OS package manager needed by buildhosts

EOF
    [[ -n ${1} ]] &&  err_msg "$1"

}

main() {

    required_commands \
        sudo systemctl install git \
        || exit

    local _usage="unknown or missing $1 command:: $2"

    case $1 in
        --getenv)  var="$2"; echo "${!var}"; exit 0;;
        -h|--help) usage; exit 0;;

        install)
            sudo_or_exit
            case $2 in
                packages)
                    pkg_install "$PROD_PACKAGES"
                    ;;
                buildhost)
                    pkg_install "$PROD_PACKAGES"
                    pkg_install "$BUILD_PACKAGES"
                    ;;
                *) usage "$_usage"; exit 42;;
            esac
            ;;
        *) usage "unknown or missing command:: $1"; exit 42;;
    esac
}

# ----------------------------------------------------------------------------
main "$@"
# ----------------------------------------------------------------------------
