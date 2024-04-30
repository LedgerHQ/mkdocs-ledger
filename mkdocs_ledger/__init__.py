"""
A Ledger theme for MkDocs + Material.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

try:
    __version__ = str(version("mkdocs-ledger"))
except (PackageNotFoundError, ImportError):
    version_file = Path(__file__).parent / "VERSION"
    __version__ = version_file.read_text() if version_file.is_file() else "0.0.0.dev"
