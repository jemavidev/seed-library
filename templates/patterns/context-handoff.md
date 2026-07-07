# Pattern — context-handoff (proactive succession)

## When to use
Long-running work on a bounded context window: when usage crosses the working band's ceiling,
hand off to a fresh instance *by design* instead of degrading toward the hard limit. The
trigger typically comes from `hook.context-zone-guard`; the packet shape comes from the
profile's `handoff_contract` (context pack `default-agent-context`).

## When not to use
- Short tasks that fit comfortably in one window — the packet overhead buys nothing.
- Mid-atomic-step: never hand off with a write half-applied or a transaction open; finish
  the step, then yield.

## Mechanics that matter
- **Proactive beats reactive**: the handoff fires while the incumbent still has room to
  write a good packet. An agent at 98% capacity writes packets that lose the task.
- **The packet is the whole interface**: the successor gets the original `task_brief` plus
  the packet — never the transcript. If continuing requires re-reading the predecessor's
  conversation, the packet failed the check.
- **Decisions travel with their why**: `decisions_made` entries carry rationale, so the
  successor doesn't relitigate settled questions (the packet-check enforces presence, the
  profile's honesty enforces quality).
- **Generation cap**: a task surviving 3+ successions without finishing is not too big for
  one window — it is under-decomposed or stuck; escalate it (charged to the meta account,
  which is why `budget.account` is `meta`).

## Failure modes
- **Summary rot**: each succession compresses a little more until the objective blurs. The
  fix is structural: `task_brief` is carried verbatim, only *progress* is summarized.
- **Orphaned artifacts**: files or refs the packet forgot to mention. The `artifacts` field
  is required and the packet-check rejects empty ones when writes occurred.

## Source attribution
Working-band + proactive-succession semantics from bounded-context operations practice;
memory-block budgeting kinship with `memory-taxonomy` (hand-seeded 2026-07-07).
