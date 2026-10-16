---
name: scroll-animation
description: "Builds scroll-based animation: scroll-triggered reveals, scroll-linked transforms and progress bars, sticky and pinned sections, parallax, and long-form storytelling, with correct cleanup and fallbacks. Use when adding scroll effects to a page, when scroll animation is janky or hides content, or when deciding whether a scroll effect helps reading and navigation."
metadata:
  category: motion
  version: "0.1.0"
  related: "motion-design, animation-performance, reduced-motion-accessibility, cinematic-motion"
---

# Scroll animation

Scroll effects tie motion to the user's position. They help when position carries meaning (progress, sequence, depth) and hurt when they slow reading, hijack scrolling, or hide content if scripts fail.

## When to use
- Adding reveals, progress indicators, pinned or sticky sections, parallax or story sequences tied to scroll.
- Diagnosing scroll jank or content that never appears.
- Not for: general component transitions (ui-animation) or full cinematic pages (cinematic-motion, which builds on this skill).

## Procedure
1. **Decide if scroll should drive anything.** Keep it for: progress indication, revealing sequential steps, linking a diagram to the text being read, subtle depth. Skip it for ordinary content pages and for anything users must read quickly.
2. **Never hijack scrolling.** Do not override scroll speed or direction, and do not block native scroll. Pinned sections must release naturally and stay keyboard and touch scrollable.
3. **Content must be visible without the effect.** Hide elements for reveal only after confirming scripting works (add a `js` class to the root) and never leave them hidden if the observer fails.
4. **Pick the mechanism** with the table below.
5. **Animate transform and opacity only,** with small distances (8-24 px) and short durations; scroll-linked effects update every frame so they must be cheap.
6. **Reveal once.** Unobserve after the first reveal unless re-entry carries meaning.
7. **Clean up:** disconnect observers, remove listeners, kill timelines and trigger instances when the component unmounts or the route changes.
8. **Add the reduced-motion version:** show content immediately, replace parallax with static layout, keep progress indicators (they are informative and not motion-heavy) or make them step-based.
9. **Test:** fast scroll, scroll jump (anchors, Home/End), resize and orientation change, back/forward restore, keyboard scrolling, touch inertia, and no-JavaScript.

## Choosing a mechanism
| Need | Mechanism | Notes |
| --- | --- | --- |
| Reveal when entering the viewport | `IntersectionObserver` | Works everywhere; one observer for many elements |
| Scroll-linked progress, parallax, view-based fade | CSS `animation-timeline: scroll()` / `view()` | Not supported everywhere; guard with `@supports` and keep a fallback |
| Sticky headers, sidebars | `position: sticky` | No script needed |
| Pinned storytelling with scrubbed timelines | Timeline library (GSAP ScrollTrigger and similar) | Verify current API and license before adding |
| Section snapping | CSS `scroll-snap-type` | Use `proximity` for reading content; `mandatory` only for slideshows |
Code for each: [scroll recipes](references/scroll-recipes.md).

## Decision rules
| Situation | Do this |
| --- | --- |
| Text-heavy article | Only a reading-progress bar and maybe sticky table of contents |
| Marketing page | Reveals for sections, parallax on one or two decorative layers at most |
| Data story with a chart that changes per paragraph | Sticky chart, steps drive state via observer |
| Mobile | Lower the effect count and distances; avoid fixed backgrounds (poor support and cost) |

## Common mistakes
- `scroll` event handlers that read layout and write styles every event (layout thrashing). Use observers, CSS timelines, or rAF-throttled passive listeners.
- Hidden-until-revealed content that stays invisible for users without scripting, with print, or with find-in-page.
- Parallax that moves text, making it hard to read.
- `position: fixed` backgrounds that jank on mobile.
- Leaving observers and timelines alive after navigation.

## Verification
- With scripting disabled and with reduced motion on, all content is visible and readable.
- Scroll quickly and by jump; elements end in their final state.
- Performance profile of a long scroll shows no long frames from scroll handlers (see animation-performance); if no profiler is available, say so.
- Resize across breakpoints and rotate a device or emulator; layout and triggers still correct.
- Unmount or navigate away and confirm observers and listeners are gone (check in dev tools or by instrumenting).

## Deliverables
Scroll behavior spec, implementation with fallbacks and cleanup, reduced-motion behavior, test notes.

## References
- [Scroll recipes](references/scroll-recipes.md)
