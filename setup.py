#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-
"""
BanbBang ``setup.py``

Metadata see :py:module:`bangbang/__pkginfo__.py`
"""

from os.path import join, dirname, abspath
import imp
from setuptools import setup

ROOT = abspath(dirname(__file__))
SRC = join(ROOT, 'src', 'bangbang')
PKG = imp.load_source('__pkginfo__', join(SRC, '__pkginfo__.py'))

# https://packaging.python.org/guides/distributing-packages-using-setuptools/#configuring-your-project
setup(
    name               = PKG.package
    , version          = PKG.version
    , description      = PKG.description
    , long_description = PKG.long_description
    , url              = PKG.url

    , author           = PKG.author
    , author_email     = PKG.author_email
    , maintainer       = PKG.maintainer
    , maintainer_email = PKG.maintainer_email

    , license          = PKG.license
    , classifiers      = PKG.classifiers
    , keywords         = PKG.keywords
    , project_urls     = PKG.project_urls

    , packages         = PKG.packages
    , package_dir      = PKG.package_dir
    , py_modules       = PKG.py_modules

    , install_requires = PKG.install_requires
    , python_requires  = PKG.python_requires

    , package_data     = PKG.package_data
    , data_files       = PKG.data_files
    , entry_points     = PKG.get_entry_points()

    , extras_require   = {
        # usage: pip install .\[develop,test\]
        # - https://pip.pypa.io/en/stable/reference/pip_install/#examples
        # - https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies
        'develop' : PKG.develop_requires
        , 'test'  : PKG.test_requires
    }

)
