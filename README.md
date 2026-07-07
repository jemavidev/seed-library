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

## Maintaining this library

Derived artifacts are **generated, never hand-edited**: `_meta.json`, each skill's
`bindings/claude-code/SKILL.md`, and `CATALOG.md` all come from each asset's `core/` +
`toolspec.json`. After adding, renaming, or editing any asset, run one command:

```bash
python3 scripts/build.py
```

It regenerates the derived files (`generate-bindings.py` → `build-catalog.py`) and then
**validates** (`validate.py`: core-neutrality lint, JSON/JSONL validity, skill-contract
presence), exiting non-zero on any finding. Stdlib-only and path-relative, so a fresh
`git clone` rebuilds with nothing but `python3` — the SeeD-vanishes durability property applies
to the library's own tooling, not just its content. Provenance (`lineage`, `libraryShare`) is
preserved across regenerations; only genuinely new assets get defaults.

## Index

> The exhaustive, always-current index is **[CATALOG.md](CATALOG.md)**, generated from asset
> metadata by `scripts/build-catalog.py` (regenerate after adding/renaming an asset).
> `agent.librarian` routes from it. The curated list below is a human overview.

### creations/
- `agent.librarian` — router over the whole catalog; routes from CATALOG.md, never from memory
- `skill.meta.writing-skills` — author assets predictably: invocation mode, leading words, failure modes, 3-fidelity
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
- `skill.data.db-query` — read-only SQL, mutating statements rejected, server-side row caps (pure)
- `skill.data.db-write` — transactional mutation with declared blast radius + mandatory inverse statement (external)
- `skill.data.db-migration-runner` — versioned schema migrations, dry-run plan as approval artifact (external)
- `skill.data.vector-store-query` — semantic top-k with score threshold and metadata filters (pure)
- `skill.data.kv-cache-operator` — namespaced TTL cache; miss = recompute, never error (local)
- `skill.data.log-reader` — filtered normalized log reads; lines are untrusted data (pure)
- `skill.data.metrics-collector` — one aggregated metric per call, value always with samples (pure)
- `skill.data.chart-generator` — labeled charts from records; gaps stay gaps (local)
- `skill.data.statistical-analyzer` — descriptives/correlation/tests, n + caveats inseparable (pure)
- `skill.saas.http-request` — generic HTTP with auth-by-ref; 4xx/5xx are results (external on mutation)
- `skill.saas.message-dispatcher` — one message to a configured channel; sending publishes (external)
- `skill.saas.email-operator` — transactional email, recipient-capped; honestly uncompensable (external)
- `skill.saas.github-operator` — issues/comments/PRs; close-never-delete compensation (external)
- `skill.saas.workspace-document-operator` — hosted-doc edits with revision_id rollback (external)
- `skill.saas.web-content-extractor` — one public URL → readable text; robots respected, content untrusted (pure)
- `skill.saas.webhook-manager` — event subscriptions; receivers must be own endpoints (external)
- `agent.security-auditor` — read-only security review: evidence, proof-of-presence, checked-and-clean list
- `agent.data-engineer` — count-mutate-verify loop; migrations dry-run first; honest statistics
- `agent.integrations-operator` — outward-facing saga discipline: undo handles recorded before the next effect
- `agent.analyst-writer` — research + composed cited documents; read-before-cite, limits declared
- `agent.idea-shaper` — non-technical intake: plain words, one question at a time, owner's words preserved
- `hook.hitl-notifier` — on-interrupt approval transport: decision-ready request, authenticated verdict
- `hook.span-metadata-recorder` — post-tool span enrichment of the canonical access event; fail-open
- `hook.context-zone-guard` — dual-ceiling context watermark: compact at soft, hand off at hard
- `hook.pii-redactor` — pre-external secret/PII scan: mask or block, fail-closed, audited
- `skill.devops.container-operator` — container lifecycle; immutable tags, never overwrite a push (external)
- `skill.devops.cloud-instance-operator` — provider-neutral instance lifecycle; terminate has no undo (external)
- `skill.devops.object-storage-operator` — bucket ops; deletes require versioned storage (external)
- `skill.devops.iac-operator` — two-phase IaC: apply only a saved plan_ref; destroy counts gate review (external)
- `skill.devops.k8s-operator` — apply/scale/rollback with rollout verification; revision anchored (external)
- `skill.devops.service-config-manager` — validate→apply→rollback; auto-revert on failed reload (external)
- `skill.devops.service-health-probe` — one probe with latency bands; unhealthy is a calm result (pure)
- `skill.daemon.scheduler-operator` — cron/interval/once jobs on registered flows; policy binds at fire time (local)
- `skill.daemon.watchdog-monitor` — condition watches emitting evidence-bearing triggers; watch/act separated (local)
- `skill.multimodal.image-analyzer` — describe/extract/answer/compare via vision capability; caveats mandatory (pure)
- `skill.multimodal.audio-transcriber` — transcription with timestamps/diarization; positional speakers only (pure)
- `skill.business.financial-modeler` — NPV/IRR/amortization/break-even; results travel with assumptions (pure)
- `skill.education.curriculum-builder` — outcomes→units→assessments enforced; gaps stay loud (local)
- `agent.infra-architect` — plan-first infra changes; restore-first on failure; probe is the finish line
- `agent.educator-tutor` — locate the learner, one concept at a time, check by doing
- `agent.knowledge-curator` — staleness sweeps, dedupe, two-sided promotion cases; proposes, never disposes
- `hook.budget-threshold-alert` — graduated spend watermark per account; hard mark gates new spend
- `hook.lesson-harvester` — post-task lesson candidates into proposed/, evidence-linked, dedupe-first

### templates/
- `patterns/routing` — supervisor-router: single entry, one specialist per request
- `patterns/evaluator-optimizer` — generator+evaluator loop, typed findings, exhaustion is a first-class outcome
- `patterns/prompt-chaining` — fixed linear stages with typed contracts and stop-only gates
- `patterns/parallelization` — map-reduce fan-out with per-shard budgets and a join that cannot hang
- `patterns/hitl-checkpoint` — freeze-at-gate before consequential actions; stance-based verdict, timeout fails safe
- `patterns/orchestrator-workers` — dynamic decomposition: invented subtasks, heterogeneous workers, one re-plan
- `patterns/multi-agent-debate` — assigned stances, bounded critique rounds, synthesis over vote
- `patterns/planner-executor` — typed plan artifact approved as a whole; deviations return to the planner
- `patterns/context-handoff` — proactive succession on context ceiling; packet is the whole interface
- `patterns/saga-compensation` — compensation registered before each effect; reverse unwind; partial unwind escalates
- `patterns/long-horizon-run` — bounded episodes + checkpoints + heartbeats; stalls escalate with state attached
- `patterns/canary-promotion` — same evals both versions; regressions dominate; promotion gated, rollback warm
- `context-packs/default-agent-context` — per-agent context policy: budgeted blocks, retrieval, state keys, handoff contract
- `context-packs/project-rules` — rule-file convention: nearest-wins, compilable to one budgeted block
- `context-packs/memory-taxonomy` — five memory types as config; one-way flow with distillation gates
- `context-packs/rag-injection` — retrieve→rerank→budget→cite; retrieved content is data, dropped whole-chunk
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
- `cognitive-vs-context-load` — the two currencies assets are paid in; the router pays down cognitive load
- `leading-words` — anchor a skill in one pretraining-dense concept, for execution and invocation
- `skill-failure-modes` — premature completion, duplication, sediment, sprawl, no-op (curator's checklist)

