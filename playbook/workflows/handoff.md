# Workflow: Handing off work

Requires: [core principles](../core/00-core-principles.md)

## When to use
Ending a session with unfinished work, or passing work to another engineer or model.

## Inspect first
- `git status` and `git diff` to see the exact state of the working tree
- Your progress record and plan
- Failing tests and known problems

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [documentation-and-handoff](../../skills/delivery/documentation-and-handoff/SKILL.md) | Always |
| [development-operating-rules](../../skills/engineering/development-operating-rules/SKILL.md) | Always |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | Uncommitted or unpushed work must be described or preserved |

## Steps
1. Stop at a safe state: builds, or clearly marked as not building; no half-applied migrations or renames.
2. List what is done, in progress and not started.
3. List relevant files with their role and what changed.
4. Record decisions and the reasons for them.
5. Record tests run with results, and known failures with error text and suspected causes.
6. List remaining work in order, with exact commands for the first actions.
7. State what was not verified, risks and open questions.
8. Use the project handoff template.

## Decisions
| Situation | Do this |
| --- | --- |
| Work cannot be left building | Say so at the top of the handoff and explain how to restore a working state |
| Unsure about the state of something | Mark it unverified instead of guessing |

## Artifacts
- Completed handoff document

## Verify
- A reader with no context could continue from the document alone
- Commands and paths in it were checked
- Facts and assumptions are labeled

## If verification fails
1. You cannot recall the state: re-inspect with `git status`, tests and file reads before writing.

## Final report
- Link or path to the handoff
- The single most important next action

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [existing-project](existing-project.md): for whoever picks it up
