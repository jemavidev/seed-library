# Lesson — the smell baseline: twelve names that review code by themselves

**Statement.** Code review carries a fixed baseline of named smells (Fowler, *Refactoring*
ch. 3) that applies even when a repo documents no standards. The names are so deep in model
priors that *naming* the smell is the whole mechanism — a reviewer told "watch for Feature
Envy" reliably says "this is Feature Envy" and reaches for the known fix. Two rules bind the
baseline: a **documented repo standard always overrides** it, and every smell is a labeled
**judgement call** ("possible Data Clumps"), never a hard violation; skip anything tooling
already enforces.

**Evidence (source).** Adapted from `mattpocock/skills` v1.1 `code-review`, reported as
"outrageously useful… and really cheap to add" after weeks of use: ~10 lines of names recruit
an entire well-cited book the model already knows. The baseline, each *what → fix*:
**Mysterious Name** (name hides intent → rename; no honest name = murky design) ·
**Duplicated Code** (same shape twice → extract) · **Feature Envy** (method lives off another
object's data → move it there) · **Data Clumps** (same fields travel together → bundle a
type) · **Primitive Obsession** (string standing in for a concept → small type) · **Repeated
Switches** (same cascade recurs → polymorphism or one shared map) · **Shotgun Surgery** (one
change, scattered edits → gather) · **Divergent Change** (one module, unrelated reasons →
split) · **Speculative Generality** (hooks for needs nobody has → delete) · **Message
Chains** (`a.b().c().d()` → hide the walk) · **Middle Man** (mostly delegates → cut it) ·
**Refused Bequest** (implementer ignores its inheritance → compose).

**How to apply.** Reviewers carry the baseline alongside repo standards. Run review on two
separate axes — **standards** (does the diff follow how code should be written here?) and
**spec** (does it faithfully implement what was asked?) — in isolated contexts, reported side
by side and never merged or reranked: a change can pass one axis and fail the other, and a
single ranking lets one axis mask the other.

**Valid at.** 2026-07-10.
