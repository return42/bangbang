# -*- coding: utf-8; mode: makefile-gmake -*-
# SPDX-License-Identifier: AGPL-3.0-or-later

.DEFAULT_GOAL=help
export MTOOLS=./manage

include utils/makefile.include

all: clean install

PHONY += help

help:
	@./manage --help
	@echo ''
	@echo 'install     : developer install into virtualenv'
	@echo 'uninstall   : uninstall developer installation'
	@echo 'clean       : clean up working tree'
	@echo 'test        : run local tests'
	@echo 'ci.test     : run CI tests'

PHONY += install uninstall
install uninstall:
	$(Q)./manage pyenv.$@

PHONY += clean
clean: py.clean docs.clean

PHONY += test ci.test test.shell
ci.test: test
test:    test.pylint test.shell
test.shell:
	$(Q)shellcheck --shell=bash --color=never --external-sources --format=tty \
		manage \
		utils/project.sh \
		utils/lib.sh
	$(Q)./manage build_msg TEST "$@ OK"

# wrap ./manage script

MANAGE += docs.html docs.live docs.gh-pages docs.clean
MANAGE += py.build py.clean
MANAGE += pyenv pyenv.install pyenv.uninstall
MANAGE += pypi.upload pypi.upload.test
MANAGE += test.pylint test.clean
MANAGE += prj.update

PHONY += $(MANAGE)

$(MANAGE):
	$(Q)$(MTOOLS) $@
