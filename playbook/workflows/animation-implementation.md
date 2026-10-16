# Workflow: Adding animation and motion

Requires: [core principles](../core/00-core-principles.md)

## When to use
Adding or reviewing transitions, micro-interactions, scroll effects, SVG, canvas or 3D animation, or cinematic sequences.

## Inspect first
- Existing motion tokens, animation library and conventions in the project
- The product type (functional tool or creative showcase)
- Browser and device support, and whether reduced-motion handling exists
- Whether a browser and a performance profiler are available

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [motion-design](../../skills/motion/motion-design/SKILL.md) | Always |
| [ui-animation](../../skills/motion/ui-animation/SKILL.md) | Always |
| [reduced-motion-accessibility](../../skills/motion/reduced-motion-accessibility/SKILL.md) | Always |
| [animation-performance](../../skills/motion/animation-performance/SKILL.md) | Always |
| [micro-interactions](../../skills/motion/micro-interactions/SKILL.md) | Controls need feedback details |
| [scroll-animation](../../skills/motion/scroll-animation/SKILL.md) | Effects are tied to scrolling |
| [svg-canvas-3d-animation](../../skills/motion/svg-canvas-3d-animation/SKILL.md) | The animation is illustrative, particle-based, data-driven or 3D |
| [cinematic-motion](../../skills/motion/cinematic-motion/SKILL.md) | The page is a creative or storytelling experience |
| [animation-planning-and-review](../../skills/animation-production/animation-planning-and-review/SKILL.md) | The sequence is multi-step or story-driven, or a review is requested |
| [visual-qa](../../skills/frontend/visual-qa/SKILL.md) | The result must be checked in a rendered browser |

## Steps
1. For each animation, answer the ten questions in the motion spec (purpose, what moves first, timing, interruption, reduced motion, verification).
2. Choose the technique with the least cost that meets the need (CSS, Web Animations API, SVG, canvas, WebGL, library).
3. Implement with the project's motion tokens, animating transform and opacity where possible.
4. Implement exit and interruption behavior and the reduced-motion alternative.
5. Clean up listeners, observers, loops and GPU resources on teardown.
6. Check frame cost with a profiler or the code-level checks; record numbers only if measured.
7. Review start, middle, end, repeat and interruption; run the review rubric for larger work.

## Decisions
| Situation | Do this |
| --- | --- |
| Cannot state what an animation communicates | Do not animate it |
| A library is proposed | Use the library selection criteria; prefer the project's existing tool |
| Creative page versus product UI | Use cinematic motion only for the creative page; keep functional screens quiet |

## Artifacts
- Motion spec per animation
- Implementation with reduced-motion variant
- Performance notes
- Review report for larger work

## Verify
- Slowed playback and rapid retriggering behave correctly
- Reduced-motion variant exercised
- No layout shift; frame budget met on the stated profile, or marked not measured
- Memory and listeners return to baseline after unmount

## If verification fails
1. Jank: profile first; replace layout-affecting properties; reduce area and count.
2. Animation fights the layout: use FLIP or layout animation instead of animating size.

## Final report
- Animations added and their purposes
- Techniques and libraries used and why
- What was measured versus reasoned
- Reduced-motion behavior

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [ui-implementation](ui-implementation.md): for the surrounding interface
