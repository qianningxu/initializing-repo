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
    architecture.md
    context-management.md
    code-mirroring.md
  persudo/

src/
data/
```

3. Verify the resulting tree.
4. Initialize git if the target directory is not already a git repository:

```bash
git init
git branch -M main
git add agents.md doc src data
git commit -m "Initialize repository structure"
```

5. If creating or publishing a remote repository, make it private by default. Use public visibility only when the user explicitly asks for public.

If the directory is not empty, preserve existing files. Do not overwrite an existing `agents.md` or instruction file without checking whether it should be patched or left as-is.
