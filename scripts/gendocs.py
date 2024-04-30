from pathlib import Path

from mkdocs_ledger.docstrings import generate_docstrings

ROOT = Path(__file__).parent.parent

generate_docstrings(ROOT / "mkdocs_ledger")
