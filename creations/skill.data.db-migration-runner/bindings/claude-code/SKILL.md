---
name: db-migration-runner
description: Apply/rollback versioned schema migrations with dry-run planning; built to run behind an approval gate.
---

Use this skill for schema evolution, always in two steps.

- **Always dry-run first.** The plan (which versions, which have no down) is what you present
  for approval; running without a reviewed plan is how schemas break at 3am.
- Down-less migrations deserve explicit mention when you request approval.
- On `partial_failure`, report exactly which versions applied and stop — do not "continue
  from where it broke" without a fresh dry-run and gate.
- On `checksum_mismatch`, someone edited history: freeze and escalate; never re-hash to match.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.data.db-migration-runner@v1
