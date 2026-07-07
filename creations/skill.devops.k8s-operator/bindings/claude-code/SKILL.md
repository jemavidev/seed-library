---
name: k8s-operator
description: Apply/scale/rollback/delete orchestrated workloads with rollout verification; every mutation anchored to revision history.
---

Use this skill to operate workloads, treating rollout readiness as the finish line.

- `apply` isn't done at "accepted" — wait for `rolled-out` or `rollout_failed`, and report
  which.
- On `rollout_failed`, the default move is `rollback` to the prior revision, then diagnose
  from the failed pods' conditions — restore service first, investigate second.
- Record the `revision` every mutation returns; it is your undo handle.
- `delete` only for resources whose manifests are in version control — re-apply is the
  compensation, and it must exist.
- `status` before `scale`: know the current count you'd be scaling back to.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.devops.k8s-operator@v1
