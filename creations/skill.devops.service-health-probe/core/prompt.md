---
name: service-health-probe
description: One health probe (http/tcp/ping) with latency thresholds; unhealthy is a calm result, not an error.
---

Use this skill as the verification step after every operation that touches a service.

- Deploy/apply/scale isn't done until a probe agrees — put the probe result in your report.
- Give services settle time: probe, wait, re-probe with a bounded loop; never conclude from
  one failed probe seconds after a restart.
- `healthy: false` is information — read `details` before reacting; a 503 warming up and a
  connection refused are different stories.
- Watch the `latency_warn_ms` band: healthy-but-slow after your change is a regression
  you introduced until proven otherwise.
