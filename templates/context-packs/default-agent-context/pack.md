# Context pack — default-agent-context

> Status: active

The baseline context policy attached to any instantiated agent profile. It declares — as
data, not prose — what enters the agent's context, what state it shares with peers, and what
it must hand off when it stops.

## The four sections

1. **`system_context_refs`** — static knowledge blocks always present (identity from the
   profile, project rules block, task brief). Each ref carries a token budget; the sum defines
   the fixed floor of every turn.
2. **`retrieval_sources`** — dynamic knowledge fetched per task (document collections, code
   search), each with `top_k` and a relevance threshold. Retrieval augments the floor; it
   never replaces the brief.
3. **`shared_state_keys` / `private_state_keys`** — the contract with the running pattern:
   shared keys are readable/writable pattern state; private keys stay with this agent and die
   with it. Anything not listed does not survive the agent.
4. **`handoff_contract`** — the fields this agent must populate before finishing or being
   replaced (results, decisions, open items). A successor must be able to continue from the
   handoff packet alone, without replaying the conversation.

## Design rules
- Budgets are per-block so overflow is a *decision* (drop lowest-priority block) instead of an
  accident (mid-block truncation).
- The handoff contract is what makes proactive replacement safe: when a runtime enforces a
  working-context ceiling, "fill the handoff packet and yield" is a routine operation, not an
  emergency.

## How to instantiate
Copy `example.json`, point `profile` at the target agent creation, tune budgets and sources.
Validation: `config.schema.json`.
