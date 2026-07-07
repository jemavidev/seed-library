# skill.data.db-migration-runner — spec

## What it does
Applies or rolls back versioned schema migrations from a migrations directory against a
configured connection, tracking the current schema version. The canonical consumer of the
`hitl-checkpoint` pattern: production runs should always sit behind an approval gate.

## When to use / when not
- **Use** for schema changes (DDL) and versioned data backfills that live as migration files.
- **Don't use** for ad-hoc data fixes (`db-write`) or unversioned schema tinkering — if it
  isn't a migration file, it doesn't run through this skill.

## Inputs / outputs
- In: `connection_ref`, `migrations_path`, `direction` (`up|down`), `target` (version to
  migrate to; null = latest for up / one step for down), `dry_run` (report the plan without
  executing).
- Out: `{ applied: [version ids in order], current_version, dry_run }`.

## Worked example
`{ "connection_ref": "app", "migrations_path": "db/migrations", "direction": "up",
"target": null, "dry_run": true }` →
`{ "applied": ["0007_add_orders_index", "0008_split_name"], "current_version": "0006", "dry_run": true }`
— the plan says *would apply* 0007–0008; nothing ran.

## Failure modes
- `checksum_mismatch` — an already-applied migration file changed after the fact
  (not retryable; the history is lying — stop and investigate).
- `migration_conflict` — two heads / out-of-order versions (not retryable).
- `partial_failure` — migration N of M failed; applied list shows how far it got; the failed
  migration's own transaction rolled back (not retryable automatically).
- `connection_not_found` (not retryable).

## Constraints
Every `up` should have a written `down`; a migration without a down is flagged in the dry-run
plan so the gate can see it. Dry-run first is the norm, not the exception — the plan output is
exactly what a human approves at the checkpoint.
