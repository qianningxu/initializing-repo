# Writing Instructions

Use instructions to shape agent behavior, not to capture every thought.

## Rules

- Writing everything is like writing nothing. Include only guidance that changes future behavior.
- Be clear and concise. Avoid waffling, repetition, motivational framing, and long background.
- Prefer short rules, tables, and examples over paragraphs when they carry the same meaning.
- If a new instruction contradicts existing instructions, stop and tell the user. Do not blindly apply the newest wording.

## File Names

Use lowercase kebab-case for human-authored instruction files. Kebab-case is easier to read in prose and works well for topic names.

```text
writing-instructions.md
context-management.md
code-mirroring.md
```

Use underscores only when the markdown file is mirroring a code file, module, or symbol that already uses underscores. In that case, preserve the source name exactly so the relationship is obvious.

```text
src/user_profiles/load_user.py
doc/persudo/user_profiles/load_user.md
```

Do not mix styles for preference. Choose hyphens for instruction topics; preserve underscores for mirrored code names.

## Heading

Repeat the filename as the first heading, converting kebab-case to title case.

```text
writing-instructions.md -> # Writing Instructions
code-mirroring.md -> # Code Mirroring
```
