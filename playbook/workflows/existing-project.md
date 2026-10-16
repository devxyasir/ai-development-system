# Workflow: Working in an existing or unfamiliar repository

Requires: [core principles](../core/00-core-principles.md)

## When to use
First time working in a repository or an unfamiliar part of one, before changing anything.

## Inspect first
- README, contributing guide, existing CLAUDE.md or AGENTS.md and other agent instructions
- Manifests and lockfiles (package.json, pyproject.toml, go.mod, Cargo.toml, pom.xml and similar)
- Entry points, directory layout, configuration and environment files
- Test setup and CI configuration; how to build, run and test
- Recent history: `git log --oneline -n 20`, and which files change most
- Current working tree: `git status`

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [architecture-decisions](../../skills/engineering/architecture-decisions/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [requirements-and-research](../../skills/engineering/requirements-and-research/SKILL.md) | The repository uses a technology you do not know |
| [documentation-and-handoff](../../skills/delivery/documentation-and-handoff/SKILL.md) | You are asked to document what you found |

## Steps
1. Read the project instructions and preserve any rules in them (they outrank this playbook).
2. Run `git status` and note uncommitted changes you must not disturb.
3. Find how to install, build, run and test; run the tests and record the baseline, including tests that already fail.
4. Map the structure: modules, entry points, data flow of one representative request or command, and external dependencies.
5. Identify conventions: naming, error handling, testing style, formatting and lint rules.
6. Locate the code relevant to the task and its callers and tests.
7. Write a half-page map of what you learned (facts only) and any questions that block you.
8. Proceed to the workflow for the actual task.

## Decisions
| Situation | Do this |
| --- | --- |
| Existing conventions differ from your preference | Follow the existing conventions |
| Tests already fail before you start | Record them as pre-existing; do not fix them unless asked |
| No documentation | Infer from code and tests, label inferences as such |

## Artifacts
- Short codebase map
- Baseline test result
- List of conventions and open questions

## Verify
- You can state how to build, run and test the project, and you have done each
- Your map names the files relevant to the task
- You did not modify any file during exploration

## If verification fails
1. Cannot run the tests: report the exact error and what you tried (versions, missing services, environment variables).
2. Project instructions conflict with the task: tell the user and ask which to follow.

## Final report
- What the project is and how it is organized
- How to build, run and test, with the baseline result
- Conventions to follow
- Questions or risks found

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [feature-development](feature-development.md): to add a feature
- [bug-fixing](bug-fixing.md): to fix a bug
- [refactoring](refactoring.md): to restructure code
