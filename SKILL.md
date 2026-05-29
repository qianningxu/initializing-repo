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
  persudo/
src/
data/
```

2. Write `agents.md` with the `Architecture` section below.
3. Leave `doc/instructions/`, `doc/persudo/`, `src/`, and `data/` ready for future files.
4. Verify the resulting tree.

If the directory is not empty, preserve existing files and patch `agents.md` in place instead of overwriting it.

## agents.md Architecture Section

Add this section if no architecture section exists. If one exists, merge the intent without duplicating headings.

````md
## Architecture

The repository is organized around a small, durable project spine:

```text
agents.md
doc/
  instructions/
  persudo/
src/
data/
```

- `agents.md` is the project operating guide for Codex and other agents. Keep standing instructions here: product intent, design rules, architecture, working loop, engineering defaults, and any repo-specific constraints agents must follow every time they work in this project.
- `doc/instructions/` stores durable project documentation. Use it for product briefs, decision logs, design-code maps, architecture notes, workflow docs, and other instructions that should remain true across multiple work sessions.
- `doc/persudo/` stores rough planning material before it becomes durable documentation or code. Use it for pseudo-code, algorithm sketches, workflow drafts, implementation notes, and temporary thinking that may later move into `doc/instructions/` or `src/`.
- `src/` stores application source code. Organize it by product workflow or domain surface as the app grows, and keep production code, components, state, types, and tests close to the behavior they support.
- `data/` stores raw domain data, seed content, imported records, fixtures, and structured knowledge that the app may consume. Do not move data into `src/` until there is an explicit import path, migration, or runtime data model.

Keep shared code and shared documentation small at first. Promote patterns only after they repeat, and keep ownership clear by placing files near the workflow, feature, or domain that uses them.
````

## Safety

- Do not delete user files while initializing the repo.
- Do not overwrite an existing `agents.md`; patch it in place.
- Do not move domain data into `src/` unless the user explicitly asks for that migration.
- Mention any existing folders that remain outside the standard structure.
