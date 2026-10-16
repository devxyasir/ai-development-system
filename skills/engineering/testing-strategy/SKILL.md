---
name: testing-strategy
description: "Chooses, writes and reports tests by risk: unit, integration, API, contract, end-to-end, performance, security, migration, regression and AI evaluation tests; covers normal, boundary, invalid, permission, failure, repeated and concurrent cases, and honest reporting of what ran. Use when adding tests, deciding what to test, fixing flaky tests, or before declaring work verified."
metadata:
  category: engineering
  version: "0.1.0"
  related: "frontend-testing, debugging, code-review, backend-api-design, database-engineering"
---

# Testing strategy

Tests exist to find real failures and to protect behavior over time. Choose them by risk, write them around behavior, run them, and report exactly what happened.

## When to use
- Any code change that needs verification; deciding what to test; flaky or slow tests; before claiming work is done.
- Front-end specifics are in frontend-testing; this skill covers the general approach.

## Procedure
1. **Find how tests run:** test framework, commands, fixtures, CI configuration, naming and layout conventions. Run the existing suite first to learn the baseline (which tests already fail).
2. **List behaviors and risks** of the change: what must work, what could break, what is costly if wrong (money, data, security, availability).
3. **Pick the lowest level that proves each behavior** using [test types](references/test-types.md).
4. **Design cases** for: normal behavior, boundary values (empty, one, many, maximum, off by one), invalid inputs, permissions (allowed and forbidden), failure modes (dependency down, timeout, partial failure), repeated operations (idempotency), concurrency where relevant, data integrity, and regression of fixed bugs.
5. **Write clear tests:** one behavior per test, a name that states the behavior, arrange-act-assert structure, minimal setup, no dependence on test order, deterministic data (fixed seeds and clocks).
6. **Mock only boundaries** (network, clock, randomness, third-party services); prefer real collaborators and a real or containerized database for integration tests.
7. **Run the tests** and read the output. For a bug fix, confirm the new test fails before the fix and passes after.
8. **Run broader checks:** the full suite, lint, type check, build.
9. **Report** using the format below.

## Decision rules
| Situation | Do this |
| --- | --- |
| Logic with many branches | Parameterized unit tests |
| Code that talks to a database | Integration tests against a real database engine |
| Service boundary between teams | Contract test of requests and responses |
| User journey that must never break | One or two end-to-end tests |
| Flaky test | Find the race, shared state or timing; fix the cause, never add sleeps or ignore |
| Test count targets requested | Prefer meaningful coverage of risks; coverage numbers show what is untested, not what is tested well |
| Legacy code without tests | Add characterization tests around the part you will change |

## Common mistakes
- Tests that pass without asserting anything meaningful.
- Mocking the unit under test, or everything, so only mocks are tested.
- Asserting implementation details instead of behavior.
- Skipping failure and permission paths.
- Marking tests skipped or loosening assertions to get green.

## Verification
- Tests were run; commands and results are recorded.
- New tests fail when the behavior is broken (mutation check by reverting or breaking code temporarily).
- No tests were disabled, skipped or weakened to pass; if any were, it is reported with the reason.

## Report format
- **Commands run:** exact commands.
- **Passed:** counts or names.
- **Failed:** names and causes; whether they were failing before.
- **Not run or not covered:** what remains unverified and why.

## Deliverables
Tests, commands, and the report above.

## References
- [Test types](references/test-types.md): what each type is for, when to use it, what it does not prove.
- [Test plan template](templates/test-plan.md)
