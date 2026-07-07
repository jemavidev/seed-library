# Pattern — long-horizon-run (checkpointed autonomous run)

## When to use
Objectives that outlive any single session: multi-day builds, large audits, continuous
curation — the daemon's native execution shape. The run must survive restarts, model
switches, and context successions without losing the plot.

## When not to use
- Work that fits one session → plain execution; checkpointing overhead buys nothing.
- Work needing human judgment at every step → this pattern is for *bounded autonomy*; if
  every episode gates, it is a conversation, not a run.

## Mechanics that matter
- **Episodes are bounded**: each does a coherent unit of work and *must* reach the
  checkpointer — an episode that can't finish inside its bound is decomposed, not extended.
- **The checkpoint is the resume contract**: `progress_summary`, `artifacts`,
  `decisions_made` (with why), `next_intent`. Resume reads the checkpoint, never the dead
  episode's transcript — same discipline as `context-handoff`'s packet, applied to time
  instead of context.
- **Heartbeats make silence detectable**: an external watcher (`watchdog-monitor` on
  `last_heartbeat`) distinguishes "working" from "hung" — without it, a dead daemon looks
  identical to a slow one.
- **Stall detection beats optimism**: three episodes without measurable progress means the
  objective, as briefed, is stuck — escalate with the checkpoint, don't burn the remaining
  budget proving it.
- Composes with: `context-handoff` (succession inside an episode), `saga-compensation`
  (external effects inside an episode), `hook.budget-threshold-alert` (spend guard).

## Failure modes
- **Checkpoint theater**: summaries that say "made progress" without artifacts. The
  checkpointer rejects checkpoints whose `artifacts`/`next_intent` are empty when work
  supposedly happened.
- **Objective drift**: each episode re-interprets the goal slightly. The objective travels
  verbatim; episodes may refine *tactics*, never the objective — scope changes escalate.

## Source attribution
Durable-execution semantics (checkpoint/resume/heartbeat) from workflow-engine practice;
stall-escalation from autonomous-agent operations (hand-seeded 2026-07-07).
