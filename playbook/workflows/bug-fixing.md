# Workflow: Fixing a bug

Requires: [core principles](../core/00-core-principles.md)

## When to use
Something produces an error, a wrong result, a crash or an intermittent failure, and the cause must be found and fixed.

## Inspect first
- The exact error message, stack trace and conditions reported
- `git status` and recent commits touching the area
- The failing test or the steps to reproduce
- Versions and configuration of the environment where it fails

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [debugging](../../skills/engineering/debugging/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [observability-and-incident-response](../../skills/delivery/observability-and-incident-response/SKILL.md) | The bug appears only in production or an environment you cannot reproduce locally |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | You are asked to commit the fix |

## Steps
1. Reproduce the bug and record the minimal steps or a failing test.
2. Collect evidence (logs, trace, recent changes) without changing behavior.
3. Narrow the location by bisecting layers and history.
4. State a specific hypothesis; test it with an experiment; repeat until the root cause is proven.
5. Fix the root cause with the smallest change; do not suppress the error.
6. Add a regression test that fails before the fix and passes after.
7. Run the original reproduction, the related tests, and the full suite.
8. Search for the same defect pattern elsewhere and report it.

## Decisions
| Situation | Do this |
| --- | --- |
| Cannot reproduce | Report what was tried and what evidence is needed; do not ship a speculative fix as proven |
| Fix needs a risky change | Apply a narrow fix now; propose the larger change separately |
| Several possible causes | Test the cheapest first; keep notes on the others |

## Artifacts
- Root cause statement
- Fix and regression test
- Bug report record if useful

## Verify
- Reproduction no longer fails
- Regression test fails without the fix
- Full relevant suite passes; pre-existing failures are listed as such

## If verification fails
1. Fix does not remove the symptom: your hypothesis was wrong; revert the change and return to evidence gathering.
2. New failures appear: undo the fix and find what coupling you missed.

## Final report
- Root cause and evidence
- The change
- Regression test and commands run with results
- Remaining risk; similar code found

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [incident-response](incident-response.md): when the bug is a live outage
- [pull-request](pull-request.md): to submit the fix
