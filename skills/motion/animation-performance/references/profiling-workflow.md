# Profiling workflow

## Setup
1. Use a production-like build (development builds distort timing).
2. Open the browser's Performance tool. Apply CPU throttling (a 4x or 6x slowdown approximates a mid-range phone; it is an approximation, not a device).
3. Turn on rendering aids: paint flashing, layer borders, and the frame-rendering stats overlay.

## Record
1. Start recording, perform the animation scenario three times, stop.
2. Look at the frame chart for frames over budget and at the Main thread for long tasks.
3. In the flame chart, identify what dominates: Layout, Recalculate Style, Paint, Composite Layers, or scripting.

## Interpret
| Finding | Likely cause | Fix |
| --- | --- | --- |
| Large Layout blocks each frame | Animating layout properties; reading layout in loops | Use transform and opacity; batch reads and writes |
| Frequent Paint of a large area | Animating color, shadow or filter on big elements | Reduce area; crossfade pseudo-element; promote only the moving layer |
| Long scripting blocks | Heavy per-frame JavaScript; allocations | Precompute, reuse objects, move work off the main thread, reduce element count |
| Many small tasks plus GC pauses | Allocations in the loop | Preallocate; typed arrays |
| Smooth when idle, janky with scrolling | Non-passive scroll listeners or layout in handlers | Passive listeners, observers, CSS timelines |
| Layout shift when animation starts | Animating size or inserting content | Reserve space; animate transform |

## Code-level checks when no profiler is available
- Search for animated properties: `grep -rE "transition: *(all|width|height|top|left)"`.
- Search for layout reads in handlers: `getBoundingClientRect`, `offsetHeight`, `scrollTop` used inside loops or scroll listeners.
- Check every `requestAnimationFrame` start has a matching `cancelAnimationFrame`.
- Check `will-change` usage and that large elements are not blurred or filtered during motion.

## Report format
- Scenario and device or throttling used
- Before: frame time or long-frame share, main-thread breakdown
- Change made
- After: same metrics
- Not measured: list
