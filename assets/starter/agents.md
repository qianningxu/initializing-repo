# Agent Guide

## Architecture

Repository knowledge is the system of record. Keep `agents.md` short: it is the table of contents for agents, not the encyclopedia. Put durable details in `doc/instructions/` and use progressive disclosure so agents can start from a compact map, then open the specific instruction files they need.

The repository starts with this structure:

```text
agents.md
doc/
  instructions/
    agents.md
  persudo/

src/
data/
```

- `agents.md` is the agent entry point. Keep it concise, roughly 100 lines when possible. It should explain how to navigate the repository, link to deeper instructions, and name the rules that must always be in context. See `doc/instructions/agents.md` for when to split details out of `agents.md`.
- `doc/instructions/` is the durable knowledge base for cross-cutting guidance. Store architecture notes, product intent, design rules, decision logs, execution plans, quality expectations, and other maintained instructions here. Treat it as the source of truth when `agents.md` points elsewhere.
- `doc/persudo/` is the module blueprint layer. Its top-level folders define the same modules that appear under `src/`, and each module folder keeps source design and test design together before implementation.
- `src/` stores implementation modules. Top-level module folders under `src/` should match the modules defined under `doc/persudo/`; tests live inside the module they verify.
- `data/` stores raw domain data, seed content, imported records, fixtures, and structured knowledge consumed by the project. Keep it separate from `src/` unless there is an explicit import path, migration, or runtime data model.

Use modules as the big structural mapping across planning, implementation, and verification:

```text
doc/persudo/<module>/
  <code-file>.md
  test/
    <test-code-file>.md
src/<module>/
  <code-file>
  test/
    <test-code-file>
```

Mirroring applies to code files and code files only. Every durable code file under `src/<module>/` should have a corresponding markdown blueprint under `doc/persudo/<module>/`; every durable test code file under `src/<module>/test/` should have a corresponding markdown blueprint under `doc/persudo/<module>/test/`. Folders, data files, generated files, config files, assets, and non-code artifacts do not automatically need mirrored markdown files.

When a module is added, moved, renamed, split, or merged, update the blueprint and source locations together. When a code file is added, removed, moved, or renamed, update its mirrored markdown file in the same change. Promote shared code or shared instructions only after a pattern repeats.
