# CANDIDATES — external intake & evaluation queue

> **Status:** living document, created 2026-07-10. This is the standing intake queue for
> ideas harvested from external sources (videos, repos, posts) that may become library
> assets. It lives in this repo — not the SeeD product repo — so intake works from any
> machine or project that clones `jemavidev/seed-library`, and so accepted candidates
> graduate in place. Hand-maintained (like `ATTRIBUTIONS.md`); never generated.
>
> Workflow: the owner drops a source into a session → the agent analyzes it against the
> rubric (§2) → new candidates land in §4 as `proposed` → the owner evaluates → verdicts
> are recorded in place. Rejected ideas move to §5 with the reason, so they are never
> re-proposed.

---

## 1. The intake loop

1. **Bring a source.** Paste a repo URL, transcript path, or article into a session and say
   "evaluate against CANDIDATES".
2. **Agent analyzes.** Read the source, run each idea through the rubric (§2), and check
   redundancy against what already exists: [CATALOG.md](CATALOG.md) (generated, always
   current), `lessons/`, `templates/`, and the Rejection log (§5). Check *by concept*, not
   by the source's wording. Append survivors to §4 as `proposed`; register the source in §3.
3. **Owner evaluates.** Each candidate is a one-screen read: what it is, what library shape
   it would take, why it fits, what's unresolved, what already overlaps.
4. **Record the verdict.** `accepted` → build the asset per this repo's seeding conventions
   (README §Seeding conventions) and run `python3 scripts/build.py`; `rejected` → move a
   one-line gist + reason to §5 and delete the full entry.

Statuses: `proposed` → `evaluating` → `accepted` | `rejected` | `deferred`.

## 2. Evaluation rubric (gates, in order)

