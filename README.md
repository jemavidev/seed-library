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
