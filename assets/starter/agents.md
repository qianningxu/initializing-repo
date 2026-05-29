Repository knowledge is the system of record. Treat this file as a map; keep durable guidance in `doc/instructions/`.

Before acting, check each `Load When` condition below one by one. Load every matching file from `doc/instructions/`.

When new guidance becomes durable, add it to the right instruction file and keep only the pointer here.

| Instruction | Purpose | Load When |
| --- | --- | --- |
| `architecture.md` | Repository structure, path ownership, and module layout. | Always load before meaningful work. |
| `context-management.md` | How to keep `agents.md` small and maintain instruction files. | Load when editing `agents.md`, adding instructions, or reorganizing docs. |
| `code-mirroring.md` | How code files mirror to blueprints under `doc/persudo/`. | Load before adding, moving, renaming, or deleting code files. |
