---
name: git-and-github
description: "Safe Git and GitHub collaboration: inspecting repository state, branching, atomic commits, reviewing staged diffs, resolving merge conflicts, pull requests and descriptions, protected branches, CI checks, secret scanning, tags and changelogs, and recovering from mistakes without destroying work. Use when committing, branching, merging, opening or reviewing pull requests, or when Git state looks wrong."
metadata:
  category: delivery
  version: "0.1.0"
  related: "code-review, ci-cd-and-deployment, security-review, development-operating-rules"
---

# Git and GitHub

Version control is the safety net. Protect other people's work, keep history understandable, and never take external or irreversible actions without authorization.

## When to use
- Committing, branching, merging, rebasing, resolving conflicts, preparing or reviewing pull requests, tagging releases, recovering from mistakes.

## Rules that always apply
1. Run `git status` and `git diff` before any commit; know what is staged and what is not.
2. Do not commit, push, merge, publish or force anything unless the user asked or authorized it. Provide the commands instead when tools or permission are missing, and never claim an action happened that did not.
3. Never run destructive commands (`git reset --hard`, `git clean -fd`, `git checkout -- .`, `git push --force`, `git branch -D`, rewriting shared history) without explicit authorization; they can destroy someone's uncommitted or unpushed work.
4. Preserve unrelated changes in the working tree: stage only the files and hunks that belong to the task (`git add <paths>` or `git add -p`), not `git add -A` blindly.
5. Never commit secrets, credentials, large generated files, or personal data. Check `.gitignore` and the staged diff.

## Procedure: commit
1. `git status`, then `git diff` (unstaged) and `git diff --staged` (staged) to review every line.
2. Stage only related changes. Run the project's checks (tests, lint, build).
3. Write a message: a short imperative summary (about 50-72 characters), a blank line, then a body explaining why when it is not obvious. Follow the project's convention if one exists (for example Conventional Commits).
4. One logical change per commit; separate refactors, formatting and features.
5. Inspect the result with `git show --stat HEAD`.

## Procedure: branch and pull request
1. Branch from the up-to-date default branch with a descriptive name (`fix/login-redirect`, `feature/export-csv`).
2. Keep the branch small and short-lived; sync with the base regularly.
3. Before opening a pull request: review your own diff against the base, run all checks, update tests and docs.
4. Write the description: what and why, how it was tested (commands and results), risks and rollout, linked issues, screenshots for UI changes. Use the [pull request checklist](references/pull-request-checklist.md).
5. Address review comments with new commits (or fixups if the team squashes), and reply to each comment.
6. Merge only when required checks pass and approvals are in place, using the team's merge strategy.

## Procedure: merge conflicts
1. `git status` to list conflicted files; open each and read both sides and the base (`git diff --base` or a merge tool).
2. Decide the intended behavior, combine both changes correctly (do not just pick a side), remove conflict markers.
3. Build and run tests; `git add` the resolved files; continue the merge or rebase.
4. If lost, abort (`git merge --abort` or `git rebase --abort`) and start again.

## Recovery
| Situation | Do this |
| --- | --- |
| Committed to the wrong branch | Create a branch at the current commit, then move the original branch pointer (ask before changing shared branches) |
| Need to undo a pushed commit | `git revert <commit>` (adds a new commit) rather than rewriting history |
| Lost commits after a reset | `git reflog` shows recent positions; create a branch at the lost commit |
| Accidentally staged secrets | Unstage; if committed or pushed, rotate the secret and clean history only with authorization |
| Rebase needed on a private branch | Allowed on unshared branches; if you must force-push use `--force-with-lease` after authorization |

## GitHub features to use when available
- Protected default branch, required reviews and status checks; CODEOWNERS for review routing; secret scanning and push protection; dependency alerts and automated updates; release tags with notes; issue and pull request templates. Use available GitHub tools according to their documented capabilities; otherwise provide commands or instructions.

## Common mistakes
- `git add -A` sweeping in unrelated or secret files.
- Force-pushing shared branches.
- Giant commits mixing refactors and features.
- Resolving conflicts by taking one side without understanding it.
- Reporting "pushed" or "merged" when no such command ran.

## Verification
- Final `git status` and `git log --oneline -n 5` match what you report.
- Staged diff reviewed; no secrets or unrelated files.
- Checks run before the commit or pull request; results reported.
- State any action not performed because it required authorization.

## Deliverables
Clean commits or the exact commands to make them, a pull request description, notes on checks and risks.

## References
- [Pull request checklist](references/pull-request-checklist.md)
