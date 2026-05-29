# agents.md

`agents.md` is a routing table, not a manual. Keep it short enough that agents can hold the whole map in context while still having room for the task, code, and relevant docs.

## Size Target

Aim for roughly 500-1,000 words, or about 75-150 lines. A shorter file is fine when the repo is small.

## Split Rule

Split by attention, not just by word count. Move details out of `agents.md` when a section becomes:

- More than about 200-300 words on one topic.
- Something an agent only needs sometimes.
- A living artifact with ongoing updates.
- A reference instead of a standing instruction.

## What Stays In agents.md

- The repository map.
- Non-negotiable rules agents must always follow.
- Pointers to deeper instruction files.
- Short workflow reminders that apply to most tasks.

## What Moves To doc/instructions/

- Product briefs and feature specs.
- Design-code maps and design parity notes.
- Stack, framework, testing, and command references.
- Architecture details beyond the top-level map.
- Decision logs, execution plans, quality notes, and release notes.
- Domain references, examples, and long explanations.

## Maintenance

When `agents.md` starts reading like an encyclopedia, move the details into `doc/instructions/` and leave a concise pointer behind. Prefer focused instruction files over one large mixed-purpose document.
