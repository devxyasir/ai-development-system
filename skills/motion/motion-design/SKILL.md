---
name: motion-design
description: "Defines purposeful motion for interfaces: what should move and why, timing, easing, duration, staggering, choreography, continuity between states, interruption behavior, and a consistent motion language. Use when adding or reviewing any animation or transition, when motion feels random, slow or jarring, or when asked for polish. Produces a motion spec before implementation."
metadata:
  category: motion
  version: "0.1.0"
  related: "ui-animation, micro-interactions, animation-performance, reduced-motion-accessibility, animation-planning-and-review, visual-design-direction"
---

# Motion design

Motion is communication. Decide what a movement tells the user before choosing how to build it. If the answer is "it looks more animated", do not animate.

## When to use
- Adding, changing or reviewing transitions and animations of any kind.
- Motion feels arbitrary, slow, jarring, or inconsistent between screens.
- Not for: building a specific component's animation code (ui-animation), tiny feedback details (micro-interactions), scroll effects (scroll-animation), or cinematic sequences (cinematic-motion).

## Procedure: answer ten questions per animation
Record the answers in a [motion spec](templates/motion-spec.md) before writing code.
1. **What is changing?** (element appears, leaves, moves, resizes, changes state)
2. **Why does it need to move?** Pick one: show spatial relationship, keep continuity between states, direct attention, give feedback, show progress, express brand. No reason means no animation.
3. **What should it communicate?** For example "this panel came from that button", "your action was received".
4. **Which element moves first?** Lead with the element the user is looking at or just acted on; supporting elements follow.
5. **How does it start and end?** Enter: decelerate (ease-out). Exit: accelerate (ease-in). Move between positions: ease-in-out. Constant-rate change (progress, loops, color): linear.
6. **What duration and easing?** Use the table below and the project's motion tokens.
7. **What if the user interrupts, cancels or repeats the input?** The animation must reverse or retarget smoothly from its current state, never queue or snap. Prefer CSS transitions (they retarget) for state-driven changes.
8. **How does it behave on mobile and low-power devices?** Use only transform and opacity when possible; shorten distances; drop decorative layers (see animation-performance).
9. **What happens with reduced motion?** Replace large movement with a fade or instant change; keep essential feedback (see reduced-motion-accessibility).
10. **How will it be verified?** See Verification.

## Duration starting points (heuristics, tune by feel and testing)
| Kind of change | Duration | Notes |
| --- | --- | --- |
| Hover, press, toggle feedback | 80-150 ms | Must feel instant |
| Tooltip, small popover, menu | 120-220 ms | Exit shorter than enter |
| Accordion, tab content, dropdown panel | 180-280 ms | |
| Dialog, drawer, bottom sheet | 200-350 ms | Larger travel, longer time |
| Route or page transition | 250-450 ms | Never block interaction longer than needed |
| Decorative or brand motion | 400-1000 ms+ | Only where it is the point (see cinematic-motion) |
Rules of thumb: exits are about 60-70% of the enter duration; larger distance or area means longer; never delay a response to input just to show an animation.

## Easing starting points
| Use | Value |
| --- | --- |
| Enter (decelerate) | `cubic-bezier(0.16, 1, 0.3, 1)` |
| Exit (accelerate) | `cubic-bezier(0.7, 0, 0.84, 0)` |
| Move on screen | `cubic-bezier(0.65, 0, 0.35, 1)` |
| Linear (progress, color) | `linear` |
| Spring-like feel | CSS `linear()` easing or a spring from your animation library; check support |

## Choreography and rhythm
- Stagger siblings by 20-50 ms, and cap the total (about 300-400 ms); with many items, animate in groups or only those in view.
- One focal motion per moment. If two things move, one is clearly primary and the other is quieter or later.
- Anticipation (small counter-movement) and follow-through (slight overshoot) suit expressive products; skip them in dense, professional tools.
- Keep the same easing and duration for the same kind of change across the whole product; consistency teaches the interface.
- Respect spatial logic: if a panel slides in from the right, it leaves to the right.

## Decision rules
| Situation | Do this |
| --- | --- |
| Frequent action (typing, toggling, sorting) | Keep motion under 150 ms or none |
| First-time or rare moment (onboarding success) | Slightly richer motion is acceptable |
| Content loads after an action | Show a stable placeholder; animate in only if it aids orientation |
| Layout changes size | Animate with FLIP or layout animations, not by animating width/height each frame |
| Unsure whether it helps | Build it, then compare with and without; remove it if no one can say what it communicates |

## Common mistakes
- Slow, floaty animations that make the product feel sluggish.
- Linear easing on entering and exiting elements.
- Animating everything on page load.
- Different durations for the same interaction in different places.
- Motion that blocks input or cannot be interrupted.

## Verification
- Every animation has a recorded purpose and answers to questions 1-10.
- Play each at real speed and at slowed speed (browser animation inspector or a temporary multiplier); check start, end and interruption.
- Trigger it twice quickly, reverse it mid-way, and enable reduced motion.
- Measure on a mid-range device or CPU-throttled profile when performance matters (see animation-performance). State what was not tested.

## Deliverables
Motion spec per animation, project motion tokens (durations and easings), list of animations intentionally omitted.

## References
- [Principles and timing](references/principles-and-timing.md): why the numbers work, choreography patterns, motion language by product type.
- [Motion spec template](templates/motion-spec.md)
- [Motion tokens](templates/motion-tokens.css)
