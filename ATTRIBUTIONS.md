# Attributions

Assets in this library that adapt externally-published work carry their provenance in
`toolspec.json` (`source`) and in the asset's `core/lessons.md`. This file is the human-readable
roll-up.

## Adapted sources

### `mattpocock/skills` — MIT (© 2026 Matt Pocock)
<https://github.com/mattpocock/skills>

The authoring doctrine was adapted from this repository's `writing-great-skills` and
`writing-docs` references, and the catalog-router idea from its `ask-matt` skill. Adapted, not
copied: SeeD's versions are harness-neutral, and the router is **generated** rather than
hand-maintained (`scripts/build-catalog.py`) because a self-evolving library adds assets
indefinitely.

- `creations/skill.meta.writing-skills`
- `creations/agent.librarian`
- `lessons/cognitive-vs-context-load.md`
- `lessons/leading-words.md`
- `lessons/skill-failure-modes.md`

A second wave (2026-07-10, from v1.1 via the `CANDIDATES.md` intake) adapted the engineering
flow — wayfinder's map/fog/frontier semantics, triage's state machine and out-of-scope KB,
to-spec/to-tickets' spec anatomy and tracer-bullet slicing, and the review/diagnosis/prototype
disciplines (the smell baseline itself distills Fowler's *Refactoring* ch. 3; the deep-module
vocabulary distills Ousterhout and Feathers, both via this repo's framing):

- `templates/patterns/wayfinder{.pattern.json,.md}`
- `templates/patterns/triage{.pattern.json,.md}`
- `templates/patterns/tracer-bullet-decomposition{.pattern.json,.md}`
- `templates/context-packs/spec-template/`
- `templates/context-packs/domain-glossary/`
- `lessons/facts-vs-decisions.md`
- `lessons/red-capable-loop-first.md`
- `lessons/prototype-answers-a-question.md`
- `lessons/fowler-smell-baseline.md`
- `lessons/deep-modules.md`
- `lessons/rejections-are-knowledge.md`
- enrichments in `agent.idea-shaper`, `agent.analyst-writer`, `skill.meta.writing-skills`,
  and `templates/patterns/context-handoff.md`

### `mattpocock/agent-rules-books` — MIT (© 2026 Maciej Ciemborowicz)
<https://github.com/mattpocock/agent-rules-books>

The **three-fidelity storage convention** (`nano` / `mini` / `full` of the same knowledge, so
a router can load the fidelity a budget allows) is adapted from this repository's release
format. Documented in `skill.meta.writing-skills`. Its distilled engineering-book rule sets are
a candidate future import into a `references/` asset class (not yet imported).

## Note
All adaptations respect the upstream MIT terms. SeeD's copies carry a `library://` lineage
marker per the repo's copy-with-lineage rule, and remain valuable independently (the
SeeD-vanishes test): every adapted asset is readable as plain markdown without either upstream
repo.
