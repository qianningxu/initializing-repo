Use repository instructions as a structured knowledge base, not as one large manual. `agents.md` is the entry point; focused files under `doc/instructions/` are the source of truth.

## agents.md

`agents.md` is a routing table, not a manual. Keep it short enough that agents can hold the whole map in context while still having room for the task, code, and relevant docs.

Aim for roughly 500-1,000 words, or about 75-150 lines. A shorter file is fine when the repo is small.

Keep these in `agents.md`:

- The repository map.
- Non-negotiable rules agents must always follow.
- Pointers to deeper instruction files.
- Short workflow reminders that apply to most tasks.

Move details out of `agents.md` when a section becomes:

- More than about 200-300 words on one topic.
- Something an agent only needs sometimes.
- A living artifact with ongoing updates.
- A reference instead of a standing instruction.

## Instruction Files

Create an instruction file when guidance is durable, reusable, and likely to be needed across more than one work session.

Good instruction files cover:

- Architecture and module boundaries.
- Product intent and feature specs.
- Design rules and design-code parity.
- Stack, testing, command, and deployment conventions.
- Decision logs, execution plans, quality notes, reliability, and security.
- Domain references that agents should consult before acting.

Name files by content, not by the file or agent that uses them.

Prefer:

```text
context-management.md
design-code-map.md
testing-strategy.md
```

Avoid:

```text
agents.md
codex.md
notes.md
misc.md
```

## Scope

Each instruction file should have one clear job. Split when a file starts mixing unrelated concerns, such as product behavior, testing policy, design rules, and architecture details.

Use a short, scannable structure:

```text
# Topic

## Purpose
## Rules
## When To Update
```

Add examples only when they prevent ambiguity. Avoid background, motivational framing, and long prose that does not change agent behavior.

## Maintenance

When `agents.md` starts reading like an encyclopedia, move the details into `doc/instructions/` and leave a concise pointer behind. Update instruction files in the same change as the behavior they describe. If an instruction becomes stale, either repair it or delete it.
