# hook.context-zone-guard — spec

## What it is
A context-watermark hook: watches an agent's working-context usage against a dual ceiling
(absolute tokens AND percentage of the window — whichever is lower governs) and triggers
graduated responses — compact at the soft mark, hand off at the hard mark. The mechanical
trigger behind the `context-handoff` pattern.

## Trigger semantics (harness-neutral)
- **Trigger:** `post-turn` — evaluated after each agent turn, when usage numbers are fresh.
- **Input:** current context usage (tokens, percent) + the profile's configured band.
- **Effect:** below soft = nothing; soft crossed = inject a compaction advisory ("summarize
  scratch state, drop dead context"); hard crossed = fire the `context-handoff` pattern at
  the next atomic-step boundary.

## Behavior rules
1. **Dual ceiling, lower wins:** `soft = min(soft_tokens, soft_percent × window)`; same for
   hard. Models with different window sizes get consistent behavior from one config.
2. **Graduated, not binary:** the soft advisory gives the agent a chance to shed weight and
   avoid succession entirely; the hard trigger is not negotiable.
3. **Atomic-step respect:** the hard trigger requests handoff at the next step boundary; it
   never interrupts a write or an open transaction mid-flight.
4. **Hysteresis:** after a compaction drops usage below soft, re-arming requires a full
   re-cross — no flapping advisories every turn.

## Configuration
`{ soft_tokens, soft_percent, hard_tokens, hard_percent }` per profile; defaults are set by
the runtime's context policy, and instantiations override per model class.

## When to attach
Any profile doing long-horizon work; mandatory for daemon-mode runs where nobody is watching
the window fill up.
