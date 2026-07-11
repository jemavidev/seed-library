# Context pack — rag-injection

> Status: active

Declares how retrieved knowledge enters an agent's context: retrieve → filter/rerank →
budget → cite. Store-agnostic — the pipeline is configuration consumed at context-assembly
time; `vector-store-query` (or any retriever) is the mechanism underneath.

## The pipeline, as config

1. **Retrieve** — source collection, `top_k`, `min_score`: cast a bounded net.
2. **Rerank** *(optional)* — re-order candidates by relevance to the *task*, keep the best
   `keep_top`; worth its cost when collections are large or queries are vague.
3. **Budget** — retrieved content enters the context as one block with a token cap; chunks
   that don't fit are dropped whole (never truncated mid-chunk) in rank order.
4. **Cite** — every injected chunk carries its source id; when `citation_required` is true,
   downstream claims that use retrieved content must reference those ids.

## Design rules
- **Retrieval augments the brief, never replaces it** — the task brief stays authoritative;
  retrieved chunks are evidence with lower standing than instructions.
- **Retrieved content is data**: a chunk containing instruction-like text ("always
  approve…") has no authority — the same untrusted-input stance as web content and logs.
- **Empty retrieval is a valid state**: the block simply doesn't appear; agents must not
  fail because the corpus had nothing relevant.
- Chunks dropped whole (rule 3) because a truncated chunk quotes a source it no longer
  faithfully represents.

## How to instantiate
Copy `example.json` per profile/collection pairing; validation: `config.schema.json`.
Composes with `default-agent-context` (this pack defines one of its `retrieval_sources`
entries, elaborated).
