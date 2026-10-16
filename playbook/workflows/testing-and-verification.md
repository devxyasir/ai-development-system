# Workflow: Writing and running tests

Requires: [core principles](../core/00-core-principles.md)

## When to use
Adding tests, choosing what to test, fixing flaky tests, or verifying a change before reporting it as done.

## Inspect first
- Test framework, commands, fixtures and conventions
- CI configuration (what runs, in what order)
- Existing coverage of the area; baseline results of the suite

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [frontend-testing](../../skills/frontend/frontend-testing/SKILL.md) | The change has user interface behavior |
| [visual-qa](../../skills/frontend/visual-qa/SKILL.md) | Rendered visual verification is needed |
| [accessibility-review](../../skills/design/accessibility-review/SKILL.md) | Accessibility claims are involved |
| [database-engineering](../../skills/engineering/database-engineering/SKILL.md) | Migration or query behavior must be tested |
| [ai-llm-engineering](../../skills/specialist/ai-llm-engineering/SKILL.md) | The behavior is model-driven and needs an evaluation set |

## Steps
1. Run the existing suite and record the baseline.
2. List the behaviors and risks of the change.
3. Choose the lowest test level that proves each behavior.
4. Write cases: normal, boundary, invalid, permissions, failures, repeats, concurrency where relevant.
5. Run the new tests; confirm they fail when the behavior is broken.
6. Run the full suite, lint, type check and build.
7. Fix flaky tests by finding the race or shared state; never add sleeps or disable them.

## Decisions
| Situation | Do this |
| --- | --- |
| Legacy code without tests | Add characterization tests around the part you will change |
| Coverage target requested | Use coverage to find untested branches; do not write meaningless tests to hit a number |
| Test is flaky | Reproduce in a loop; fix the cause |

## Artifacts
- Tests
- Commands and results record

## Verify
- Commands run and results recorded
- No tests skipped, disabled or weakened (or reported with reasons)
- New tests fail on a deliberate break

## If verification fails
1. Tests fail: read the failure, find the cause, fix the code or the test only if the test is wrong, and say which.
2. Environment prevents running tests: report exactly what is missing.

## Final report
- Commands run
- Passed, failed (and whether pre-existing), not run
- What the tests do not prove

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [pull-request](pull-request.md): to prepare for review
