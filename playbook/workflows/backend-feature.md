# Workflow: Building a backend feature

Requires: [core principles](../core/00-core-principles.md)

## When to use
Adding or changing an endpoint, service, background job or business rule on the server side.

## Inspect first
- Existing routes, services, repositories and the conventions for errors, validation and auth
- The data model involved and its constraints
- Existing tests (unit, integration, API) for the area
- Configuration and secrets handling in the project

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [backend-api-design](../../skills/engineering/backend-api-design/SKILL.md) | Always |
| [database-engineering](../../skills/engineering/database-engineering/SKILL.md) | Always |
| [security-review](../../skills/engineering/security-review/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [architecture-decisions](../../skills/engineering/architecture-decisions/SKILL.md) | The feature introduces a new service boundary, queue or major dependency |
| [observability-and-incident-response](../../skills/delivery/observability-and-incident-response/SKILL.md) | The feature adds jobs, alerts, health checks or other operational behavior |
| [performance-analysis](../../skills/engineering/performance-analysis/SKILL.md) | There is a latency or volume target |

## Steps
1. Write the API contract: inputs, outputs, status codes, errors, auth, idempotency, limits.
2. Design the data changes; if the schema changes, switch to the database-migration workflow for that part.
3. Implement validation at the boundary, then business logic in the service layer, then storage.
4. Enforce authorization on the specific object for every request.
5. Add timeouts and bounded retries for external calls; make retried operations idempotent.
6. Add structured logging without sensitive data.
7. Write tests: success, validation errors, forbidden access, duplicates or retries, and concurrency if relevant.
8. Run the service and call the endpoint for real; compare responses with the contract.

## Decisions
| Situation | Do this |
| --- | --- |
| Operation is slow | Return an accepted status and process in a background job |
| Clients may retry | Require an idempotency key or a unique constraint |
| List can be large | Cursor pagination with a maximum page size |

## Artifacts
- API contract
- Implementation and tests
- Migration files if any
- Notes on limits and operations

## Verify
- Real calls return the contracted statuses and shapes, including errors
- Another user's resource is refused
- Full tests, lint and type checks pass

## If verification fails
1. Test fails at the database level: inspect constraints and transactions; do not remove a constraint to make it pass.
2. Intermittent failure: suspect shared state, ordering or timing; reproduce under repetition.

## Final report
- Contract and where implemented
- Tests and real calls run with results
- Security and limits decisions
- Not verified (load, concurrency, third-party calls)

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [database-migration](database-migration.md): for schema changes
- [api-integration](api-integration.md): when calling external services
