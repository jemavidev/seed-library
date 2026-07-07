# skill.daemon.watchdog-monitor — spec

## What it does
Manages condition watches: register a watch that observes a source (metric, log pattern,
health probe, file change) and **emits a trigger event** when its condition holds; remove or
list watches. The watchdog observes and signals — it never acts. Acting belongs to the flow
the trigger event starts, under normal policy.

## When to use / when not
- **Use** for "when X happens, start Y": error-rate spikes, disk filling, a service going
  unhealthy, a drop-folder receiving a file.
- **Don't use** for time-based work (`scheduler-operator`) or as the action itself — a watch
  that "fixes things" is two responsibilities in one and is rejected by design.

## Inputs / outputs
- In: `action` (`register|remove|list`), `watch_ref`, `source` (`{ kind:
  metric|log|health|file, … kind-specific fields }`), `condition` (threshold/pattern over
  the source, e.g. `"value > 0.05 for 5m"`), `trigger_ref` (registered flow the event
  starts), `cooldown_seconds` (minimum gap between firings).
- Out: `{ action, watch_ref, active }`.

## Worked example
`{ "action": "register", "watch_ref": "error-spike", "source": { "kind": "metric",
"source_ref": "app-metrics", "metric": "http.request.errors", "window": "5m",
"aggregation": "sum" }, "condition": "value > 50", "trigger_ref": "flow.incident-triage",
"cooldown_seconds": 900 }` → `{ "action": "register", "watch_ref": "error-spike",
"active": true }`.

## Failure modes
- `invalid_condition` (not retryable; message shows the condition grammar)
- `source_unknown` / `trigger_ref_unknown` (not retryable)
- `watch_not_found` (not retryable) · `duplicate_watch_ref` (not retryable).

## Constraints
`cooldown_seconds` is mandatory — a flapping condition without cooldown is an alert storm
that drowns the audit log and burns budget. Trigger events carry the observed evidence
(value, matched line, probe result) so the started flow begins with facts, not a re-check.
The started flow runs under fire-time policy, exactly like scheduled jobs.
