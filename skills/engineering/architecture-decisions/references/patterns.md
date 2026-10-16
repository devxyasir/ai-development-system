# Architecture pattern guide

For each pattern: the problem it solves, when it fits, when it is unnecessary, costs, operational implications, failure modes, safe implementation and how to test it.

## Layered architecture
- **Solves:** separation of presentation, business logic and data access.
- **Fits:** most CRUD-style applications.
- **Unnecessary when:** layers merely forward calls with no logic.
- **Costs:** indirection. **Failure modes:** business logic leaking into controllers or queries; circular dependencies.
- **Implement:** controllers parse and validate; services hold rules; repositories handle storage; dependencies point down.
- **Test:** service tests with fake repositories; a few integration tests through the real stack.

## Modular monolith
- **Solves:** clear boundaries without distributed-system costs.
- **Fits:** most new products and small to mid-size teams.
- **Unnecessary when:** the system is tiny with a single concern.
- **Costs:** discipline to keep modules separate. **Failure modes:** boundaries erode through direct table access or shared models.
- **Implement:** one module per business capability with a public interface; no cross-module imports of internals; separate schemas or table ownership by module; enforce with lint rules or architecture tests.
- **Test:** module-level tests; one architecture test that fails on forbidden imports.

## Microservices
- **Solves:** independent deployment and scaling, team autonomy.
- **Fits:** multiple teams, clearly different scaling or reliability needs, stable boundaries.
- **Unnecessary when:** a small team, one product, unclear boundaries.
- **Costs:** network failures, distributed data, versioned contracts, deployment and observability overhead.
- **Operations:** per-service CI, monitoring, tracing, on-call.
- **Failure modes:** distributed monolith (services that must deploy together), chatty calls, shared databases.
- **Implement:** split along stable business boundaries, one data owner per service, timeouts and retries with backoff, idempotent operations, versioned APIs, tracing across services.
- **Test:** contract tests between services, a small set of end-to-end tests, failure injection for dependencies.

## Event-driven architecture
- **Solves:** decoupling producers from consumers; asynchronous workflows; fan-out.
- **Fits:** several consumers of the same fact; long-running or unreliable steps.
- **Unnecessary when:** one consumer and a simple call would do.
- **Costs:** eventual consistency, harder debugging, ordering and duplication concerns.
- **Failure modes:** lost or duplicated events, poison messages, unbounded queues.
- **Implement:** outbox pattern for reliable publishing, idempotent consumers, dead-letter queue, schema versioning, backpressure and limits.
- **Test:** consumer tests with duplicate and out-of-order events; integration test of the outbox.

## Hexagonal / clean architecture (ports and adapters)
- **Solves:** keeping domain logic independent of frameworks, databases and delivery mechanisms.
- **Fits:** logic-heavy domains, long-lived systems, multiple interfaces (API, CLI, jobs).
- **Unnecessary when:** thin CRUD with little logic.
- **Costs:** more files and mapping code. **Failure modes:** needless abstraction, ports for everything.
- **Implement:** domain core with ports (interfaces) it needs; adapters implement them; wiring at the edge.
- **Test:** core tested without I/O; adapters tested against real services or contract tests.

## Domain-driven design (where appropriate)
- **Solves:** complex business rules with shared language.
- **Fits:** rich domains with many rules and experts.
- **Unnecessary when:** simple data management.
- **Implement:** a ubiquitous language, bounded contexts, aggregates that protect invariants, domain events. Use selectively.

## Plugin architecture
- **Solves:** extending behavior without changing the core.
- **Implement:** a stable plugin interface, versioning, sandboxing or permission model for untrusted plugins, discovery and lifecycle.
- **Test:** a reference plugin as a contract test.

## Background jobs and async workflows
- **Solves:** slow or unreliable work off the request path.
- **Implement:** a durable queue, idempotent jobs with unique keys, retry with backoff and a cap, dead-letter handling, visibility into job status.
- **Test:** retries, duplicates, crashes mid-job.

## State management and caching
- Decide the source of truth first. Cache only what is expensive and tolerates staleness; define invalidation (time-based or event-based) and what happens on a cache miss storm. Test stale reads and invalidation paths.

## Migration from legacy systems
- Strangler: route a slice of traffic to the new component, keep the old one running, compare behavior, then retire the slice. Avoid big-bang rewrites. Keep data migration reversible and verified.

## Architecture decision checklist
1. Requirement that drives the choice is named.
2. At least one simpler alternative was considered and rejected with a reason.
3. Operational cost (deploy, monitor, debug) is estimated.
4. Failure behavior defined.
5. How it will be tested is defined.
6. Reversal or evolution path noted.
