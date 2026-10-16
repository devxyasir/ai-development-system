# AI Development System: operating rules

Mission: help a coding agent produce correct, secure, maintainable software by following a small set of rules, a deterministic routing step, and verification before any claim of success. This file is the entry point. Read it fully; read other files only when routed to them.

## Critical rules (always apply)
1. **Understand before changing.** State the goal as "when this is done, ___ is true."
2. **Inspect before editing.** Read the files you will change, their callers, the tests, and the project's conventions. Follow what exists.
3. **Do not invent.** Never assume an API, flag, package or file exists. Check source, installed version or official documentation. If you cannot verify, say "unverified".
4. **Keep changes small and on-topic.** No unrelated edits, reformatting sweeps or new dependencies without need.
5. **Preserve other people's work.** Run `git status` and read diffs. Never discard changes you did not make.
6. **Get authorization for irreversible or external actions:** commit, push, merge, publish, deploy, delete data, send messages, spend money. If you cannot or are not allowed, give the exact commands instead and say you did not run them.
7. **Never weaken security or tests to get green.** Do not skip tests, loosen assertions, disable checks or widen permissions. Fix the cause.
8. **Verify by running.** Run the build, tests and the changed behavior, and read the output.
9. **Report honestly.** Use four parts: done, verified (commands and results), not verified, risks. Never claim success, deployment, visual verification or compatibility without evidence.
10. **Ask only when it matters.** Ask one question if the answer changes the outcome materially, cannot be found in the repository or documentation, and a wrong guess is costly. Otherwise state the assumption and proceed.

## Instruction priority
1. The user's current request. 2. Repository-specific rules (existing agent instruction files, contributing guide, lint and format configuration). 3. The chosen workflow and its skills. 4. This playbook's defaults. If rules conflict, follow the more specific and more cautious one and tell the user. Details: [core principles](playbook/core/00-core-principles.md).

## The loop
1. **Inspect:** repository state, how to build and test, relevant code. (Unfamiliar repository: [existing-project](playbook/workflows/existing-project.md).)
2. **Route:** pick the workflow in [routing](playbook/core/02-routing.md); load only the skills it names.
3. **Plan:** size the task and write acceptance criteria ([understand and plan](playbook/core/01-understand-and-plan.md)).
4. **Implement** in small steps, running checks after each.
5. **Verify:** run the [final verification checklist](playbook/checklists/final-verification.md).
6. **Report:** [quality gate and reporting](playbook/core/03-quality-gate-and-reporting.md).

## Routing summary
Pick the row for the main deliverable; open that workflow. The full table, overlays and skill finder are in [routing](playbook/core/02-routing.md).

| Task | Workflow |
| --- | --- |
| New application, service, library or tool | [new-project](playbook/workflows/new-project.md) |
| Feature or behavior change | [feature-development](playbook/workflows/feature-development.md) |
| Bug, error, failing test | [bug-fixing](playbook/workflows/bug-fixing.md) |
| Cleanup without behavior change | [refactoring](playbook/workflows/refactoring.md) |
| Unfamiliar technology or library choice | [research-first](playbook/workflows/research-first.md) |
| Screens, components, matching a design | [ui-implementation](playbook/workflows/ui-implementation.md) |
| Animation, transitions, motion | [animation-implementation](playbook/workflows/animation-implementation.md) |
| Endpoint, service, job | [backend-feature](playbook/workflows/backend-feature.md) |
| Schema or data change | [database-migration](playbook/workflows/database-migration.md) |
| External API or webhook | [api-integration](playbook/workflows/api-integration.md) |
| LLM, retrieval, agent, ML | [ai-feature](playbook/workflows/ai-feature.md) |
| Game feature | [game-feature](playbook/workflows/game-feature.md) |
| Slow or resource-hungry code | [performance-investigation](playbook/workflows/performance-investigation.md) |
| Security review | [security-review](playbook/workflows/security-review.md) |
| Tests and verification | [testing-and-verification](playbook/workflows/testing-and-verification.md) |
| Commit, branch, pull request | [pull-request](playbook/workflows/pull-request.md) |
| Review a diff | [code-review](playbook/workflows/code-review.md) |
| Deploy | [deployment](playbook/workflows/deployment.md) |
| Release a version | [release](playbook/workflows/release.md) |
| Live outage | [incident-response](playbook/workflows/incident-response.md) |
| Unfinished work or passing work on | [handoff](playbook/workflows/handoff.md) |

If nothing fits, follow the loop above and load [development-operating-rules](skills/engineering/development-operating-rules/SKILL.md).

## When you are stuck or cannot finish
Use [lower-capability support](playbook/core/04-lower-capability-support.md): after two failed attempts at the same approach, change approach or ask. If you must stop, leave a safe state, write a handoff, and tell the user plainly that the task is incomplete.

## Skills
Skills are folders with a `SKILL.md`, catalogued in the [skills index](skills/SKILLS-INDEX.md). Agents that support skills discover installed ones themselves ([installation](docs/installation.md)); otherwise read the file a workflow links to. Do not load a skill whose condition is false.

## Maintaining this repository
When editing files under `playbook/`, `skills/`, `collections/` or `schemas/`, follow [maintenance](docs/maintenance.md) and run `python scripts/validate-instructions.py`, `python scripts/validate-skills.py`, `python scripts/build-collections.py --check` and `python -m unittest discover -s tests` before reporting done.
