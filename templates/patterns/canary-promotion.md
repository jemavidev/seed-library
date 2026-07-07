# Pattern — canary-promotion (eval-gated upgrade)

## When to use
Whenever a creation (skill, agent profile, hook, prompt) has a new version that claims to be
better: the claim is tested against the same eval set the incumbent runs, compared
case-by-case, and promoted only through a gate. This is the system's self-evolution loop
expressed as a procedure a human can audit.

## When not to use
- Brand-new creations with no incumbent → the validation gate covers first admission; canary
  compares *versions*.
- Emergency fixes for a broken incumbent → fix forward under normal review; a canary against
  a broken baseline proves nothing.

## Mechanics that matter
- **Same evals, both versions, no shortcuts**: the candidate runs at least every case the
  incumbent runs (plus any new ones). "It passed *its* tests" is the classic self-evaluation
  trap this pattern exists to close.
- **Regressions dominate the comparison**: one case the candidate fails that the incumbent
  passed outweighs several new wins — users depend on what already worked. The comparator
  leads with regressions, and a regression-free candidate is the normal bar for promotion.
- **Promotion is gated, never automatic**: the gate sees win/loss/regression counts and the
  per-case diffs. Timeout rejects — an unreviewed promotion never slides through.
- **Rollback stays warm**: the prior version is retained (lineage intact) until the promoted
  one proves itself in real use; reverting is a lineage pointer move, not a rebuild.
- **Meta-account budget**: evolving the system is meta-work; it never silently drains a
  user task's budget.

## Failure modes
- **Eval overfitting**: candidates tuned to the eval set. Mitigate by growing evals from
  real outcome history (the eval net) faster than candidates iterate, and by curator
  spot-checks on fresh cases.
- **Stale incumbent baseline**: if the incumbent's evals were never re-run recently, its
  pass rate may be fiction. The eval_runner re-runs both — never trusts recorded results.

## Source attribution
Canary/shadow deployment practice applied to promptware; regression-dominance from
release-engineering norms; two-sided critique kinship with the library's promotion gate
(hand-seeded 2026-07-07).
