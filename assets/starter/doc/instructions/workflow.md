Use the smallest durable slice that advances the project without leaving intent, blueprints, code, and verification out of sync.

## Creation

For new source or test code:

1. Ask clarifying questions in rounds of up to three. Keep asking until the structure and blueprint are testable, and explain questions as if the user has little prior context.
2. Propose the mirrored module structure first. Show only the `doc/persudo/` tree; the matching `src/` tree is implied.
3. After structure approval, create the `.md` blueprint before creating code. For blueprint standards, read [[writing-persudo|writing-persudo]].
4. Treat the blueprint as needing review and approval before code implementation unless the user says otherwise.
5. After blueprint approval, implement the matching code file.
6. Keep helper logic inline unless it is reused or meaningfully reduces complexity.
7. Run configured checks.

Example proposal:

```python
storage/
  sqlite_row.md
  - insert_row(db_path, table, values) -> int  # Insert one row and return its id
  - update_rows(db_path, table, values, where) -> int  # Update matching rows and return rowcount
  - select_rows(db_path, table, where=None, columns=None) -> list  # Return matching rows
```

## Editing

When changing existing code:

1. If testing reveals an issue, identify the root cause before changing code.
2. Send a concise proposal naming the affected files(like above), functions, and blueprint changes unless the user already approved the edit.
3. After approval, edit the code and sync mirrored blueprints in the same change.
4. Run `python3 src/agents/mirror_check.py --root .` whenever a function is added or deleted.
5. Record unresolved behavior, design-code, or verification deltas before moving on.
