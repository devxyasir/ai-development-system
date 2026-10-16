# Task routing

Requires: [core principles](00-core-principles.md)

Routing answers two questions without guesswork: which **workflow** to follow, and which **skills** to load. Do not read files you are not routed to.

## How to route
1. Find the row in step 1 that matches the main deliverable of the task. Read that workflow.
2. In the workflow's Load table, load every "Always" skill, and each other skill only when its condition is true.
3. Apply the overlays in step 2 for anything the change touches. An overlay adds a skill or a workflow; it never replaces the main workflow.
4. If you are unsure which row applies, use the skill finder in step 3, or ask one question.

## Step 1: choose the workflow
| If the task is | Workflow |
| --- | --- |
| Start a new application, service, library or tool | [new-project](../workflows/new-project.md) |
| First time in a repository, or an unfamiliar area | [existing-project](../workflows/existing-project.md) |
| Add or change a feature or behavior | [feature-development](../workflows/feature-development.md) |
| Error, crash, wrong result, failing test, intermittent failure | [bug-fixing](../workflows/bug-fixing.md) |
| Restructure or clean up code without changing behavior | [refactoring](../workflows/refactoring.md) |
| Learn, evaluate or choose a library, API, framework or technique | [research-first](../workflows/research-first.md) |
| Build or change screens, components or layouts; match a mockup, screenshot or site | [ui-implementation](../workflows/ui-implementation.md) |
| Animate: transitions, micro-interactions, scroll effects, SVG, canvas, 3D, cinematic sequences | [animation-implementation](../workflows/animation-implementation.md) |
| Add or change an endpoint, service, background job or business rule | [backend-feature](../workflows/backend-feature.md) |
| Change tables, columns, indexes, constraints or move data | [database-migration](../workflows/database-migration.md) |
| Call a third-party API, service or webhook | [api-integration](../workflows/api-integration.md) |
| Add an LLM, retrieval, agent, speech, vision or ML feature | [ai-feature](../workflows/ai-feature.md) |
| Add or change gameplay, game systems, rendering, input or game builds | [game-feature](../workflows/game-feature.md) |
| Something is slow or uses too much memory or CPU; meet a latency target | [performance-investigation](../workflows/performance-investigation.md) |
| Security review or hardening | [security-review](../workflows/security-review.md) |
| Add tests, fix flaky tests, or verify a change | [testing-and-verification](../workflows/testing-and-verification.md) |
| Prepare a commit, branch or pull request | [pull-request](../workflows/pull-request.md) |
| Review a diff or pull request | [code-review](../workflows/code-review.md) |
| Deploy to an environment | [deployment](../workflows/deployment.md) |
| Publish a version, package, tag or changelog | [release](../workflows/release.md) |
| A live system is down or degraded right now | [incident-response](../workflows/incident-response.md) |
| Stop with unfinished work, or pass work to someone else | [handoff](../workflows/handoff.md) |

Mixed tasks: choose the workflow of the main deliverable and follow its Related workflows. Typical order when several apply: research-first, database-migration, backend-feature, api-integration, ui-implementation, animation-implementation, testing-and-verification, pull-request, deployment, release.

Examples:
- New web application: new-project (it loads requirements, product design, architecture, frontend, backend, database, security, testing and deployment guidance as its conditions apply).
- Bug fix: bug-fixing (reproduce, find the root cause, smallest fix, regression test).
- Game feature: game-feature (gameplay, engine structure, simulation tests, performance).
- LLM feature: ai-feature (task definition, model choice, safety, evaluation, cost).
- Database change: database-migration (schema, integrity, migration safety, rollback, tests).
- Deployment: deployment (configuration, secrets, build, migrations, health checks, rollback, verification).

## Step 2: overlays
Add these whenever the change touches the thing on the left.

| If the change touches | Also |
| --- | --- |
| Authentication, permissions, user input, file handling, secrets or personal data | [security-review](../../skills/engineering/security-review/SKILL.md) |
| A database schema or stored data | [database-migration](../workflows/database-migration.md) workflow |
| User interface files (HTML, CSS, JSX, TSX, Vue, Svelte, templates) | [visual-qa](../../skills/frontend/visual-qa/SKILL.md) and [accessibility-review](../../skills/design/accessibility-review/SKILL.md) |
| CSS transitions, keyframes or any animation | [animation-implementation](../workflows/animation-implementation.md) workflow (includes reduced motion) |
| Commits, branches, merges or pull requests | [git-and-github](../../skills/delivery/git-and-github/SKILL.md) |
| A claim that something is faster or slower | [performance-analysis](../../skills/engineering/performance-analysis/SKILL.md) |
| A call to a language model or ML model | [ai-feature](../workflows/ai-feature.md) workflow |
| README, docs, changelog or runbooks | [documentation-and-handoff](../../skills/delivery/documentation-and-handoff/SKILL.md) |
| CI configuration, Dockerfiles, infrastructure or deployment settings | [ci-cd-and-deployment](../../skills/delivery/ci-cd-and-deployment/SKILL.md) |

## Step 3: skill finder
Every skill, with the words that should make you load it. Use this when no workflow row fits.

