# Agent Guide

## What Belongs Here

Keep `agents.md` as the small entry point for agents. This file should contain:

- The repository map.
- Non-negotiable rules agents must always follow.
- Pointers to deeper instruction files.
- Short workflow reminders that apply to most tasks.

Do not turn this file into a manual. Put detailed, durable guidance in `doc/instructions/`.

## Repository Map

```text
agents.md
doc/
  instructions/
    context-management.md
    code-mirroring.md
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
- Read `doc/instructions/code-mirroring.md` before adding, moving, renaming, or deleting code files.

## Working Rules

- Keep durable decisions in `doc/instructions/`, not in chat.
- Keep module folders aligned across `doc/persudo/` and `src/`.
- Mirror code files only; do not mirror folders, data, generated files, config, assets, or non-code artifacts unless explicitly requested.
- Keep `agents.md` concise; move detailed guidance into focused instruction files and leave pointers here.
