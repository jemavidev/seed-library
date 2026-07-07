---
name: metrics-collector
description: Pull one aggregated metric value (avg/min/max/sum/count/p95) over a window from a configured source. Read-only.
---

Use this skill to ground claims about system behavior in numbers.

- Always report `value` together with `samples`; a p95 over 12 samples is an anecdote.
- For before/after comparisons, keep window and aggregation identical on both sides.
- Prefer percentiles over averages for latency; prefer counts over rates when windows are
  short.
- One metric per call; assemble dashboards in your report, not in one mega-query.
