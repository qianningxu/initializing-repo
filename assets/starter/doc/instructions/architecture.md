Whenever you make a change, preserve this structure: instructions in `doc/instructions/`, code blueprints in `doc/persudo/`, implementation in `src/`, and raw data in `data/`.

```text
.obsidian/           # Obsidian workspace configuration
agents.md            # map of instruction files
doc/
  instructions/      # all durable instructions
  persudo/           # markdown blueprints for code files under src/
    <module>/
      test/
src/                 # implementation code, organized by workflow or domain
  <module>/
    test/            # tests for that module
data/                # raw data and structured knowledge before an app model exists
```

Keep module folders aligned across `doc/persudo/` and `src/`. Mirror code files and code files only:

```text
doc/persudo/<module>/<code-file>.md       -> src/<module>/<code-file>
doc/persudo/<module>/test/<test-file>.md  -> src/<module>/test/<test-file>
```

For each mirrored pair, top-level functions, classes, and objects must match exactly: every code object appears in the blueprint, and every documented object exists in code.

Do not create or implement a code file unless its matching `.md` blueprint exists.

Do not create markdown mirrors for folders, data, generated files, config files, assets, or other non-code artifacts unless explicitly requested.

When adding, moving, renaming, or deleting a code file, update its mirrored markdown file in the same change.

The starter mirror check covers `.py` files by default. Before expanding coverage, ask whether the project is Python, TypeScript, or mixed.

Run `python3 src/agents/mirror_check.py --root .` every time a function is added or deleted. This is a universal repo check: run it across all configured code files, not only the file changed.
