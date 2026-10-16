---
name: animation-planning-and-review
description: "Plans animation work before building (goals, storyboard, timing table, easing, assets, acceptance criteria) and reviews finished animation against a rubric with severity levels. Use when a request involves multi-step, multi-element or story-driven animation, when handing animation work to another agent, or when reviewing animation quality before release."
metadata:
  category: animation-production
  version: "0.1.0"
  related: "motion-design, cinematic-motion, ui-animation, animation-performance, reduced-motion-accessibility, visual-qa"
---

# Animation planning and review

Two jobs: plan an animation so it can be built once, correctly; and review the result with a consistent rubric instead of a feeling.

## When to use
- Multi-element, multi-step or story-driven animation, or any animation another person or agent will build from your plan.
- Reviewing animation quality before merge or release.
- Not for: single simple transitions (use motion-design and ui-animation directly).

## Procedure: plan
1. **Write the goal** in one sentence: what the viewer should understand or feel, and the product's motion language (from motion-design or visual-design-direction).
2. **List the scenes or states** and the trigger for each (load, scroll position, click, time).
3. **Fill the storyboard** ([template](templates/storyboard.md)): for each beat give time range, visual, motion, easing and duration tokens, sound if any, trigger, and reduced-motion version.
4. **Check the timing table for rhythm:** durations vary meaningfully; one primary motion at a time; total length acceptable; stagger capped.
5. **List assets and dependencies:** images, SVGs, fonts, models, libraries (with the reason each is needed).
6. **Pick implementation techniques** per beat (CSS, WAAPI, SVG, canvas, library) using ui-animation and svg-canvas-3d-animation.
7. **Define acceptance criteria** a reviewer can check (durations, no layout shift, reduced-motion behavior, frame budget on the target device).

## Procedure: review
1. **Watch it three ways:** normal speed, slowed (animation inspector or multiplier), and frame by frame for key moments.
2. **Score with the [review rubric](references/quality-review-rubric.md)** and log each finding with severity.
3. **Test interruption and repetition,** reduced motion, a throttled device profile, and keyboard use during the animation.
4. **Report** findings, severity, fixes, and what was not verified.

## Severity
| Level | Meaning | Example |
| --- | --- | --- |
| Blocker | Harms use, accessibility or performance | Flashing content; animation blocks input; reduced motion ignored |
| Major | Clearly wrong but usable | Janky frames on target device; inconsistent easing for the same change |
| Minor | Polish | Slightly long stagger; easing could be crisper |

## Common mistakes
- Planning only the happy path and not interruption.
- Storyboards without durations, so rhythm cannot be judged.
- Reviewing only on a fast machine.
- Treating subjective taste as a defect without stating the effect on the user.

## Verification
- Every beat has duration, easing, trigger and reduced-motion treatment.
- Every acceptance criterion has a way to check it.
- Review report lists severity, evidence (screenshot, recording, profile) or marks the item "reasoned only".

## Deliverables
Storyboard and timing table, asset list, acceptance criteria; review report with severities.

## References
- [Storyboard template](templates/storyboard.md)
- [Quality review rubric](references/quality-review-rubric.md)
