# skill.sdlc.git-vcs-operator — spec

## What it does
Runs version-control operations on the project repository: inspect status, create/switch
branches, commit staged work, push a ref to the remote, or revert a commit. One action per
call, always returning the resulting ref and raw output.

## When to use / when not
- **Use** to checkpoint reviewed work into history (`commit`), publish it (`push`), or undo a
  bad commit (`revert`).
- **Don't use** for repository surgery (rebase, force-push, history rewrite) — deliberately out
  of this interface; those are expert-review operations that need their own spec.
- `push` is the only action that leaves the machine: treat it as an external effect and expect
  the runtime to require confirmation.

## Inputs / outputs
- In: `repo_path`, `action` (`status|branch|checkout|commit|push|revert`), optional `branch`,
  optional `commit_message` (required for `commit`), optional `ref` (required for `revert`).
- Out: `{ action, ref, output }` — `ref` is the branch/commit the repo points at afterwards.

## Worked example
`{ "repo_path": ".", "action": "commit", "branch": null, "commit_message": "fix: null check",
"ref": null }` → `{ "action": "commit", "ref": "a1b2c3d", "output": "1 file changed" }`.

## Failure modes
- `not_a_repo` (not retryable) · `nothing_to_commit` (not retryable; not an error to loop on)
- `merge_conflict` (not retryable automatically — surface to a human or a resolver flow)
- `push_rejected` (retryable once after fetch; never force)
- `auth_failed` (not retryable; credential reference problem, never inline a token to fix it)

## Reversibility
Every mutating action has a same-tool inverse: `commit` → `revert`; `branch` → delete-branch
(via `checkout` back + branch cleanup); a pushed ref is compensated by pushing the revert
commit. This inverse mapping is what the compensation contract of this tool relies on.
