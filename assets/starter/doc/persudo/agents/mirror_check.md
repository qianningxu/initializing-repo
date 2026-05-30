# `python_functions`

```python
path: Path -> set[str]:
```

- Read `path` as UTF-8 text.
- Parse the file with Python AST.
- Collect top-level function nodes:
	- `FunctionDef`
	- `AsyncFunctionDef`
- Return the collected function names.

# `expected_markdown`

```python
root: Path,
code_path: Path -> Path:
```

- Compute `code_path` relative to `root / "src"`.
- Replace the source extension with `.md`.
- Return the matching blueprint path under `root / "doc" / "persudo"`.

# `check_mirrors`

```python
root: Path,
extensions: tuple[str, ...] = (".py",)
-> list[str]:
```

- Convert `root` to an absolute path before checking files.
- Walk every file under `root / "src"`.
- For each file:
	- Skip non-files.
	- Skip files whose extension is not configured.
	- Find the required blueprint with [[#expected_markdown| expected_markdown]].
	- If the blueprint is missing:
		- Add a missing-blueprint error.
		- Continue to the next file.
	- If the file is Python:
		- Extract top-level functions with [[#python_functions| python_functions]].
		- Check that each function name appears in the blueprint.
		- Add a missing-function error for each undocumented function.
- Return all errors.

# `main`

```python
argv: list[str] | None = None
-> int:
```

- Parse CLI arguments:
	- `--root`
	- `--extension`
- Run [[#check_mirrors| check_mirrors]].
- If errors exist:
	- Print each error.
	- Return `1`.
- Print success.
- Return `0`.
