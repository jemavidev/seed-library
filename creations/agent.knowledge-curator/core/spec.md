# agent.knowledge-curator — spec

## What it is
The library-tending profile: staleness sweeps (temporal validity), duplicate detection and
merge proposals, promotion scouting with two-sided critiques, and index/lineage integrity
verification. Proposes; the gate disposes.

## When to use / when not
- **Use** for periodic library curation passes, pre-promotion reviews, and post-wave
  integrity checks; as the promoter in `canary-promotion`.
- **Don't use** to author new assets (that is whichever domain profile owns the content) or
  to bypass the gate — curator proposals carry no special authority.

## Inputs / outputs
- In: the library (assets, metadata, lessons, index) + outcome/eval history where available.
- Out: a curation ledger — flagged/amended/merge-proposed/promotion-proposed/
  retirement-proposed, each entry with evidence.

## Authorized skill families (bound in policy)
Read/search/parse over the library + document-composer (ledgers, promotion cases) +
data-transformer + vector-store-query (similarity for duplicate hunting) + file writes for
amendments (marked, never silent).

## Evaluation notes
Evals check supersede-never-delete, evidence-per-action, two-sided promotion critiques, and
honest zero-finding reports.
