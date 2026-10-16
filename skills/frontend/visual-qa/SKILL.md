---
name: visual-qa
description: "Inspects rendered interfaces critically: layout and alignment, typography and wrapping, contrast, spacing consistency, responsive behavior, component states, animation, overflow and clipping, realistic content, loading, empty and error states, with an issue-severity system. Use after building or changing UI, before release, or when asked to review how an interface looks and behaves."
metadata:
  category: frontend
  version: "0.1.0"
  related: "design-to-code, accessibility-review, animation-planning-and-review, frontend-testing, layout-and-responsive-design"
---

# Visual QA

Look at the real rendered result, not just the code. Find problems before users do, rank them, and fix the ones that matter. Never claim visual verification when only source code was read.

## When to use
- After building or changing any UI, before merging or releasing, or when asked to review appearance and behavior.
- Not for: deciding the design direction (visual-design-direction) or code review of logic (code-review).

## Procedure
1. **Establish what is available.** Can you run the app and drive a browser, take screenshots, or inspect the DOM? Choose the strongest option: automated browser with screenshots, then a headless render, then manual instructions for the user. Say which level you reached.
2. **Prepare realistic states:** real-length content, long and short strings, many and zero items, error responses, slow loading, logged-in and logged-out, right-to-left if supported.
3. **Capture** each key screen at widths 320, 375, 768, 1024 and 1440 (and one very wide), in each theme. Save screenshots with names that state screen, width and state.
4. **Run the [checklist](references/checklist.md)** on each capture. Log findings with severity using the [report template](templates/qa-report.md).
5. **Exercise interactions:** hover, focus (keyboard), active, disabled, open and close of overlays, form validation, navigation, loading and error transitions, and animation start, middle, end and interruption.
6. **Compare across screens** for consistency of spacing, type, color, component shapes and motion.
7. **Fix** Blockers and Majors first, re-capture, and confirm the fix did not cause new issues; record Minors that remain.
8. **Report** what was verified visually, what was reasoned from code only, and what was not checked.

## Severity
| Level | Meaning | Examples |
| --- | --- | --- |
| Blocker | Task cannot be completed or content is unreadable | Overlapping controls; button off-screen on mobile; text clipped; unreadable contrast |
| Major | Clearly broken or inconsistent, task still possible | Misaligned columns; missing hover or focus state; layout shift on load |
| Minor | Polish | 2 px misalignment; slightly uneven spacing; icon weight mismatch |
| Note | Observation or suggestion | Possible improvement, not a defect |

## Decision rules
| Situation | Do this |
| --- | --- |
| No browser tool | Say so; review code for the checklist items and give the user steps to verify |
| Screenshot shows a bug that code review missed | Trust the render; investigate |
| Cosmetic nit versus deadline | Fix Blockers and Majors; list Minors |
| Visual diff tool exists | Use it for regressions, then still inspect manually |

## Common mistakes
- Checking only the default desktop width and default data.
- Reporting "looks good" without capturing anything.
- Ignoring focus, error and empty states.
- Fixing a symptom by hiding overflow.

## Verification
- A list of screens, widths, themes and states actually captured, with file names.
- Every Blocker and Major has a fix and a re-capture, or is reported as open.
- The final message states the verification level: rendered and inspected, rendered by tool without human review, or code-only.

## Deliverables
QA report with severities and evidence, fixes applied, remaining issues.

## References
- [Checklist](references/checklist.md)
- [QA report template](templates/qa-report.md)
