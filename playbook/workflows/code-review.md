# Workflow: Reviewing code

Requires: [core principles](../core/00-core-principles.md)

## When to use
Reviewing someone else's diff or pull request, or doing a final review of your own work.

## Inspect first
- The description, linked issue and acceptance criteria
- The full diff against the base branch
- The code around each change: callers, tests, configuration

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [code-review](../../skills/engineering/code-review/SKILL.md) | Always |
| [security-review](../../skills/engineering/security-review/SKILL.md) | The change touches authentication, input handling, files, secrets or personal data |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Tests look thin or missing |
| [performance-analysis](../../skills/engineering/performance-analysis/SKILL.md) | The change affects hot paths, queries or large data |
| [database-engineering](../../skills/engineering/database-engineering/SKILL.md) | The change includes migrations or queries |
| [visual-qa](../../skills/frontend/visual-qa/SKILL.md) | The change is visual and can be rendered |

## Steps
1. Understand the intent; note if it is unclear.
2. Read the whole diff and the surrounding code.
3. Run build, tests and lint; run the changed behavior if possible.
4. Check correctness, security, design fit, tests, performance, maintainability, and delivery concerns in that order.
5. Write findings with severity, location, reason and a suggested fix.
6. State what was run and what was only read.
7. Give a verdict.

## Decisions
| Situation | Do this |
| --- | --- |
| Style disagreement not in project rules | Mark as a nit; do not block |
| Change is too large to review well | Ask to split or state what you did not cover |
| Unfamiliar area | State the limit of your review |

## Artifacts
- Review comments by severity
- Verdict

## Verify
- Every Blocker and Major has a reason and a fix suggestion
- Commands run are listed
- The verdict matches the findings

## If verification fails
1. You cannot run the code: say so and mark behavior findings as reasoned only.

## Final report
- Verdict
- Blockers and Majors
- What was run and not reviewed

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [pull-request](pull-request.md): when preparing your own change
