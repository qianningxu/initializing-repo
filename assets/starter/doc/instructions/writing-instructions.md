## Editing Flow

- Before changing instructions, read the whole prompt and add the smallest general rule that fixes the class of problem. Avoid overfitting to one example.
- If a new instruction contradicts existing instructions, stop and tell the user.
- Order rules by logical dependency: define behavior before adding checks or enforcement.
- Keep rules distinct. If two rules overlap by roughly a third or more, merge or rewrite them so each rule governs a separate behavior.
- Before finishing an instruction edit, reread the changed text and remove repetition, weak headings, and sentences that do not change behavior.

## File Management

- When adding a new instruction file or renaming an existing file under `doc/instructions/`, update the table in `agents.md`.
- Keep instruction files flat under `doc/instructions/` unless each topic folder would contain at least three instruction files.
- Reorganize a folder once it has more than seven instruction files.

## Writing Structure

- Use bullets by default.
- Use sub-bullets to break a rule into smaller parts.
- Use headings only to segment substantial content; do not repeat the filename as the first heading.
- If a section has more than seven top-level bullets, split it with subheadings.
- If an instruction file grows past 600 words, consider splitting it into more files.

## Style

- Be selective, specific, clear, and concise. Compress instruction text until removing more would lose required information.
- Use XML tags when they make long, complicated prompts easier to segment and reference.

## Links

- For instruction docs, use Obsidian wiki links for internal references: `[[path/to/page|page]]`.
- When renaming an instruction file, run `python3 src/agents/update_wiki_links.py --root . --old old/path --new new/path` to update wiki links.
