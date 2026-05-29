# Architecture

Use the repository structure as the durable map of project knowledge, implementation, and data.

## Structure

```text
agents.md
doc/
  instructions/
    architecture.md
    context-management.md
    code-mirroring.md
  persudo/

src/
data/
```

## Scope

- `agents.md`: map to instruction files only.
- `doc/instructions/`: durable knowledge base and source of truth.
- `doc/persudo/`: code-file blueprints, organized by module.
- `src/`: implementation modules; tests live inside the module they verify.
- `data/`: raw domain data, imports, fixtures, seed content, and structured knowledge.

## Module Ownership

Keep module folders aligned across `doc/persudo/` and `src/`.

```text
doc/persudo/<module>/
src/<module>/
```

Tests live inside the implementation module:

```text
src/<module>/test/
```

Their blueprints live under the matching module blueprint:

```text
doc/persudo/<module>/test/
```
