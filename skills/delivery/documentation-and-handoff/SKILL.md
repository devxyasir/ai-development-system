---
name: documentation-and-handoff
description: "Writes and maintains project documentation and handoffs: README and quick start, setup and configuration references, architecture notes, API docs, runbooks, troubleshooting, release notes, migration guides, contributor guidance, and progress records for long tasks or handing work to another engineer or model. Use when documenting a project, updating docs after a change, or ending a session with unfinished work."
metadata:
  category: delivery
  version: "0.1.0"
  related: "architecture-decisions, ci-cd-and-deployment, development-operating-rules, git-and-github"
---

# Documentation and handoff

Documentation is part of the change. It should be accurate, findable, and short enough to be kept current. A handoff lets the next person continue without re-discovering anything.

## When to use
- Creating or updating a README, setup guide, API reference, runbook, release notes or migration guide.
- Ending work that is unfinished, or passing it to another engineer or model.

## Procedure: project documentation
1. **Identify the reader and their task** (new contributor installing, user calling the API, operator handling an alert). Write for that task.
2. **README essentials:** what it is and who it is for, a quick start that works from a clean machine, how to configure, how to run tests, project layout, how to contribute, where to get help, and license information as chosen by the maintainer.
3. **Verify every command and path** by running it or by checking it against the files; copy output rather than recalling it. Remove or fix anything you could not verify.
4. **Reference docs:** configuration options (name, type, default, effect), API reference generated from the contract where possible, error codes.
5. **Architecture docs:** a short overview with a diagram or list of modules, data flow, decisions (link to decision records), and what not to change lightly.
6. **Runbooks:** for each alert or routine operation: symptoms, checks, commands, escalation, rollback; written to be followed under stress.
7. **Release notes and migration guides:** what changed for users, what they must do, in plain language; breaking changes first.
8. **Keep docs near the code** and update them in the same change; delete outdated pages instead of letting them mislead.

## Procedure: handoff
1. Stop at a safe state: code builds or is clearly marked broken; uncommitted work is described; no half-applied migrations.
2. Fill the [project handoff template](templates/project-handoff.md): goal, current state, relevant files, decisions and reasons, changes done, tests run and results, known failures, remaining work in order, next actions with exact commands, risks, and open questions.
3. Be precise: file paths, command lines, error messages, version numbers; separate verified facts from assumptions.
4. State what you did not verify.

## Decision rules
| Situation | Do this |
| --- | --- |
| Docs and code disagree | Check the code's behavior, fix the docs (or file a bug if the code is wrong) |
| Information changes often | Generate it from the source instead of writing it by hand |
| A step cannot be verified now | Mark it clearly as unverified |
| Long task across sessions | Keep a short progress record updated at each milestone |

## Common mistakes
- Quick starts that no one has run.
- Duplicating the same information across many files.
- Documenting what the code does line by line instead of why and how to use it.
- Handoffs that say "almost done" with no state or next steps.

## Verification
- Follow the quick start in a clean environment (or state that you could not).
- Every link and command in changed docs was checked.
- A reader with no context could continue from the handoff alone: ask yourself whether the next action is obvious.

## Deliverables
Updated documentation, runbooks as needed, handoff document.

## References
- [Project handoff template](templates/project-handoff.md)
