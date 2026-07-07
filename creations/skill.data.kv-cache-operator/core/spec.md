# skill.data.kv-cache-operator — spec

## What it does
Get/set/delete operations against a namespaced key-value cache with per-key TTL. State is
local to the runtime's cache service (a binding: in-memory, file-backed, or a cache server)
and explicitly *ephemeral* — the cache may vanish at any time.

## When to use / when not
- **Use** for expensive-to-recompute intermediates, rate-limit counters, session-scoped
  state, memoized lookups.
- **Don't use** as a system of record (anything you can't afford to lose belongs in a
  database or file) or as a communication channel between agents (that's pattern state).

## Inputs / outputs
- In: `action` (`get|set|delete`), `key`, `namespace`, `value` (string; serialize richer data
  yourself — required for `set`), `ttl_seconds` (required for `set`; null = binding default).
- Out: `{ action, key, value, hit }` — `get` miss returns `hit: false` with null value
  (a miss is a normal outcome, not a failure).

## Worked example
`{ "action": "set", "key": "openapi-spec:acme", "namespace": "task-42", "value": "{…}",
"ttl_seconds": 3600 }` → `{ "action": "set", "key": "openapi-spec:acme", "value": null,
"hit": false }` — then a later `get` returns the payload with `hit: true`.

## Failure modes
- `store_unreachable` (retryable) · `value_too_large` (not retryable; cache less, or don't)
- `missing_value` — `set` without value/ttl (not retryable).

## Constraints
Namespaces isolate consumers — a key without a namespace is invalid by schema. Never cache
secrets or credentials. Design every consumer to survive a cold cache: the correct reaction
to `hit: false` is recompute, never error.
