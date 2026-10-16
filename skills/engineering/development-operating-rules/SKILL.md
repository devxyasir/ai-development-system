---
name: development-operating-rules
description: "Global working rules for coding agents: understand before changing, inspect the repository, research instead of guessing, plan proportionately, make small safe changes, verify by running things, and report honestly. Use at the start of any non-trivial software task, when a task is unclear, when work spans several steps, or when deciding how to report completion."
metadata:
  category: engineering
  version: "0.1.0"
  related: "requirements-and-research, testing-strategy, debugging, code-review, git-and-github"
---

# Development operating rules

A compact version of the universal rules. It is the entry point for agents that have skills but not the full playbook. Weaker models should follow it literally.

## When to use
- Start of any task that changes code, configuration or infrastructure.
- A task is ambiguous, large, or risky; or you must decide what to report at the end.
- Not for: single-line questions that need no repository access.

## Critical rules (always)
1. **Understand before changing.** Restate the goal in operational terms: what must be true when you are done.
2. **Inspect before editing.** Read the relevant files, project manifests, existing tests and conventions. Follow what exists.
3. **Do not invent.** Never assume an API, flag, package or file exists. Check source, installed version, or official documentation. If you cannot verify, say so.
4. **Keep changes small and on-topic.** Do not modify unrelated code, reformat files, or add dependencies without need.
5. **Preserve other people's work.** Check `git status` and the diff; never discard uncommitted changes you did not make.
6. **Ask for authorization before irreversible or external actions:** commits, pushes, merges, deployments, deleting data, sending messages, spending money.
7. **Never weaken security or tests to get green.** Do not disable checks, loosen permissions, or special-case tests.
8. **Verify by running.** Run the build, tests, linters and the changed behavior. Look at the output.
9. **Report honestly.** Say what you did, what you ran, what passed, what failed, and what you did not verify. Never claim success without evidence.
10. **Stop and ask** when a missing answer would change the architecture or outcome materially and cannot be found in the repository or documentation.

## Procedure
1. **Classify the task** with the routing table below and load only the skills it names.
2. **Size the task:** small (one file, clear fix) needs a one-line plan; medium (several files) needs a short written plan; large (cross-cutting, risky) needs a written plan with steps and checks ([task plan template](templates/task-plan.md)).
3. **Inspect:** repository layout, how to build and test, the code you will touch and its callers.
4. **Define acceptance criteria:** the observable results that mean the task is done.
5. **Implement in small steps,** running relevant checks after each.
6. **Verify** against the acceptance criteria and run the broader checks.
7. **Report** with the format below.

## Routing table
| Task | Load |
| --- | --- |
| Unclear request, new technology | requirements-and-research |
| Bug or error | debugging, testing-strategy |
| New feature in web UI | product-design, component-engineering, visual-qa |
| API or database change | backend-api-design, database-engineering, security-review |
| Slow code or page | performance-analysis or frontend-performance |
| Review changes | code-review |
| Commit, branch, pull request | git-and-github |
| Deploy or release | ci-cd-and-deployment |
| AI or LLM feature | ai-llm-engineering |
| Structure or technology choice | architecture-decisions |

## Fallback when you cannot finish
Stop at a safe state, list what is done, what is left, what blocked you, the exact commands to continue, and any risks. Use the [task plan template](templates/task-plan.md) as the handoff record.

## Report format
- **Done:** what changed (files, behavior).
- **Verified:** commands run and results.
- **Not verified:** what was not checked and why.
- **Risks and follow-ups:** anything the user should decide or watch.

## Common mistakes
- Starting to code before reading the existing code.
- Large rewrites for a small problem.
- Claiming tests pass without running them.
- Papering over errors (catching and ignoring them) rather than fixing causes.

## Verification
- Every critical rule is reflected in how the task was done; the final report uses the four-part format.
- Acceptance criteria are each marked met, not met, or unverified.

## Deliverables
The change, a verification summary, and the report.

## References
- [Task plan template](templates/task-plan.md)
