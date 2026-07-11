# Lesson — no red-capable loop, no hypothesis

**Statement.** Diagnosing a hard bug starts by building a **feedback loop** — one command,
already run at least once, that is *red-capable* (goes red on this exact bug and green once
fixed, asserting the user's exact symptom, not "didn't crash"), *deterministic*, *fast*
(seconds), and *agent-runnable*. Until that command exists, no hypothesizing: reading code to
build a theory first is the exact failure the discipline prevents.

**Evidence (source).** Adapted from `mattpocock/skills` v1.1 `diagnosing-bugs`. The loop is
90% of the fix — bisection, hypothesis-testing, and instrumentation all just *consume* it.
Loop-construction options, in rough order: failing test, HTTP script, CLI + fixture diff,
headless browser, replayed trace, throwaway harness, property/fuzz loop, bisection harness,
differential run. Non-deterministic bugs: raise the reproduction rate (loop the trigger,
stress, narrow timing) until debuggable — a 50% flake is workable, 1% is not.

**How to apply.** After the loop goes red: **minimise** the repro until every remaining
element is load-bearing; only then generate 3–5 *falsifiable* hypotheses ("if X is the cause,
changing Y makes it disappear") and rank them before testing any; instrument one variable at
a time, tagging every probe with a unique greppable prefix so cleanup is one grep. Fix behind
a regression test at a **correct seam** — one that exercises the real bug pattern at its call
site; if no correct seam exists, that absence is itself a finding to record. When the loop
genuinely cannot be built, say so explicitly and ask for a captured artifact — never proceed
on vibes.

**Valid at.** 2026-07-10.
