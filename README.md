# LePIC 3D

Modular Fortran Particle-in-Cell code for plasma simulations.

## Documentation

This repository is ready for Read the Docs using Sphinx.

Build the docs locally:

```bash
python3 -m venv .venv-docs
source .venv-docs/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
```

The Read the Docs configuration is in `.readthedocs.yaml`.
