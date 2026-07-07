---
name: kv-cache-operator
description: Namespaced key-value cache with TTL (get/set/delete). Ephemeral by contract — a miss means recompute.
---

Use this skill to avoid recomputing expensive intermediates.

- Treat every `get` miss as "recompute", never as an error; the cache is allowed to be cold.
- Always set a TTL that matches how long the value stays true, not how long you'd like it to.
- Namespace by task/flow so cleanup is a namespace drop, not a key hunt.
- Never cache secrets, tokens, or personal data — the cache has weaker guarantees than
  everything else in the system.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.data.kv-cache-operator@v1
