# Technique selection

## Decision flow
1. Can CSS transform and opacity do it? Use CSS.
2. Is it vector artwork whose parts move, draw or morph? Use SVG.
3. Do you need to draw thousands of items, per-pixel effects, or custom physics? Use Canvas 2D.
4. Do you need a 3D scene, lighting, shaders or very large GPU workloads? Use WebGL (usually through a maintained library).
5. Is the animation authored by a designer in a motion tool? Export and use a player; keep the file small and check runtime size.

## SVG details
- **Stroke drawing:** set `pathLength="1"` on the path, then animate `stroke-dashoffset` from 1 to 0 with `stroke-dasharray: 1`.
```css
.draw { stroke-dasharray: 1; stroke-dashoffset: 1; animation: draw var(--dur-page) var(--ease-in-out) forwards; }
@keyframes draw { to { stroke-dashoffset: 0; } }
```
- **Transforms on SVG parts:** use `transform-box: fill-box; transform-origin: center;` so rotations and scales pivot on the element, not the SVG origin.
- **Morphing:** path data must have matching command structure. Animating the CSS `d` property or SMIL has uneven support; the Web Animations API with precomputed intermediate paths, or a morphing library, is the portable route. Verify support for your audience.
- **Motion along a path:** CSS `offset-path: path("...")` with `offset-distance` animation, or animate a transform from computed points.
- **Filters and masks** are expensive when animated; animate opacity and transform on a layer above them instead.
- **Accessibility:** meaningful graphics need `role="img"` and a `<title>`; decorative ones `aria-hidden="true"`.

## Canvas 2D details
- Draw into an off-screen canvas for static layers and composite once.
- Batch similar draw calls; avoid changing state (fillStyle, font) more than needed.
- Use `OffscreenCanvas` in a worker for heavy drawing when supported.
- Spatial structures (grids, quadtrees) for collision or neighbor queries when element count is high.

## WebGL / 3D details
- Prefer a maintained library over raw WebGL unless there is a specific reason; read its official docs for the version you install.
- Budget: draw calls, triangle count, texture sizes, shader complexity. Reduce before optimizing code.
- Compress textures and models; load asynchronously with a visible static placeholder.
- Cap pixel ratio around 2; lower quality on small or low-power devices.
- Test on integrated graphics and a mid-range phone, not only a development workstation.

## Library selection for animation
Choose by need, verify the current API and license in official docs, and prefer what the project already uses.
| Need | Candidates |
| --- | --- |
| Declarative UI animation in React | The project's existing animation library; otherwise a maintained React motion library |
| Timelines, scroll scrubbing, SVG morphing | A timeline library such as GSAP; check licensing terms |
| Designer-authored animation | Lottie or Rive players |
| 3D | three.js (with a React wrapper if the project uses React) |
Do not add a dependency for what CSS or the Web Animations API already does.
