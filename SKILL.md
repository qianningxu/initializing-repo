---
name: initializing-repo
description: Initialize a repository with the user's standard starter structure and agent guide. Use when the user asks to initialize, scaffold, reset, or standardize a repo structure containing agents.md, doc/instructions, doc/persudo, src/functions, src/test, and data, or asks for an architecture section explaining that structure.
---

# Initializing Repo

## Workflow

Assume the target directory is empty unless the user says otherwise.

1. Create this structure:

```text
agents.md
doc/
  instructions/
  persudo/

src/
  functions/
  test/
data/
```

2. Write `agents.md` with the `Architecture` section below.
3. Leave `doc/instructions/`, `doc/persudo/`, `src/functions/`, `src/test/`, and `data/` ready for future files.
4. Verify the resulting tree.

If the directory is not empty, preserve existing files and patch `agents.md` in place instead of overwriting it.

## agents.md Architecture Section

Add this section if no architecture section exists. If one exists, merge the intent without duplicating headings.

````md
## Architecture

Repository knowledge is the system of record. Keep `agents.md` short: it is the table of contents for agents, not the encyclopedia. Put durable details in `doc/instructions/` and use progressive disclosure so agents can start from a compact map, then open the specific instruction files they need.

The repository starts with this structure:

```text
agents.md
doc/
  instructions/
  persudo/

src/
  functions/
  test/
data/
```

- `agents.md` is the agent entry point. Keep it concise, roughly 100 lines when possible. It should explain how to navigate the repository, link to deeper instructions, and name the rules that must always be in context.
- `doc/instructions/` is the durable knowledge base for cross-cutting guidance. Store architecture notes, product intent, design rules, decision logs, execution plans, quality expectations, and other maintained instructions here. Treat it as the source of truth when `agents.md` points elsewhere.
- `doc/persudo/` is the module blueprint layer. Its top-level folders define the same modules that appear under `src/functions/` and `src/test/`, and each module folder keeps source design and test design together before implementation.
- `src/functions/` stores implementation modules. Top-level module folders under `src/functions/` should match the modules defined under `doc/persudo/`.
- `src/test/` stores verification modules. Top-level module folders under `src/test/` should match the modules defined under `doc/persudo/` and implemented under `src/functions/`.
- `data/` stores raw domain data, seed content, imported records, fixtures, and structured knowledge consumed by the project. Keep it separate from `src/` unless there is an explicit import path, migration, or runtime data model.

Use modules as the big structural mapping across planning, implementation, and verification:

```text
doc/persudo/<module>/
  src.md
  test.md
src/functions/<module>/
src/test/<module>/
```

The `doc/persudo/<module>/` folder is where source behavior and test behavior are designed together. `src.md` describes the intended implementation for `src/functions/<module>/`; `test.md` describes the intended verification for `src/test/<module>/`. When a module is added, moved, renamed, split, or merged, update the blueprint, source, and test locations together. Promote shared code or shared instructions only after a pattern repeats.
````

## Safety

- Do not delete user files while initializing the repo.
- Do not overwrite an existing `agents.md`; patch it in place.
- Do not move domain data into `src/` unless the user explicitly asks for that migration.
- Keep module folders structurally aligned across `doc/persudo/`, `src/functions/`, and `src/test/`.
- When adding a module, create or update `doc/persudo/<module>/src.md`, `doc/persudo/<module>/test.md`, `src/functions/<module>/`, and `src/test/<module>/` together when relevant.
- Mention any existing folders that remain outside the standard structure.
