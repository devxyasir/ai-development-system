# Pull request checklist

## Before opening
- [ ] Branch is up to date with the base and conflicts are resolved.
- [ ] `git diff <base>...HEAD` reviewed line by line; no debug code, stray files, secrets or unrelated formatting.
- [ ] Build, lint, type check and tests pass locally; commands noted.
- [ ] New behavior has tests, including a failure path.
- [ ] Documentation, changelog and configuration updated where needed.
- [ ] Database migrations included, reversible or with a forward-fix plan, and tested.
- [ ] Breaking changes called out with migration steps.

## Description template
```
## What
<summary of the change>

## Why
<problem, issue link>

## How tested
- <command>: <result>
- Manual checks: <steps>

## Risks and rollout
<what could break, feature flags, rollback>

## Screenshots or recordings (UI changes)
<attach>

## Notes for reviewers
<where to look first, known limitations>
```

## Size and focus
- One purpose per pull request. If it is large, split it (preparatory refactor, then the feature).
- Mark work in progress as a draft.

## Review etiquette
- Respond to every comment; resolve only when addressed.
- Re-run checks after changes; do not force-push over reviewed commits unless the team's convention allows it.

## Merge
- Required checks green; approvals in place; merge strategy per team convention (merge commit, squash or rebase).
- After merging: delete the branch, verify the deployment pipeline, watch for alerts if the change is risky.
