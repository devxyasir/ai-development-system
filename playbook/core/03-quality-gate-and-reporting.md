# Quality gate and reporting

Requires: [core principles](00-core-principles.md)

Run this gate before declaring substantive work complete. Not every area applies; evaluate the relevant ones explicitly and skip the rest in one line ("not applicable: no UI changes"). The short checklist is [final verification](../checklists/final-verification.md).

## The gate
| Area | Questions | Evidence |
| --- | --- | --- |
| Requirements | Is the requested outcome delivered? Are the acceptance criteria met? | Each criterion marked with evidence |
| Architecture | Does it fit the existing project? Is added complexity justified by a requirement? | Which existing patterns were followed; why any new abstraction exists |
| Code | Is it understandable and maintainable? Are important errors handled? | Diff review; no dead code or debug output |
| Design | Is the interface suited to the product, responsive, accessible and functional? | Rendered inspection, or an explicit "not rendered" |
| Data and security | Are validation, permissions, secrets and data integrity handled? | Tests or review notes for each |
| Performance | Any obvious bottleneck, unbounded loop, query or payload? | Measurements, or "not measured" |
| Tests | Were relevant checks run? Are failure paths covered? | Commands and results |
| Delivery | Configuration, documentation, migration and deployment concerns addressed? | Files changed; steps listed |
| Truthfulness | Are assumptions and limits disclosed? | The "not verified" section is filled in |

## Severity of unresolved gaps
| Level | Meaning | Action |
| --- | --- | --- |
| Blocker | The task's goal is not met, data or security at risk, or the build fails | Do not report as done; fix or report as incomplete |
| Major | Works but with a significant known weakness | Fix, or report prominently |
| Minor | Polish | Report briefly |

## The final report
Use these four parts, in this order, in plain language:
1. **Done:** what changed (files and behavior), and how to use it.
2. **Verified:** exact commands and their outcomes; for visual work, widths and states rendered.
3. **Not verified:** what was not checked and why (tool unavailable, no access, out of scope).
4. **Risks and follow-ups:** decisions the user should make, things to watch, related problems noticed.
Keep it short. Do not pad with a changelog of every keystroke.

## Evidence rules
- A claim needs evidence: a command output, a file path and line, a rendered capture, or a source document.
- If evidence is old (from before your last edit), run it again.
- If a tool was unavailable (no browser, no network, no database), say what you did instead and what that cannot prove.

## When the gate fails
1. Fix what you can inside the task's scope.
2. Re-run the failed check.
3. If it still fails or cannot be fixed, report the failure and your best understanding of the cause. Do not hide it or lower the check.

## When you cannot finish
Use the fallback in [lower-capability support](04-lower-capability-support.md): stop at a safe state, hand off clearly, never present partial work as complete.
