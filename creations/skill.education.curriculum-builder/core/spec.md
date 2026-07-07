# skill.education.curriculum-builder — spec

## What it does
Builds teaching artifacts from declared learning outcomes: a course outline, a full
syllabus, a single lesson plan, or an assessment rubric — written into the project as a
structured document. The outcome→unit→assessment mapping is enforced: nothing exists in the
artifact that doesn't serve a declared outcome.

## When to use / when not
- **Use** to materialize the teaching side of a course charter: turn outcomes into units,
  units into lesson plans, outcomes into rubrics.
- **Don't use** to *deliver* teaching (that is `agent.educator-tutor`, live) or to write
  general documents (`document-composer`).

## Inputs / outputs
- In: `subject`, `audience` (`{ level, prerequisites[] }` — what learners must NOT be
  assumed to know matters most), `outcomes` (observable "learner can…" statements),
  `duration` (e.g. `"6 weeks"`, `"1 session"`), `format`
  (`outline|full-syllabus|lesson-plan|rubric`), `output_path`.
- Out: `{ output_path, units, outcomes_covered, gaps }` — `gaps` lists declared outcomes no
  unit serves; a non-empty `gaps` is a loud result, never silently dropped.

## Worked example
`{ "subject": "Video calls for retirees", "audience": { "level": "absolute beginner",
"prerequisites": ["owns a smartphone"] }, "outcomes": ["learner can join a call from an
invitation link", "learner can mute/unmute and use the camera"], "duration": "2 sessions",
"format": "outline", "output_path": "course/outline.md" }` →
`{ "output_path": "course/outline.md", "units": 2, "outcomes_covered": 2, "gaps": [] }`.

## Failure modes
- `outcomes_missing` — empty or non-observable outcomes ("understands X" is rejected with
  the reason) (not retryable as-is)
- `invalid_duration` (not retryable) · `write_denied` (not retryable).

## Constraints
Every unit names the outcomes it serves; every outcome maps to at least one assessment in
syllabus/rubric formats. Audience prerequisites gate vocabulary: an outline for absolute
beginners that leans on unexplained jargon fails its own review checklist (embedded in the
artifact for the human reviewer).
