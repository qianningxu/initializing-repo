---
name: initializing-repo
description: Initialize a repository with the user's standard starter structure and agent guide. Use when the user asks to initialize, scaffold, reset, or standardize a repo structure containing agents.md, doc/instructions, doc/persudo, src, and data, or asks for an architecture section explaining that structure.
---

# Initializing Repo

## Workflow

Assume the target directory is empty unless the user says otherwise.

1. Create this structure:

```text
agents.md
doc/
  instructions/
    agents-md.md
  persudo/

src/
data/
```

2. Write `agents.md` with the `Architecture` section below.
3. Write `doc/instructions/agents-md.md` with the `agents.md Splitting Guidance` section below.
4. Leave `doc/persudo/`, `src/`, and `data/` ready for future files.
5. Verify the resulting tree.

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
    agents-md.md
  persudo/

src/
data/
```

- `agents.md` is the agent entry point. Keep it concise, roughly 100 lines when possible. It should explain how to navigate the repository, link to deeper instructions, and name the rules that must always be in context. See `doc/instructions/agents-md.md` for when to split details out of `agents.md`.
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
````

## agents.md Splitting Guidance

Create this file at `doc/instructions/agents-md.md`.

```md
# agents.md

`agents.md` is a routing table, not a manual. Keep it short enough that agents can hold the whole map in context while still having room for the task, code, and relevant docs.

## Size Target

Aim for roughly 500-1,000 words, or about 75-150 lines. A shorter file is fine when the repo is small.

## Split Rule

Split by attention, not just by word count. Move details out of `agents.md` when a section becomes:

- More than about 200-300 words on one topic.
- Something an agent only needs sometimes.
- A living artifact with ongoing updates.
- A reference instead of a standing instruction.

## What Stays In agents.md

- The repository map.
- Non-negotiable rules agents must always follow.
- Pointers to deeper instruction files.
- Short workflow reminders that apply to most tasks.

## What Moves To doc/instructions/

- Product briefs and feature specs.
- Design-code maps and design parity notes.
- Stack, framework, testing, and command references.
- Architecture details beyond the top-level map.
- Decision logs, execution plans, quality notes, and release notes.
- Domain references, examples, and long explanations.

## Maintenance

When `agents.md` starts reading like an encyclopedia, move the details into `doc/instructions/` and leave a concise pointer behind. Prefer focused instruction files over one large mixed-purpose document.
```

## Safety

- Do not delete user files while initializing the repo.
- Do not overwrite an existing `agents.md`; patch it in place.
- Do not move domain data into `src/` unless the user explicitly asks for that migration.
- Keep module folders structurally aligned across `doc/persudo/` and `src/`.
- Mirror code files only. Do not create markdown mirrors for folders, data, generated files, config, assets, or non-code artifacts unless the user explicitly asks.
- When adding a module, create or update `doc/persudo/<module>/` and `src/<module>/` together when relevant.
- When adding a code file, create or update the matching markdown blueprint under `doc/persudo/<module>/`.
- Mention any existing folders that remain outside the standard structure.
