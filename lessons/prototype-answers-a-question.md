# Lesson — a prototype is throwaway code that answers a named question

**Statement.** When "how should it behave?" or "how should it look?" is the open question,
raise the fidelity of the discussion with a **prototype**: cheap, rough, concrete code built
to be reacted to — and the question decides the shape. Logic/state questions → a tiny
interactive terminal app that pushes the state machine through cases hard to reason about on
paper. Look/feel questions → several *radically different* variations, switchable in place.
Name the question before writing a line; a prototype without one is just unshipped code.

**Evidence (source).** Adapted from `mattpocock/skills` v1.1 `prototype`. Discussions about
behaviour stall at the fidelity of prose; a runnable artifact converts opinion-trading into
reaction, which is faster and truer. The failure the rules prevent: prototypes quietly
becoming production code because they lived in the wrong place with the wrong name.

**How to apply.** Rules that keep it honest: **throwaway from day one and named as such**
(placed near where the real code will live, labeled so no reader mistakes it); **one command
to run**; **no persistence** (state in memory — persistence is usually what's being checked,
not a dependency); **skip the polish** (no tests, no error handling beyond runnable, no
abstractions); **surface the full state** after every action so the human sees what changed.
When done, **capture the verdict, discard the code**: fold the validated decision into real
work, park the prototype out of the main line as a primary source, and record the question it
settled. The main line keeps only the decision. Inherently human-in-the-loop: the human's
reaction *is* the answer.

**Valid at.** 2026-07-10.
