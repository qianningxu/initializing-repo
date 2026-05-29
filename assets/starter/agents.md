# Agent Guide

Repository knowledge is the system of record. This file is only a map to durable instructions.

## Instructions

| Instruction | Purpose | Load When |
| --- | --- | --- |
| `doc/instructions/architecture.md` | Repository structure, path ownership, and module layout. | Always load before meaningful work. |
| `doc/instructions/context-management.md` | How to keep `agents.md` small and maintain instruction files. | Load when editing `agents.md`, adding instructions, or reorganizing docs. |
| `doc/instructions/code-mirroring.md` | How code files mirror to blueprints under `doc/persudo/`. | Load before adding, moving, renaming, or deleting code files. |

## Rule

When guidance becomes durable, put it in the relevant file under `doc/instructions/` and keep only the pointer here.
