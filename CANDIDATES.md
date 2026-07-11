# CANDIDATES — external intake & evaluation queue

> **Status:** living document, created 2026-07-10. This is the standing intake queue for
> ideas harvested from external sources (videos, repos, posts) that may become library
> assets. It lives in this repo — not the SeeD product repo — so intake works from any
> machine or project that clones `jemavidev/seed-library`, and so accepted candidates
> graduate in place. Hand-maintained (like `ATTRIBUTIONS.md`); never generated.
>
> Workflow: the owner drops a source into a session → the agent analyzes it against the
> rubric (§2) → new candidates land in §4 as `proposed` → the owner evaluates → verdicts
> are recorded: accepted → built and moved to the Accepted log (§5); rejected → one line in
> the Rejection log (§6) with the reason, so it is never re-proposed.

---

## 1. The intake loop

1. **Bring a source.** Paste a repo URL, transcript path, or article into a session and say
   "evaluate against CANDIDATES".
2. **Agent analyzes.** Read the source, run each idea through the rubric (§2), and check
   redundancy against what already exists: [CATALOG.md](CATALOG.md) (generated, always
   current), `lessons/`, `templates/`, the Accepted log (§5), and the Rejection log (§6).
   Check *by concept*, not by the source's wording. Append survivors to §4 as `proposed`;
   register the source in §3.
3. **Owner evaluates.** Each candidate is a one-screen read: what it is, what library shape
   it would take, why it fits, what's unresolved, what already overlaps.
4. **Record the verdict.** `accepted` → build the asset per this repo's seeding conventions
   (README §Seeding conventions), run `python3 scripts/build.py`, and compress the entry to
   one line in §5; `rejected` → move a one-line gist + reason to §6 and delete the full
   entry.

Statuses: `proposed` → `evaluating` → `accepted` | `rejected` | `deferred`.

## 2. Evaluation rubric (gates, in order)

