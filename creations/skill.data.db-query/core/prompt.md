---
name: db-query
description: Read-only SQL against a configured connection; rows + truncation metadata. Mutating statements are rejected.
---

Use this skill to look at data, never to change it.

- Name the connection by its configured ref; if you find yourself constructing a connection
  string, stop — that is a configuration task, not a query.
- Aggregate in SQL (GROUP BY, count, sum) instead of pulling raw rows to summarize yourself.
- Respect `truncated: true`: refine the query; don't just raise `row_limit`.
- If the statement is rejected as non-read-only, that is the contract working — switch to
  `db-write` and its approval flow instead of rephrasing to sneak past the check.
