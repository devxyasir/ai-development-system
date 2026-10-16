---
name: observability-and-incident-response
description: "Makes systems diagnosable and handles production incidents: structured logs, metrics, traces, health checks, alerts, SLIs and SLOs, timeouts and backpressure, and the incident process of triage, mitigation, communication, recovery and blameless post-incident review. Use when adding logging or monitoring, designing alerts, investigating a production problem, or responding to an outage."
metadata:
  category: delivery
  version: "0.1.0"
  related: "debugging, ci-cd-and-deployment, backend-api-design, security-review, performance-analysis"
---

# Observability and incident response

You cannot fix what you cannot see. Make failures visible and diagnosable without hiding them or leaking sensitive data, and when something breaks, restore service first and find the cause second.

## When to use
- Adding logs, metrics, traces, health checks or alerts; defining reliability targets.
- A live problem: errors, slowness, outage, suspicious activity.
- Root-cause analysis after the fact is in debugging; this skill covers the response and the review.

## Procedure: build observability
1. **Logs:** structured (JSON), consistent fields (timestamp, level, service, request id, user or tenant id where permitted, operation, outcome, duration); levels used consistently; log errors with context and the cause, not only a message. Never log secrets, tokens, full card or national id numbers, or unnecessary personal data.
2. **Metrics:** for services, track rate, errors and duration per endpoint (RED); for resources, utilization, saturation and errors (USE); add business metrics for key outcomes (orders, signups). Keep label cardinality low.
3. **Traces:** propagate a request or trace id across services and into logs; trace slow paths and external calls.
4. **Health checks:** liveness (process alive) and readiness (can serve; dependencies reachable); cheap and safe to expose.
5. **Alerts:** alert on user-facing symptoms (error rate, latency, failed key flows, saturation approaching limits), not on every cause; each alert has an owner and a runbook link; tune to avoid noise.
6. **Reliability targets (when warranted):** choose indicators users feel (availability, latency), set objectives (for example a percentage over a window), and track error budget; do not invent targets without business input.
7. **Failure behavior:** timeouts on every outbound call, bounded retries with backoff and jitter, circuit breakers, backpressure and queue limits, graceful degradation.
8. **Avoid cost surprises:** log volume, metric cardinality and trace sampling have costs; sample and set retention.

## Procedure: incident response
1. **Detect and declare:** confirm impact (who, what, since when); assign a lead; open an incident record ([incident report template](templates/incident-report.md)).
2. **Triage severity:** by user impact and scope (for example: full outage or data loss is highest; degraded feature is lower).
3. **Mitigate first:** the fastest safe way to stop the harm, usually roll back the last change, disable a feature flag, scale up, fail over, or block abusive traffic. Do not start deep debugging while users are down if a rollback is available.
4. **Communicate:** short factual updates to stakeholders on a regular cadence: impact, what is known, what is being done, next update time. No speculation.
5. **Investigate with evidence:** timeline of changes and alerts, logs, metrics, traces; form and test hypotheses one at a time (see debugging).
6. **Resolve and verify:** confirm metrics and user flows have recovered; keep monitoring; record the resolution time.
7. **Review within days:** blameless post-incident review: timeline, impact, root cause (and contributing factors), what went well, what did not, and action items with owners and dates. Fix the process and the system, not the person.
8. **Security incidents:** preserve evidence, limit access, rotate credentials, follow legal and disclosure obligations; involve the responsible people early.

## Decision rules
| Situation | Do this |
| --- | --- |
| Recent deploy correlates with the problem | Roll back first, investigate after |
| Alert fires constantly and is ignored | Fix or delete the alert; do not leave noise |
| Cannot tell what failed | Add the missing log, metric or trace, then redeploy; make failures louder |
| Sensitive data appears in logs | Remove it, rotate if secrets, add redaction at the logging layer |
| Unsure of severity | Treat as higher until impact is understood |

## Common mistakes
- Logging only success paths or only messages with no context.
- Swallowing exceptions so failures disappear.
- Alerting on CPU instead of user impact.
- Skipping the post-incident review, so the same failure repeats.

## Verification
- Induce or simulate a failure in a safe environment and confirm the logs, metrics, alerts and traces make it diagnosable.
- Confirm no secrets or personal data in logs (search samples).
- After an incident: recovery verified with metrics and a user-flow check; review actions assigned.

## Deliverables
Logging and metrics conventions, dashboards and alert definitions, runbooks, incident report and review.

## References
- [Incident report template](templates/incident-report.md)
