# Lesson — rejections are knowledge: a proposing system remembers its "no"

**Statement.** Any system that *proposes* — improvement suggestions, intake queues, triage —
must keep a **rejection log**: one line per rejected proposal (gist, source, date, reason),
consulted *before* any new proposal is surfaced. A rejection without a recorded reason is not
a decision, it's a postponement: the idea will return wearing different words, and the human
pays the evaluation cost again each time.

**Evidence (source).** Adapted from `mattpocock/skills` v1.1 `triage` and its out-of-scope
knowledge base: rejected enhancement requests are written to a small KB with the reasoning,
and every new triage begins by reading it — turning "we said no" from tribal memory into a
checkable artifact. The complementary rule: *built* things don't go in the rejection log
(point to the implementation instead) — the log holds only conscious refusals.

**How to apply.** Every proposal surface pairs with a rejection log and a gate: check the log
by *concept* (not wording) before proposing; on rejection, require the reason before the item
may close. Self-improvement digests consult the log so declined suggestions stay declined
until the human reopens them deliberately. A rejection can cite scope ("past the
destination"), redundancy ("exists as X"), or judgement ("cost exceeds value because…") — any
is fine; *absent* is not. Prune honestly: if a logged reason stops being true, the entry is
invalidated with a date, not silently deleted.

**Valid at.** 2026-07-10.
