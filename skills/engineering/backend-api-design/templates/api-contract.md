# API contract: <operation name>

Method and path: <POST /orders> | Version: <v1> | Owner: <team>

## Purpose
<One sentence on what the caller achieves>

## Authentication and authorization
- Auth required: <yes / no, method>
- Permission needed: <role or policy, and object-level rule>

## Request
| Part | Field | Type | Required | Validation | Notes |
| --- | --- | --- | --- | --- | --- |
| Path | <id> | <string> | yes | <format> | <...> |
| Query | <limit> | <integer> | no | <1-100, default 50> | <...> |
| Header | <Idempotency-Key> | <string> | <yes for this operation> | <length> | <...> |
| Body | <field> | <type> | <yes/no> | <rules> | <...> |

Example request:
```json
{ "example": "replace with a realistic request" }
```

## Responses
| Status | When | Body |
| --- | --- | --- |
| 201 | Created | <schema> |
| 400 | Validation failure | <error shape> |
| 401 / 403 | Not authenticated / not permitted | <error shape> |
| 404 | Not found | <error shape> |
| 409 | Duplicate or version conflict | <error shape> |
| 429 | Rate limited | <error shape, Retry-After> |

Example success response:
```json
{ "example": "replace with a realistic response" }
```

## Behavior
- Idempotency: <how repeats are handled>
- Concurrency: <locking or constraints>
- Side effects: <events emitted, jobs queued, emails sent>
- Limits: <page size, payload size, rate limit>
- Performance expectation: <target and how measured>

## Errors and edge cases
- <case and behavior>

## Tests required
- [ ] Success path
- [ ] Each validation failure
- [ ] Permission failure (another user's resource)
- [ ] Duplicate or retry
- [ ] Concurrency or conflict
