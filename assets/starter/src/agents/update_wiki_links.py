"""Update Obsidian wiki links after a markdown file rename."""
from __future__ import annotations

import argparse
from pathlib import Path
import re


WIKI_LINK_RE = re.compile(r"\[\[([^#|\]]+)(#[^|\]]+)?(\|[^\]]*)?\]\]")


def normalize_target(target: str) -> str:
    target = target.strip()
    if target.endswith(".md"):
        target = target[:-3]
    while target.startswith("./"):
        target = target[2:]
    return target


def rewrite_wiki_links(text: str, old: str, new: str) -> tuple[str, int]:
    old = normalize_target(old)
    new = normalize_target(new)
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        page = normalize_target(match.group(1))
        if page != old:
            return match.group(0)

        count += 1
        heading = match.group(2) or ""
        alias = match.group(3) or ""
        return f"[[{new}{heading}{alias}]]"

    return WIKI_LINK_RE.sub(replace, text), count


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if path.is_file() and ".git" not in path.parts
    )


def update_file(
    path: Path,
    old: str,
    new: str,
    dry_run: bool = False
) -> int:
    text = path.read_text(encoding="utf-8")
    updated, count = rewrite_wiki_links(text, old, new)
    if count and not dry_run:
        path.write_text(updated, encoding="utf-8")
    return count


def update_links(
    root: Path,
    old: str,
    new: str,
    dry_run: bool = False
) -> dict[Path, int]:
    root = root.resolve()
    changed: dict[Path, int] = {}
    for path in markdown_files(root):
        count = update_file(path, old, new, dry_run)
        if count:
            changed[path] = count
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root to update.")
    parser.add_argument("--old", required=True, help="Old wiki link target.")
    parser.add_argument("--new", required=True, help="New wiki link target.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    changed = update_links(root, args.old, args.new, args.dry_run)
    if not changed:
        print("no wiki links matched")
        return 0

    for path, count in sorted(changed.items()):
        print(f"{path.relative_to(root)}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
