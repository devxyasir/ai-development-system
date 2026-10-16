# Deployment options

## Comparison
| Option | Operational burden | Good for | Watch out for |
| --- | --- | --- | --- |
| Static hosting plus CDN | Very low | Sites, SPAs, docs | No server logic; form handling and APIs need other services |
| Managed platform (PaaS) | Low | Web apps and APIs with simple needs | Cost at scale, platform limits, vendor specifics |
| Single VPS | Medium | Small apps, full control, predictable cost | You own patching, backups, monitoring, TLS renewal, downtime during updates |
| Containers on a managed service | Medium | Repeatable multi-service deployments | Image hygiene, networking, secrets handling |
| Serverless functions | Low to medium | Event-driven, spiky load | Cold starts, execution limits, local testing, vendor coupling |
| Container orchestrator | High | Large multi-team systems | Complexity, cost; justify with concrete needs |

## Container image practices
- Multi-stage builds; pin base image versions; run as a non-root user; minimal base images; `.dockerignore` to keep secrets and junk out; no secrets baked into images; scan images; define health checks.

## VPS baseline
- Non-root deploy user, SSH keys only, firewall allowing needed ports, automatic security updates, reverse proxy (with TLS via an ACME client such as Let's Encrypt), process manager, log rotation, backups with restore tests, monitoring and alerts.

## TLS, DNS and domains
- Use TLS everywhere with automatic renewal; verify certificate and chain with a client check. Lower the DNS TTL before a planned cutover; keep the old target running until traffic moves; confirm propagation from more than one resolver.

## Environment variables and secrets
- Same variable names across environments; a documented list of required variables; validated at startup; secrets in a secret manager or the platform's secret store; rotate on exposure.

## Health checks
- Liveness: the process is running. Readiness: dependencies are reachable and it can serve traffic. Keep health checks cheap and do not expose sensitive details.

## Release strategies
| Strategy | Use when |
| --- | --- |
| Rolling | Stateless services, backward-compatible changes |
| Blue-green | Fast rollback needed; double capacity available |
| Canary | Risky changes; real traffic validation with a small share |
| Feature flags | Decouple deploy from release; gradual enablement |

## Cost and resource controls
- Set budgets and alerts; right-size instances; cap autoscaling; delete unused resources; watch egress and storage growth; for model or GPU workloads, track cost per request and schedule off-peak batch jobs.

## Infrastructure as code
- Keep infrastructure definitions in version control; review changes with a plan or preview step; separate state per environment; protect state files; avoid manual console changes that drift.
