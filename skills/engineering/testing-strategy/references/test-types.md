# Test types

| Type | Purpose | Use when | Does not prove |
| --- | --- | --- | --- |
| Unit | Logic of a function or class in isolation | Pure logic, calculations, parsers, state machines | That parts work together |
| Integration | Components with real collaborators (database, queue, file system) | Data access, service layers, framework wiring | Full user journeys, production scale |
| API | Requests through the HTTP interface | Endpoints, auth, validation, error shapes | UI behavior, third-party reliability |
| Contract | Producer and consumer agree on a schema or behavior | Services or front end and back end owned separately | Business correctness |
| Component (UI) | Rendered component behavior | UI states and interactions | Real browser layout, real network |
| End-to-end | A real user journey in a real browser or client | Critical flows (sign up, pay) | Edge cases (too slow to enumerate them) |
| Accessibility | Automated and manual checks | Any UI | Full usability for all users |
| Visual regression | Pixel or layout changes | Stable, design-critical views | Behavior or semantics |
| Performance | Latency, throughput, resource use under load | Hot paths, capacity limits, SLOs | Correctness; results depend on environment |
| Security | Abuse of auth, input, files, dependencies | Anything exposed to users | Absence of all vulnerabilities |
| Migration | Schema and data changes apply and (where reversible) revert | Every database migration | Production data quirks not present in the copy |
| AI evaluation | Quality of model-driven behavior against a labeled set | LLM features, retrieval, classifiers | Performance on unseen real-world inputs |
| Game | Simulation logic headlessly, plus playtests | Game rules, determinism, performance | Fun and balance (needs humans) |
| Regression | A specific past failure stays fixed | After every bug fix | New unrelated failures |

## Which case set to write
1. Normal use.
2. Boundaries: empty, single, maximum, off by one, unicode and long strings, time zones, daylight changes.
3. Invalid input: wrong type, missing, malformed, hostile.
4. Permissions: owner, other user, unauthenticated, admin.
5. Failures: timeouts, errors from dependencies, partial writes, retries.
6. Repetition: same request twice, double submit, replayed message.
7. Concurrency: two writers, interleaved operations.
8. Integrity: constraints hold; counts and totals reconcile.

## Test data and environment
- Create data inside the test; clean up or isolate (transactions, temporary databases, unique names).
- Fixed clock and seeded randomness.
- Avoid shared mutable fixtures.
- Make tests runnable with one command and in CI.

## Flaky test triage
1. Reproduce by running the test repeatedly and in isolation.
2. Look for: real time, random data, shared state, order dependence, un-awaited promises, network.
3. Fix the cause; quarantine only with an owner and a deadline.

## Coverage
Use coverage reports to find untested branches in code you changed. Do not set targets that reward trivial tests.
