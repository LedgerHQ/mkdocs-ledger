"""Generate the code reference pages and navigation."""

from pathlib import Path

import mkdocs_gen_files


def generate_docstrings(pkg: Path, doc_ns: str = "reference"):
    """An helper to generate docstrings for a given package"""
    nav = mkdocs_gen_files.Nav()
    mod_symbol = '<code class="doc-symbol doc-symbol-nav doc-symbol-module"></code>'

    src = pkg.parent
    root = src.parent if src.parts[-1] == "src" else src

    for path in sorted(pkg.rglob("*.py")):
        module_path = path.relative_to(src).with_suffix("")
        doc_path = path.relative_to(pkg).with_suffix(".md")
        full_doc_path = Path(doc_ns, doc_path)

        parts = tuple(module_path.parts)

        if parts[-1] == "__init__":
            parts = parts[:-1]
            doc_path = doc_path.with_name("index.md")
            full_doc_path = full_doc_path.with_name("index.md")
        elif parts[-1].startswith("_"):
            continue

        nav_parts = [f"{mod_symbol} {part}" for part in parts]
        nav[tuple(nav_parts)] = doc_path.as_posix()

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)
            fd.writelines(f"::: {ident}\n")

        mkdocs_gen_files.set_edit_path(full_doc_path, ".." / path.relative_to(root))

    with mkdocs_gen_files.open(f"{doc_ns}/SUMMARY.md", "w") as nav_file:
        nav_file.writelines(nav.build_literate_nav())
