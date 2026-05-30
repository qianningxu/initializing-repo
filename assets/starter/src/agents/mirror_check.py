"""Check that source files have matching markdown blueprints."""
from __future__ import annotations

import argparse
import ast
from pathlib import Path
import re


def python_functions(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def expected_markdown(root: Path, code_path: Path) -> Path:
    relative = code_path.relative_to(root / "src").with_suffix(".md")
    return root / "doc" / "persudo" / relative


def check_mirrors(
    root: Path,
    extensions: tuple[str, ...] = (".py",)
) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    for code_path in sorted((root / "src").rglob("*")):
        if not code_path.is_file() or code_path.suffix not in extensions:
            continue

        markdown_path = expected_markdown(root, code_path)
        if not markdown_path.exists():
            errors.append(f"missing blueprint: {markdown_path.relative_to(root)} for {code_path.relative_to(root)}")
            continue

        if code_path.suffix == ".py":
            markdown = markdown_path.read_text(encoding="utf-8")
            for name in sorted(python_functions(code_path)):
                if not re.search(rf"(?<![A-Za-z0-9_]){re.escape(name)}(?![A-Za-z0-9_])", markdown):
                    errors.append(f"missing function: {name} in {markdown_path.relative_to(root)}")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root to check.")
    parser.add_argument("--extension", action="append", default=None, help="Code extension to check. Defaults to .py.")
    args = parser.parse_args(argv)

    extensions = tuple(args.extension or [".py"])
    errors = check_mirrors(Path(args.root), extensions)
    if errors:
        for error in errors:
            print(error)
        return 1

    print("mirror check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
