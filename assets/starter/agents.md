# Agent Guide

## Repository Knowledge

Repository knowledge is the system of record. Treat this file as the map, not the manual.

`agents.md` is intentionally short so agents can keep the entry point in context while still having room for the task, code, and relevant docs. Durable guidance belongs in `doc/instructions/`; module blueprints belong in `doc/persudo/`.

## Map

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

- `agents.md`: stable table of contents and always-on rules.
- `doc/instructions/`: durable knowledge base and source of truth.
- `doc/persudo/`: code-file blueprints, organized by module.
- `src/`: implementation modules; tests live inside the module they verify.
- `data/`: raw domain data, imports, fixtures, seed content, and structured knowledge.

## Navigation

- Read `doc/instructions/context-management.md` before expanding `agents.md` or creating instruction files.
- Read `doc/instructions/code-mirroring.md` before adding, moving, renaming, or deleting code files.
- Add new durable guidance under `doc/instructions/`, named by content.
- Add code blueprints under `doc/persudo/`, mirroring code files only.

## Rules

- Do not treat chat as the source of truth; record durable decisions in repository docs.
- Do not pack detailed procedures into `agents.md`; leave a pointer to the relevant instruction file.
- Keep module folders aligned across `doc/persudo/` and `src/`.
- Mirror code files only. Do not mirror folders, data, generated files, config, assets, or non-code artifacts unless explicitly requested.
- When docs and code disagree, update the stale side in the same change or record the known delta before moving on.
