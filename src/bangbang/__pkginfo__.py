"""Python package meta information used by setup.py and other project files.

Single point of source for all package metadata.  After modifying this file it
is needed to recreate some project files (``make prj.update``)::

  python -c "from __pkginfo__ import *; print(README)" > README.rst
  python -c "from __pkginfo__ import *; print(requirements_txt)" > requirements.txt

About python packaging see `Python Packaging Authority`_.  Most of the names
here are mapped to ``setup(<name1>=..., <name2>=...)`` arguments in
``setup.py``.  See `Packaging and distributing projects`_ about ``setup(...)``
arguments.  If this is all new for you, start with `PyPI Quick and Dirty`_.

Further read:

- pythonwheels_
- setuptools_
- packaging_
- sdist_
- installing_

.. _`Python Packaging Authority`:
   https://www.pypa.io
.. _`Packaging and distributing projects`:
    https://packaging.python.org/guides/distributing-packages-using-setuptools/
.. _`PyPI Quick and Dirty`:
   https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
.. _pythonwheels:
   https://pythonwheels.com/
.. _setuptools:
   https://setuptools.readthedocs.io/en/latest/setuptools.html
.. _packaging:
   https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-and-distributing-projects
.. _sdist:
    https://packaging.python.org/guides/distributing-packages-using-setuptools/#source-distributions
.. _bdist_wheel:
   https://packaging.python.org/guides/distributing-packages-using-setuptools/#pure-python-wheels
.. _installing:
   https://packaging.python.org/tutorials/installing-packages/

"""
# pylint: enable=line-too-long

from setuptools import find_packages

org = 'return42'
project = 'BangBang (!!)'
package = 'bangbang'
version = '20210101'

copyright = '2021 Markus Heiser'  # pylint: disable=redefined-builtin
license = 'AGPL-3.0-or-later'     # pylint: disable=redefined-builtin

cls_lic = "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)"
description = 'Bangs from duckduckgo and more.'

url = 'https://github.com/%s/%s' % (org, package)
docs = 'https://%s.github.io/%s' % (org, package)
issues = url + '/issues'

author = 'Markus Heiser'
author_email = 'markus.heiser@darmarit.de'
maintainer = 'Markus Heiser'
maintainer_email = 'markus.heiser@darmarit.de'

authors      = [author, ]
emails       = [author_email, ]
keywords     = ''

maintainers = [maintainer, ]

project_urls = {
    'Documentation' : docs,
    'Code' : url,
    'Issue tracker' : issues,
}

# When your source code is in a subdirectory under the project root, e.g.
# `src/`, it is necessary to specify the `package_dir` argument.
# https://docs.python.org/3/distutils/setupscript.html#listing-whole-packages
package_dir = {'': 'src'}

packages = find_packages(where="src", exclude=['docs', 'tests'])

# https://packaging.python.org/guides/distributing-packages-using-setuptools/#py-modules
py_modules = []

# If there are data files included in your packages that need to be
# installed, specify them here.
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#package-data
# https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html
package_data = {
#     'xxxx' : [
#         'config.ini',
#         'log.ini',
#         'mime.types',
#     ]
}

# Although 'package_data' is the preferred approach, in some case you may
# need to place data files outside of your packages. See:
# https://docs.python.org/distutils/setupscript.html#installing-additional-files
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#data-files
# https://www.scivision.dev/newer-setuptools-needed/
# https://setuptools.readthedocs.io/en/latest/history.html#v40-5-0
data_files = [
#     ('/etc/xxxx', [
#         'xxxx/config.ini',
#         'xxxx/log.ini',
#     ])
#     , ('/usr/share/doc/xxxx', [
#         'README.rst',
#         'LICENSE.txt',
#     ])
]

# https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
python_requires  ='>=3.7'

# [git+] https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support
# [requirements.txt] https://pip.pypa.io/en/stable/user_guide/#requirements-files
# [dependency_links] https://python-packaging.readthedocs.io/en/latest/dependencies.html

install_requires = [
    'fspath',
]

install_requires_txt = "\n".join(install_requires)

# usage: pip install .[test, develop]
#
# The setup.py 'extra_require' specifies optional parts of a distribution
# [PEP-508 extras], here in the example 'devel' and 'test' requirements also
# installed.
#
# [PEP-508 URL]      https://www.python.org/dev/peps/pep-0508/
# [PEP-508 extras]   https://www.python.org/dev/peps/pep-0508/#extras

test_requires = [
    'pylint'
    ]

develop_requires = [
    'twine',
    # 'wheel'
    'Sphinx',
    'pallets-sphinx-themes',
    'sphinx-autobuild',
    'sphinx-issues',
    'sphinx-jinja',
    'sphinx-tabs',
    'sphinxcontrib-programoutput',
    'linuxdoc',
    # slide-shows with revaljs
    # 'sphinxjp.themes.revealjs @ git+https://github.com/return42/sphinxjp.themes.revealjs',
    # https://jedi.readthedocs.io/
    # 'jedi',
    ]

def get_entry_points():
    """get entry points of the python package"""
    return {
        # 'console_scripts': [
        #     'xxxx = xxxx.cli:main' # Main xxxx_ console script
        # ]
    }

# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    # "Intended Audience :: Developers",
    cls_lic,
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    # "Topic :: Software Development :: Libraries :: Application Frameworks",
    # "Topic :: Software Development :: Libraries :: Python Modules",
]

long_description = """

:package:     %(package)s v%(version)s
:copyright:   %(copyright)s
:license:     %(license)s
:docs:        %(docs)s
:repository:  %(url)s

Install
=======

Install and update using `pip <https://pip.pypa.io/en/stable/quickstart/>`__::

  pip install %(package)s

or a bleeding edge installation from the repository::

  pip install %(url)s
""" % globals()

README = """\
.. SPDX-License-Identifier: %(license)s
.. do not edit this file, the origin is in __pkginfo__.py

==============================================================================
%(project)s
==============================================================================

%(description)s

|homepage| |Issues| |commits|

-----

%(long_description)s

.. |homepage| image:: https://img.shields.io/badge/-homepage-blue
   :target: %(docs)s

.. |Issues| image:: https://img.shields.io/github/issues/%(org)s/%(package)s?color=yellow&label=issues
   :target: https://github.com/%(org)s/%(package)s/issues

.. |PR| image:: https://img.shields.io/github/issues-pr-raw/%(org)s/%(package)s?color=yellow&label=PR
   :target: https://github.com/%(org)s/%(package)s/pulls

.. |commits| image:: https://img.shields.io/github/commit-activity/y/%(org)s/%(package)s?color=yellow&label=commits
   :target: https://github.com/%(org)s/%(package)s/commits/master

""" % globals()

test_requires_txt = "\n".join(test_requires)
develop_requires_txt = "\n".join(develop_requires)

requirements_txt = """\
# -*- coding: utf-8; mode: conf -*-
# do not edit this file, the origin is in __pkginfo__.py

# requirements of package %(package)s
%(install_requires_txt)s

# test requires
%(test_requires_txt)s

# development requires
%(develop_requires_txt)s
""" % globals()
