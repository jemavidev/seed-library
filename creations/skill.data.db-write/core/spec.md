# skill.data.db-write — spec

## What it does
Executes a **mutating** SQL statement (INSERT/UPDATE/DELETE) inside a transaction, with two
built-in safety rails: the caller must state the expected blast radius (`expected_max_rows`)
and must provide the inverse statement (`inverse_statement`) that undoes the change — or run
in dry-run mode.

## When to use / when not
- **Use** for data mutations whose inverse you can write down.
- **Don't use** for schema changes (`db-migration-runner`) or when you cannot express the
  inverse — that inability is a signal the change needs a migration + backup, not a quick write.

## Inputs / outputs
- In: `connection_ref`, `statement`, `expected_max_rows` (fail if exceeded, pre-checked in
  the transaction), `inverse_statement` (null ⇒ dry-run: execute, report, roll back).
- Out: `{ affected_rows, committed, dry_run }`.

## Worked example
`{ "connection_ref": "app", "statement": "UPDATE users SET plan='pro' WHERE id=42",
"expected_max_rows": 1, "inverse_statement": "UPDATE users SET plan='free' WHERE id=42" }` →
`{ "affected_rows": 1, "committed": true, "dry_run": false }`.

## Failure modes
- `affected_rows_exceeded` — statement would touch more rows than declared; rolled back,
  nothing committed (not retryable: re-scope the WHERE clause, don't raise the number blindly).
- `constraint_violation` (not retryable) · `syntax_error` (not retryable)
- `connection_not_found` (not retryable) · `deadlock` (retryable once).

## Constraints
The inverse statement is recorded with the invocation so compensation can run it later without
reconstruction. `expected_max_rows` is a contract, not a hint: the implementation counts first
(same transaction) and aborts on excess. Dry-run mode is the preview tool — use it before any
statement whose WHERE clause you have not already verified with `db-query`.
