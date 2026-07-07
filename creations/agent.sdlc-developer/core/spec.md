# agent.sdlc-developer — spec

## What it is
The building profile for software work: reads, edits, tests, and commits code inside the
project sandbox, with verification as part of the definition of done. Generator role in
`evaluator-optimizer`; stage worker in `prompt-chaining`.

## When to use / when not
- **Use** for implementing features, fixes, refactors, and config changes from a brief.
- **Don't use** for pure review (qa-reviewer is read-only and cheaper to trust) or for
  routing/decomposition decisions (supervisor).

## Inputs / outputs
- In: a self-contained brief (goal, constraints, expected result form).
- Out: applied changes + a verification report (analyzer delta, test results, commits made,
  leftovers declared).

## Authorized skill families (bound in policy)
Read/search/edit/test/analyze/dependency/git from the `sdlc` domain, plus `core-utils`
file-search and data-transformer as support. Push and any external effect ride the approval
flow of the active policy.

## Evaluation notes
Evals check method (read-before-write, verify-after-change) and honesty of the final report,
not merely whether code compiles.
