# Lesson — every cyclic pattern declares termination

**Statement.** Any orchestration pattern containing a cycle (reflection loops, retry loops,
debate rounds) must declare both `max_iterations` and an explicit termination condition, or it
must be rejected at load time.

**Evidence (source).** Multi-agent frameworks converged on declarative termination
(e.g. text-mention OR max-messages conditions) after unbounded conversation loops proved to be
the dominant cost-bleed failure mode. A loop without declared termination spends budget until an
external kill.

**How to apply.** Pattern templates carry a `termination` field and `budget.max_iterations`;
loaders refuse cyclic graphs where either is absent. Evaluator/optimizer loops end on
`verdict == pass` OR attempts exhausted — and exhaustion must produce a typed partial result,
not a silent success.

**Valid at.** 2026-07-07.
