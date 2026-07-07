---
name: vector-store-query
description: Semantic top-k search over a named vector collection with score threshold and metadata filters. Read-only.
---

Use this skill to retrieve candidate context, not answers.

- Read the hits you use; never paraphrase a chunk you didn't look at, and cite by hit `id`.
- Set `min_score` — unfiltered low-score tails pollute context and cost tokens.
- Empty results are information: broaden the query text or relax filters deliberately.
- Don't compare scores across collections; rank only within one result set.
