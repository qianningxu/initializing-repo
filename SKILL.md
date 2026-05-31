---
name: initializing-repo
description: Initialize a repository with the user's standard starter structure and agent guide. Use when the user asks to initialize, scaffold, reset, or standardize a repo structure containing agents.md, doc/instructions, doc/persudo, src, and data, or asks for an architecture section explaining that structure.
---

# Initializing Repo

## Workflow

Assume the target directory is empty unless the user says otherwise.

1. Copy `assets/starter/` into the target repository, excluding `agent-legacy.md`.
2. Ensure these paths exist:

```text
.obsidian/
agents.md
doc/
  instructions/
    architecture.md
    feature-slice.md
    persudo.md
    rules.md
  persudo/

src/
  agents/
    mirror_check.py
data/
```

Keep `assets/starter/agent-legacy.md` as a migration reference for this skill. Do not copy it into initialized repositories.

3. Verify the resulting tree.
4. Run the starter mirror check:

```bash
python3 src/agents/mirror_check.py --root .
```

If the target repo already has code, ask whether it is Python, TypeScript, or mixed before expanding mirror-check coverage beyond `.py`.

5. Initialize git if the target directory is not already a git repository:

```bash
git init
git branch -M main
git add .
git commit -m "Initialize repository structure"
```

For a non-empty target directory, replace `git add .` with `git add .obsidian agents.md doc src data` to avoid staging unrelated files.

6. If creating or publishing a remote repository, make it private by default. Use public visibility only when the user explicitly asks for public.

If the directory is not empty, preserve existing files. Do not overwrite an existing `agents.md` or instruction file without checking whether it should be patched or left as-is.
