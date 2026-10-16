---
name: backend-api-design
description: "Designs and implements backend services and APIs: routing, validation at the boundary, business logic placement, authentication and authorization, error format, idempotency, pagination, transactions, concurrency, background jobs, external service calls with timeouts and retries, rate limiting, structured logging and configuration. Use when adding or changing an endpoint, service or integration, or reviewing an API contract."
metadata:
  category: engineering
  version: "0.1.0"
  related: "database-engineering, security-review, testing-strategy, architecture-decisions, observability-and-incident-response"
---

# Backend and API design

Reliable APIs have explicit contracts, validated inputs, enforced permissions, predictable errors, and behavior that is safe to retry. Keep business rules out of transport code.

## When to use
- Adding or changing an endpoint, service, job or external integration.
- Defining an API contract or reviewing one.
- Not for: schema design (database-engineering) or vulnerability review (security-review), though both should be loaded for endpoints that store or expose data.

## Procedure
1. **Inspect the project:** language, framework, existing routes and conventions (naming, error format, auth), service and repository layers, test setup.
2. **Write the contract first** with the [API contract template](templates/api-contract.md): method and path or operation, request and response schemas, status codes, errors, auth, idempotency, pagination, rate limits.
3. **Validate at the boundary:** parse and validate every input (body, query, path, headers) against a schema; reject unknown or malformed data with a client error; never trust client-supplied identifiers or roles.
4. **Enforce authorization on every request:** check the caller's permission on the specific resource, not only that they are logged in (object-level checks prevent users from reading each other's records).
5. **Keep layers separate:** handler parses and responds; service holds business rules; repository talks to storage; external clients are wrapped behind an interface.
6. **Return consistent errors** ([conventions](references/api-conventions.md)): correct status code, stable machine-readable code, human-readable message, no internals or stack traces.
7. **Make writes safe:** use transactions for multi-step changes; design idempotency for operations that clients may retry (idempotency keys or natural keys); handle concurrent updates (optimistic locking or constraints).
8. **Handle slow and unreliable work:** external calls get timeouts and bounded retries with backoff and jitter (only for idempotent calls); long work goes to a background job with status reporting.
9. **Bound everything:** page size limits, request size limits, rate limits on abusive or expensive endpoints, maximum concurrency on costly operations.
10. **Add observability:** structured logs with request id and key identifiers (no secrets or personal data), metrics for rate, errors and latency, a health endpoint.
11. **Test:** unit tests for rules, integration tests through the API with a real or containerized database, tests for validation errors, permission failures, duplicates, and concurrency where relevant.

## Decision rules
| Situation | Do this |
| --- | --- |
| Clients may retry a create | Require an idempotency key or use a unique constraint |
| List endpoint on a large table | Cursor pagination with a stable sort and a maximum page size |
| Breaking change needed | Version the API or add fields compatibly; never silently change meaning |
| Third-party API unreliable | Timeout, retry with limits, circuit breaker, fallback behavior, queue |
| Config differs by environment | Environment variables or config service, validated at startup, never hard-coded secrets |
| Operation takes longer than a few seconds | Accept, return a job id, process in the background |

## Common mistakes
- Checking authentication but not authorization on the specific object.
- Business logic inside controllers or SQL strings built by concatenation.
- Returning 200 with an error body, or 500 for client mistakes.
- Retrying non-idempotent calls blindly.
- Unbounded queries and uploads.
- Logging request bodies with passwords or tokens.

## Verification
- Run the project's tests and add tests for the new behavior, including a rejected input and a forbidden access.
- Call the endpoint for real (test client, curl or an HTTP tool) and inspect responses for success and failure cases.
- Confirm status codes and error shapes match the contract.
- State anything not exercised (for example concurrency, load, real third-party calls).

## Deliverables
API contract, implementation, tests, notes on auth, limits, and operational behavior.

## References
- [API conventions](references/api-conventions.md)
- [API contract template](templates/api-contract.md)
