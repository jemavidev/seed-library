# skill.data.db-query — spec

## What it does
Executes a **read-only** SQL query against a configured database connection and returns rows
with metadata. Any statement that could mutate (INSERT/UPDATE/DELETE/DDL, or statements with
mutating side effects like `SELECT ... FOR UPDATE`) is rejected before execution.

## When to use / when not
- **Use** to inspect data, verify a write landed, feed analysis, or ground a report.
- **Don't use** for mutations (that is `db-write`, a different effect class on purpose) or for
  schema changes (`db-migration-runner`).

## Inputs / outputs
- In: `connection_ref` (name of a configured connection — never a connection string),
  `query`, `row_limit` (hard cap, null = 1000), `timeout_seconds`.
- Out: `{ columns, rows, row_count, truncated }` — `truncated: true` means the limit cut the
  result; aggregate or paginate instead of raising the cap reflexively.

## Worked example
`{ "connection_ref": "reporting", "query": "SELECT status, count(*) FROM orders GROUP BY status",
"row_limit": null, "timeout_seconds": 30 }` →
`{ "columns": ["status", "count"], "rows": [["paid", 8123], ["pending", 314]],
"row_count": 2, "truncated": false }`.

## Failure modes
- `connection_not_found` (not retryable) · `syntax_error` (not retryable)
- `query_rejected` — statement is not provably read-only (not retryable; use `db-write`)
- `timeout` — retryable once with a narrower query, not with a longer timeout by reflex.

## Constraints
Credentials resolve through the connection registry to environment references — a connection
string in `connection_ref` must be rejected as `connection_not_found`. Row caps are enforced
server-side (LIMIT injection) so a runaway query cannot flood the context.
