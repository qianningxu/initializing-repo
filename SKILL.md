---
name: initializing-repo
description: Initialize a repository with the user's standard starter structure and agent guide. Use when the user asks to initialize, scaffold, reset, or standardize a repo structure containing agents.md, doc/instructions, doc/persudo, src, test, and data, or asks for an architecture section explaining that structure.
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
test/
data/
```

2. Write `agents.md` with the `Architecture` section below.
3. Leave `doc/instructions/`, `doc/persudo/`, `src/`, `test/`, and `data/` ready for future files.
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
test/
data/
```

- `agents.md` is the agent entry point. Keep it concise, roughly 100 lines when possible. It should explain how to navigate the repository, link to deeper instructions, and name the rules that must always be in context.
- `doc/instructions/` is the durable knowledge base. Store architecture notes, product intent, design rules, decision logs, execution plans, quality expectations, and other maintained instructions here. Treat it as the source of truth when `agents.md` points elsewhere.
- `doc/persudo/` is the planning mirror for the module structure. Each module should get its own folder here, and that folder should contain both the source plan and the test plan for that module before they become durable code.
- `src/` stores implementation modules. Top-level module folders under `src/` should match the module folders under `doc/persudo/`.
- `test/` stores verification modules. Top-level module folders under `test/` should match the module folders under `src/` and `doc/persudo/`.
- `data/` stores raw domain data, seed content, imported records, fixtures, and structured knowledge consumed by the project. Keep it separate from `src/` unless there is an explicit import path, migration, or runtime data model.

Use modules as the big structural mapping across planning, implementation, and verification:

```text
doc/persudo/<module>/
  src.md
  test.md
src/<module>/
test/<module>/
```

The `doc/persudo/<module>/` folder is where source behavior and test behavior are designed together. Once implemented, the matching code lives in `src/<module>/` and the matching tests live in `test/<module>/`. Promote shared code or shared instructions only after a pattern repeats.
````

## Safety

- Do not delete user files while initializing the repo.
- Do not overwrite an existing `agents.md`; patch it in place.
- Do not move domain data into `src/` unless the user explicitly asks for that migration.
- Keep module folders structurally aligned across `doc/persudo/`, `src/`, and `test/`.
- When adding a module, create or update `doc/persudo/<module>/src.md`, `doc/persudo/<module>/test.md`, `src/<module>/`, and `test/<module>/` together when relevant.
- Mention any existing folders that remain outside the standard structure.
