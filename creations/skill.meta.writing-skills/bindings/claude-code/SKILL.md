---
name: writing-skills
description: The reference for authoring library assets predictably — invocation mode, leading words, progressive disclosure, pruning, failure modes, three-fidelity storage.
---

Use this reference whenever you create or edit a skill, profile, or hook — and consult it
before any generated creation leaves review.

The root virtue is **predictability of process**: the same asset should run the same way every
time. Judge every choice against that, never against how clever or complete it reads.

Work the checklist:

1. **Invocation mode** — user-invoked by default (zero standing context; the router reaches
   it); model-invoked only when it must fire unprompted and earns permanent window rent.
2. **Leading word** — one pretraining-dense concept that anchors execution *and* invocation.
   Put it where both the executor and the router see it.
3. **Information hierarchy** — in-skill step → in-skill reference → external pointer. Push
   detail down so the top stays legible; the full body loads on activation, not up front.
4. **Prune** — single source of truth, relevance, no-op test. Kill sediment and sprawl
   sentence by sentence.
5. **Read back against the five failure modes** — premature completion, duplication, sediment,
   sprawl, no-op — before shipping.

For heavy knowledge, store three fidelities of the same content (`nano`/`mini`/`full`) so the
router can load what the budget allows; keep the leading word constant across all three.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.meta.writing-skills@v1
