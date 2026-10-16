# Workflow: Integrating an external API or service

Requires: [core principles](../core/00-core-principles.md)

## When to use
Calling a third-party API or service, or exposing an integration to partners.

## Inspect first
- The provider's current official documentation, version and authentication method
- Existing integrations in the project and their wrapper conventions
- Rate limits, quotas, pricing and data-handling terms
- How credentials are stored and rotated in the project

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [requirements-and-research](../../skills/engineering/requirements-and-research/SKILL.md) | Always |
| [backend-api-design](../../skills/engineering/backend-api-design/SKILL.md) | Always |
| [security-review](../../skills/engineering/security-review/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [observability-and-incident-response](../../skills/delivery/observability-and-incident-response/SKILL.md) | The integration is critical and needs monitoring and alerts |
| [ai-llm-engineering](../../skills/specialist/ai-llm-engineering/SKILL.md) | The service is a model or AI provider |

## Steps
1. Read the official documentation for the exact version; confirm endpoints, parameters and error formats exist as you plan to use them.
2. Put the integration behind a small interface (client wrapper) so it can be tested and replaced.
3. Store credentials in the secret store or environment; never in code or logs.
4. Set timeouts; retry only idempotent calls with backoff, jitter and a cap; respect rate-limit headers.
5. Map provider errors to your own error types; do not leak provider details to end users.
6. Validate and sanitize data coming back; treat it as untrusted.
7. Test with a recorded or mocked provider and, if safe, a sandbox account; test failure modes (timeout, 429, 5xx, malformed response).
8. Add logging and metrics for calls, errors and latency, without secrets or personal data.

## Decisions
| Situation | Do this |
| --- | --- |
| Provider has a sandbox | Use it for integration tests; never test against production with real data |
| Webhooks are used | Verify signatures, handle duplicates and ordering, respond quickly and process asynchronously |
| Costs scale with usage | Add budgets, caching where valid, and alerts |

## Artifacts
- Client wrapper and tests
- Configuration documentation
- Notes on limits, costs and failure behavior

## Verify
- Calls succeed against a sandbox or are verified by recorded fixtures (state which)
- Failure modes produce the intended behavior
- No secrets in code, logs or test output

## If verification fails
1. Documentation does not match behavior: capture the real request and response, note the discrepancy, follow observed behavior.
2. Rate limited: add backoff and queueing; do not hammer.

## Final report
- What was integrated and how
- What was tested against the real service versus mocks
- Credentials handling
- Limits, costs and open risks

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [deployment](deployment.md): when new credentials or configuration must reach an environment
