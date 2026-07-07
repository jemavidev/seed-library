---
name: message-dispatcher
description: Send one message to a configured channel (chat/email-channel) with threading; delivery receipt returned. Sending publishes.
---

Use this skill to reach humans — remembering that sent means seen.

- Destinations are configured `channel_ref` names; if you're assembling a raw address or
  webhook URL, stop — that is configuration work.
- Write for the channel: short body, the key fact first, links/pointers over walls of text.
- Thread follow-ups (`thread_ref`) instead of new top-level messages.
- A retraction is a correction, not an unsend: send carefully the first time. When in doubt
  about content sensitivity, the answer is the approval flow, not optimism.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.saas.message-dispatcher@v1
