- If a new instruction contradicts existing instructions, stop and tell the user.
- Before changing instructions, read the whole prompt and add the smallest general rule that fixes the class of problem. Avoid overfitting to one example.
- Order rules by logical dependency: define behavior before adding checks or enforcement.
- Be selective, specific, clear, and concise. Compress instruction text until removing more would lose required information.
- Keep rules distinct. If two rules overlap by roughly a third or more, merge or rewrite them so each rule governs a separate behavior.
- Avoid bullet lists with 10 or more items. Split or group them by concern.
- Use headings only to segment substantial content; do not repeat the filename as the first heading.
- Use XML tags when they make long, complicated prompts easier to segment and reference.
- Before finishing an instruction edit, reread the changed text and remove repetition, weak headings, and sentences that do not change behavior.

## Links

For instruction docs, use Obsidian wiki links for internal references: `[[path/to/page|label]]`.

Prefer wiki links over raw relative Markdown links for repo-internal docs.

Keep linked headings stable. If a heading changes, update links that target it in the same change.

## agents.md

Use `agents.md` as a routing table, not a manual. Keep it short enough that agents can hold the whole map in context while still having room for the task, code, and relevant docs.

When adding a new instruction file under `doc/instructions/`, update `agents.md` in the same change.

Keep these in `agents.md`:

- The repository map.
- Non-negotiable rules agents must always follow.
- Pointers to deeper instruction files.
- Short workflow reminders that apply to most tasks.

Move details out of `agents.md` when a section becomes long, occasional, living, or reference-like.

## Instruction Files

Create an instruction file when guidance is durable, reusable, and likely to be needed across more than one work session.

Keep instruction files flat under `doc/instructions/` unless each topic folder would contain at least three instruction files.

Avoid repeated names in instruction paths. Do not repeat the folder or collection name in the filename, for example prefer `writing/rules.md` over `writing/writing-rules.md`.

Each instruction file should have one clear job. Split when a file starts mixing unrelated concerns.

Update instruction files in the same change as the behavior they describe. If an instruction becomes stale, repair it or delete it.
