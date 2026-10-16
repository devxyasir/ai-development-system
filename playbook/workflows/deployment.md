# Workflow: Deploying an application

Requires: [core principles](../core/00-core-principles.md)

## When to use
Putting a build into an environment (staging or production), including configuration, migrations and verification.

## Inspect first
- The target environment, how it is reached and what credentials exist
- The existing deployment method, scripts and pipeline
- The artifact and the commit it was built from
- Pending database migrations and configuration changes
- Monitoring and rollback options

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [ci-cd-and-deployment](../../skills/delivery/ci-cd-and-deployment/SKILL.md) | Always |
| [observability-and-incident-response](../../skills/delivery/observability-and-incident-response/SKILL.md) | Always |
| [database-engineering](../../skills/engineering/database-engineering/SKILL.md) | The deployment includes migrations |
| [security-review](../../skills/engineering/security-review/SKILL.md) | New secrets, ports, permissions or dependencies are involved |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | Tags or branches are involved |

## Steps
1. Obtain explicit authorization for the target environment.
2. Write a deployment plan sized to the risk: order of steps, migrations, configuration, health checks, rollback, who watches.
3. Verify prerequisites: tested commit, build artifact, configuration and secrets present, backup current.
4. Apply migrations compatibly (old and new code both work during rollout).
5. Deploy (staged, canary or rolling when risk warrants); keep the previous version ready.
6. Check health endpoints, logs, error rate and key user flows; record commands and outputs.
7. Roll back if checks fail; follow the forward-fix plan if a migration prevents rollback.
8. Record what was deployed, when, and the result.

## Decisions
| Situation | Do this |
| --- | --- |
| No staging environment | Take smaller steps, use feature flags, add extra monitoring |
| Destructive migration | Verified backup and explicit authorization first |
| Hotfix | Smallest change, fast but real checks, rollback ready |

## Artifacts
- Deployment plan
- Evidence record (commands and outputs)
- Rollback notes

## Verify
- The live system reports the expected version and healthy status (evidence captured)
- Key user flows pass a smoke test
- Error rate and latency are normal after deployment

## If verification fails
1. Health check fails: roll back first, investigate after.
2. Cannot reach the environment: report that deployment is unverified; never claim success.

## Final report
- What was deployed where, with evidence
- Checks and results
- Rollback readiness
- Not verified

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [release](release.md): for versioned releases
- [incident-response](incident-response.md): if the deployment causes an outage
