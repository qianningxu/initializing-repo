# Agent Guide

## Role

Use this repository's knowledge base as the system of record. Keep this file as a short map for agents, not a full manual.

## Repository Map

```text
agents.md
doc/
  instructions/
    context-management.md
  persudo/

src/
data/
```

- `agents.md`: agent entry point, repo map, and non-negotiable rules.
- `doc/instructions/`: durable instructions and cross-cutting source of truth.
- `doc/persudo/`: module blueprints that mirror code files in `src/`.
- `src/`: implementation modules; tests live inside the module they verify.
- `data/`: raw domain data, seed content, imports, fixtures, and structured knowledge.

## Required Reading

- Read `doc/instructions/context-management.md` before expanding this file or creating new instruction docs.

## Mirroring Rule

Mirror code files and code files only:

```text
doc/persudo/<module>/<code-file>.md
src/<module>/<code-file>

doc/persudo/<module>/test/<test-code-file>.md
src/<module>/test/<test-code-file>
```

Do not create markdown mirrors for folders, data, generated files, config files, assets, or non-code artifacts unless explicitly requested.

## Working Rules

- Keep module folders aligned across `doc/persudo/` and `src/`.
- When adding, moving, renaming, or deleting a code file, update its mirrored markdown file in the same change.
- Keep durable decisions in `doc/instructions/`, not in chat.
- Keep `agents.md` concise; move detailed guidance into focused instruction files and leave pointers here.
