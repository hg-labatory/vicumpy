# Lumache Python Library - AI Agent Instructions

## Project Overview

Lumache is a simple Python library for generating random cooking ingredients. This codebase serves as a template for Read the Docs tutorials, demonstrating Python packaging, documentation, and CI/CD setup.

## Architecture

- **Single-module library**: Core functionality in `lumache.py`
- **Flit-based packaging**: Uses `pyproject.toml` with flit_core backend
- **Sphinx documentation**: Located in `docs/` directory with reStructuredText source files

## Key Components

- `docs/source/`: Sphinx documentation source with `conf.py`, `index.rst`, `usage.rst`, `api.rst`

## Development Workflow

### Building and Installing

```bash
# Install in development mode
pip install -e .

# Build distribution packages
python -m flit build
```

### Documentation

```bash
# Build HTML docs (from project root)
cd docs
make html
# Or directly: sphinx-build source build/html

# View docs locally
python -m http.server 8000 -d docs/build/html
```

### Testing

No test suite currently exists. When adding tests:

- Place in `tests/` directory
- Use pytest framework (common for Python projects)
- Follow existing code patterns

## Code Patterns

### Exception Handling

Define custom exception classes for library-specific errors:

```python
class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass
```

### Docstring Format

Use NumPy-style docstrings with type hints:

```python
def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
```

### Sphinx Configuration

Key extensions in `docs/source/conf.py`:

- `sphinx.ext.autodoc`: Auto-generate API docs from docstrings
- `sphinx.ext.autosummary`: Create summary tables
- `sphinx.ext.intersphinx`: Cross-reference external docs (Python, Sphinx)

Use `.. autofunction::`, `.. autoexception::` directives in RST files.

## File Organization

- `lumache.py`: Core library code
- `modul1/src/main.py`: Additional module (currently empty)
- `docs/`: Complete Sphinx documentation setup
- `.readthedocs.yaml`: Read the Docs CI configuration

## Deployment

- Hosted on Read the Docs (configured via `.readthedocs.yaml`)
- Uses Ubuntu 22.04 with Python 3.10 in CI
- Installs docs requirements from `docs/requirements.txt`
