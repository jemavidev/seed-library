# Lesson — the five skill failure modes (a curator's checklist)

**Statement.** A misbehaving or low-value skill almost always exhibits one of five named
failure modes. Naming them turns "this skill feels off" into a diagnosis:

1. **Premature completion** — the skill declares done before its job is finished (stops at the
   first plausible answer, skips verification). Cure: make the finish line an observable check,
   not a vibe.
2. **Duplication** — the same instruction lives in two places, so they drift. Cure: single
   source of truth; one asset owns each fact, others link ([[single-source-of-truth-schemas]]).
3. **Sediment** — restatements and hedges that accumulated over edits and no longer earn their
   place. Cure: the no-op test — delete a sentence; if nothing changes, it was sediment.
4. **Sprawl** — the skill grew to cover cases it shouldn't, blurring its defining constraint.
   Cure: split by the boundary where each part is independently understandable, or cut scope.
5. **No-op** — a step or clause that changes nothing about what the agent does. Cure: remove it;
   if it mattered, its absence will show in an eval.

**Evidence (source).** The failure-mode vocabulary of `writing-great-skills` in
`mattpocock/skills` (MIT). Complements the pruning discipline SeeD already applies and gives
[[seed-library-seeding|the knowledge-curator]] a concrete rubric beyond "looks fine".

**How to apply.**
- The curator runs this checklist per asset during staleness/quality sweeps; a finding cites
  the failure mode by name plus the offending lines.
- Authoring a new skill: read it back against the five before shipping — most first drafts
  carry sediment and at least one no-op.
- Promotion gate: a candidate exhibiting sprawl or duplication against an existing asset is a
  merge proposal, not a new entry.

**Valid at.** 2026-07-07.
