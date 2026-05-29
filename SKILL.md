---
name: initializing-repo
description: Initialize a repository with the user's standard starter structure and agent guide. Use when the user asks to initialize, scaffold, reset, or standardize a repo structure containing agents.md, doc/instructions, doc/persudo, src, and data, or asks for an architecture section explaining that structure.
---

# Initializing Repo

## Workflow

Assume the target directory is empty unless the user says otherwise.

1. Copy `assets/starter/` into the target repository.
2. Ensure these paths exist:

```text
agents.md
doc/
  instructions/
    agents-md.md
  persudo/

src/
data/
```

3. Verify the resulting tree.

If the directory is not empty, preserve existing files. Do not overwrite an existing `agents.md` or instruction file without checking whether it should be patched or left as-is.

## Template Contents

- `assets/starter/agents.md` contains the starter agent guide and architecture section.
- `assets/starter/doc/instructions/agents-md.md` contains guidance for keeping `agents.md` short and moving deeper material into `doc/instructions/`.
- Empty starter folders under `doc/persudo/`, `src/`, and `data/` may need placeholder files if the destination system does not preserve empty directories.

## Safety

- Do not delete user files while initializing the repo.
- Keep module folders structurally aligned across `doc/persudo/` and `src/`.
- Mirror code files only. Do not create markdown mirrors for folders, data, generated files, config, assets, or non-code artifacts unless the user explicitly asks.
- When adding a module, create or update `doc/persudo/<module>/` and `src/<module>/` together when relevant.
- When adding a code file, create or update the matching markdown blueprint under `doc/persudo/<module>/`.
- Mention any existing folders that remain outside the standard structure.
