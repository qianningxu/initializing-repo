- If a new instruction contradicts existing instructions, stop and tell the user.
- Before changing instructions, read the whole prompt and add the smallest general rule that fixes the class of problem. Avoid overfitting to one example.
- Order rules by logical dependency: define behavior before adding checks or enforcement.
- Be selective, specific, clear, and concise. Compress instruction text until removing more would lose required information.
- Keep rules distinct. If two rules overlap by roughly a third or more, merge or rewrite them so each rule governs a separate behavior.
- Use bullets by default. Use sub-bullets to break a rule into smaller parts.
- If a section has more than seven top-level bullets, split it with subheadings.
- If an instruction file grows past 600 words, consider splitting it into more files.
- Use headings only to segment substantial content; do not repeat the filename as the first heading.
- Use XML tags when they make long, complicated prompts easier to segment and reference.
- Before finishing an instruction edit, reread the changed text and remove repetition, weak headings, and sentences that do not change behavior.

## Links

For instruction docs, use Obsidian wiki links for internal references: `[[path/to/page|label]]`.

Prefer wiki links over raw relative Markdown links for repo-internal docs.

Keep linked headings stable. If a heading changes, update links that target it in the same change.
