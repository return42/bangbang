# -*- coding: utf-8 -*-
# SPDX-License-Identifier: AGPL-3.0-or-later

import sys, os, re
from bangbang import __pkginfo__ as _
from pallets_sphinx_themes import ProjectLink

# Project --------------------------------------------------------------

project = 'BangBang'
copyright = _.copyright
version   = _.version
release   = _.version
show_authors = True
author = _.author

GIT_URL = _.url
DOCS_URL = _.docs
WIKI_URL = GIT_URL + '/wiki'
ISSUE_URL = _.issues
CONTACT_URL = None # mailto:contact@example.com

# issues_github_path = "return42/" + project

# General --------------------------------------------------------------

# hint: sphinx.ext.viewcode won't highlight when 'highlight_language' [1] is set
#       to string 'none' [2]
#
# [1] https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html
# [2] https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-highlight_language

highlight_language = 'default'
master_doc = "index"
source_suffix = '.rst'
numfig = True

exclude_patterns = []

# usage::   lorem :patch:`f373169` ipsum
extlinks = {}
extlinks['wiki']      = (WIKI_URL + '/%s', ' ')
extlinks['pull']      = (GIT_URL + '/pull/%s', 'PR ')
extlinks['origin']    = (GIT_URL + '/blob/master/%s', 'git://')
extlinks['patch']     = (GIT_URL + '/commit/%s', '#')
extlinks['docs']      = (_.docs + '/%s', 'docs: ')
extlinks['pypi'] = ('https://pypi.org/project/%s', 'PyPi: ')
extlinks['man'] = ('https://manpages.debian.org/jump?q=%s', '')

extensions = [
    'sphinx.ext.imgmath',
    'sphinx.ext.extlinks',
    'sphinx.ext.viewcode',
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "pallets_sphinx_themes",
    # https://github.com/sloria/sphinx-issues/blob/master/README.rst
    "sphinx_issues",
    # https://github.com/tardyp/sphinx-jinja
    "sphinxcontrib.jinja",
    # https://github.com/NextThought/sphinxcontrib-programoutput
    "sphinxcontrib.programoutput",
    # Implementation of the 'kernel-include' reST-directive.
    'linuxdoc.kernel_include',
    # Implementation of the 'flat-table' reST-directive.
    'linuxdoc.rstFlatTable',
    # Sphinx extension which implements scalable image handling.
    'linuxdoc.kfigure',
    # https://github.com/djungelorm/sphinx-tabs
    "sphinx_tabs.tabs",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}


def get_valid_filename(fname):
    fname = str(fname).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', fname)


# sys.path.append(os.path.abspath('_themes'))
# sys.path.insert(0, os.path.abspath("../utils/"))
html_theme_path = ['_themes']
html_theme = "project"

# sphinx.ext.imgmath setup
html_math_renderer = 'imgmath'
imgmath_image_format = 'svg'
imgmath_font_size = 14
# sphinx.ext.imgmath setup END

html_theme_options = {"index_sidebar_logo": True}
html_context = {"project_links": [] }

extlinks['wiki']      = (GIT_URL + '/wiki/%s', ' ')
extlinks['pull']      = (GIT_URL + '/pull/%s', 'PR ')
extlinks['origin']    = (GIT_URL + '/blob/master/%s', 'git://')
extlinks['patch']     = (GIT_URL + '/commit/%s', '#')
extlinks['docs']      = (DOCS_URL + '/%s', 'docs: ')

if GIT_URL:
    html_context["project_links"].append(ProjectLink("Source", GIT_URL))
if WIKI_URL:
    html_context["project_links"].append(ProjectLink("Wiki", WIKI_URL))
if _.issues:
    html_context["project_links"].append(ProjectLink("Issue Tracker", _.issues))
if CONTACT_URL:
    html_context["project_links"].append(ProjectLink("Contact", CONTACT_URL))

html_sidebars = {
    "**": ["project.html", "relations.html", "searchbox.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html"]}
html_static_path = ["static"]
#html_logo = "static/logo_small.png"
html_title = project
html_show_sourcelink = False

# LaTeX ----------------------------------------------------------------

latex_documents = [
    (master_doc, get_valid_filename(project) + ".tex", html_title, author, "manual")
]
