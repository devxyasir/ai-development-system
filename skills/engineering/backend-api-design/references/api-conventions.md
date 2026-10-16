# API conventions

Follow the project's existing conventions first. Use the defaults below when none exist.

## Resource and operation naming
- Plural nouns for collections: `/orders`, `/orders/{id}`. Verbs only for actions that are not resource changes: `POST /orders/{id}/cancel`.
- Consistent casing (pick `snake_case` or `camelCase` for JSON and keep it).
- Timestamps in UTC ISO 8601 text; money as integer minor units (or decimal strings) with a currency code; identifiers opaque strings.

## Status codes
| Code | Use |
| --- | --- |
| 200 / 201 / 204 | Success / created (with location) / success without body |
| 400 | Malformed request or validation failure |
| 401 | Not authenticated |
| 403 | Authenticated but not permitted |
| 404 | Resource does not exist (or must not be revealed) |
| 409 | Conflict (duplicate, version mismatch) |
| 422 | Semantically invalid (if the project distinguishes it from 400) |
| 429 | Rate limited; include a `Retry-After` header |
| 5xx | Server fault; never for client errors |

## Error format
Use one shape everywhere. The problem-details format (RFC 9457) is a standard choice:
```json
{ "type": "https://example.com/errors/validation", "title": "Validation failed", "status": 400,
  "detail": "email must be a valid address", "code": "validation_error",
  "errors": [{ "field": "email", "message": "must be a valid address" }], "request_id": "req_abc123" }
```
Messages are safe to show; internals go to logs keyed by `request_id`.

## Pagination
- Prefer cursor (keyset) pagination: `?limit=50&cursor=...`, stable sort by a unique key, response includes `next_cursor`.
- Offset pagination is acceptable for small, static sets; it gets slow and inconsistent for large or changing data.
- Always cap `limit` (for example 100).

## Idempotency
- Safe by definition: GET, HEAD. Idempotent: PUT, DELETE (repeating gives the same state).
- For POST that creates or charges: accept an `Idempotency-Key` header; store key plus request fingerprint plus response for a defined period; return the stored response on repeat; reject a reused key with a different payload.

## Concurrency control
- Optimistic locking: a `version` or `ETag`; update with `If-Match`; return 409 or 412 on mismatch.
- Database constraints (unique, foreign keys) are the last line of defense; do not rely on check-then-insert in code.

## Authentication and authorization
- Authentication: sessions with secure cookies, or short-lived tokens; follow the project's existing method.
- Authorization: central policy function; check permission on the specific object and action; deny by default.
- Never trust a role or user id sent by the client.

## Timeouts, retries, circuit breakers
- Every outbound call has a connect and total timeout.
- Retry only idempotent operations, with exponential backoff and jitter, a small attempt cap, and respect for `Retry-After`.
- Circuit breaker for dependencies that fail often, with a fallback or clear error.

## Rate limiting
- Per user or key and per IP for unauthenticated endpoints; stricter on login, password reset, and expensive endpoints; return 429 with `Retry-After`.

## File handling
- Limit size and type; validate content, not only extension; store outside the web root with generated names; scan if the risk warrants; stream large files instead of loading into memory.

## Background jobs
- Durable queue; job payload contains identifiers, not large data; idempotent handlers; retries with backoff and a dead-letter queue; expose job status.

## Logging
- Structured JSON logs; levels used consistently; include request id, user id (internal), and operation; never log secrets, tokens or full personal data.

## Versioning
- Prefer additive changes (new optional fields). For breaking changes use a version in the path or header and a documented deprecation period.