Derived from this repo's rules (README §The rules this repo lives by) and the SeeD product
contracts ([portable-assets](https://github.com/jemavidev/SeeD/blob/main/docs/design/portable-assets.md),
[library-seeding-plan](https://github.com/jemavidev/SeeD/blob/main/docs/implementation/library-seeding-plan.md)).
A candidate that fails G1 is dead; the rest are judgement calls to record.

- **G1 — Kernel exclusion.** If the idea drifts toward approval logic, credentials, audit,
  or raw shell, stop: the SeeD Kernel owns it. Never a library asset.
- **G2 — Redundancy.** Does an existing creation, pattern, lesson, or template already
  cover it? Check `CATALOG.md`, `lessons/`, `templates/`, §5, and §6. Partial overlap is
  not rejection — but the candidate must then be narrowed to its genuine delta.
- **G3 — Asset-kind mapping.** A "skill" in the Claude-Code sense (a prompt-shaped
  `SKILL.md`) rarely maps to a library *skill* (JSON Schema + ToolSpec executable). Decide
  the real kind: **skill** (executable tool) · **pattern** (declarative graph) · **lesson**
  (distilled discipline) · **context pack** · **charter** · **hook** · **agent-profile
  enrichment**. Most process/method ideas land as patterns or lessons.
- **G4 — SeeD-vanishes.** Usable as plain markdown / JSON Schema / MCP-shaped tool without
  SeeD? The acceptance test for every asset in this repo.
- **G5 — Two-layer split.** What is harness-neutral `core/`, what is disposable
  `bindings/`? If nothing survives in core, it's glue, not an asset.
- **G6 — Effects class.** `pure | local | external`; external requires `compensate` or
  `dryRunOnly`. Method/process assets are usually `pure`/`local` by construction.
- **G7 — Prior leverage.** Does it recruit knowledge already deep in model priors with a
  few *leading words* (cheap, robust — see `lessons/leading-words.md`), or does it paste a
  manual (expensive, brittle)? Prefer candidates where ten lines buy a whole behaviour.
- **G8 — HITL mapping.** If a human belongs in the loop, which kernel stance materializes
  it (`confirm` / `expert-review`)? A candidate that lets the agent stand in for the
  human's side of a decision fails this gate.

## 3. Source registry

| id | Source | Ingested | Notes |
|---|---|---|---|
| S1 | [mattpocock/skills](https://github.com/mattpocock/skills) v1.1 — `skills/engineering/` + `skills/productivity/` | 2026-07-10 | Plus owner-supplied video transcript. Prompt-shaped SKILL.md files for Claude-Code-like harnesses; an SDLC flow: grilling → wayfinder → to-spec → to-tickets → implement (TDD) → code-review → triage. An earlier pass over this source had already been absorbed (`skill.meta.writing-skills`, `lessons/leading-words.md`, `lessons/progressive-disclosure.md`, `lessons/skill-failure-modes.md`, `lessons/cognitive-vs-context-load.md`, `agent.librarian`, `agent.idea-shaper`) — the 2026-07-10 wave built only the deltas. Verdicts: C-01…C-12 accepted (§5), C-13 rejected (§6), C-14 deferred (§4). |

## 4. Open candidates

#### C-14a · Invocation-surface field in ToolSpec — `deferred`
- **Source:** S1 (repo convention: `disable-model-invocation` frontmatter)
- **Redundancy check:** the *concept* (model-invoked vs user-invoked as context-load vs
  cognitive-load) is already in `lessons/cognitive-vs-context-load.md`; what's missing is
  the **machine-readable** expression so bindings can generate the right frontmatter per
  harness.
- **Remaining delta:** a field in ToolSpec / `_meta.json` — a product **contract change**,
  needs a decision-log ruling before any library work.
- **Status:** deferred 2026-07-10 — blocked on the product-side ruling; revisit when it
  lands. (Part (b) of the original C-14 — lifecycle states — was accepted and built the
  same day; see §5.)

## 5. Accepted log

Accepted 2026-07-10 (owner verdict: "approve what's pertinent, complement what exists,
reject what won't carry value"), all built the same day:

- **C-01 Wayfinder** → `templates/patterns/wayfinder{.pattern.json,.md}` — shared-map
  planning; one charting or one resolution per session, budget-enforced.
- **C-02 Facts-vs-decisions grilling** → `lessons/facts-vs-decisions.md` + constraint added
  to `agent.idea-shaper` (never answer your own question; confirmation gate).
- **C-03 Skill-authoring delta** → `skill.meta.writing-skills` checklist gained completion
  criteria (new step 4) and positive-phrasing pruning (step 5).
- **C-04 Triage** → `templates/patterns/triage{.pattern.json,.md}` +
  `lessons/rejections-are-knowledge.md` (rejection log as first-class gate).
- **C-05 Fowler smell baseline** → `lessons/fowler-smell-baseline.md` (12 smells +
  two-axis review rules; pairs with `agent.qa-reviewer`).
- **C-06 Diagnosis discipline** → `lessons/red-capable-loop-first.md` ("no red-capable
  loop, no hypothesis").
- **C-07 Spec anatomy + decomposition** → `templates/context-packs/spec-template/` +
  `templates/patterns/tracer-bullet-decomposition{.pattern.json,.md}`.
- **C-08 Primary-sources research** → constraint + gather-step enrichment in
  `agent.analyst-writer` (follow claims upstream; save to convention).
- **C-09 Prototype discipline** → `lessons/prototype-answers-a-question.md` (also the
  prototype node of the wayfinder pattern).
- **C-10 Domain glossary + 3-gate ADR rule** → `templates/context-packs/domain-glossary/`.
- **C-11 Deep-module vocabulary** → `lessons/deep-modules.md`.
- **C-12 Handoff deltas** → two mechanics added to `templates/patterns/context-handoff.md`
  (packet names its skills; reference, don't duplicate).
- **C-14b Lifecycle states** → naming & lifecycle governance (README §Naming & lifecycle
  governance): `status` field on every asset (`incubating`/`active`/`deprecated`/`retired`,
  deprecate requires `superseded_by`), enforced by `validate.py` and rendered by the
  catalog's lifecycle section. Renames ship as deprecate-and-re-add.

## 6. Rejection log

Rejected candidates land here as one line each — gist, source, reason — and are checked
during every intake (rubric G2) so nothing is re-proposed.

- Catalog router skill, "ask-seed" (S1 `ask-matt`) — rejected 2026-07-10: already exists as
  `agent.librarian`, whose router role and rationale are recorded in
  `lessons/cognitive-vs-context-load.md`; a second router would duplicate it.
