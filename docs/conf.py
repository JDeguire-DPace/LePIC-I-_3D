import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

project = "LePIC+ 3D"
author = "Jasmin Deguire"
copyright = "2026, Jasmin Deguire"
release = "0.1.0"

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "myst_parser",
]

autosectionlabel_prefix_document = True
todo_include_todos = True

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_title = "LePIC+ 3D documentation"

html_static_path = ["_static"]
html_logo = "_static/lepic_logo.png"

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")

html_css_files = [
    "css/custom.css",
]
