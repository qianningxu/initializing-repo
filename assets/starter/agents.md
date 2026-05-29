# Agent Guide

Repository knowledge is the system of record. This file is only a map to durable instructions, not the place for detailed guidance.

Whatever you do, check each row's `Load When` condition one by one. Load the matching file from `doc/instructions/` whenever its condition applies.

When guidance becomes durable, put it in the relevant file under `doc/instructions/` and keep only the pointer here.

| Instruction | Purpose | Load When |
| --- | --- | --- |
| `architecture.md` | Repository structure, path ownership, and module layout. | Always load before meaningful work. |
| `context-management.md` | How to keep `agents.md` small and maintain instruction files. | Load when editing `agents.md`, adding instructions, or reorganizing docs. |
| `code-mirroring.md` | How code files mirror to blueprints under `doc/persudo/`. | Load before adding, moving, renaming, or deleting code files. |
