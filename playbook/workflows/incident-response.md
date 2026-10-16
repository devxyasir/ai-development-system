# Workflow: Responding to a production incident

Requires: [core principles](../core/00-core-principles.md)

## When to use
A live system is down, degraded, losing data or under attack, and users are affected now.

## Inspect first
- Impact: who, what, since when, how severe
- Recent changes: deploys, configuration, dependencies, traffic
- Dashboards, alerts and logs for the affected service
- Available mitigations: rollback, feature flags, scaling, failover

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [observability-and-incident-response](../../skills/delivery/observability-and-incident-response/SKILL.md) | Always |
| [debugging](../../skills/engineering/debugging/SKILL.md) | Always |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | The mitigation is a revert |
| [ci-cd-and-deployment](../../skills/delivery/ci-cd-and-deployment/SKILL.md) | The mitigation is a redeploy or rollback |
| [security-review](../../skills/engineering/security-review/SKILL.md) | A security incident is suspected |
| [database-engineering](../../skills/engineering/database-engineering/SKILL.md) | Data integrity or a database is involved |

## Steps
1. Confirm impact and severity; open an incident record and name a lead.
2. Mitigate first: roll back the latest change, disable a flag, scale, fail over or block abusive traffic.
3. Communicate briefly and regularly: impact, known facts, actions, next update time.
4. Investigate with evidence once harm is contained (timeline of changes and alerts, logs, metrics, traces).
5. Verify recovery with metrics and a user-flow check; keep watching.
6. Write the incident report and hold a blameless review within days; assign action items.

## Decisions
| Situation | Do this |
| --- | --- |
| Recent deploy correlates with the problem | Roll back first |
| Cause unknown and impact growing | Choose the safest broad mitigation; investigate after |
| Possible security breach | Preserve evidence, limit access, rotate credentials, involve the responsible people |

## Artifacts
- Incident record and timeline
- Incident report
- Action items

## Verify
- Impact has ended (metrics and flow check)
- Mitigation is understood and documented
- Action items have owners

## If verification fails
1. Mitigation does not help: try the next safest option; escalate; do not stack unverified changes.

## Final report
- Impact and duration
- Mitigation and resolution
- Root cause or current best understanding
- Action items

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [bug-fixing](bug-fixing.md): for the permanent fix
