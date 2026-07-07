# skill.saas.github-operator — spec

## What it does
Operates on a hosted code-collaboration repository (issues, comments, pull requests): read
operations plus create/comment/close. One action per call. The hosting provider is a binding;
the interface models the common issue/PR vocabulary.

## When to use / when not
- **Use** to file issues from findings, open pull requests for pushed branches, comment
  results back to a thread, or read issue/PR state.
- **Don't use** for git operations themselves (`git-vcs-operator` owns clone/commit/push) or
  for repo administration (settings, permissions — deliberately out of scope).

## Inputs / outputs
- In: `repo` (`owner/name`), `action`
  (`get-issue|list-issues|create-issue|comment|create-pr|close-issue`), and the fields the
  action needs: `title`, `body`, `number`, `base`, `head`.
- Out: `{ action, number, url, state }`.

## Worked example
`{ "repo": "acme/api", "action": "create-issue", "title": "p95 regression after 1.4.2",
"body": "Evidence: …", "number": null, "base": null, "head": null }` →
`{ "action": "create-issue", "number": 118, "url": "https://…/issues/118", "state": "open" }`.

## Failure modes
- `auth_failed` (not retryable) · `not_found` — repo/number (not retryable)
- `validation_failed` — e.g. PR with no diff between base and head (not retryable)
- `rate_limited` (retryable after window).

## Constraints
Everything created is public to the repo's audience the moment it exists: bodies pass
redaction first. Compensation is `close-issue` (or closing the PR) with a comment linking the
reason — created artifacts are closed, never deleted, so the audit trail survives.
