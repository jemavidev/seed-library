# hook.budget-threshold-alert — spec

## What it is
A spend-watermark hook: watches cumulative spend per account (task and meta, fed by the
spans `hook.span-metadata-recorder` writes) against each account's budget, and responds in
graduated steps — notify at the warning mark, gate further spending at the hard mark. The
financial twin of `hook.context-zone-guard`.

## Trigger semantics (harness-neutral)
- **Trigger:** `post-tool` — evaluated after every cost-recorded invocation, when the ledger
  is freshest.
- **Input:** the account's cumulative spend + its configured budget and thresholds.
- **Effect:** below warn = nothing; warn crossed = one notification with the burn breakdown
  (top spenders by tool/flow) and projected exhaustion; hard crossed = an interrupt with
  stance `confirm` — continuing to spend on this account requires an explicit human yes.

## Behavior rules
1. **Graduated and hysteretic:** warn fires once per crossing (re-arms only after spend
   authority is raised or the run ends); no per-call nagging.
2. **The hard gate stops *new* spend, not work in flight:** the current invocation
   completes; the next cost-bearing call on the account waits at the gate. Pure/free
   operations continue — analysis is never starved by a spend gate.
3. **Notifications carry the breakdown**, not just the number: which tools/flows spent what,
   and the projection at current burn rate — a decision-ready alert (delivered via
   `hook.hitl-notifier`'s channel).
4. **Per-account isolation:** task overruns never gate meta work and vice versa — evolving
   the system and doing the user's work fail independently.

## Configuration
`{ account, budget, warn_percent (default 70), hard_percent (default 90) }` per account;
long-horizon runs should set absolute values too — percent-only thresholds drift as budgets
get raised.

## When to attach
Globally wherever cost is recorded; mandatory for daemon/long-horizon runs, where nobody is
watching the meter.
