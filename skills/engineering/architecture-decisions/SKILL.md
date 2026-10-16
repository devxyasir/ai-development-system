---
name: architecture-decisions
description: "Guides architecture work: discovering the existing architecture, mapping requirements to structure, choosing proportionate patterns (layered, modular monolith, microservices, event-driven, hexagonal, plugin), module boundaries, dependency direction, data ownership, failure isolation, and recording decisions in ADRs. Use when starting a system, adding a major capability, splitting or merging services, or when asked which architecture to use."
metadata:
  category: engineering
  version: "0.1.0"
  related: "requirements-and-research, backend-api-design, database-engineering, security-review, observability-and-incident-response"
---

# Architecture decisions

Architecture is the set of decisions that are expensive to change. Make the fewest of them, make them from stated requirements, and record why.

## When to use
- New system or major feature; splitting, merging or migrating components; choosing patterns or infrastructure.
- Understanding an unfamiliar codebase's structure.
- Not for: small changes inside an established structure (follow the existing patterns).

## Procedure
1. **Discover the existing architecture** (existing projects): read manifests, entry points, directory tree, configuration, deployment files; trace one request end to end; list modules and their dependencies; run the tests; check recent history for hotspots. Write a one-page map.
2. **Extract architecturally significant requirements:** scale and growth, latency, availability, consistency needs, security and compliance, team size and skills, deployment constraints, budget.
3. **Draw module boundaries** by business capability and by what changes together; keep dependencies pointing inward toward stable code (domain does not depend on frameworks or I/O).
4. **Choose a pattern** with [the pattern guide](references/patterns.md). Default to the simplest structure that meets the requirements (usually a modular monolith). Justify any added complexity with a requirement.
5. **Define data ownership:** each piece of data has one owner; others read through an interface or event.
6. **Plan failure isolation:** timeouts, retries with limits, circuit breakers, queues for slow or unreliable work, graceful degradation.
7. **Plan observability and testing** as part of the design: logs, metrics, health checks; how each module is tested in isolation and together.
8. **Write an ADR** for each significant decision using the [ADR template](templates/adr.md); for larger designs fill the [technical design template](templates/technical-design.md).
9. **Review** the design against requirements; list risks and what would trigger revisiting.

## Choosing a structure (summary)
| Situation | Prefer |
| --- | --- |
| New product, small team, uncertain requirements | Modular monolith |
| Independent scaling or deployment needed by different teams | Services along stable boundaries |
| Workflows with slow or unreliable steps | Queue or background jobs |
| Many consumers of the same facts | Events, with an outbox for reliability |
| Core logic must not depend on frameworks | Ports and adapters (hexagonal) |
| Behavior extended by third parties | Plugin architecture |
| Legacy system | Strangler approach: wrap and replace part by part |

## Decision rules
- No architecture is universally better; each has costs. Compare on the project's requirements, not on popularity.
- If you cannot name the requirement that needs the complexity, do not add it.
- Prefer reversible decisions; isolate irreversible ones behind interfaces.
- Distributed systems add network failure, consistency and operational cost; adopt them with a concrete reason.

## Common mistakes
- Microservices for a small team with one deployable product.
- Layers that only forward calls.
- Shared database tables between services.
- Choosing technology before listing requirements.
- Undocumented decisions that no one can revisit.

## Verification
- Every added component maps to a stated requirement.
- Dependency direction checked (a tool or a grep for forbidden imports); no cycles between modules.
- Failure of each external dependency has a defined behavior.
- ADRs exist for the major choices; open risks are listed.
- State what was not validated (for example load behavior not tested).

## Deliverables
Architecture map or design, ADRs, risk list, test and observability plan.

## References
- [Pattern guide](references/patterns.md)
- [ADR template](templates/adr.md)
- [Technical design template](templates/technical-design.md)
