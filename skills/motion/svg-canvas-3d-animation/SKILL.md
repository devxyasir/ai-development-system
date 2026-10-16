---
name: svg-canvas-3d-animation
description: "Chooses and builds the right rendering technique for visual animation: CSS, SVG paths and morphing, Canvas 2D loops, or WebGL and 3D scenes (three.js style), with asset loading, resource cleanup, frame budgets, device limits and fallbacks. Use when adding illustrative, data-driven, particle or 3D animation to a web page, or when canvas or WebGL animation leaks memory or runs slowly."
metadata:
  category: motion
  version: "0.1.0"
  related: "motion-design, animation-performance, reduced-motion-accessibility, cinematic-motion"
---

# SVG, Canvas and 3D animation

Use the simplest technique that achieves the visual result. Complexity (and its cost in performance, accessibility and maintenance) must be justified by a requirement CSS or SVG cannot meet.

## When to use
- A visual animation beyond ordinary UI transitions: drawing lines, morphing shapes, particles, generative visuals, charts with custom motion, product 3D views.
- A canvas or WebGL animation leaks memory, drops frames, or fails on some devices.
- Not for: UI component transitions (ui-animation).

## Procedure
1. **State the visual requirement** in one sentence, plus interaction (none, hover, drag, scroll-linked, data-driven) and element count.
2. **Choose the technique** using [technique selection](references/technique-selection.md) and the table below. Start at the top and stop at the first row that works.
3. **Plan assets:** vector over bitmap where possible; compress textures and models; load lazily and show a static placeholder first; set explicit dimensions to avoid layout shift.
4. **Build with a frame budget:** 16.7 ms per frame at 60 Hz (8.3 ms at 120 Hz). Cap device pixel ratio (about 2), size the drawing surface to the displayed size, and use delta time rather than frame counts.
5. **Manage the loop:** one `requestAnimationFrame` loop; pause when the tab is hidden or the canvas is off screen; stop when the component unmounts.
6. **Clean up resources:** cancel the loop, remove listeners, disconnect observers, and for WebGL dispose geometries, materials, textures, render targets and the renderer ([patterns](references/canvas-and-webgl-patterns.md)).
7. **Provide fallbacks:** feature-detect (WebGL context creation can fail or be lost); show a static image or simplified SVG; honor reduced motion by rendering a still or very slow version.
8. **Make it accessible:** decorative canvases get `aria-hidden="true"`; meaningful ones get a text alternative or equivalent data table; interactive ones need keyboard operation.
9. **Profile** on a mid-range device or throttled CPU, and watch memory across repeated mount and unmount.

## Choosing a technique
| Requirement | Use | Why |
| --- | --- | --- |
| Move, fade, scale, rotate elements | CSS transform and opacity | Compositor-friendly, no script |
| Draw a stroke, animate an icon, morph shapes with equal point counts | SVG with CSS or Web Animations API | Resolution-independent, styleable, accessible text |
| Many moving elements (hundreds to thousands), particles, custom drawing, pixel effects | Canvas 2D | One element, you control the loop |
| True 3D, shaders, very large element counts, lighting, depth | WebGL (often via a library) | GPU rendering; highest cost |
| Designer-authored vector animation | Exported player (Lottie, Rive) | Avoid hand-coding complex timelines; verify runtime size and license |

## Decision rules
- Fewer than about 100 animated elements and no per-pixel work: SVG or CSS is usually enough.
- Need to animate along a path: SVG path with `offset-path` in CSS or the Web Animations API before reaching for a library.
- Morphing shapes: paths must have the same number and type of commands; otherwise use a tool or library designed for morphing.
- Do not use a 3D engine for a 2D parallax effect or a gradient background.

## Common mistakes
- Redrawing the whole canvas at full resolution on high-DPI displays without capping the ratio.
- Allocating new objects every frame (garbage-collection stutter); reuse arrays and vectors.
- Starting a new render loop on every route visit without stopping the old one.
- Not disposing WebGL resources, which leaks GPU memory.
- No fallback when WebGL is unavailable or the context is lost.

## Verification
- The technique chosen is justified in one line; simpler options were rejected with a reason.
- Mount and unmount the component ten times; memory and the number of active loops stay flat.
- Frame time stays within budget on the target device profile; if not measured, state so.
- Reduced motion, WebGL-disabled and tab-hidden cases behave correctly.
- Text alternative or `aria-hidden` set appropriately.

## Deliverables
Technique decision with reasons, implementation with cleanup and fallbacks, profiling notes.

## References
- [Technique selection](references/technique-selection.md): decision flow and SVG details.
- [Canvas and WebGL patterns](references/canvas-and-webgl-patterns.md): loop, resizing, disposal, context loss.
