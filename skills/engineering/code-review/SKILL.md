---
name: code-review
description: "Reviews code changes for correctness, design fit, security, tests, performance and maintainability, with severity-ranked, actionable feedback and a clear verdict. Use when asked to review a diff, pull request or file, before merging your own work, or when preparing review feedback."
metadata:
  category: engineering
  version: "0.1.0"
  related: "testing-strategy, security-review, git-and-github, refactoring, development-operating-rules"
---

# Code review

A review answers: is this change correct, safe, understandable and tested, and does it fit the project? Give specific, ranked, actionable feedback.

## When to use
- Reviewing a diff, pull request or file; self-review before opening a pull request; summarizing risks of a change.
- Not for: implementing the fixes (do that separately after the review).

## Procedure
1. **Understand intent:** read the description, linked issue and acceptance criteria. If intent is unclear, say so in the review.
2. **Read the whole diff** (`git diff` against the base) and then the surrounding code of each changed area, including callers and tests. Do not review lines in isolation.
3. **Run the change** when possible: build, tests, lint, and the changed behavior. Note commands and results.
4. **Check in this order:**
   1. Correctness: does it do what was asked; edge cases; error handling; concurrency; data integrity.
   2. Security and privacy: input validation, authorization, secrets, injection, logging of sensitive data (see security-review).
   3. Design fit: follows project patterns, right layer, no needless abstraction, dependencies justified.
   4. Tests: new behavior and failure paths covered; tests would fail if the code broke.
   5. Performance: obvious unbounded work, N+1 queries, large allocations, blocking calls.
   6. Maintainability: naming, clarity, comments that explain why, dead code, duplication.
   7. Delivery: migrations, configuration, documentation, backwards compatibility, rollout and rollback.
5. **Write findings** with severity (below), location, why it matters and a suggested fix. Separate required changes from suggestions. Acknowledge what is done well and keep tone factual.
6. **Give a verdict:** approve, approve with comments, or request changes, with the blocking items listed.

## Severity
| Level | Meaning | Action |
| --- | --- | --- |
| Blocker | Bug, security issue, data loss risk, broken build or missing essential test | Must fix before merge |
| Major | Likely problem or significant design issue | Should fix before merge |
| Minor | Small improvement | Fix now or later |
| Nit | Style or preference | Optional |

## Decision rules
| Situation | Do this |
| --- | --- |
| Change is very large | Ask to split, or review by commit and list what you did not cover |
| Style disagreement not covered by the project's rules | Do not block; mark as nit |
| Unfamiliar area | State limits of your review; do not guess about behavior you did not check |
| Tests missing for new behavior | Blocker or Major, depending on risk |
| Reviewing your own change | Review the diff as if someone else wrote it; run the checks |

## Common mistakes
- Commenting on style while missing a logic or security issue.
- Vague feedback ("clean this up") with no concrete suggestion.
- Approving without running the code or tests when they were available.
- Rewriting the author's approach to your preference.

## Verification
- The review states what was run (commands) and what was only read.
- Every Blocker and Major includes a reason and a suggested fix.
- The verdict matches the findings.

## Deliverables
Review comments grouped by severity, verdict, list of commands run and areas not reviewed.

## References
- [Review template](templates/review.md)
