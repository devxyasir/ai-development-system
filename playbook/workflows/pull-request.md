# Workflow: Preparing a pull request

Requires: [core principles](../core/00-core-principles.md)

## When to use
Preparing work for review: cleaning the change, writing the description, and making sure checks pass.

## Inspect first
- `git status`, `git diff` and `git log` against the base branch
- The project's contributing guide and pull request template
- CI checks required for merging

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | Always |
| [code-review](../../skills/engineering/code-review/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Tests are missing or incomplete |
| [documentation-and-handoff](../../skills/delivery/documentation-and-handoff/SKILL.md) | Documentation or a changelog must change |
| [ci-cd-and-deployment](../../skills/delivery/ci-cd-and-deployment/SKILL.md) | A CI failure must be investigated |

## Steps
1. Confirm the branch is current with the base and conflicts are resolved.
2. Review your own diff line by line; remove debug code, stray files and unrelated formatting.
3. Run build, lint, type check and tests; note the commands.
4. Make sure there are no secrets or large generated files staged.
5. Split mixed work into separate commits or pull requests.
6. Write the description using the pull request checklist.
7. Only commit, push or open the pull request if the user authorized it; otherwise give the exact commands and the description text.

## Decisions
| Situation | Do this |
| --- | --- |
| Change is large | Split into a preparatory refactor and the feature |
| Required check fails | Fix the cause; do not bypass or mark as optional |
| Not authorized to push | Provide commands; do not claim it was pushed |

## Artifacts
- Clean commits or the commands to create them
- Pull request description

## Verify
- `git diff <base>...HEAD` contains only intended changes
- All checks run locally and pass
- Description states how it was tested

## If verification fails
1. Checks fail: investigate with the debugging skill; do not skip them.
2. Conflicts: resolve by understanding both sides; rerun tests.

## Final report
- What the change does
- Checks run and results
- Actions taken versus actions left for the user
- Risks

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [code-review](code-review.md): for a thorough self-review
