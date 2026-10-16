# Workflow: Starting a new project

Requires: [core principles](../core/00-core-principles.md)

## When to use
Starting an application, service, library or tool from an empty directory or new repository.

## Inspect first
- The target directory (empty? existing files? existing git history?)
- The user's stated stack, platform, deployment target and constraints
- Tool versions available on the machine (language runtime, package manager, container tooling)
- Any organization templates, lint or formatting standards the user mentions

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [requirements-and-research](../../skills/engineering/requirements-and-research/SKILL.md) | Always |
| [architecture-decisions](../../skills/engineering/architecture-decisions/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | Always |
| [documentation-and-handoff](../../skills/delivery/documentation-and-handoff/SKILL.md) | Always |
| [product-design](../../skills/design/product-design/SKILL.md) | The project has a user interface |
| [visual-design-direction](../../skills/design/visual-design-direction/SKILL.md) | The project has a user interface and no existing brand or design system |
| [frontend-architecture](../../skills/frontend/frontend-architecture/SKILL.md) | The project has a web front end |
| [backend-api-design](../../skills/engineering/backend-api-design/SKILL.md) | The project has a service or API |
| [database-engineering](../../skills/engineering/database-engineering/SKILL.md) | The project stores data |
| [security-review](../../skills/engineering/security-review/SKILL.md) | The project handles accounts, personal data, files or payments |
| [ci-cd-and-deployment](../../skills/delivery/ci-cd-and-deployment/SKILL.md) | A pipeline or deployment is requested |

## Steps
1. Write the requirements and assumptions (ask only about answers that would change the architecture).
2. Choose the stack: use what the user names or the team already uses; check current versions and setup instructions in official documentation; add nothing just because it is popular.
3. Choose the simplest structure that meets the requirements (usually a modular monolith); record major choices as short decision records.
4. Scaffold the minimum with the framework's official generator or by hand; run it to confirm it starts.
5. Set up tests, lint, formatter, `.gitignore` (including secrets and build output), and a README with a quick start.
6. Build one thin vertical slice end to end (one real user flow through every layer).
7. Add tests for the slice and run the full checks.
8. Extend feature by feature using the feature-development workflow.
9. If deployment is in scope, continue with the deployment workflow.

## Decisions
| Situation | Do this |
| --- | --- |
| The user did not name a stack | Propose one with a one-line reason per choice and proceed unless it conflicts with a constraint |
| Many technologies seem equally good | Choose the one with the best official documentation and the team's familiarity |
| Temptation to add microservices, queues or orchestration | Only if a stated requirement needs it |

## Artifacts
- Requirements and assumptions note
- Decision records for major choices
- Project scaffold, test configuration, README
- Initial commit instructions (do not commit without authorization)

## Verify
- A fresh clone installs and starts by following only the README
- Tests, lint and build pass
- No secrets, caches or build output in the repository (check `git status` and `.gitignore`)
- The vertical slice works through the real interface

## If verification fails
1. Scaffold fails: read the first error, check runtime and tool versions against the framework's documentation, and fix the environment before changing generated code.
2. Dependency conflicts: use the versions the framework documents; do not force-install.
3. If the stack cannot be made to work after two attempts, report the exact error and options instead of switching stacks silently.

## Final report
- Stack chosen and why
- What runs now and how to run it
- Commands run and results
- Assumptions made and what is not built yet

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [feature-development](feature-development.md): for each further feature
- [deployment](deployment.md): when the project must go live
