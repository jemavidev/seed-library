# skill.devops.service-health-probe — spec

## What it does
Probes a configured endpoint once — HTTP status check, TCP connect, or ICMP-style
reachability — and returns health with latency, judged against optional thresholds.
Effect-free; the verification step every mutating devops skill calls after acting.

## When to use / when not
- **Use** after deploys, config applies, restarts, and scaling — "the operation succeeded"
  means nothing until the probe agrees; also as the `source: health` feeding
  `watchdog-monitor`.
- **Don't use** for continuous monitoring loops (register a watchdog instead) or for load
  testing (one probe per call, on purpose).

## Inputs / outputs
- In: `endpoint_ref` (configured endpoint name), `protocol` (`http|tcp|ping`),
  `expected_status` (http only), `timeout_seconds`, `thresholds`
  (`{ latency_warn_ms, latency_fail_ms }`).
- Out: `{ healthy, latency_ms, status_code, details }` — `healthy` combines reachability,
  expected status, and the fail threshold.

## Worked example
`{ "endpoint_ref": "api-staging", "protocol": "http", "expected_status": 200,
"timeout_seconds": 5, "thresholds": { "latency_warn_ms": 300, "latency_fail_ms": 2000 } }` →
`{ "healthy": true, "latency_ms": 187, "status_code": 200, "details": "ok" }`.

## Failure modes
- `endpoint_not_configured` (not retryable) · `invalid_threshold` (not retryable).

**Unhealthy is a successful result** (`healthy: false` with the reason in `details`), never a
tool failure — probes exist to report bad news calmly.

## Constraints
One probe per call; convergence checks are the caller's loop with its own budget (e.g. probe
up to N times over M seconds after a deploy, then conclude). Latency is measured to first
meaningful response, documented per protocol in the binding.
