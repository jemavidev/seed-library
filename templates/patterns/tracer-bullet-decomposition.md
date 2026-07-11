# Pattern — tracer-bullet-decomposition (vertical-slice tickets)

## When to use
An accepted spec or plan is too big for one session and must be spread across many — split it
into **tracer bullets**: slices that each cut a narrow but *complete* path through every layer
(schema, logic, surface, tests), so every finished ticket is demoable or verifiable on its
own. Sessions then work the **frontier** — any ticket whose blockers are all closed — one
ticket per fresh context window.

## When not to use
- The *whether* is still open → `triage`; the *way* is still foggy → `wayfinder`. This
  pattern starts after both: destination known, decisions made.
- Work that fits one session → just do it; tickets would be ceremony.

## Mechanics that matter
- **Vertical, never horizontal.** A slice of one layer ("all the schemas, then all the
  endpoints") verifies imagined behaviour and goes stale by the third ticket. Each tracer
  bullet lands end-to-end, teaching the next slice what the last one learned.
- **Sized to one fresh window.** The unit of sizing is an agent session, not a day of work.
  Prefactoring ("make the change easy, then make the easy change") goes first, as its own
  slice.
- **Edges are declared, not implied.** Every ticket names what blocks it; a ticket with no
  blockers can start immediately. Publish blockers first so edges reference real identifiers.
- **Wide refactors are the exception.** One mechanical change whose blast radius fans across
  the codebase (rename a column, retype a shared symbol) cannot land green as a slice.
  Sequence it **expand–contract**: expand (new form beside the old, nothing breaks) →
  migrate call sites in batches sized by blast radius, each batch a ticket blocked by the
  expand → contract (delete the old form) blocked by every batch.
- **No stale anchors.** Tickets avoid file paths and code snippets — they rot. The one
  exception: a prototype-validated snippet that encodes a decision more precisely than prose
  (a schema, a reducer, a type shape), trimmed to the decision-rich part.

## Failure modes
- **Granularity unreviewed** — the human sees the slice list *before* publication (the gate);
  wrong granularity discovered after twenty tickets exist costs twenty edits.
- **Hidden coupling** — two "independent" tickets editing the same seam; the tell is a
  frontier that serializes anyway. Fix the edges, not the schedule.
- **Parent mutation** — decomposition publishes children; it never closes or edits the spec
  it decomposes.

## Source attribution
Adapted from `mattpocock/skills` v1.1 `to-tickets` (MIT) — tracer-bullet slicing, blocking
edges, expand–contract for wide refactors; recast as a declarative graph with a granularity
gate (hand-seeded 2026-07-10).
