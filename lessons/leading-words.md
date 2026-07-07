# Lesson — leading words: anchor a skill in the fewest tokens

**Statement.** Give each skill a **leading word** — a compact concept already dense in the
model's pretraining (*tight* feedback loop, *deep* module, *red-green*, *tracer bullet*,
*count-mutate-verify*, *restore-first*). The agent thinks *with* that word while executing the
skill, and reaches *for* the skill by it. One well-chosen word does two jobs — execution
anchor and invocation handle — in a fraction of the tokens a paragraph of restatement spends.

**Evidence (source).** From the `writing-great-skills` reference in `mattpocock/skills` (MIT).
SeeD's own strongest specs already do this implicitly — the data-engineer's *count-mutate-
verify*, the infra-architect's *restore-first-diagnose-second*, the saga's *compensation-
before-effect*. Naming the technique makes it repeatable instead of accidental.

**How to apply.**
- When authoring a skill or profile, find the one word/phrase that names its defining move and
  put it where both the executor and the router will see it (the `core/prompt.md` and the
  one-line description).
- Hunt restatements a single leading word could retire — every sentence that re-explains the
  anchor is [[skill-failure-modes|sediment]].
- Prefer words the model already knows over coined jargon; a leading word only pays off if the
  pretraining already gives it meaning.

**Valid at.** 2026-07-07.
