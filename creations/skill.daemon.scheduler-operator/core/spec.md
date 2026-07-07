# skill.daemon.scheduler-operator — spec

## What it does
Manages scheduled jobs in the runtime's scheduler: create (cron expression or interval),
list, pause, resume, cancel. A job names a **configured task/flow** to run — the scheduler
never executes arbitrary payloads. Local effect: scheduling state only.

## When to use / when not
- **Use** for recurring work (nightly audits, weekly reports) and delayed one-shots
  ("run the cleanup Saturday 03:00").
- **Don't use** for condition-based reactions ("when X happens" is `watchdog-monitor`) or
  for immediate execution (just run the flow).

## Inputs / outputs
- In: `action` (`create|list|pause|resume|cancel`), `job_ref`, `schedule` (cron or
  `every:<interval>` or `once:<ISO timestamp>`), `task_ref` (configured flow/task id),
  `window` (optional `{ start, end }` validity bounds).
- Out: `{ action, job_ref, next_run, active }`.

## Worked example
`{ "action": "create", "job_ref": "nightly-audit", "schedule": "0 3 * * *",
"task_ref": "flow.project-audit", "window": null }` →
`{ "action": "create", "job_ref": "nightly-audit", "next_run": "2026-07-08T03:00:00Z",
"active": true }`.

## Failure modes
- `invalid_schedule` (not retryable; message shows the accepted forms)
- `task_ref_unknown` — the job must point at a registered flow (not retryable)
- `job_not_found` (not retryable) · `duplicate_job_ref` (not retryable; update = cancel+create).

## Constraints
**Policy binds at fire time, not at schedule time**: a job fires under whatever approval
policy and budget are in force when it runs — scheduling something is never a way to
pre-approve it. Every fired run is an ordinary task: audited, budgeted, gate-able. Jobs
without a `window` end only by explicit cancel; report created jobs so they are never
orphaned intent.
