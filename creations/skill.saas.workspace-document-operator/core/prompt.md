---
name: workspace-document-operator
description: Read/append/replace-range/create in hosted collaborative documents; every edit returns a revision_id for rollback.
---

Use this skill to work with the team's shared documents.

- `read` before any edit — shared documents change under you; a `conflict` means re-read,
  re-derive, retry once.
- Prefer `append` and `replace-range` over full rewrites: smaller edits, cleaner revisions,
  easier rollback.
- Record the returned `revision_id` in your report; it is the undo handle.
- Shared means seen: colleagues may read your edit before any rollback lands. Draft locally
  when unsure, publish when sure.
