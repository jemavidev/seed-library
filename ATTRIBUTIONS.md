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
