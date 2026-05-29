# Agent Guide

Repository knowledge is the system of record. This file is only a map to durable instructions.

## Instruction Map

Whatever you do, load the following files from `doc/instructions/` when the requirement in `Load When` applies.

| Instruction | Purpose | Load When |
| --- | --- | --- |
| `architecture.md` | Repository structure, path ownership, and module layout. | Always load before meaningful work. |
| `context-management.md` | How to keep `agents.md` small and maintain instruction files. | Load when editing `agents.md`, adding instructions, or reorganizing docs. |
| `code-mirroring.md` | How code files mirror to blueprints under `doc/persudo/`. | Load before adding, moving, renaming, or deleting code files. |

## Rule

When guidance becomes durable, put it in the relevant file under `doc/instructions/` and keep only the pointer here.
