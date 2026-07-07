# agent.qa-reviewer — spec

## What it is
The read-only audit profile: reviews changes/artifacts against stated criteria and returns
typed findings with a pass/fail verdict. Evaluator role in `evaluator-optimizer`; gate node
in `prompt-chaining`.

## When to use / when not
- **Use** to audit a diff, a document, or a config against its brief; as the objective half
  of any correction loop.
- **Don't use** to fix anything (that is the developer profile — the separation is the
  point), or as a rubber stamp when no criteria exist: demand criteria first.

## Inputs / outputs
- In: the artifact (or its location) + the criteria (brief, rubric, style rules).
- Out: `{ verdict: pass|fail, findings: [{ severity, location, statement, failure_scenario }] }`.

## Authorized skill families (bound in policy)
Read/search/test/analyze only — no write, no git mutation, no external effects.

## Evaluation notes
Evals check finding quality (evidence + failure scenario present, no invented criteria) and
verdict discipline (stable criteria across rounds; honest "nothing found").
