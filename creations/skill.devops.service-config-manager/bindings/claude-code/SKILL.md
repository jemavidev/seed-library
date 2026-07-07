---
name: service-config-manager
description: Two-phase service config changes: validate (diagnostics), apply (validated candidates only, auto-revert on failed reload), rollback.
---

Use this skill to change running-service behavior safely.

- `validate` first, read every diagnostic — warnings are tomorrow's incident.
- `apply` only what you validated in this same flow; editing the file between the two calls
  restarts the flow.
- Record the returned `version_ref`; it is the rollback handle.
- After `apply`, verify behavior with a health probe — a reload that succeeded is not yet a
  service that works.
- On `reload_failed`, the prior config is already back; your job is the diagnosis, not the
  recovery.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.devops.service-config-manager@v1
