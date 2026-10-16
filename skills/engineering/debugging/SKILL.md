---
name: debugging
description: "Finds and fixes bugs by root cause: reproduce, collect evidence, narrow the failure, form and test hypotheses one at a time, make the smallest reliable fix, add a regression test, and verify related behavior. Covers frontend, backend, database, build, dependency, race condition, performance, network, deployment and environment-specific problems. Use for any error, crash, wrong output, flaky behavior or production-only failure."
metadata:
  category: engineering
  version: "0.1.0"
  related: "testing-strategy, observability-and-incident-response, git-and-github, performance-analysis, development-operating-rules"
---

# Debugging

Debugging is evidence gathering, not guessing. Work from observed behavior to a proven cause, then fix the cause.

## When to use
- Errors, crashes, wrong results, flaky behavior, failing builds or tests, performance regressions, environment-specific bugs.
- Not for: live outage coordination (observability-and-incident-response covers mitigation and communication; use this skill for root cause afterwards).

## Procedure
1. **Capture the symptom precisely:** exact error message and stack trace, expected versus actual behavior, where and when it happens, how often, since when.
2. **Reproduce it.** Find the smallest input or steps that trigger it. If you cannot reproduce, gather more evidence (logs, versions, environment, recent changes) before changing code. Use the [bug report template](templates/bug-report.md) to record it.
3. **Collect evidence without changing behavior:** read logs and traces, run the failing test alone, check recent commits (`git log`, `git bisect` when the regression window is wide), compare working and failing environments (versions, configuration, data).
4. **Narrow the location** by bisection: which layer (UI, API, service, database, network, build) and which component. Add temporary logging or breakpoints at boundaries to see where data first goes wrong.
5. **Form hypotheses** that are specific and testable ("the cache returns a stale value after update because the key lacks the tenant id"). Rank by likelihood and cost to test.
6. **Test one hypothesis at a time** with an experiment that could disprove it. Record the result. Discard disproved hypotheses; do not stack changes.
7. **Identify the root cause,** not the trigger: ask why until the answer is a defect in code, configuration, data or design.
8. **Fix the smallest thing that removes the cause.** Do not suppress the error, add a blind retry, or rewrite broadly.
9. **Add regression protection:** a test that fails before the fix and passes after (see testing-strategy), or a monitor or assertion if a test is impractical.
10. **Verify:** the original reproduction passes, the related behavior still works, the full relevant test suite passes; remove temporary logging.
11. **Document remaining risks** and similar places the same defect may exist (search for the pattern).

## Where to look by symptom
| Symptom | First checks |
| --- | --- |
| Frontend error or blank page | Console and network panel, source maps, failing request, hydration mismatches, undefined data on first render |
| Backend exception | Stack trace, request payload, recent deploys, configuration and environment variables, null handling |
| Wrong data | Query and parameters, transaction boundaries, caching, time zones, rounding |
| Slow | Profile before guessing (see performance-analysis) |
| Works locally, fails in CI or production | Versions, environment variables, file paths and case sensitivity, permissions, time zone, data differences, missing services |
| Build or dependency failure | Full error from the first failure, lockfile and version conflicts, cache, Node or language version |
| Intermittent | Race conditions, shared state, ordering, timeouts, resource limits; add logging with timestamps and ids; run repeatedly |
| Network failure | DNS, TLS and certificates, proxies, timeouts, CORS (browser only), firewall |

## Decision rules
- Cannot reproduce after reasonable effort: report what was tried and what evidence is needed; do not ship speculative fixes presented as proven.
- Two causes plausible: test the cheaper one first, but keep the other in the record.
- Fix requires a risky change: isolate with a feature flag or fix narrowly now and file the larger refactor.

## Common mistakes
- Random edits until the error disappears.
- Fixing the symptom (catch and ignore, retry loop, increased timeout) while the cause remains.
- Changing several things at once, so the effective change is unknown.
- Declaring a fix without re-running the reproduction.

## Verification
- Reproduction steps before and after, with outputs.
- Regression test present and failing without the fix.
- Full relevant suite passes; unrelated failures are reported as pre-existing.
- State what could not be reproduced or verified.

## Deliverables
Root cause statement, minimal fix, regression test, notes on risk and similar code.

## References
- [Bug report template](templates/bug-report.md)
