---
name: curriculum-builder
description: Turn observable learning outcomes into outlines/syllabi/lesson-plans/rubrics with enforced outcome→unit→assessment mapping.
---

Use this skill to build teaching artifacts that can be audited against their promises.

- Outcomes first, always: if they aren't observable ("learner can <do something checkable>"),
  fix the outcomes before building anything on them.
- Respect the audience's floor: the `prerequisites` list is what you may assume — nothing
  else.
- Read `gaps` in the result: an outcome no unit serves is a promise the course breaks;
  either add a unit or remove the outcome, explicitly.
- Rubrics grade outcomes, not effort — each criterion traces to an outcome by number.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.education.curriculum-builder@v1
