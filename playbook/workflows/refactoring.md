# Workflow: Refactoring

Requires: [core principles](../core/00-core-principles.md)

## When to use
Restructuring code without changing its behavior: cleanup, extraction, renaming, moving modules, preparing for a feature.

## Inspect first
- The code in scope, its callers and its tests
- Public interfaces consumed elsewhere (APIs, file formats, schemas, CLI flags)
- Baseline: run the tests and record results

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [refactoring](../../skills/engineering/refactoring/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [code-review](../../skills/engineering/code-review/SKILL.md) | Before finishing, or when review is requested |
| [architecture-decisions](../../skills/engineering/architecture-decisions/SKILL.md) | The change moves module boundaries or dependency direction |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | You are asked to commit in steps |

## Steps
1. State the goal and the boundary of the refactor.
2. Check coverage of the area; add characterization tests if thin.
3. Plan small steps that each keep the code working.
4. Perform one step; run the tests; if they fail, undo that step.
5. Keep behavior changes, dependency upgrades and formatting sweeps out of this work.
6. Search for every usage before moving, renaming or deleting code.
7. Re-run tests, lint, type check and build; read the full diff for accidental behavior changes.

## Decisions
| Situation | Do this |
| --- | --- |
| No tests and cannot add any | Limit to mechanical, tool-assisted changes and state the risk |
| Public interface must change | Treat as a separate, announced change with a migration path |
| Tempted to fix a bug you noticed | Note it; fix it separately |

## Artifacts
- Refactored code in reviewable steps
- Characterization tests
- Note on what was left alone

## Verify
- Tests that passed before still pass
- No remaining references to removed or renamed symbols
- Diff contains structural changes only

## If verification fails
1. Tests fail after a step: revert the step and take a smaller one.
2. A test depended on old structure: update it only if behavior is unchanged, and say so.

## Final report
- Goal and what changed structurally
- Tests run and results
- Behavior-affecting changes (should be none)
- What was deliberately not changed

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [code-review](code-review.md): to review the result
