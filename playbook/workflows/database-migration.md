# Workflow: Changing a database schema

Requires: [core principles](../core/00-core-principles.md)

## When to use
Creating or altering tables, columns, indexes or constraints, or moving or transforming stored data.

## Inspect first
- The migration tool and its conventions; existing migrations and their naming
- The current schema and the data volume of affected tables
- Code that reads and writes the affected tables
- Backup status and the environment that will run the migration

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [database-engineering](../../skills/engineering/database-engineering/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [security-review](../../skills/engineering/security-review/SKILL.md) | The change touches personal, financial or otherwise sensitive data |
| [ci-cd-and-deployment](../../skills/delivery/ci-cd-and-deployment/SKILL.md) | The migration runs as part of a deployment |
| [git-and-github](../../skills/delivery/git-and-github/SKILL.md) | You are asked to commit the migration |

## Steps
1. State the desired schema and why; list the queries it must support.
2. Choose the safe pattern (expand and contract for anything not trivially additive).
3. Write the migration as a new versioned file; never edit an applied migration.
4. Write the rollback or forward-fix plan; destructive steps need a verified backup and explicit authorization.
5. Test on a copy with realistic volume: apply, check constraints and counts, revert if reversible.
6. Update the application code to work with both old and new schema during the rollout.
7. Run the application test suite against the migrated schema.
8. Record row counts and constraint checks before and after when applying.

## Decisions
| Situation | Do this |
| --- | --- |
| Table is large | Batch the backfill; use concurrent or online index creation where supported; set lock timeouts |
| Column type change | Add new column, backfill, switch, drop in a later release |
| Destructive change requested | Stop and obtain authorization; confirm a restorable backup |

## Artifacts
- Migration file(s)
- Rollback or forward-fix plan
- Test results on a copy

## Verify
- Migration applies cleanly on a copy; constraints enforce the rules (invalid insert is rejected)
- Application tests pass on the new schema
- Old code still works during the rollout window

## If verification fails
1. Migration fails midway: stop; do not rerun blindly; inspect the state, then revert or complete in a controlled way.
2. Lock waits or timeouts: reduce batch size or use an online method; retry in a quiet window.

## Final report
- Schema change and pattern used
- Tests on a copy with data volume
- Rollback plan
- Authorizations obtained; what was not verified

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [deployment](deployment.md): to apply it in an environment
