# skill.data.metrics-collector — spec

## What it does
Fetches an aggregated value for a named metric from a configured metrics source over a time
window (avg/min/max/sum/count/p95). Read-only. The metrics backend is a binding.

## When to use / when not
- **Use** to answer "how is X behaving" questions with numbers: latency, error rate, queue
  depth, spend — before and after a change.
- **Don't use** for log-line evidence (`log-reader`) or continuous alerting (that is a
  watchdog/trigger concern, not a pull).

## Inputs / outputs
- In: `source`, `metric`, `window` (relative, e.g. `"5m"`, `"24h"`), `aggregation`
  (`avg|min|max|sum|count|p95`).
- Out: `{ metric, window, aggregation, value, samples }` — `samples` is the datapoint count
  behind the aggregate; treat low-sample aggregates with suspicion.

## Worked example
`{ "source": "app-metrics", "metric": "http.request.latency_ms", "window": "1h",
"aggregation": "p95" }` → `{ "metric": "http.request.latency_ms", "window": "1h",
"aggregation": "p95", "value": 287.4, "samples": 11842 }`.

## Failure modes
- `source_not_found` (not retryable) · `metric_not_found` (not retryable)
- `window_invalid` (not retryable) · `source_unreachable` (retryable).

## Constraints
A value without its `samples` count is not reportable — the implementation must always return
both. Comparisons (before/after) must use the same window and aggregation; the skill does not
prevent apples-to-oranges, the caller's method must.
