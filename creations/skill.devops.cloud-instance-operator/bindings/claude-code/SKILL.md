---
name: cloud-instance-operator
description: Provider-neutral instance lifecycle (provision/start/stop/reboot/terminate/status); terminate destroys data and has no undo.
---

Use this skill for VM lifecycle work, with cost and blast radius in mind.

- Tag every provision with owner and purpose; untagged instances are future orphan bills.
- `status` before any mutation — act on the state that is, not the state you remember.
- Stop is the default "make it not run"; `terminate` only when the brief says destroy, and
  expect expert review — instance-local data dies with it.
- Never terminate an instance you didn't provision or that isn't named in the brief; shared
  environments contain other people's work.
- Provisioning costs money per hour from this call on: note it in your report.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.devops.cloud-instance-operator@v1
