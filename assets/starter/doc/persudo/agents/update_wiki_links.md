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

# `rewrite_wiki_heading_links`

```python
text: str,
old_heading: str,
new_heading: str,
page: str | None = None -> tuple[str, int]:
```

- Normalize `old_heading` and `new_heading` with [[#normalize_heading| normalize_heading]].
- Normalize `page` with [[#normalize_target| normalize_target]] when provided.
- Find Obsidian wiki links with heading targets:
	- `[[#heading]]`
	- `[[#heading|alias]]`
	- `[[page#heading]]`
	- `[[page#heading|alias]]`
- Replace links whose heading target matches `old_heading`.
- When `page` is provided, replace only links whose page target also matches.
- Preserve page targets and aliases.
- Return the rewritten text and replacement count.

# `normalize_heading`

```python
heading: str -> str:
```

- Trim whitespace.
- Remove a leading `#` when present.
- Return the normalized heading target.

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
old: str | None = None,
new: str | None = None,
old_heading: str | None = None,
new_heading: str | None = None,
page: str | None = None,
dry_run: bool = False -> int:
```

- Read `path` as UTF-8 text.
- Rewrite matching page links with [[#rewrite_wiki_links| rewrite_wiki_links]] when `old` and `new` are provided.
- Rewrite matching heading links with [[#rewrite_wiki_heading_links| rewrite_wiki_heading_links]] when `old_heading` and `new_heading` are provided.
- Raise an error when neither rename mode is provided.
- If replacements exist and `dry_run` is false, write the updated text back to `path`.
- Return the replacement count.

# `update_links`

```python
root: Path,
old: str | None = None,
new: str | None = None,
old_heading: str | None = None,
new_heading: str | None = None,
page: str | None = None,
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
	- `--old-heading`
	- `--new-heading`
	- `--page`
	- `--dry-run`
- Require exactly one rename mode:
	- `--old` with `--new`
	- `--old-heading` with `--new-heading`
- Run [[#update_links| update_links]].
- Print each changed file and replacement count relative to `root`.
- Print a no-match message when no links changed.
- Return `0`.
