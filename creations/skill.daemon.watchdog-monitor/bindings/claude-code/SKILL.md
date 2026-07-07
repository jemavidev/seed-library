---
name: watchdog-monitor
description: Register condition watches (metric/log/health/file) that emit trigger events with evidence; watch and act are separate by design.
---

Use this skill to give the system reflexes — watches that signal, flows that act.

- Write conditions with duration ("for 5m") where the source is noisy; instantaneous
  thresholds on jittery metrics are storm generators.
- `cooldown_seconds` sized to the response flow: firing again before the triage flow
  finished helps nobody.
- The watch's `trigger_ref` flow receives the evidence — design it to start from that, not
  to re-derive the world.
- `list` your watches periodically in long-running projects; stale watches firing into
  retired flows are silent budget leaks.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.daemon.watchdog-monitor@v1
