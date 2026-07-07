# Pattern — multi-agent-debate

## When to use
High-stakes judgment calls with real trade-offs and no objective evaluator: architecture
choices, security-versus-velocity decisions, cost-model selection, build-vs-buy. The value is
in forcing the strongest version of each side to be written down.

## When not to use
- An objective check exists → evaluator-optimizer; debating what a test can settle is theater.
- The answer is retrievable → research, not debate.
- Low stakes → a single agent's recommendation is cheaper and usually as good.

## Mechanics that matter
- **Assigned, distinct stances**: each debater gets a `stance_brief` (e.g. "argue operational
  simplicity", "argue security posture") — without assignment, all debaters converge to the
  same reasonable-sounding middle and the pattern buys nothing.
- **Critique rounds are bounded** (default 2): positions must respond to specific critiques,
  not restate themselves.
- **The moderator synthesizes, it does not average**: the output is one recommendation with
  confidence, plus the disagreements that survived — a decision-maker needs to know what the
  losing argument was.

## Failure modes
- **Groupthink**: debaters drift to consensus early. The convergence exit exists for genuine
  agreement, but the moderator should treat round-1 unanimity as a smell (stance briefs too
  weak).
- **Verbosity arms race**: cap position lengths in the stance briefs; arguments win on
  content, not volume.

## Source attribution
Multi-agent debate from conversational-framework practice (group chat with distinct
personas + termination conditions); synthesis-over-vote from decision-record practice
(hand-seeded 2026-07-07).
