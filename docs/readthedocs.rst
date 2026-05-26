Read the Docs setup
===================

Files added for Read the Docs
-----------------------------

``.readthedocs.yaml``
   Main Read the Docs build configuration. This file must be at the root of the Git repository.

``docs/conf.py``
   Sphinx configuration.

``docs/requirements.txt``
   Python packages required to build the documentation.

``docs/index.rst``
   Documentation home page.

Local documentation build
-------------------------

Install the documentation dependencies in a virtual environment:

.. code-block:: bash

   python3 -m venv .venv-docs
   source .venv-docs/bin/activate
   pip install -r docs/requirements.txt

Build the HTML documentation:

.. code-block:: bash

   sphinx-build -b html docs docs/_build/html

Open the local result:

.. code-block:: bash

   xdg-open docs/_build/html/index.html

Publishing on Read the Docs
---------------------------

1. Commit and push ``docs/`` and ``.readthedocs.yaml`` to GitHub.
2. Log in to Read the Docs.
3. Import the GitHub repository.
4. Let Read the Docs build the project using ``.readthedocs.yaml``.

Troubleshooting
---------------

If the build fails, check:

* ``.readthedocs.yaml`` is at the repository root.
* ``sphinx.configuration`` points to ``docs/conf.py``.
* All Python documentation dependencies are listed in ``docs/requirements.txt``.
* The documentation builds locally with ``sphinx-build -b html docs docs/_build/html``.
