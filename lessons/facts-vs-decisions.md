# Lesson — facts are the agent's to find; decisions are the human's to make

**Statement.** In any human-in-the-loop exchange, split every open point into two kinds:
**facts** — answerable by exploring the codebase, the docs, or the data — which the agent
looks up itself and never asks; and **decisions** — genuine choices with trade-offs — which
are put to the human one at a time, each with a recommended answer, and are never answered by
the agent on the human's behalf. Nothing is enacted until the human confirms shared
understanding.

**Evidence (source).** `mattpocock/skills` v1.1 changelog: grilling sessions ran without this
distinction and agents were observed *grilling themselves* — answering their own questions by
exploring the codebase and proceeding — or dumping bewildering multi-question forms, or
skipping the confirmation and going straight to implementation. Two sentences separating
facts from decisions plus an explicit do-not-enact gate resolved all three failure reports.

**How to apply.** Interrupt stances (`confirm`, `expert-review`) trigger on *decisions*,
never on facts — an approval request whose answer is discoverable is noise that trains humans
to click yes. Interviewing profiles ask one question per turn, attach a recommendation, and
end on an explicit confirmation gate before any plan is enacted. The tell that the rule is
broken: a transcript where the agent poses a question and the next voice answering it is its
own.

**Valid at.** 2026-07-10.
