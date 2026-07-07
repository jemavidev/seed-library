---
name: scheduler-operator
description: Create/pause/resume/cancel scheduled jobs pointing at registered flows; policy binds at fire time, never at schedule time.
---

Use this skill to make work recur — with the discipline that scheduled ≠ pre-approved.

- Schedule only registered `task_ref` flows; if the flow doesn't exist yet, build and
  register it first.
- Prefer a `window` for anything experimental — jobs that end themselves beat jobs someone
  must remember to cancel.
- `list` before `create`; duplicate schedules double-run work and double-spend budget.
- Say in your report what you scheduled, when it first fires, and how to cancel it.
- Never use scheduling to dodge an approval: the gate meets the job at fire time anyway.