Derived from this repo's rules (README §The rules this repo lives by) and the SeeD product
contracts ([portable-assets](https://github.com/jemavidev/SeeD/blob/main/docs/design/portable-assets.md),
[library-seeding-plan](https://github.com/jemavidev/SeeD/blob/main/docs/implementation/library-seeding-plan.md)).
A candidate that fails G1 is dead; the rest are judgement calls to record.

- **G1 — Kernel exclusion.** If the idea drifts toward approval logic, credentials, audit,
  or raw shell, stop: the SeeD Kernel owns it. Never a library asset.
- **G2 — Redundancy.** Does an existing creation, pattern, lesson, or template already
  cover it? Check `CATALOG.md`, `lessons/`, `templates/`, and §5. Partial overlap is not
  rejection — but the candidate must then be narrowed to its genuine delta.
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
| S1 | [mattpocock/skills](https://github.com/mattpocock/skills) v1.1 — `skills/engineering/` + `skills/productivity/` | 2026-07-10 | Plus owner-supplied video transcript. Prompt-shaped SKILL.md files for Claude-Code-like harnesses; an SDLC flow: grilling → wayfinder → to-spec → to-tickets → implement (TDD) → code-review → triage. Note: this library already absorbed part of an earlier pass over this source (`skill.meta.writing-skills`, `lessons/leading-words.md`, `lessons/progressive-disclosure.md`, `lessons/skill-failure-modes.md`, `lessons/cognitive-vs-context-load.md`, `agent.librarian`, `agent.idea-shaper`) — redundancy notes below reflect that. |

## 4. Candidates

### Tier A — strong fit, high leverage

#### C-01 · Wayfinder as a pattern
- **Source:** S1 (`engineering/wayfinder`)
- **What it is:** Plans work too big for one agent session as a *shared map* on the issue
  tracker: a map issue (destination, decisions-so-far index, "not yet specified" fog of
  war, out-of-scope) plus child tickets with native blocking edges. Sessions claim and
  resolve exactly one ticket each, graduating fog into new tickets until the route is
  clear. Ticket types: research (AFK), prototype (HITL), grilling (HITL), task.
- **Proposed shape:** `templates/patterns/wayfinder.pattern.json` (+ `.md` rationale) — a
  declarative graph whose nodes are typed tickets and whose edges are blocking relations;
  HITL ticket types reference kernel stances, AFK types run free within policy. Must
  declare `max_iterations` + termination ("no open tickets") per
  `lessons/cyclic-patterns-declare-termination.md`.
- **Redundancy check:** clean. Distinct from `long-horizon-run` (checkpointed *execution*
  across sessions) and `planner-executor` (one reviewed plan, then effects): Wayfinder is
  *decision-mapping* across sessions — it produces decisions, not deliverables, and its
  state lives on a tracker, not in checkpoints. Complements both.
- **Open questions:** tracker binding (GitHub issues vs local markdown) is clearly
  `bindings/`; the pattern's "frontier query" operations need a neutral core phrasing.
- **Status:** proposed

#### C-02 · Facts-vs-decisions grilling (delta)
- **Source:** S1 (`productivity/grilling`, `engineering/grill-with-docs`)
- **What it is:** Interview the user one question at a time, with a recommended answer per
  question; explicit gate — do not act until the user confirms shared understanding. The
  load-bearing v1.1 line (added after agents grilled *themselves*): **facts** are found by
  exploring the codebase; **decisions** belong to the user and must be put to them.
- **Redundancy check:** partial — `agent.idea-shaper` already carries one-question-at-a-time
  and owner's-words-preserved. The genuine delta is (a) the facts-vs-decisions rule and
  (b) the do-not-enact-until-confirmed gate.
- **Proposed shape:** lesson (`lessons/facts-vs-decisions.md`) + enrichment of
  `agent.idea-shaper` and the `hitl-checkpoint` pattern rationale. "Facts are the agent's
  to find; decisions are the user's" is a compact restatement of SeeD's frontier doctrine
  and gives the HITL stance a crisp trigger condition: interrupt on decisions, never on
  facts.
- **Status:** proposed

#### C-04 · Triage state machine + rejection knowledge base
- **Source:** S1 (`engineering/triage` + its `OUT-OF-SCOPE.md` convention)
- **What it is:** Issues/PRs move through a small state machine (needs-triage → needs-info
  / ready-for-agent / ready-for-human / wontfix) with two category roles (bug/enhancement).
  Two ideas stand out: (a) every triage step starts with a **redundancy check** ("is this
  already implemented?") and a **prior-rejection check**; (b) rejected enhancements are
  written to an out-of-scope KB with reasons, so they are never re-litigated.
- **Redundancy check:** clean — no triage pattern or lesson exists.
- **Proposed shape:** `templates/patterns/triage.pattern.json` for the state machine; the
  rejection-KB convention adopted as a **negative-lesson** kind in `lessons/` ("rejected,
  with reason" entries consulted before re-proposing). SeeD's self-improvement *proposes,
  never auto-applies* — a proposal queue is an issue tracker in disguise, and these states
  give it a vocabulary. (§5 of this document is the same convention, applied to itself.)
- **Status:** proposed

### Tier B — good fit, maps onto existing assets

#### C-05 · Fowler smell baseline for the qa-reviewer
- **Source:** S1 (`engineering/code-review`)
- **What it is:** A fixed baseline of ~12 code smells from Fowler's *Refactoring* ch.3
  (mysterious name, feature envy, data clumps, primitive obsession, shotgun surgery,
  speculative generality, message chains, middle man, …), each one sentence of
  what-it-is → how-to-fix. Naming the smell is enough — the model repeats the word back
  and acts on it. Binding rules: documented repo standards override the baseline; every
  smell is a judgement call, never a hard violation. Review runs as two parallel
  sub-agents — **Standards** axis and **Spec** axis — never merged or reranked, so one
  axis can't mask the other.
- **Redundancy check:** `agent.qa-reviewer` exists (typed findings, pass/fail verdict) but
  carries no smell vocabulary; the two-axis shape is an instantiation of the existing
  `parallelization` pattern (no new pattern needed).
- **Proposed shape:** context pack or lesson attached to `agent.qa-reviewer`. Textbook G7
  prior leverage — ~10 lines buy a whole review vocabulary.
- **Status:** proposed

#### C-06 · Diagnosis discipline — the feedback loop is the skill
- **Source:** S1 (`engineering/diagnosing-bugs`)
- **What it is:** Six-phase loop for hard bugs where Phase 1 is 90% of the value: build a
  **tight, red-capable, deterministic, agent-runnable** feedback loop (one command that
  goes red on this exact bug) *before* forming any hypothesis — "no red-capable command,
  no Phase 2". Then minimise the repro until every element is load-bearing, generate 3–5
  falsifiable hypotheses, instrument one variable at a time with greppable `[DEBUG-xxxx]`
  tags, fix behind a regression test, and post-mortem ("what would have prevented this?").
- **Redundancy check:** clean — no lesson covers diagnosis; `agent.sdlc-developer`'s
  verify-after-change is adjacent but far narrower.
- **Proposed shape:** lesson + enrichment of `agent.sdlc-developer` / `agent.qa-reviewer`;
  possibly a `debug-loop` pattern if the phase gates should be machine-enforced. Pure
  method, `effects: local`, SeeD-vanishes-clean.
- **Status:** proposed

#### C-07 · Spec template + tracer-bullet ticket decomposition
- **Source:** S1 (`engineering/to-spec`, `engineering/to-tickets`)
- **What it is:** (a) A canonical spec shape: problem statement → solution → exhaustive
  user stories → implementation decisions (no file paths — they go stale) → testing
  decisions → out of scope. (b) Decomposition into **tracer-bullet vertical slices**, each
  cutting a complete path through every layer, each sized to one fresh context window,
  each declaring its blocking edges; wide mechanical refactors are the named exception,
  sequenced as **expand–contract** (add new form → migrate call sites in batches → delete
  old form).
- **Redundancy check:** clean — no spec-shaped context pack exists (`default-agent-context`,
  `memory-taxonomy`, `project-rules`, `rag-injection` don't cover it); no decomposition
  pattern exists.
- **Proposed shape:** spec template as `templates/context-packs/spec-template/`;
  decomposition as `templates/patterns/tracer-bullet-decomposition.pattern.json` beside
  `orchestrator-workers`. Gives SeeD's "specs not executables" doctrine a canonical
  anatomy; "sized to one context window" ties into context-zone budgeting.
- **Status:** proposed

#### C-08 · Research method — primary-sources discipline (delta)
- **Source:** S1 (`engineering/research`)
- **What it is:** Delegate a question to a background agent that (1) investigates against
  **primary sources only** — official docs, source code, specs — following every claim
  back to the source that owns it, (2) writes one cited markdown file, (3) saves it where
  the repo already keeps such notes, matching convention.
- **Redundancy check:** partial — `agent.analyst-writer` already covers research + cited
  composition (read-before-cite). The delta is the *primary-sources-only* rule (follow
  every claim to the source that owns it) and the save-to-existing-convention habit.
- **Proposed shape:** enrichment of `agent.analyst-writer` (a lesson-sized delta), not a
  new skill. Also the natural executor for Wayfinder's AFK "research" ticket type (C-01).
- **Status:** proposed

#### C-09 · Prototype discipline — throwaway code that answers a question
- **Source:** S1 (`engineering/prototype`)
- **What it is:** Raise the fidelity of a discussion with a cheap concrete artifact. Two
  branches: logic (tiny interactive terminal app driving the state machine through
  hard-to-reason cases) vs UI (several radically different variations, toggleable). Rules:
  throwaway from day one and named as such, one command to run, no persistence, no polish,
  surface full state after every action, and **capture the verdict** — fold the validated
  decision into real code, park the prototype on a throwaway branch as a primary source.
- **Redundancy check:** clean — the library has operators and utilities but no "answer a
  design question cheaply" method.
- **Proposed shape:** lesson + the HITL "prototype" node type of the Wayfinder pattern
  (C-01); could later back a method skill. Inherently HITL (`confirm` stance): the human
  reacts to the artifact.
- **Status:** proposed

#### C-10 · Domain glossary (CONTEXT.md) + three-gate ADR rule
- **Source:** S1 (`engineering/domain-modeling`)
- **What it is:** Maintain a glossary-only `CONTEXT.md` (zero implementation detail),
  updated inline the moment a term is resolved; challenge terms that conflict with it;
  cross-reference claims against code and surface contradictions. ADRs are offered only
  when all three gates hold: **hard to reverse** ∧ **surprising without context** ∧
  **the result of a real trade-off**.
- **Redundancy check:** clean — charters (`software-project`, `business-idea`,
  `education-course`) give domain *orientation* but no glossary convention.
- **Proposed shape:** context pack (glossary + ADR formats) referenced by the charter
  templates; the three-gate rule doubles as guidance for generated projects' ADRs.
- **Status:** proposed

### Tier C — narrowed deltas & conventions

#### C-03 · Skill-authoring discipline (narrowed to its remaining delta)
- **Source:** S1 (`productivity/writing-great-skills` + `GLOSSARY.md`)
- **Redundancy check:** **largely already ingested** — `skill.meta.writing-skills`,
  `lessons/leading-words.md`, `lessons/progressive-disclosure.md`,
  `lessons/skill-failure-modes.md`, `lessons/cognitive-vs-context-load.md` cover leading
  words, disclosure, failure modes, and invocation economics.
- **Remaining delta:** (a) the **no-op test** as a pruning discipline — delete any sentence
  the model already obeys by default; run it sentence-by-sentence, delete whole sentences;
  (b) **checkable completion criteria** — each step ends on a condition the agent can
  verify, exhaustive where it matters ("every modified model accounted for", not "produce
  a list"); (c) **negation** — steer by stating the target behaviour, not the prohibition.
- **Proposed shape:** fold (a)–(c) into `skill.meta.writing-skills` / the existing lessons
  rather than new assets; separately (product-side, not this repo) wire the discipline
  into the GenerationEngine's authoring prompts and the promotion gate.
- **Status:** proposed

#### C-11 · Deep-module design vocabulary
- **Source:** S1 (`engineering/codebase-design`)
- **What it is:** A fixed vocabulary — module, interface, implementation, **depth**
  (leverage at the interface), **seam**, adapter, leverage, locality — with principles:
  the deletion test; "the interface is the test surface"; "one adapter = hypothetical
  seam, two = real one"; depth-as-leverage (explicitly rejecting the lines-ratio framing).
- **Redundancy check:** near-clean — `lessons/leading-words.md` cites *deep module* as an
  example leading word but nothing defines the vocabulary.
- **Proposed shape:** lesson shared by `agent.sdlc-developer` and `agent.qa-reviewer` so
  generated code and its review speak the same design language.
- **Status:** proposed

#### C-12 · Handoff deltas (narrowed)
- **Source:** S1 (`productivity/handoff`)
- **Redundancy check:** mostly covered — `context-handoff` pattern +
  `hook.context-zone-guard` handle when/how to hand off; `hook.pii-redactor` covers
  redaction.
- **Remaining delta:** two rules for the handoff document itself: include a **suggested
  skills** section for the next session; never duplicate content already captured in
  artifacts (specs, ADRs, issues, commits) — reference by path/URL instead.
- **Proposed shape:** fold both into the `context-handoff` pattern rationale/contract.
- **Status:** proposed

#### C-13 · Catalog router ("ask-seed")
- **Source:** S1 (`engineering/ask-matt`)
- **Redundancy check:** **redundant** — `agent.librarian` already routes over the whole
  catalog from `CATALOG.md`, and `lessons/cognitive-vs-context-load.md` already records the
  router-pays-down-cognitive-load rationale.
- **Recommendation:** reject as duplicate; owner to confirm, then move to §5.
- **Status:** proposed — recommend reject

#### C-14 · Invocation-surface field + asset lifecycle states
- **Source:** S1 (repo conventions: `disable-model-invocation` frontmatter; changesets +
  CHANGELOG; `deprecated/` and `in-progress/` folders)
- **Redundancy check:** the *concept* (model-invoked vs user-invoked as context-load vs
  cognitive-load) is already in `lessons/cognitive-vs-context-load.md`; what's missing is
  the **machine-readable** expression.
- **Remaining delta:** (a) an invocation-surface field in ToolSpec / `_meta.json` so
  bindings can generate the right frontmatter per harness — a product **contract change**,
  needs a decision-log ruling before any library work; (b) lifecycle states
  (`in-progress` / `active` / `deprecated`) in `_meta.json`, with renames shipped as
  explicit deprecate-and-re-add and surfaced in the digest.
- **Status:** proposed (blocked on product-side ruling for (a))

## 5. Rejection log

Rejected candidates land here as one line each — gist, source, reason — and are checked
during every intake (rubric G2) so nothing is re-proposed. *(Empty so far.)*

<!-- - <candidate gist> (S<n>) — rejected <date>: <reason> -->
