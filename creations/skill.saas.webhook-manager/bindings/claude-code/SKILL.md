---
name: webhook-manager
description: Register/remove/list webhook subscriptions on configured providers; receivers must be the runtime's own endpoints.
---

Use this skill to wire event sources into automated flows — and to unwire them.

- Subscribe to the narrowest event set that serves the flow; broad subscriptions are noise
  plus attack surface.
- Keep the returned `webhook_id`: it is the exact undo handle.
- `list` before `register` — duplicate subscriptions double-fire flows.
- When a flow is retired, removing its webhooks is part of the retirement, not an optional
  cleanup.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.saas.webhook-manager@v1
