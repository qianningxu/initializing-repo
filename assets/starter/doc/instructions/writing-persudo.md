- Use these rules only when writing or editing mirrored blueprints under `doc/persudo/`.

## Function Calls

- When a function, class, or object uses another documented symbol, link only to that symbol heading:
	- Same file: `[[#symbol| symbol]]`.
	- Cross-file: `[[page#symbol| symbol]]`.
- Link calls in pseudo code, target sections, diagram notes, examples, and implementation notes.
- If the called symbol has no blueprint heading yet, create or update that blueprint before linking.
- Do not link generic actions such as validate input, build result, loop, or return output.

## Blueprints

- Write pseudo code as human-level behavior, not executable code.
- Prefer understandable behavior over maximum compression. Avoid implementation-only shorthand like `Resolve root`.
- Use numbered steps when order matters. Use bullets when order does not matter.
- Use bullets or nested bullets when they better match the code structure, branches, or grouped operations. Indent nested bullets with tabs.
- Function, class, and object headings must match the code name exactly so `#symbol` links resolve.
- For functions, use `# \`function_name\``, then a compact `python` block with parameters and return type, then behavior bullets.

## Diagrams And Notes

- Use fenced Mermaid blocks only when a diagram adds value: ```` ```mermaid ````.
- Keep Mermaid syntax parser-safe: quoted labels, one edge per line, simple node names.
- For loops in Mermaid diagrams, draw repeated steps inside a labeled `subgraph`.
- Use Obsidian callouts for inline or nested implementation notes when needed: `> [!example] name`.
