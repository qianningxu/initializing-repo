# Instruction Creation

Use repository instructions as a structured knowledge base, not as one large manual. `agents.md` is the entry point; focused files under `doc/instructions/` are the source of truth.

## Purpose

Create an instruction file when guidance is durable, reusable, and likely to be needed across more than one work session.

Good instruction files cover:

- Architecture and module boundaries.
- Product intent and feature specs.
- Design rules and design-code parity.
- Stack, testing, command, and deployment conventions.
- Decision logs, execution plans, quality notes, reliability, and security.
- Domain references that agents should consult before acting.

## Naming

Name files by content, not by the file or agent that uses them.

Prefer:

```text
context-management.md
instruction-creation.md
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

Keep `agents.md` small by moving details into focused instruction files and linking to them.

## Structure

Use a short, scannable structure:

```text
# Topic

## Purpose
## Rules
## When To Update
```

Add examples only when they prevent ambiguity. Avoid background, motivational framing, and long prose that does not change agent behavior.

## Maintenance

Update instruction files in the same change as the behavior they describe. If an instruction becomes stale, either repair it or delete it. Prefer a small accurate doc over a large partially true one.
