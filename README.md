# mkdocs-ledger

[![CI](https://github.com/LedgerHQ/mkdocs-ledger/actions/workflows/ci.yml/badge.svg)](https://github.com/LedgerHQ/mkdocs-ledger/actions/workflows/ci.yml)

MkDocs Ledger theme  based on Material for MkDocs.

<!-- --8<-- [start:getting-started] -->

## Getting started

Just follow the README steps. Those are

### Installation

Just install `mkdocs-ledger` from the [GemFury](https://manage.fury.io/dashboard/ledger/) repository (this requires credentials).
Properly chose the extra depending on what you want to document:

```bash
# Basic installation
pip install mkdocs-ledger
# Installation with docstring support
pip install mkdocs-ledger[docstrings]
# Installation with `click` documentation support
pip install mkdocs-ledger[click]
# Installation with all features
pip install mkdocs-ledger[docstrings,click]
```

### Configure mkdocs

Just use the `ledger` theme in your `mkdocs.yml` configuration:

```yaml
theme: ledger
```

For docstrings support, use the `mkdocstrings` plugin (`material/search` needs to be added too).
For click support, use the `mkdocs-click` markdown plugin.

```yaml
theme: ledger

markdown_extensions:
  - mkdocs-click

plugins:
  - material/search
  - mkdocstrings
```

<!-- --8<-- [end:getting-started] -->
