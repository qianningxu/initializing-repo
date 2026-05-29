Use `doc/persudo/` as the blueprint layer for code files under `src/`.

## Rule

Mirror code files and code files only.

```text
doc/persudo/<module>/<code-file>.md
src/<module>/<code-file>

doc/persudo/<module>/test/<test-code-file>.md
src/<module>/test/<test-code-file>
```

Every durable code file under `src/<module>/` should have a corresponding markdown blueprint under `doc/persudo/<module>/`. Every durable test code file under `src/<module>/test/` should have a corresponding markdown blueprint under `doc/persudo/<module>/test/`.

Do not create markdown mirrors for folders, data, generated files, config files, assets, or non-code artifacts unless explicitly requested.

## Module Alignment

Keep module folders aligned across `doc/persudo/` and `src/`.

When adding a module, create or update:

```text
doc/persudo/<module>/
src/<module>/
```

When adding, moving, renaming, or deleting a code file, update its mirrored markdown file in the same change.

## Tests

Tests live inside the module they verify:

```text
src/<module>/test/
```

Their blueprints live in the corresponding planning folder:

```text
doc/persudo/<module>/test/
```
