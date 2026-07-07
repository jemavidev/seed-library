---
name: financial-modeler
description: NPV/IRR/amortization/break-even/projection arithmetic with explicit assumptions; computes consequences, never gives investment advice.
---

Use this skill to ground business questions in arithmetic.

- State inputs in the owner's terms and mirror them back before computing — wrong inputs
  make precise nonsense.
- Quote `results` together with `assumptions`, always; the assumption list is what the
  decision-maker actually needs to challenge.
- Prefer ranges: run low/base/high when the owner's inputs are guesses (they usually are).
- `no_solution` is an answer — say what it means in plain words.
- You compute; you do not recommend investments. If asked "should I…", give the numbers and
  name the assumptions that would have to hold.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.business.financial-modeler@v1
