# Architecture

## Goals
1. Make weaker coding models more reliable by turning expert judgment into procedures, checklists and routing.
2. Keep the always-loaded text small and load everything else on demand.
3. Make each skill usable on its own, installable in isolation, and portable across agents that follow the Agent Skills format.
4. Make the whole system checkable by scripts, and be honest about what the scripts cannot check.

## Layers
| Layer | Files | Loaded |
| --- | --- | --- |
| Entry rules | `AGENTS.md` (canonical), `CLAUDE.md` (imports it) | Every session |
| Playbook | `playbook/core`, `workflows`, `checklists`, `references` | By link, one workflow per task |
| Skills | `skills/<category>/<name>/` | By the agent's skill discovery or by link |
| Scoped Claude rules | `.claude/rules/*.md` with `paths:` | When matching files are touched (Claude Code) |
| Tooling | `scripts/`, `schemas/`, `tests/` | Never by agents during tasks |

## Design decisions and their evidence
| Decision | Reason |
| --- | --- |
| `AGENTS.md` is the canonical manual; `CLAUDE.md` is `@AGENTS.md` plus Claude notes | Claude Code reads `CLAUDE.md`, not `AGENTS.md`, and supports `@path` imports; importing avoids two copies that drift (Claude Code memory documentation) |
| The playbook is not stored in `.claude/rules/` | Rules without a `paths` field load at launch, so thirty rule files would load into every session. Only path-scoped pointer rules live there |
| Entry files stay under 200 lines | The Claude Code documentation recommends short instruction files; the validator enforces the limit |
| Skills use the Agent Skills layout and frontmatter | A documented, portable format; only `name`, `description`, and standard optional fields are used, with portable `metadata` for category and version |
| Skills are self-contained | Installers copy one folder; links that leave it would break after installation |
| Routing is a table, and each workflow has a Load table with conditions | A weak model should not decide which of 43 skills to read; the table decides, and the validator caps the always-loaded set at six |
| Templates live with the skill that owns them | One owner per topic avoids duplicated templates drifting apart |
| Tests and validators use only the standard library | Nothing to install; works in CI and on contributors' machines |

## How the master-prompt coverage map was realized
The original request proposed about 30 rule files, 20 workflows, 24 reference files, 11 templates and 8 checklists under `.claude/`. To avoid shallow files and duplicated guidance, the discipline handbooks became skills and the playbook keeps only what is universal.

| Proposed area | Where it lives now |
| --- | --- |
| Core principles, task understanding, reasoning and planning, completion and handoff | `playbook/core/00` to `04`, plus the development-operating-rules and documentation-and-handoff skills |
| Research and evidence | requirements-and-research skill |
| Architecture, patterns, monolith versus services, event-driven | architecture-decisions skill and its patterns reference |
| Product thinking, design system, UI/UX, accessibility | design skills (product-design, visual-design-direction, design-system-creation, color-palette-selection, typography-selection, layout-and-responsive-design, accessibility-review) |
| Frontend engineering and patterns | frontend skills |
| Backend, API patterns, authentication, caching and queues | backend-api-design and database-engineering skills (conventions reference) |
| Database and data engineering | database-engineering skill |
| Security, privacy, threat modeling | security-review skill (checklist and threat-model template) |
| Testing and QA | testing-strategy and frontend-testing skills |
| Debugging | debugging skill |
| Performance | performance-analysis, frontend-performance, animation-performance skills |
| Git and GitHub, collaboration | git-and-github skill and the pull-request and code-review workflows |
| CI/CD, deployment, release | ci-cd-and-deployment skill and the deployment and release workflows |
| Observability, incident response | observability-and-incident-response skill |
| Documentation | documentation-and-handoff skill |
| Dependencies and cost | security-review (supply chain), requirements-and-research (technology evaluation), ci-cd-and-deployment (cost controls) |
| AI and LLM, retrieval, agents, ML | ai-llm-engineering skill |
| Game development | game-development skill |
| Desktop, mobile, CLI, libraries | desktop-and-mobile-development and cli-and-library-design skills |
| Workflows (21 requested) | `playbook/workflows` (22 files: the two UI workflows are merged into ui-implementation; animation-implementation and code-review are added) |
| Templates | with their owning skills (task plan, requirements, ADR, technical design, API contract, test plan, bug report, code review, release checklist, incident report, handoff, threat model) |
| Checklists | `playbook/checklists` (global) and inside skills (security, design review, WCAG) |
| Validator | `scripts/validate-instructions.py`, `scripts/validate-skills.py` and tests |
| Internationalization | covered inside typography-selection and layout-and-responsive-design (right-to-left, scripts) rather than as a separate file |

## What the validators check, and what they cannot
Checked mechanically: required files, broken links, unfinished-work markers, required sections, routing and index coverage, circular `Requires:` chains, size limits, frontmatter, skill self-containment, collection integrity, documented commands versus real scripts, installer safety.

Not checkable mechanically: whether the guidance is correct, whether two pieces of advice contradict each other in meaning, and whether an agent will follow it. Those need review. The routing tests in `tests/` verify that representative tasks reach the right skills without loading unrelated ones; they are tests of the instruction graph, not runs of a real agent.
