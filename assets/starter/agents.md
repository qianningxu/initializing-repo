Before acting, check each `Load When` condition below one by one. Load every matching file from `doc/instructions/`.

When a loaded instruction file links to another instruction file with `[[...]]`, read every linked instruction file before applying the instruction.

When adding a new instruction file under `doc/instructions/`, update this table in the same change.

| Instruction         | Scope                                                                                           | Load When                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `architecture.md`   | Repository structure, path ownership, module layout, and code-file mirroring.                   | Always                                                                                        |
| `rules.md`          | Instruction style, `agents.md` routing, and instruction-file maintenance.                       | Load before creating or editing `agents.md` or any instruction file.                          |
| `persudo.md`        | Obsidian links, heading targets, callouts, Mermaid, and blueprint writing rules.                 | Load before writing or editing mirrored files under `doc/persudo/`.                           |
| `feature-slice.md`  | Feature-slice workflow, doc updates, implementation checks, and optional design-code alignment. | Load before planning or implementing a feature slice, changing scope, or recording decisions. |
