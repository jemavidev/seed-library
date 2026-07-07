---
name: file-search
description: Find files by name or lines by content/regex across the project, with locations and excerpts. Read-only.
---

Use this skill to locate before you read.

- Start specific (an identifier, an exact phrase); broaden only if you get zero matches.
- Zero matches is information — do not retry the same pattern.
- If `truncated: true`, either narrow the pattern or raise `max_results` — never assume you saw
  everything.
- Follow up on a hit by reading that file at the reported line, not by re-searching.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.core-utils.file-search@v1
