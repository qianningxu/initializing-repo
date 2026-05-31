- Before acting, check each `Load condition` below one by one. Load every matching file from `doc/instructions/`.
- When a loaded instruction file links to another instruction file with `[[...]]`, read every linked instruction file before applying the instruction.

| Instruction               | Scope                                                          | Load condition                                                                                |
| ------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `architecture.md`         | Repository layout and code/blueprint mirroring.                | Always                                                                                        |
| `writing-instructions.md` | Instruction authoring, routing, and maintenance.               | Load before creating or editing `agents.md` or any instruction file.                          |
| `writing-persudo.md`      | Blueprint syntax, Obsidian links, callouts, and diagrams.      | Load before writing or editing mirrored files under `doc/persudo/`.                           |
| `workflow.md`             | Feature-slice planning, implementation, and verification flow. | Load before planning or implementing a feature slice, changing scope, or recording decisions. |
