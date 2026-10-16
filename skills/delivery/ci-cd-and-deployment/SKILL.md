---
name: ci-cd-and-deployment
description: "Plans and executes CI/CD, deployment and release work: build pipelines, automated checks, environments and secrets, containers, infrastructure as code, choosing hosting (static, PaaS, VPS, containers, serverless), migrations during deploys, health checks, rollback, release versioning and changelogs, and post-deployment verification with evidence. Use when setting up pipelines, deploying an application, preparing a release, or reviewing deployment risk."
metadata:
  category: delivery
  version: "0.1.0"
  related: "git-and-github, security-review, observability-and-incident-response, database-engineering, documentation-and-handoff"
---

# CI/CD, deployment and release

Automate what is repeatable, keep environments similar, make every deployment reversible, and prove the result with evidence. Never say something is deployed or reachable without checking it.

## When to use
- Creating or changing pipelines; deploying; choosing hosting; preparing a versioned release; reviewing deployment risk.
- Not for: incident coordination (observability-and-incident-response).

## Procedure: pipelines (CI)
1. Inspect existing automation (workflow files, scripts, Makefile, package scripts) and extend it rather than replacing it.
2. Stages: install with a lockfile, lint and type check, unit tests, integration tests, build, security scans (dependency audit, secret scan), then publish artifacts. Fail fast on cheap checks first.
3. Make it reproducible: pinned tool versions, cached dependencies, no reliance on a developer's machine, same commands locally and in CI.
4. Handle secrets through the CI secret store; prefer short-lived credentials (workload identity) to long-lived keys; give each workflow minimal permissions; pin third-party actions to reviewed versions.
5. Keep the pipeline fast enough to be used (parallelize, cache), and treat flaky tests as defects.

## Procedure: choose how to deploy
| Situation | Prefer |
| --- | --- |
| Static site or SPA | Static hosting with a CDN |
| Small web app or API, small team | A managed platform (PaaS) or a single VPS with a process manager and reverse proxy |
| Several services, need isolation and repeatability | Containers on a managed container service |
| Spiky or event-driven workloads | Serverless functions, mindful of limits and cold starts |
| Many services, large team, concrete orchestration needs | A container orchestrator; not before a concrete need exists |
See [deployment options](references/deployment-options.md). Do not introduce complex infrastructure without a stated reason.

## Procedure: deploy
1. **Write a deployment plan** sized to the risk (small change: a few lines; risky change: full checklist in [release checklist](templates/release-checklist.md)): what is deployed, order of steps, migrations, configuration and secrets, health checks, rollback, who is watching.
2. **Verify prerequisites:** correct environment and credentials, build artifact from the tested commit, configuration present, database migration tested, backups current.
3. **Apply database migrations compatibly** (expand and contract): the old and new code versions must both work with the schema during the rollout.
4. **Deploy gradually when risk warrants:** staging first, then canary or blue-green, or a rolling update; keep the previous version ready.
5. **Check health:** liveness and readiness endpoints, error rates, latency, logs, key user flows (smoke test).
6. **Verify with evidence:** record the commands and outputs (HTTP status of the live URL, version endpoint, log lines). If you cannot reach it, say so rather than assuming.
7. **Roll back** when health checks or smoke tests fail: revert to the previous artifact; if a migration blocks rollback, follow the forward-fix plan.
8. **Record** what was deployed, when, by whom, and the result.

## Procedure: release (versioned software)
1. Decide the version with semantic versioning: MAJOR for breaking changes, MINOR for compatible features, PATCH for fixes.
2. Update the changelog (what changed, grouped by added, changed, fixed, removed, security; migration notes for breaking changes) and the version file(s).
3. Run the full checks on the release commit; build artifacts from a clean checkout; test installation from the artifact.
4. Tag the commit and publish only with authorization; publish artifacts and release notes.
5. Verify the published package installs and runs; announce.
6. If a release is bad: yank or mark it, publish a fixed patch release; avoid rewriting published tags.

## Decision rules
| Situation | Do this |
| --- | --- |
| Migration is destructive | Take and verify a backup; require explicit authorization |
| Config differs between environments | Parameterize; validate required variables at startup |
| Production hotfix | Smallest change, normal checks (fast path), rollback ready |
| No staging environment | Increase caution: smaller steps, feature flags, extra monitoring |
| Costs could grow | Set budgets, alerts and limits before launch |

## Common mistakes
- Deploying an artifact not built from the tested commit.
- Migrations that break the running old version.
- No rollback plan; secrets in repository or logs.
- Claiming success without checking the live system.
- Complex infrastructure for a simple app.

## Verification
- Pipeline passes on a clean run; commands and results reported.
- Post-deployment evidence captured (status codes, version, logs) or the limitation stated.
- Rollback path stated and, for risky changes, rehearsed or reasoned.

## Deliverables
Pipeline configuration, deployment plan, release checklist, deployment record, rollback notes.

## References
- [Deployment options](references/deployment-options.md)
- [Release checklist](templates/release-checklist.md)
