---
name: initializing-repo
description: Initialize a repository with the user's standard starter structure and agent guide. Use when the user asks to initialize, scaffold, reset, or standardize a repo structure containing agents.md, doc/instructions, doc/persudo, src, and data, or asks for an architecture section explaining that structure.
---

# Initializing Repo

## Workflow

1. Inspect the current project tree before editing.
2. Create this structure if missing:

```text
agents.md
doc/
  instructions/
  persudo/
src/
data/
```

3. Preserve existing files. Move or rename only when the user's requested structure clearly requires it.
4. If an uppercase `AGENTS.md` exists and `agents.md` does not, rename it to `agents.md`.
5. If `docs/` exists and `doc/instructions/` does not, move `docs/` to `doc/instructions/`.
6. Create missing directories with `mkdir -p`.
7. Add or update an `Architecture` section in `agents.md`.
8. Update stale references from `docs/` to `doc/instructions/` when they appear in `agents.md`.
9. Verify the resulting tree.

## agents.md Architecture Section

Add this section if no architecture section exists. If one exists, merge the intent without duplicating headings.

```md
## Architecture

- Keep durable app code under `src/`.
- Keep project instructions, product notes, design-code mapping, and decision records under `doc/instructions/`.
- Use `doc/persudo/` for early pseudo-code, workflow sketches, and implementation notes that are not yet durable product documentation.
- Keep raw domain data and seed content under `data/` until there is an explicit import, migration, or application data model for it.
- Organize `src/` by product workflow as the app grows.
- Promote shared code only after a repeated pattern is real.
- Keep domain types explicit and close to the workflow that owns them until a cross-workflow contract is real.
```

## Safety

- Do not delete user files while initializing the repo.
- Do not overwrite an existing `agents.md`; patch it in place.
- Do not move domain data into `src/` unless the user explicitly asks for that migration.
- Mention any existing folders that remain outside the standard structure.
