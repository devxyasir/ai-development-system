# Workflow: Implementing a feature

Requires: [core principles](../core/00-core-principles.md)

## When to use
Adding or changing user-visible or API-visible behavior in an existing project.

## Inspect first
- The most similar existing feature, and how it is structured and tested
- Files and modules the feature will touch, and their callers
- Existing tests and fixtures for the area
- Project conventions (see the existing-project workflow if unfamiliar)

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [requirements-and-research](../../skills/engineering/requirements-and-research/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [product-design](../../skills/design/product-design/SKILL.md) | The feature adds or changes a user interface flow |
| [backend-api-design](../../skills/engineering/backend-api-design/SKILL.md) | The feature adds or changes an API or service |
| [database-engineering](../../skills/engineering/database-engineering/SKILL.md) | The feature changes stored data |
| [security-review](../../skills/engineering/security-review/SKILL.md) | The feature handles authentication, permissions, user input, files or personal data |
| [frontend-testing](../../skills/frontend/frontend-testing/SKILL.md) | The feature has user interface behavior |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | You are asked to commit or open a pull request |
| [documentation-and-handoff](../../skills/delivery/documentation-and-handoff/SKILL.md) | Documentation or a changelog must change |

## Steps
1. State the goal and write acceptance criteria that a tester could check.
2. Inspect the closest existing feature and copy its structure.
3. Make a plan sized to the task (one line, a short plan, or a full plan).
4. Implement in thin slices, each leaving the project working; run the relevant tests after each slice.
5. Handle failure paths: invalid input, permissions, empty data, dependency failure.
6. Add tests for new behavior, including at least one failure path.
7. Run the full checks (tests, lint, type check, build).
8. Update documentation and configuration notes.
9. Run the quality gate and write the report.

## Decisions
| Situation | Do this |
| --- | --- |
| Feature requires a new dependency | Check the project for an existing solution first; justify the new one (see dependency checks in security-review) |
| Requirements are ambiguous | Ask one question only if the answer changes the design materially; otherwise assume and state it |
| The change grows large | Split it into separately verifiable steps or pull requests |

## Artifacts
- Code and tests
- Updated documentation
- Notes on assumptions and limits

## Verify
- Each acceptance criterion is demonstrated (test or manual run)
- Full checks pass; no existing tests were weakened
- For UI: rendered and inspected, or explicitly stated as not rendered

## If verification fails
1. A test fails: read the failure, find the cause, fix the cause; if it is a pre-existing failure, report it.
2. Cannot meet a criterion: report which and why rather than redefining the criterion.

## Final report
- What the feature does and where it lives
- Commands run and results
- Acceptance criteria with status
- Not verified; risks; follow-ups

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [pull-request](pull-request.md): to prepare the change for review
- [ui-implementation](ui-implementation.md): for the interface part
