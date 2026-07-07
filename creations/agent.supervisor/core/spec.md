# agent.supervisor — spec

## What it is
The routing profile: single entry point of a multi-agent setup. Classifies intent, delegates
to one specialist with a self-contained brief, consolidates the answer. Owns no effectful
tools by design.

## When to use / when not
- **Use** as the top node of the `routing` pattern, or anywhere one consistent voice must
  front several specialists.
- **Don't use** for decomposition of a big task into subtasks (that is an orchestrator role)
  or where only one specialist exists (call it directly).

## Inputs / outputs
- In: a user request (free text) + a routing table (intent → specialist) provided by the
  instantiating context.
- Out: one consolidated answer; internally, briefs and returned results per the `routing`
  pattern state.

## Evaluation notes
Evals check routing quality (right specialist, or direct answer for trivialities) and honesty
of consolidation (limitations preserved), not the specialists' own output quality.
