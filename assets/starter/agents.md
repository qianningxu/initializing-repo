Before acting, check each `Load When` condition below one by one. Load every matching file from `doc/instructions/`.

When a loaded instruction file links to another instruction file with `[[...]]`, read every linked instruction file before applying the instruction.

Use `agents.md` as a routing table, not a manual. Keep it short enough that agents can hold the whole map in context while still having room for the task, code, and relevant docs.

When adding a new instruction file under `doc/instructions/`, update this table in the same change.

Keep these in `agents.md`:

- The repository map.
- Non-negotiable rules agents must always follow.
- Pointers to deeper instruction files.
- Short workflow reminders that apply to most tasks.

Move details out of `agents.md` when a section becomes long, occasional, living, or reference-like.

Create an instruction file when guidance is durable, reusable, and likely to be needed across more than one work session.

Keep instruction files flat under `doc/instructions/` unless each topic folder would contain at least three instruction files.

Avoid repeated names in nested instruction paths. Do not repeat the folder name in the filename, for example prefer `writing/rules.md` over `writing/writing-rules.md`.

Each instruction file should have one clear job. Split when a file starts mixing unrelated concerns.

Update instruction files in the same change as the behavior they describe. If an instruction becomes stale, repair it or delete it.

| Instruction                | Scope                                                         | Load When                                                                                     |
| -------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `architecture.md`          | Repository layout and code/blueprint mirroring.               | Always                                                                                        |
| `writing-instructions.md`  | Instruction authoring, routing, and maintenance.              | Load before creating or editing `agents.md` or any instruction file.                          |
| `writing-persudo.md`       | Blueprint syntax, Obsidian links, callouts, and diagrams.     | Load before writing or editing mirrored files under `doc/persudo/`.                           |
| `workflow.md`              | Feature-slice planning, implementation, and verification flow. | Load before planning or implementing a feature slice, changing scope, or recording decisions. |
