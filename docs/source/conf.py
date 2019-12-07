# -*- coding: utf-8 -*-
# pylint: skip-file
# type: ignore
"""
Configuration file for the Sphinx documentation builder.

This file only contain a selection of the most common options. For a
full list see the documentation: http://www.sphinx-doc.org/en/master/config

"""
import os
from shutil import copyfile
import sys

# add to path for imports
sys.path.insert(0, os.getcwd())

from pygment_styles import OneDark, pygments_patch_style  # noqa


pygments_patch_style("one_dark", OneDark)

copyfile('../../CHANGELOG.md', './changelog.md')

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# from os.path import dirname, realpath
# import os.path
# import sys
# root_dir = dirname(dirname(dirname(realpath(__file__))))
# sys.path.insert(0, os.path.join(root_dir, 'src'))
#
# from local_package import __version__  # noqa


# -- Project information -----------------------------------------------------

project = 'generic-template'
copyright = '2019, Kyle Finley'
author = 'Kyle Finley'
version = '0.0.0'
release = '0.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

# The file extensions of source files. Sphinx considers the files with
# this suffix as sources. The value can be a dictionary mapping file
# extensions to file types.

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}


# The document name of the “master” document, that is, the document that
# contains the root toctree directive.

master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

exclude_patterns = []

# A list of paths that contain extra templates (or templates that overwrite
# builtin/theme-specific templates). Relative paths are taken as relative
# to the configuration directory.

templates_path = ['_templates']

# The style name to use for Pygments highlighting of source code. If not
# set, either the theme’s default style or 'sphinx' is selected for HTML
# output.

pygments_style = 'one_dark'  # TODO add custom style


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# A list of CSS files. The entry must be a filename string or a tuple
# containing the filename string and the attributes dictionary. The
# filename must be relative to the html_static_path, or a full URI with
# scheme like http://example.org/style.css. The attributes is used for
# attributes of <link> tag. It defaults to an empty list.

html_css_files = [
    'css/rtd_dark.css',
    # 'css/code_one_dark.scss'
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pydoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, f'{project}.tex', f'{project} Documentation',
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, project, f'{project} Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, project, f'{project} Documentation',
     author, project, 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Options for autodoc  -----------------------------------------------------

autoclass_content = 'both'

# -- Options for napoleon  ----------------------------------------------------
napoleon_google_docstring = True
napoleon_include_init_with_doc = False
