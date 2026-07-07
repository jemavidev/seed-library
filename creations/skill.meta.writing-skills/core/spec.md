# skill.meta.writing-skills — spec

## What it does
The reference an author (a human, or a host system's generation engine) writes and edits
library assets against: the shared vocabulary and principles that make a skill behave the same
way every run. Its defining constraint: it optimizes for **predictability of process**, not for
cleverness, completeness, or how impressive the asset reads.

## When to use / when not
- **Use** whenever authoring a new skill/profile/hook, editing an existing one, or diagnosing
  why one misfires — and as the checklist a generation engine consults before a creation
  leaves review.
- **Don't use** to author *content* assets (references, lessons) — those follow the lesson
  format; this governs executable creations.

## Inputs / outputs
- In: a draft creation (or the intent for one) + the target asset class.
- Out: an authored/edited creation that satisfies the predictability checklist below, or a
  diagnosis naming which failure mode a misbehaving creation exhibits.

## The predictability checklist (the substance)

1. **Pick the invocation mode deliberately.** User-invoked (zero standing context, but the
   router must be able to reach it) vs model-invoked (fires unprompted, pays permanent window
   rent). Default to user-invoked; justify every model-invoked promotion. See
   `cognitive-vs-context-load`.
2. **Give it a leading word.** One pretraining-dense concept that anchors both execution and
   invocation; put it where the executor and the router both see it. See `leading-words`.
3. **Place information on the right rung.** In-skill step → in-skill reference → external
   reference behind a context pointer. Move detail *down* the ladder so the top stays legible
   (progressive disclosure). Full spec loads on activation, never up front.
4. **Prune sentence by sentence.** Single source of truth, relevance, and the no-op test,
   applied against sediment and sprawl.
5. **Read it back against the five failure modes** — premature completion, duplication,
   sediment, sprawl, no-op (see `skill-failure-modes`) — before shipping.

## The three-fidelity convention (how knowledge is stored for a bounded context)

Any asset heavy enough to strain a context budget SHOULD ship at three fidelities of the *same*
knowledge, so the router can load the one that fits:

- **nano** — the decision rules only, the compact fallback for tight budgets.
- **mini** — the working version: rules + triggers + checklist, the default most tasks load.
- **full** — the canonical complete source and reference.

Store them as `core/asset.nano.md`, `core/asset.mini.md`, `core/asset.md`. The nano must be
derivable-in-spirit from the full (never say something the full contradicts), and every
fidelity carries the same leading word. A one-fidelity asset is fine when even its full form is
small; the three-tier form is for knowledge that would otherwise be all-or-nothing in the
window.

## Failure modes (of this skill's own use)
- Authoring for completeness instead of predictability produces sprawl.
- Skipping the leading word makes the asset unroutable — the router has nothing to reach for.

## Constraints
Everything here is capability-level and harness-neutral: it never names a model, a harness, or
a provider. Predictability is the root virtue; every rule above is judged against it.
