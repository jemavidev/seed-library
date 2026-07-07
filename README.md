# SeeD Library — the cumulative, cross-project brain

This repository is **SeeD's library** (PRD §7.6 of [jemavidev/SeeD](https://github.com/jemavidev/SeeD)):
the knowledge SeeD carries from project to project. It is deliberately a **separate repository**
from the SeeD product — the product is code that evolves; this is knowledge that accumulates.

> **Status:** pre-F3.5 scaffold. SeeD does not manage this repo yet (no code exists);
> the structure below is the contract it will manage once F3.5 lands. Until then, assets
> may be added by hand following [portable-assets.md](https://github.com/jemavidev/SeeD/blob/main/docs/design/portable-assets.md).

## The four asset classes (all cross-project)

| Directory | Holds | Closes |
|---|---|---|
| `creations/` | agents, skills, hooks, tools, prompts — each in the **two-layer format** (`core/` harness-neutral + `bindings/` per-harness) | meta-cost: don't rebuild what exists |
| `model-knowledge/` | empirical catalog data — which model wins at which task-type, cost, latency (JSONL) | cold-start: a new project routes well from day one |
| `lessons/` | generalizable system-level learnings, distilled (markdown/JSONL) | repeating past mistakes |
| `templates/` | orchestration setups, frontier policies, charter scaffolds that worked | re-deciding solved problems |

## The rules this repo lives by

1. **Two-layer format.** A creation's `core/` (spec + prompt + evals + lessons) never references
   Pi APIs, SeeD commands, or model IDs — capabilities only. Harness glue lives in `bindings/`
   and is disposable.
2. **Copy-with-lineage.** Projects *copy* assets from here (with a `library://<id>@v<n>` lineage
   marker), never live-reference them — projects stay portable.
3. **Promote only what generalizes.** Project-local assets enter this repo through SeeD's
   promotion gate (two-sided critique + eval net); a project-specific quirk never pollutes the
   shared brain.
4. **The SeeD-vanishes test.** If SeeD stopped existing tomorrow, this repo alone must remain
   valuable: prompts readable as markdown, skills droppable into `.claude/skills/`, tools
   runnable as MCP servers, lessons greppable. Any format choice that fails this test is rejected.

## Seeding conventions (hand-seeded assets, pre-F3.5)

Seeded per the [library-seeding-plan](https://github.com/jemavidev/SeeD/blob/main/docs/implementation/library-seeding-plan.md):

- Creation ids: `<kind>.<domain>.<name>` (e.g. `skill.sdlc.read-project-file`, `agent.supervisor`).
- Skills carry a `toolspec.json` sidecar at the creation root (SeeD ToolSpec contract);
  the pure JSON Schema interface lives in `core/interface.schema.json` (strict: `additionalProperties:false`).
- Every hand-seeded `_meta.json` sets `lineage: "hand-seeded@<date>"` and `libraryShare: "candidate"` —
  the F3.5 promotion gate re-validates everything seeded by hand.
- Templates are filename-addressed: `templates/patterns/<id>.pattern.json` (+ `<id>.md` rationale),
  `templates/context-packs/<name>/`, `templates/charters/`, `templates/frontier-policies/`.

## Index

### creations/
- `skill.sdlc.read-project-file` — read one project file safely, truncation-aware (pure)
- `skill.sdlc.write-modify-file` — create/overwrite or patch one file, atomic, patch-over-write (local)
- `skill.sdlc.git-vcs-operator` — status/branch/checkout/commit/push/revert, one action per call (external: push)
- `skill.sdlc.run-test-suite` — run tests, structured pass/fail with per-failure location (local)
- `skill.sdlc.code-static-analyzer` — normalized lint/type findings, judge by delta (pure)
- `skill.sdlc.dependency-manager` — add/remove/update/install/audit via the project's manager (local)
- `skill.core-utils.file-search` — filename/content/regex search with excerpts, ignore-aware (pure)
- `skill.core-utils.document-parser` — PDF/DOCX/XLSX/HTML → markdown/text, structure kept (pure)
- `skill.core-utils.regex-data-extractor` — emails/IPs/URLs/hashes/custom regex, deduplicated (pure)
- `skill.core-utils.crypto-token-generator` — tokens/UUID/SHA-256/HMAC, key by env-name only (pure)
- `skill.core-utils.data-transformer` — JSON/YAML/CSV/markdown-table 1:1 conversion, fails over guessing (local)
- `skill.core-utils.archive-operator` — zip/tar.gz compress/extract/list, zip-slip-safe, atomic (local)
- `skill.core-utils.web-search` — provider-backed search, no secrets in queries (pure, network)
- `skill.core-utils.document-composer` — outline → structured document with required-section enforcement (local)
- `agent.supervisor` — router profile: classify, delegate once, consolidate honestly; no effect tools
- `agent.sdlc-developer` — builder profile: read-before-write, verify-after-change, honest reporting
- `agent.qa-reviewer` — read-only auditor: typed findings with failure scenarios, pass/fail verdict
- `hook.output-schema-guard` — post-output strict schema validation with bounded error-carrying retry
- `hook.style-rules-injector` — pre-run project-rules block assembly, nearest-wins, budgeted

### templates/
- `patterns/routing` — supervisor-router: single entry, one specialist per request
- `patterns/evaluator-optimizer` — generator+evaluator loop, typed findings, exhaustion is a first-class outcome
- `patterns/prompt-chaining` — fixed linear stages with typed contracts and stop-only gates
- `patterns/parallelization` — map-reduce fan-out with per-shard budgets and a join that cannot hang
- `patterns/hitl-checkpoint` — freeze-at-gate before consequential actions; stance-based verdict, timeout fails safe
- `context-packs/default-agent-context` — per-agent context policy: budgeted blocks, retrieval, state keys, handoff contract
- `context-packs/project-rules` — rule-file convention: nearest-wins, compilable to one budgeted block
- `charters/software-project` — vision/scope/constraints/success-criteria scaffold with guidance
- `charters/education-course` — outcomes-driven course scaffold, every outcome assessed
- `charters/business-idea` — plain-language idea charter: customer, model, assumptions, validation plan
- `frontier-policies/conservative` — gate every mutation; uncompensated external effects blocked
- `frontier-policies/balanced` — silent reads, narrated local work, confirm at the egress boundary
- `frontier-policies/autonomous` — unattended preset; only un-undoable effects interrupt

### lessons/
- `strict-schemas-always` — additionalProperties:false + full required, everywhere
- `progressive-disclosure` — inject the index, never the catalog
- `cyclic-patterns-declare-termination` — max_iterations + termination or reject at load
- `knowledge-carries-temporal-validity` — facts carry valid_at; supersede, don't delete
- `single-source-of-truth-schemas` — bindings are derived, never hand-written twins
- `profiles-as-config-not-code` — agent identity lives in versioned, readable config

