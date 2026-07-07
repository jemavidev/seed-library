# Lessons — git-vcs-operator

No operational lessons yet (hand-seeded 2026-07-07). Design notes carried from practice:
history rewriting is excluded from the interface on purpose (revert-only undo keeps every
compensation append-only), and "one action per call" exists so approval flows can gate `push`
separately from `commit`.
