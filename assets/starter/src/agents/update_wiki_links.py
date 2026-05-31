"""Update Obsidian wiki links after markdown file or heading renames."""
from __future__ import annotations

import argparse
from pathlib import Path
import re


WIKI_LINK_RE = re.compile(r"\[\[([^#|\]]*)(#[^|\]]+)?(\|[^\]]*)?\]\]")


def normalize_target(target: str) -> str:
    target = target.strip()
    if target.endswith(".md"):
        target = target[:-3]
    while target.startswith("./"):
        target = target[2:]
    return target


def normalize_heading(heading: str) -> str:
    heading = heading.strip()
    if heading.startswith("#"):
        heading = heading[1:]
    return heading


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


def rewrite_wiki_heading_links(
    text: str,
    old_heading: str,
    new_heading: str,
    page: str | None = None
) -> tuple[str, int]:
    old_heading = normalize_heading(old_heading)
    new_heading = normalize_heading(new_heading)
    page = normalize_target(page) if page else None
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        link_page = normalize_target(match.group(1))
        heading = match.group(2) or ""
        if normalize_heading(heading) != old_heading:
            return match.group(0)
        if page is not None and link_page != page:
            return match.group(0)

        count += 1
        alias = match.group(3) or ""
        return f"[[{match.group(1)}#{new_heading}{alias}]]"

    return WIKI_LINK_RE.sub(replace, text), count


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if path.is_file() and ".git" not in path.parts
    )


def update_file(
    path: Path,
    old: str | None = None,
    new: str | None = None,
    old_heading: str | None = None,
    new_heading: str | None = None,
    page: str | None = None,
    dry_run: bool = False
) -> int:
    text = path.read_text(encoding="utf-8")
    if old_heading is not None and new_heading is not None:
        updated, count = rewrite_wiki_heading_links(text, old_heading, new_heading, page)
    elif old is not None and new is not None:
        updated, count = rewrite_wiki_links(text, old, new)
    else:
        raise ValueError("provide either old/new or old_heading/new_heading")

    if count and not dry_run:
        path.write_text(updated, encoding="utf-8")
    return count


def update_links(
    root: Path,
    old: str | None = None,
    new: str | None = None,
    old_heading: str | None = None,
    new_heading: str | None = None,
    page: str | None = None,
    dry_run: bool = False
) -> dict[Path, int]:
    root = root.resolve()
    changed: dict[Path, int] = {}
    for path in markdown_files(root):
        count = update_file(path, old, new, old_heading, new_heading, page, dry_run)
        if count:
            changed[path] = count
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root to update.")
    parser.add_argument("--old", help="Old wiki link page target.")
    parser.add_argument("--new", help="New wiki link page target.")
    parser.add_argument("--old-heading", help="Old wiki link heading target.")
    parser.add_argument("--new-heading", help="New wiki link heading target.")
    parser.add_argument("--page", help="Only update heading links for this page target.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files.")
    args = parser.parse_args(argv)

    page_mode = args.old is not None or args.new is not None
    heading_mode = args.old_heading is not None or args.new_heading is not None
    if page_mode == heading_mode:
        parser.error("provide either --old/--new or --old-heading/--new-heading")
    if page_mode and (args.old is None or args.new is None):
        parser.error("--old and --new must be provided together")
    if heading_mode and (args.old_heading is None or args.new_heading is None):
        parser.error("--old-heading and --new-heading must be provided together")

    root = Path(args.root).resolve()
    changed = update_links(
        root,
        old=args.old,
        new=args.new,
        old_heading=args.old_heading,
        new_heading=args.new_heading,
        page=args.page,
        dry_run=args.dry_run,
    )
    if not changed:
        print("no wiki links matched")
        return 0

    for path, count in sorted(changed.items()):
        print(f"{path.relative_to(root)}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
