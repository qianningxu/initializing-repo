# `normalize_target`

```python
target: str -> str:
```

- Trim whitespace.
- Remove a trailing `.md` suffix when present.
- Remove leading `./` segments.
- Return the normalized wiki target.

# `rewrite_wiki_links`

```python
text: str,
old: str,
new: str -> tuple[str, int]:
```

- Normalize `old` and `new` with [[#normalize_target| normalize_target]].
- Find Obsidian wiki links with a page target:
	- `[[page]]`
	- `[[page|alias]]`
	- `[[page#heading]]`
	- `[[page#heading|alias]]`
- Leave heading-only links such as `[[#symbol| symbol]]` unchanged.
- Replace links whose page target matches `old`.
- Preserve heading targets and aliases.
- Return the rewritten text and replacement count.

# `markdown_files`

```python
root: Path -> list[Path]:
```

- Walk every markdown file under `root`.
- Skip files inside `.git`.
- Return paths sorted by their relative path.

# `update_file`

```python
path: Path,
old: str,
new: str,
dry_run: bool = False -> int:
```

- Read `path` as UTF-8 text.
- Rewrite matching wiki links with [[#rewrite_wiki_links| rewrite_wiki_links]].
- If replacements exist and `dry_run` is false, write the updated text back to `path`.
- Return the replacement count.

# `update_links`

```python
root: Path,
old: str,
new: str,
dry_run: bool = False -> dict[Path, int]:
```

- Normalize `root` to an absolute path.
- Check each file from [[#markdown_files| markdown_files]].
- Update links in each file with [[#update_file| update_file]].
- Return only files with one or more replacements.

# `main`

```python
argv: list[str] | None = None -> int:
```

- Parse CLI arguments:
	- `--root`
	- `--old`
	- `--new`
	- `--dry-run`
- Run [[#update_links| update_links]].
- Print each changed file and replacement count relative to `root`.
- Print a no-match message when no links changed.
- Return `0`.
