---
name: github-operator
description: Issues/comments/PRs on a hosted repo (create, comment, close, read). One action per call; creations are visible immediately.
---

Use this skill to move findings and changes into the team's collaboration flow.

- Search first (`list-issues`) before `create-issue` — duplicates cost reviewer attention.
- Write issue bodies with evidence: what, where, how to reproduce, what you already checked.
- A PR needs a pushed branch (`git-vcs-operator` handles that, with its own approval);
  `create-pr` only frames it for review.
- To undo a creation, `close-issue` with a comment saying why — never pretend it didn't
  happen.
