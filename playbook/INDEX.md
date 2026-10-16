# Playbook index

Every file in the playbook, what it covers, when to read it, and what it depends on. Skills have their own index: [skills index](../skills/SKILLS-INDEX.md).

| File | Covers | Read when | Depends on |
| --- | --- | --- | --- |
| [README](README.md) | How the playbook is organized and loaded | You are new to the system | none |
| [00 core principles](core/00-core-principles.md) | Instruction priority, the ten principles in practice, honest language | Always, once per task | none |
| [01 understand and plan](core/01-understand-and-plan.md) | Goals, assumptions, when to ask, sizing and decomposing work, progress records | Before a medium or large task | core principles |
| [02 routing](core/02-routing.md) | Task to workflow table, overlays, skill finder | Choosing what to follow and load | core principles |
| [03 quality gate and reporting](core/03-quality-gate-and-reporting.md) | Completion gate, evidence rules, the four-part report | Before declaring work done | core principles |
| [04 lower-capability support](core/04-lower-capability-support.md) | Compact procedure, self-checks, fallback when you cannot finish | You are unsure or running short of context | core principles |
| [workflow: new-project](workflows/new-project.md) | Starting a new project | Starting an application, service, library or tool from an empty directory or new repository. | core principles |
| [workflow: existing-project](workflows/existing-project.md) | Working in an existing or unfamiliar repository | First time working in a repository or an unfamiliar part of one, before changing anything. | core principles |
| [workflow: feature-development](workflows/feature-development.md) | Implementing a feature | Adding or changing user-visible or API-visible behavior in an existing project. | core principles |
| [workflow: bug-fixing](workflows/bug-fixing.md) | Fixing a bug | Something produces an error, a wrong result, a crash or an intermittent failure, and the cause must be found and fixed. | core principles |
| [workflow: refactoring](workflows/refactoring.md) | Refactoring | Restructuring code without changing its behavior: cleanup, extraction, renaming, moving modules, preparing for a feature. | core principles |
| [workflow: research-first](workflows/research-first.md) | Researching an unfamiliar technology | A library, framework, API, service or technique is unfamiliar, may have changed, or must be chosen among alternatives, before implementation starts. | core principles |
| [workflow: ui-implementation](workflows/ui-implementation.md) | Building a user interface | Building or changing screens, components or layouts, whether from a design reference (screenshot, mockup, existing site) or from a description. | core principles |
| [workflow: animation-implementation](workflows/animation-implementation.md) | Adding animation and motion | Adding or reviewing transitions, micro-interactions, scroll effects, SVG, canvas or 3D animation, or cinematic sequences. | core principles |
| [workflow: backend-feature](workflows/backend-feature.md) | Building a backend feature | Adding or changing an endpoint, service, background job or business rule on the server side. | core principles |
| [workflow: database-migration](workflows/database-migration.md) | Changing a database schema | Creating or altering tables, columns, indexes or constraints, or moving or transforming stored data. | core principles |
| [workflow: api-integration](workflows/api-integration.md) | Integrating an external API or service | Calling a third-party API or service, or exposing an integration to partners. | core principles |
| [workflow: ai-feature](workflows/ai-feature.md) | Building an AI or LLM feature | Adding model-driven behavior: generation, classification, extraction, retrieval, agents, speech, vision or other machine learning. | core principles |
| [workflow: game-feature](workflows/game-feature.md) | Building a game feature | Adding or changing gameplay, game systems, rendering, input, UI, saves, networking or builds in a game project. | core principles |
| [workflow: performance-investigation](workflows/performance-investigation.md) | Investigating performance | Something is slow, uses too much memory or CPU, regressed, or must meet a latency or capacity target. | core principles |
| [workflow: security-review](workflows/security-review.md) | Conducting a security review | Reviewing a feature, change, repository or deployment for vulnerabilities, or hardening before release. | core principles |
| [workflow: testing-and-verification](workflows/testing-and-verification.md) | Writing and running tests | Adding tests, choosing what to test, fixing flaky tests, or verifying a change before reporting it as done. | core principles |
| [workflow: pull-request](workflows/pull-request.md) | Preparing a pull request | Preparing work for review: cleaning the change, writing the description, and making sure checks pass. | core principles |
| [workflow: code-review](workflows/code-review.md) | Reviewing code | Reviewing someone else's diff or pull request, or doing a final review of your own work. | core principles |
| [workflow: deployment](workflows/deployment.md) | Deploying an application | Putting a build into an environment (staging or production), including configuration, migrations and verification. | core principles |
| [workflow: release](workflows/release.md) | Releasing a version | Publishing a versioned release of an application, package, library or CLI. | core principles |
| [workflow: incident-response](workflows/incident-response.md) | Responding to a production incident | A live system is down, degraded, losing data or under attack, and users are affected now. | core principles |
| [workflow: handoff](workflows/handoff.md) | Handing off work | Ending a session with unfinished work, or passing work to another engineer or model. | core principles |
| [checklist: before coding](checklists/before-coding.md) | Readiness to start editing | Before editing files | none |
| [checklist: before commit](checklists/before-commit.md) | Safe commits | Before committing | none |
| [checklist: before merge](checklists/before-merge.md) | Pull request and merge readiness | Before merging | none |
| [checklist: before deployment](checklists/before-deployment.md) | Deployment readiness | Before deploying | none |
| [checklist: before release](checklists/before-release.md) | Release readiness | Before publishing a version | none |
| [checklist: final verification](checklists/final-verification.md) | The completion gate as a checklist | Before the final report | none |
| [decision trees](references/decision-trees.md) | Thirteen recurring decisions with good and bad examples | A decision is unclear | none |
| [common anti-patterns](references/common-anti-patterns.md) | Process, code, architecture, design, test, security and delivery pitfalls | Reviewing work or checking for known mistakes | none |
