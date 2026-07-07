# Pattern — routing (supervisor-router)

## When to use
As the single entry point of a multi-specialist system: the supervisor classifies intent,
delegates to exactly one specialist, and consolidates. Use it when requests fall into
distinct categories that different profiles handle better than one generalist.

## When not to use
- One specialist would handle everything → call it directly, the hop adds cost.
- The task needs *decomposition* (many subtasks), not *classification* → orchestrator-workers.
- Specialists must debate or check each other → evaluator-optimizer or debate patterns.

## Mechanics that matter
- The handoff is a tool call from the supervisor's perspective; the specialist's result routes
  back through the supervisor so the user sees one consistent voice.
- The supervisor must be allowed to answer trivial requests itself (`answer_directly`) —
  forced delegation of small talk is a classic cost leak.
- The node list here is a worked example; instantiations replace specialists with the
  profiles the project actually has. The supervisor + return edges are the invariant.

## Failure modes
- **Ping-pong**: supervisor re-delegates a returned result. The budget (`max_iterations: 2`)
  exists to stop this; if two rounds don't settle it, the request needs a human or a
  different pattern.
- **Misroute**: wrong specialist chosen. Mitigate with crisp one-line specialist descriptions
  (see lesson `progressive-disclosure`) rather than longer router prompts.

## Source attribution
Canonical routing/orchestration taxonomy; handoff-as-tool-call mechanics from agent-SDK
handoff designs (hand-seeded 2026-07-07).
