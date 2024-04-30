# mkdocs-ledger

[![CI](https://github.com/LedgerHQ/mkdocs-ledger/actions/workflows/ci.yml/badge.svg)](https://github.com/LedgerHQ/mkdocs-ledger/actions/workflows/ci.yml)

A [MkDocs](https://www.mkdocs.org) Ledger theme based on [Material for MkDocs](https://www.mkdocs.org).

<!-- --8<-- [start:getting-started] -->

## Getting started

Just follow the following steps.

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

For docstrings support, use the [`mkdocstrings` plugin](https://mkdocstrings.github.io).
For click support, use the [`mkdocs-click` plugin](https://github.com/mkdocs/mkdocs-click).

```yaml
theme: ledger

markdown_extensions:
  - mkdocs-click

plugins:
  - material/search
  - mkdocstrings
```

> [!NOTE]
> If you override `plugins`, you need to put every provided plugins, including `material/search`.

### Detailed `mkdocstrings` configuration

In order to have a shiny docstring reference, you may use the following configuration:

```yaml
  - mkdocstrings:
      default_handler: python
      handlers:
        python:
          import:
            # Add used libs for external cross-references
            - https://docs.python.org/3/objects.inv
          paths: [src]
          options:
            docstring_options:
              ignore_init_summary: true
            docstring_section_style: list
            filters: ["!^_"]
            heading_level: 1
            inherited_members: true
            merge_init_into_class: true
            parameter_headings: true
            separate_signature: true
            show_root_heading: true
            show_root_full_path: true
            show_signature_annotations: true
            show_symbol_type_heading: true
            show_symbol_type_toc: true
            signature_crossrefs: true
            summary: true
  - gen-files:
      scripts:
      - scripts/gendocs.py
  - literate-nav:
      nav_file: SUMMARY.md
```

And in `scripts/gendocs.py`:

```python
from pathlib import Path
from mkdocs_ledger.docstrings import generate_docstrings

ROOT = Path(__file__).parent.parent
# Path to root package
generate_docstrings(ROOT / "mkdocs_ledger")
```

### Github Alerts

To enable support for [GitHub Alerts][github-alerts], you need to enable the [GitHub Callouts extension](https://oprypin.github.io/markdown-callouts/).

```yaml
markdown_extensions:
  - github-callouts
```

[github-alerts]: https://docs.github.com/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts
<!-- --8<-- [end:getting-started] -->

## Documentation

Documentation is available at <https://ledgerhq.github.io/mkdocs-ledger/>

## Contributing

Read the [dedicated contributing guidelines](./CONTRIBUTING.md).
