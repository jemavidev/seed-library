# Context pack — memory-taxonomy

> Status: active

Declares the five kinds of memory an agent system runs on, each as configuration: what it
holds, its budget, where it lives (a binding), and how content enters and leaves. The point
is that "memory" is never one undifferentiated blob — each kind has different guarantees, and
mixing them is how systems forget the wrong things.

## The five memory types

1. **Working** — the current turn's context: blocks assembled per `default-agent-context`.
   Budgeted per block; evicted by the context-zone policy. Guarantee: none beyond the turn.
2. **Session** — state that survives turns within one task: pattern state, checkpoints,
   handoff packets. Backed by the runtime's state store; dies with the task unless promoted.
3. **Semantic** — durable facts and preferences distilled *about* the user/projects: entered
   only by explicit distillation (see `hook.lesson-harvester`, wave 3), each fact carrying
   temporal validity (`valid_at`/`invalid_at` — supersede, never delete).
4. **Episodic** — the record of what happened: access events, task outcomes, decisions with
   their why. Append-only; the raw material distillation draws from.
5. **Knowledge base** — indexed reference corpora queried on demand (`vector-store-query`
   via the `rag-injection` pack). Read-mostly; refreshed by ingestion, not by conversation.

## Design rules
- **Flow is one-way with gates:** episodic → (distillation) → semantic → (packing) →
  working. Nothing writes directly into semantic memory mid-conversation.
- **Budgets are per-type and per-block** so overflow is a decision, not an accident.
- **Backends are bindings:** the config names types and guarantees; whether session state is
  a file or a cache server is instantiation detail.

## How to instantiate
Copy `example.json`, wire the `backend_ref`s to the runtime's stores, tune budgets;
validation: `config.schema.json`.
