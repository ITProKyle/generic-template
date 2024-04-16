"""Configuration file for the Sphinx documentation builder.

https://www.sphinx-doc.org/en/master/usage/configuration.html

"""

import os
import re
import tomllib
from datetime import date
from pathlib import Path

from pkg_resources import get_distribution

DOCS_DIR = Path(__file__).parent.parent.resolve()
ROOT_DIR = DOCS_DIR.parent
DOC_SRC = DOCS_DIR / "source"

PYPROJECT_TOML = tomllib.loads((ROOT_DIR / "pyproject.toml").read_text())
"""Read in the contents of ``../../pyproject.toml`` to reuse it's values."""


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = PYPROJECT_TOML["tool"]["poetry"]["name"]
copyright = f"{date.today().year}, Kyle Finley"  # noqa: A001, DTZ011
author = PYPROJECT_TOML["tool"]["poetry"]["authors"][0]
version = get_distribution(project).version
release = ".".join(version.split(".")[:2])  # short X.Y version


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
add_function_parentheses = True
add_module_names = True
default_role = None
exclude_patterns = []
extensions = [
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.apidoc",
    "sphinxcontrib.jquery",
]
highlight_language = "default"
intersphinx_mapping = {}
language = "en"
master_doc = "index"
needs_extensions = {}
needs_sphinx = "4.2"
nitpicky = False
primary_domain = "py"
pygments_style = "material"  # syntax highlighting style
rst_epilog = ""  # appended to the end of each rendered file
rst_prolog = ""  # appended to the end of each rendered file
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}
templates_path = ["_templates"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_codeblock_linenos_style = "inline"
html_css_files = ["css/custom.css"]
html_favicon = None
html_js_files = ["js/custom.js"]
html_logo = None
html_short_title = f"{project} v{release}"
html_show_copyright = True
html_show_sphinx = False
html_static_path = ["_static"]  # dir with static files relative to this dir
html_theme = "furo"  # theme to use for HTML and HTML Help pages
html_theme_options = {
    "dark_css_variables": {
        "font-stack--monospace": "Inconsolata, monospace",
    },
    "light_css_variables": {
        "font-stack--monospace": "Inconsolata, monospace",
    },
}
html_title = f"{project} v{release}"


# -- Options for sphinx-apidoc -----------------------------------------------
# https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html#environment
os.environ["SPHINX_APIDOC_OPTIONS"] = "members"


# -- Options of sphinx.ext.autodoc -------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autoclass_content = "class"
autodoc_class_signature = "separated"
autodoc_default_options = {
    "inherited-members": True,  # show all inherited members
    "member-order": "bysource",
    "members": True,
    "show-inheritance": True,
}
autodoc_type_aliases = {}
autodoc_typehints = "signature"


# -- Options for sphinx.ext.autosectionlabel ---------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = None


# -- Options for sphinx.ext.napoleon  ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
napoleon_google_docstring = True
napoleon_include_init_with_doc = False
napoleon_type_aliases = autodoc_type_aliases


# -- Options for sphinxcontrib.apidoc  ---------------------------------------
# https://github.com/sphinx-contrib/apidoc
apidoc_excluded_paths = [
    ".demo",
    ".venv",
    "docs",
    "node_modules",
    "test*",
    "typings",
]
apidoc_extra_args = [f"--templatedir={DOC_SRC / '_templates' / 'apidocs'}"]
apidoc_module_dir = "../../" + re.sub(r"(\.|-)", "_", project)
apidoc_module_first = True
apidoc_output_dir = "apidocs"
apidoc_separate_modules = True
apidoc_toc_file = "index"


# -- Options of sphinx.ext.intersphinx ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),  # link to python docs
}


# -- Options for sphinx_copybutton ---------------------------------
# https://sphinx-copybutton.readthedocs.io/en/latest/index.html
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_remove_prompts = True
copybutton_line_continuation_character = "\\"
