---
name: crypto-token-generator
description: Generate random tokens, UUIDs, SHA-256 digests, or HMAC signatures (key by env-var name only). Pure.
---

Use this skill whenever you need a cryptographic value — never improvise one.

- Never invent "random" strings yourself; always call this for tokens and ids.
- For HMAC, pass the environment variable *name* in `key_env`; if you ever have the key value
  in hand, something upstream is wrong — stop and report it.
- Do not use sha256-digest for passwords; say so if asked, and recommend a proper KDF flow.
- Default token length (32 bytes) is right for most uses; justify any deviation.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.core-utils.crypto-token-generator@v1
