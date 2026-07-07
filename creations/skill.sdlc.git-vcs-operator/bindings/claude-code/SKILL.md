---
name: git-vcs-operator
description: Version-control operations (status, branch, checkout, commit, push, revert) — one action per call; push publishes and needs confirmation.
---

Use this skill to record and publish work through version control.

- Run `status` before `commit`; commit only what the change intended, with a message that
  states the why.
- Never `push` unasked: pushing publishes. Expect and respect a confirmation step.
- On `push_rejected`, fetch/rebase once and retry once; never force-push through it.
- To undo, prefer `revert` (adds an inverse commit) over anything that rewrites history.
- One action per call — no compound "commit and push" shortcuts.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.sdlc.git-vcs-operator@v1
