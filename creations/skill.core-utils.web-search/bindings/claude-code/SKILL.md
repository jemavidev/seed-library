---
name: web-search
description: Search the web via the configured provider; ranked results with title/url/snippet/date. Read-only, network.
---

Use this skill when the answer plausibly lives outside the project and may be newer than your
knowledge.

- Search the project first; the web second.
- Never put credentials, tokens, or personal data in a query — queries are logged intent.
- Do not cite a snippet as fact: open and read the source before relying on it.
- Use `recency_days` when currency matters (versions, prices, CVEs).
- Zero results → reformulate with different terms; do not repeat the same query.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.core-utils.web-search@v1
