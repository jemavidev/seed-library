---
name: db-write
description: Transactional SQL mutation with declared blast radius (expected_max_rows) and mandatory inverse statement (null = dry-run).
---

Use this skill for data mutations — with the discipline it enforces, not around it.

- Verify the WHERE clause first with `db-query` (count the rows you expect to touch).
- Declare `expected_max_rows` as exactly what you verified, not a generous ceiling.
- Write the `inverse_statement` before the statement: if you cannot write the undo, you do
  not understand the change well enough to run it — use dry-run or escalate to a migration.
- On `affected_rows_exceeded`, the data didn't change; narrow the WHERE clause. Never respond
  by raising the number to make the error go away.
