---
name: animation-performance
description: "Implements and tunes animation performance: choosing CSS, Web Animations API, SVG, Canvas, WebGL or a library; compositor-friendly properties; avoiding layout thrash; requestAnimationFrame use; cancellation and cleanup; frame-time measurement and profiling. Use when animation stutters, when choosing an animation approach or library, or before shipping heavy animation."
metadata:
  category: motion
  version: "0.1.0"
  related: "motion-design, ui-animation, svg-canvas-3d-animation, frontend-performance, reduced-motion-accessibility"
---

# Animation performance

Smooth animation means each frame finishes inside its budget (16.7 ms at 60 Hz, 8.3 ms at 120 Hz) with the browser doing as little layout and paint work as possible. Measure first; guess second.

## When to use
- Animation drops frames, causes layout shift, or drains battery.
- Choosing between CSS, WAAPI, SVG, canvas, WebGL or a library, or deciding whether to add an animation dependency.
- Before shipping scroll-linked, canvas, or large-area animation.
- Not for: whether to animate at all (motion-design).

## Procedure
1. **Describe the scenario to test:** which animation, which device class (mid-range phone, throttled CPU, integrated GPU), which page state (heavy DOM, long list).
2. **Measure a baseline.** Use the browser Performance panel with CPU throttling (record the animation, look for long frames and the Main thread breakdown). Enable paint flashing and layer borders to see repaints and compositing. Record frame times, long tasks and layout/paint counts. If no profiler is available, say the result is estimated.
3. **Classify the cost by property:**
| Property type | Cost | Examples |
| --- | --- | --- |
| Compositor only | Cheapest | `transform`, `opacity` (and some `filter` on promoted layers) |
| Paint | Medium | `background-color`, `color`, `border-color`, `box-shadow` |
| Layout | Expensive | `width`, `height`, `top`, `left`, `margin`, `padding`, font size |
4. **Replace expensive properties:** move with `translate`, resize with `scale` (or FLIP), fade with `opacity`; animate shadows by crossfading a pseudo-element's opacity; keep text out of scaled layers when blur matters.
5. **Avoid layout thrash:** batch reads (`getBoundingClientRect`, `offsetHeight`) before writes in the same frame; never alternate read, write, read, write in a loop.
6. **Use the right clock:** CSS and WAAPI for declarative animation (browser-optimized); `requestAnimationFrame` for per-frame scripted work (one loop for everything, with delta time); never `setInterval` for animation.
7. **Promote layers carefully:** `will-change: transform` only on elements about to animate, removed afterward; too many layers cost memory.
8. **Limit the work:** animate fewer elements, shorten distances, avoid animating large blurred or filtered areas, use `content-visibility: auto` for off-screen sections, and virtualize long lists.
9. **Cancel and clean up:** cancel running animations on unmount or interruption, remove listeners, disconnect observers, stop loops when hidden.
10. **Re-measure** with the same scenario and record before and after numbers. Report only numbers you measured.

## Choosing an approach and library
| Need | Prefer |
| --- | --- |
| State-driven UI transitions | CSS transitions |
| Keyframed or sequenced effects without logic | CSS animations or WAAPI |
| Interruptible, scripted, layout or shared-element animation | WAAPI, framework transitions, or the project's existing library |
| Complex timelines, scroll scrubbing | A timeline library; check [library selection](references/library-selection.md) |
| Heavy visuals | Canvas or WebGL (see svg-canvas-3d-animation) |
Add a dependency only when the requirement cannot be met cheaply otherwise; verify the API against the installed version's official docs, check bundle size, license and maintenance, and prefer one animation library per project.

## Common mistakes
- Animating `height`, `top` or `box-shadow` blur directly.
- Reading layout in scroll handlers.
- `will-change` on everything.
- Several animation libraries in one app.
- Declaring animation "smooth" from watching it on a fast development machine.

## Verification
- Record before and after profiles in the same scenario; state frame times or the share of long frames, and the device or throttling used.
- No layout or paint work during the animation except where intended (check paint flashing).
- Memory returns to baseline after repeated mount and unmount.
- If profiling was not possible, state that and list the code-level checks performed instead.

## Deliverables
Implementation or fixes, before and after measurements, notes on technique and library choices.

## References
- [Profiling workflow](references/profiling-workflow.md): step-by-step measurement and common findings.
- [Library selection](references/library-selection.md): criteria for adding or choosing an animation dependency.
