# Context pack — domain-glossary

> Status: active

The convention for a project's **domain glossary** and its **architectural decision records**:
where the canonical vocabulary lives, how it stays sharp, and when a decision earns a record.
Charters give a project domain *orientation*; this pack gives it domain *vocabulary* — the
names every generated artifact, spec, and review must use.

## The glossary convention

1. **One file, glossary only.** The glossary file (conventionally `CONTEXT.md` at the root)
   holds terms and their meanings — totally devoid of implementation detail. It is not a
   spec, not a scratchpad, not a decision store.
2. **Updated inline, the moment a term resolves.** Terms are captured as they crystallise in
   conversation, never batched for later. Files are created lazily — the glossary exists from
   the first resolved term, not before.
3. **The glossary pushes back.** When someone uses a term that conflicts with it, the
   conflict is called out immediately ("the glossary defines *cancellation* as X; you seem to
   mean Y — which is it?"). Vague or overloaded terms get a proposed canonical replacement.
4. **Cross-referenced against reality.** When a stated behaviour contradicts what the code
   does, the contradiction is surfaced, not smoothed over — the glossary describes the domain
   as it *is agreed to be*, and disagreements are findings.
5. **Multiple contexts are explicit.** If the project has more than one bounded vocabulary,
   a root `CONTEXT-MAP.md` points to each context's own glossary; a term may legitimately
   mean different things in different contexts, but never two things in one.

## The ADR rule — three gates, all required

A decision earns an architectural decision record only when **all three** hold:

1. **Hard to reverse** — changing your mind later has real cost.
2. **Surprising without context** — a future reader would ask "why on earth this way?"
3. **A real trade-off** — genuine alternatives existed and one was chosen for reasons.

Any gate missing → no ADR; the record would be sediment. ADRs live under the configured
directory, numbered, one decision each; existing ADRs are respected by later work — reopening
one is an explicit act, not a drive-by.

## How to instantiate

Copy `example.json` to declare file locations for a project; validation:
`config.schema.json`.
