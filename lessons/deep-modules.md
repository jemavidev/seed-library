# Lesson — deep modules: much behaviour behind a small interface

**Statement.** Design **deep modules** — a lot of behaviour behind a small interface, placed
at a clean seam, testable through that interface — and use one fixed vocabulary while doing
it: **module** (anything with an interface and an implementation, scale-agnostic), **interface**
(everything a caller must know: signature *plus* invariants, ordering, error modes, config,
performance), **seam** (where behaviour can be altered without editing in place — the
location of an interface), **adapter** (a concrete thing satisfying an interface at a seam —
a role, not a substance), **depth** (leverage at the interface: behaviour exercised per unit
of interface learned), **leverage** (what callers get from depth) and **locality** (what
maintainers get: change, bugs, and verification concentrate in one place).

**Evidence (source).** Adapted from `mattpocock/skills` v1.1 `codebase-design` (itself
distilling Ousterhout and Feathers). Deliberately rejects depth-as-lines-ratio — it rewards
padding the implementation; depth-as-leverage is the usable measure. Consistent vocabulary is
half the value: "component", "service", and "boundary" each drag in a different prior and
blur the discussion.

**How to apply.** Three principles do most of the work. **The deletion test**: imagine
deleting the module — if complexity vanishes it was a pass-through; if it reappears across N
callers it was earning its keep. **The interface is the test surface**: callers and tests
cross the same seam; wanting to test past the interface means the module is the wrong shape.
**One adapter means a hypothetical seam; two adapters means a real one**: don't introduce a
seam until something actually varies across it. For testability: accept dependencies rather
than creating them, return results rather than producing side effects, keep the surface
small. Builder and reviewer share this vocabulary so generated code and its review argue in
the same terms.

**Valid at.** 2026-07-10.
