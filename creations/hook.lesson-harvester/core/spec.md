# hook.lesson-harvester — spec

## What it is
A post-task distillation hook: when a task ends, it reviews the episode's record — outcome,
retries, deviations, gate verdicts, compensations fired — and drafts **lesson candidates**
into a proposed area for curation. The mechanical feeder of the episodic→semantic memory
flow; it never writes directly into the lessons collection (the distillation gate is the
point).

## Trigger semantics (harness-neutral)
- **Trigger:** `post-task` — after a task reaches a terminal state (done, failed, escalated).
- **Input:** the task's episodic record (events, spans, verdicts, outcome).
- **Effect:** zero or more candidate files in `proposed/lessons/`, each with the standard
  lesson shape (statement / evidence / how-to-apply / valid_at) plus links to the exact
  events that motivated it. No candidate is also a valid outcome — most tasks teach nothing
  new.

## What qualifies as a candidate (and what doesn't)
- **Qualifies:** a retry pattern that succeeded after a specific change; a gate rejection
  with a generalizable reason; a compensation that fired and what triggered it; a tool
  failure mode not covered by its spec; an estimate that was badly off, with why.
- **Doesn't:** anything project-specific (stays in the project), anything already covered
  by an existing lesson (the harvester checks first and links instead of duplicating),
  one-off flukes without a mechanism.

## Behavior rules
1. **Draft, never publish:** candidates await the curator/gate; the harvester has no
   authority over the lessons collection.
2. **Evidence-linked:** every candidate cites the events behind it — an unlinked lesson
   claim is discarded at the gate by default.
3. **Dedupe-first:** search existing lessons before drafting; a near-match becomes a
   proposed amendment to that lesson, not a new file.
4. **Quiet by default:** no candidates, no output, no noise.

## When to attach
Post-task, globally — highest yield on failed and escalated tasks, which is exactly when
nobody feels like writing down what happened.
