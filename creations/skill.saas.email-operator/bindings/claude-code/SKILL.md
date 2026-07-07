---
name: email-operator
description: Transactional email with explicit recipients and sandbox attachments. Cannot be unsent — expect strict gating.
---

Use this skill for deliberate mail to named people.

- Triple-check the recipient list; `to` is the highest-consequence field you will fill today.
- Sent is final: draft the body, re-read it as the recipient, then send. There is no undo,
  only embarrassing corrections.
- Partial acceptance is a result: report `rejected` addresses; never blind-retry the whole
  list.
- Attachments come from the project sandbox by path — verify the file is the version you
  mean to share before attaching.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.saas.email-operator@v1
