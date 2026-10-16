---
name: frontend-testing
description: "Plans and writes front-end tests: unit and component tests (user-centered queries), integration with mocked network, end-to-end browser tests, accessibility tests, visual regression, and test reliability, matched to risk. Use when adding tests to UI code, when front-end tests are flaky or brittle, or when deciding which kind of test a UI change needs."
metadata:
  category: frontend
  version: "0.1.0"
  related: "testing-strategy, accessibility-review, visual-qa, component-engineering, frontend-architecture"
---

# Frontend testing

Test what users and callers rely on, at the cheapest level that proves it. Report exactly what ran and what it does not prove.

## When to use
- Adding or changing UI behavior; deciding which tests it needs; fixing flaky tests.
- Not for: general test strategy across backend and data (testing-strategy).

## Procedure
1. **Inspect the setup:** test runner, assertion and rendering libraries, mocking approach, E2E tool, existing patterns, how tests run in CI. Reuse them.
2. **List behaviors to protect** from the change: what the user can do and see, important states, error paths, permissions.
3. **Choose the level** with the table below, as low as proves the behavior.
4. **Write tests around behavior:** render the component, interact as a user would (click, type, keyboard), assert on visible results and accessible roles and names. Avoid asserting on internal state, class names or implementation details.
5. **Control the environment:** fake the network at the boundary (a request interceptor or mocked client), freeze time, seed random data, reset state between tests. Do not mock the component under test.
6. **Cover failure paths:** loading, error, empty, validation failures, permission-denied, rapid repeated actions.
7. **Add accessibility checks** to component and E2E tests where the project supports it (an automated rule engine plus keyboard assertions). Automated checks do not replace manual review.
8. **Add visual regression** only for stable, design-critical components or pages; review diffs by eye; keep the baseline set small to limit noise.
9. **Run the tests** (and lint and type checks), fix failures at the cause, and run again several times if a test touches timing.

## Choosing the level
| Behavior | Level | What it does not prove |
| --- | --- | --- |
| Pure functions, formatters, reducers | Unit | Anything about rendering |
| A component's behavior and states | Component (rendered, user-event) | Real browser layout, real network |
| A feature across components with data | Integration with mocked network | Real backend contract |
| Critical journey (sign in, checkout) | End-to-end in a real browser | Edge cases; it is slow and costly, so keep it few |
| API contract between front and back end | Contract test or schema validation | UI behavior |
| Appearance of a stable component | Visual regression | Behavior |

## Decision rules
| Situation | Do this |
| --- | --- |
| Bug fix | Write a failing test that reproduces it first |
| Flaky test | Find the race (missing await, shared state, real timers, network); never add arbitrary sleeps |
| Many near-duplicate tests | Parameterize |
| Query choice | Prefer by role and accessible name, then label text, then text; test ids as the last resort |
| Third-party widget | Test your integration boundary, not the library |

## Common mistakes
- Testing implementation details so refactors break tests.
- Snapshot tests of large trees that nobody reads.
- E2E tests for everything.
- Asserting only the happy path.
- Fixed `sleep` waits instead of waiting for a condition.

## Verification
- Run the new tests and the whole relevant suite; report commands and results.
- Break the behavior on purpose (or revert the fix) and confirm the test fails.
- State what remains unverified (browsers not tested, real backend not exercised, visual appearance not reviewed).

## Deliverables
Tests, test commands, list of covered and uncovered behaviors.

## References
This skill is self-contained. For test strategy beyond the front end, also load testing-strategy.