| Skill | Load when the task mentions |
| --- | --- |
| [animation-planning-and-review](../../skills/animation-production/animation-planning-and-review/SKILL.md) | storyboards, multi-step animation plans, animation review |
| [ci-cd-and-deployment](../../skills/delivery/ci-cd-and-deployment/SKILL.md) | pipelines, containers, hosting, deployment, release versioning |
| [documentation-and-handoff](../../skills/delivery/documentation-and-handoff/SKILL.md) | README files, runbooks, documentation, handing work over |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | commits, branches, merges, conflicts, pull requests, tags |
| [observability-and-incident-response](../../skills/delivery/observability-and-incident-response/SKILL.md) | logging, metrics, alerts, outages, post-incident reviews |
| [accessibility-review](../../skills/design/accessibility-review/SKILL.md) | accessibility, keyboard use, screen readers, WCAG, ARIA |
| [color-palette-selection](../../skills/design/color-palette-selection/SKILL.md) | colors, palette, contrast ratios, chart colors |
| [design-system-creation](../../skills/design/design-system-creation/SKILL.md) | design tokens, theming, dark mode, component library styles |
| [layout-and-responsive-design](../../skills/design/layout-and-responsive-design/SKILL.md) | layout, spacing, breakpoints, mobile problems, overflow |
| [product-design](../../skills/design/product-design/SKILL.md) | screen flow, navigation, information architecture, form or dashboard structure, empty and error states |
| [typography-selection](../../skills/design/typography-selection/SKILL.md) | fonts, type scale, readability, right-to-left or multilingual text |
| [visual-design-direction](../../skills/design/visual-design-direction/SKILL.md) | look and feel, brand, a generic-looking UI, redesign |
| [architecture-decisions](../../skills/engineering/architecture-decisions/SKILL.md) | choosing structure, splitting or merging services, decision records, mapping a codebase |
| [backend-api-design](../../skills/engineering/backend-api-design/SKILL.md) | endpoints, services, API contracts, validation, authorization, jobs |
| [code-review](../../skills/engineering/code-review/SKILL.md) | reviewing a diff or pull request, self-review before merging |
| [database-engineering](../../skills/engineering/database-engineering/SKILL.md) | schemas, migrations, slow queries, indexes, backups |
| [debugging](../../skills/engineering/debugging/SKILL.md) | errors, crashes, wrong output, failing tests |
| [development-operating-rules](../../skills/engineering/development-operating-rules/SKILL.md) | start of any task, unclear tasks, how to report completion |
| [performance-analysis](../../skills/engineering/performance-analysis/SKILL.md) | slow backend code, memory or CPU use, benchmarks |
| [refactoring](../../skills/engineering/refactoring/SKILL.md) | restructuring code without changing behavior |
| [requirements-and-research](../../skills/engineering/requirements-and-research/SKILL.md) | vague requests, unfamiliar libraries or APIs, comparing technologies, specifications |
| [security-review](../../skills/engineering/security-review/SKILL.md) | authentication, input handling, uploads, secrets, dependencies, vulnerability review |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | writing or choosing tests, flaky tests, verifying a claim that something works |
| [component-engineering](../../skills/frontend/component-engineering/SKILL.md) | building or refactoring a UI component, props design |
| [design-to-code](../../skills/frontend/design-to-code/SKILL.md) | building from a screenshot, mockup, design file or reference site |
| [frontend-architecture](../../skills/frontend/frontend-architecture/SKILL.md) | rendering strategy, state placement, routing, data fetching structure |
| [frontend-performance](../../skills/frontend/frontend-performance/SKILL.md) | slow pages, Web Vitals, bundle size |
| [frontend-testing](../../skills/frontend/frontend-testing/SKILL.md) | component and end-to-end tests for interfaces |
| [visual-qa](../../skills/frontend/visual-qa/SKILL.md) | checking how the UI looks and behaves when rendered |
| [animation-performance](../../skills/motion/animation-performance/SKILL.md) | janky animation, choosing an animation library, frame time |
| [cinematic-motion](../../skills/motion/cinematic-motion/SKILL.md) | portfolio or landing page storytelling, intro sequences |
| [micro-interactions](../../skills/motion/micro-interactions/SKILL.md) | hover, press, toggle, copy and form feedback, undo |
| [motion-design](../../skills/motion/motion-design/SKILL.md) | why and how something should animate, timing, easing |
| [reduced-motion-accessibility](../../skills/motion/reduced-motion-accessibility/SKILL.md) | prefers-reduced-motion, flashing, autoplay, pause controls |
| [scroll-animation](../../skills/motion/scroll-animation/SKILL.md) | scroll reveals, parallax, sticky or pinned sections, progress bars |
| [svg-canvas-3d-animation](../../skills/motion/svg-canvas-3d-animation/SKILL.md) | SVG, canvas, WebGL, three.js, particles |
| [ui-animation](../../skills/motion/ui-animation/SKILL.md) | animating dialogs, menus, toasts, lists, route transitions |
| [ai-llm-engineering](../../skills/specialist/ai-llm-engineering/SKILL.md) | LLMs, retrieval, agents, embeddings, evaluation, machine learning |
| [cli-and-library-design](../../skills/specialist/cli-and-library-design/SKILL.md) | command-line tools, libraries, SDKs, package interfaces |
| [desktop-and-mobile-development](../../skills/specialist/desktop-and-mobile-development/SKILL.md) | desktop or mobile apps, offline behavior, signing, stores |
| [game-development](../../skills/specialist/game-development/SKILL.md) | games, engines, game loops, gameplay systems |
| [skill-authoring](../../skills/tooling/skill-authoring/SKILL.md) | creating or editing agent skills |
| [skill-installation](../../skills/tooling/skill-installation/SKILL.md) | installing, updating or removing agent skills |

## Loading rules
- Never load a skill "just in case". If its condition is false, skip it.
- A workflow loads at most six "Always" skills; if you want more, you have picked the wrong workflow or are loading conditionals too early.
- Skills that are installed in an agent's skills directory may be discovered by the agent itself; routing still decides which ones you follow.
- When two skills give different advice, the more specific skill wins for its area; tell the user about real conflicts.
- If no workflow matches, follow the generic loop in AGENTS.md (inspect, plan, implement, verify, report) and load [development-operating-rules](../../skills/engineering/development-operating-rules/SKILL.md).
