# hook.hitl-notifier — spec

## What it is
An on-interrupt hook: when a workflow gate fires (see pattern `hitl-checkpoint` /
`planner-executor`), this hook formats the pending action into a human-readable approval
request, delivers it over the configured channel, collects the verdict, and hands it back to
the gate. It is transport, not judgment.

## Trigger semantics (harness-neutral)
- **Trigger:** `on-interrupt` — a gate has frozen state and awaits a verdict.
- **Input:** the gate's `pending_action` (what, where, blast radius, undo story), the stance
  in force, the timeout and its on-timeout behavior.
- **Effect:** one approval-request message out (via the configured dispatcher); one verdict
  in (`approved | rejected | amended` + notes); delivered to the gate. Timeout expiry is
  reported to the gate as timeout — the hook never fabricates a verdict.

## Behavior rules
1. **The request is decision-ready:** what will happen, to what, the worst case, the undo
   story, and the deadline — in that order, short enough to read on a phone.
2. **One request per gate event.** Reminders (at most one, at half-timeout) thread onto the
   original; they never open a new request.
3. **Verdicts authenticate.** Only the configured approver identities count; a reply from
   anyone else is logged and ignored.
4. **Every exchange is recorded** — request, reminder, verdict, verdict notes — attached to
   the gate event for audit.

## When to attach
Any workflow whose patterns declare interrupts; the daemon/remote setting is where it earns
its keep (approvals from a phone via the messaging bridge).
