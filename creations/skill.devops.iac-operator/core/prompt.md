---
name: iac-operator
description: Two-phase infrastructure-as-code: plan saves an immutable change set; apply executes only a saved plan_ref; destroy counts gate review.
---

Use this skill for declarative infrastructure changes, always in two phases.

- `plan` first, always. Read the change counts — a plan with unexpected `destroy > 0` is a
  finding to raise, not a detail to approve past.
- `apply` takes the `plan_ref` you reviewed; if the world drifted (`plan_stale`), re-plan
  and re-review — never force the old intent onto a changed world.
- On `partial_apply`, report exactly which resources changed and stop; reconciliation starts
  from a fresh plan, not from optimism.
- `state_locked` means someone else is operating: back off, don't break locks.
