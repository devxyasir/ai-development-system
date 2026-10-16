# Release checklist: <name> <version>

Date: <date> | Release owner: <name> | Environment: <staging / production>

## Scope
- Changes included: <list or link to changelog>
- Breaking changes: <list and migration steps, or "none">
- Migrations: <list, reversible? yes/no>

## Before release
- [ ] All required checks pass on the release commit (<commands or CI link>)
- [ ] Build created from a clean checkout of the tested commit
- [ ] Version number decided and updated (<MAJOR.MINOR.PATCH>, reason)
- [ ] Changelog updated; release notes drafted
- [ ] Configuration and secrets present in the target environment
- [ ] Database backup taken and restore verified (if data changes)
- [ ] Migration tested on a copy with realistic data
- [ ] Rollback plan written: <steps>
- [ ] Monitoring and alerts ready; person watching: <name>
- [ ] Authorization to publish or deploy obtained from: <name>

## Release steps
1. <step, command>
2. <step, command>
3. <step, command>

## Verification after release
| Check | Command or action | Result and evidence |
| --- | --- | --- |
| Version served | <command> | <output> |
| Health endpoints | <command> | <status codes> |
| Key user flows | <smoke test> | <result> |
| Error rate and latency | <dashboard or logs> | <values> |
| Package installs (libraries) | <install in clean environment> | <result> |

## Rollback triggers and steps
- Roll back if: <conditions>
- Steps: <commands>

## Record
- Deployed by: <name> | Time: <time> | Outcome: <success / rolled back / partial>
- Follow-ups: <list>
