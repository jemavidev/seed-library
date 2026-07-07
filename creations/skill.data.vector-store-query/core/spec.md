# skill.data.vector-store-query — spec

## What it does
Semantic similarity search over a named vector collection: embeds the query text and returns
the top-scoring stored chunks with their metadata. Read-only. The store and embedding model
are bindings; the interface never names them.

## When to use / when not
- **Use** as the retrieval step of a RAG flow (see context pack `rag-injection`) or to find
  "content like this" across an indexed corpus.
- **Don't use** for exact matches (`db-query` / `file-search` are cheaper and precise) or as
  a source of truth — retrieved chunks are candidates to read, not facts to repeat.

## Inputs / outputs
- In: `collection`, `query_text`, `top_k`, `min_score` (drop weaker hits), `filters`
  (metadata equality constraints, e.g. `{"lang": "en"}`).
- Out: `{ hits: [{ id, score, content, metadata }] }` — ordered by score descending.

## Worked example
`{ "collection": "runbooks", "query_text": "how to rotate the signing key", "top_k": 5,
"min_score": 0.35, "filters": null }` →
`{ "hits": [{ "id": "rb-114#3", "score": 0.82, "content": "Rotate the key by…",
"metadata": { "doc": "rb-114", "section": 3 } }, …] }`.

## Failure modes
- `collection_not_found` (not retryable)
- `embedding_failed` (retryable — transient model/provider issue)
- `store_unreachable` (retryable with backoff)
- `invalid_filter` — filter references an unindexed metadata key (not retryable).

Zero hits above `min_score` is a successful empty result: broaden the query or lower the
threshold deliberately.

## Constraints
Scores are comparable only within one collection+model pairing; never compare scores across
collections. Hit content is quoted material — carry `id` through to any citation.
