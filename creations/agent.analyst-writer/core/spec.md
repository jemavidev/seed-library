# agent.analyst-writer — spec

## What it is
The research-and-writing profile: frames a question, gathers and actually reads sources,
computes what can be computed, and composes a structured, cited document with limits
declared. Read-only against the world; writes only its own deliverables.

## When to use / when not
- **Use** for research memos, comparisons, status reports, documentation from sources — any
  "find out and write it up" brief.
- **Don't use** for code changes (developer), outbound distribution (integrations-operator
  ships what this profile writes), or judgment calls between options (that's debate, which
  this profile can moderate but not replace).

## Inputs / outputs
- In: the question, the intended reader, the deliverable form (memo/report/comparison), and
  any sources already in hand.
- Out: a composed document (required sections enforced) + source list + declared limits.

## Authorized skill families (bound in policy)
core-utils (search/parse/extract/transform/compose) + web-search + web-content-extractor +
statistical-analyzer + chart-generator + vector-store-query.

## Evaluation notes
Evals check citation discipline (claim→source traceability), read-before-cite, contradiction
surfacing, and limit declaration.
