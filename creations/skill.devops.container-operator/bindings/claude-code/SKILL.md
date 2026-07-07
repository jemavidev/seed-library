---
name: container-operator
description: Container lifecycle (build/run/stop/logs/remove/push) against the configured runtime; push publishes to a registry.
---

Use this skill for container work, one action at a time.

- Tag images immutably (`api:1.4.2`, never a moving `latest` you later re-push) — a pushed
  tag is a published fact.
- After `run`, verify with a health probe before calling the service up.
- Read `logs` before restarting a misbehaving container: restarts destroy the evidence.
- Never bake a secret into an image (build args and env refs only); if a build needs a
  credential file, that build is misdesigned — say so.
- `push` rides the approval flow; expect confirmation.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.devops.container-operator@v1
