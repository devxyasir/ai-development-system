# Canvas and WebGL patterns

## Canvas loop with delta time, visibility pause and cleanup
```js
function createLoop(update, draw) {
  let raf = 0, last = 0, running = false;
  const frame = (now) => {
    const dt = Math.min((now - last) / 1000, 0.05);   // clamp after tab switches
    last = now; update(dt); draw();
    raf = requestAnimationFrame(frame);
  };
  const start = () => { if (running) return; running = true; last = performance.now(); raf = requestAnimationFrame(frame); };
  const stop = () => { running = false; cancelAnimationFrame(raf); };
  const onVis = () => (document.hidden ? stop() : start());
  document.addEventListener('visibilitychange', onVis);
  return { start, stop, destroy() { stop(); document.removeEventListener('visibilitychange', onVis); } };
}
```
Also pause when the canvas is off screen with an `IntersectionObserver`.

## High-DPI sizing with a cap and ResizeObserver
```js
function fit(canvas, ctx) {
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  const { width, height } = canvas.getBoundingClientRect();
  canvas.width = Math.round(width * dpr); canvas.height = Math.round(height * dpr);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);               // draw in CSS pixels
}
const ro = new ResizeObserver(() => fit(canvas, ctx)); ro.observe(canvas);
// cleanup: ro.disconnect();
```

## Avoid per-frame allocations
- Preallocate particle arrays (typed arrays for numeric data) and reuse objects.
- Do not create closures, arrays or strings inside the draw loop.

## Reduced motion
```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
if (reduce.matches) { drawStaticFrame(); } else { loop.start(); }
reduce.addEventListener('change', e => (e.matches ? (loop.stop(), drawStaticFrame()) : loop.start()));
```

## three.js-style scene setup and teardown
```js
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setAnimationLoop(render);                       // stop with renderer.setAnimationLoop(null)

function disposeScene(scene, renderer) {
  scene.traverse((obj) => {
    if (obj.geometry) obj.geometry.dispose();
    const mats = obj.material ? (Array.isArray(obj.material) ? obj.material : [obj.material]) : [];
    for (const m of mats) {
      for (const v of Object.values(m)) if (v && v.isTexture) v.dispose();
      m.dispose();
    }
  });
  renderer.setAnimationLoop(null);
  renderer.dispose();
}
```
Also dispose render targets, remove event listeners, and cancel pending asset loads on unmount. API names follow the three.js library; confirm against the version you install.

## Context loss and fallback
```js
canvas.addEventListener('webglcontextlost', (e) => { e.preventDefault(); stopLoop(); showStaticFallback(); });
canvas.addEventListener('webglcontextrestored', () => { rebuildGpuResources(); startLoop(); });
function hasWebGL() { try { return !!document.createElement('canvas').getContext('webgl2'); } catch { return false; } }
```
If `hasWebGL()` is false, render the fallback image or SVG and skip loading the 3D library entirely.

## Memory-leak check (manual)
1. Open the page, take a heap snapshot or note GPU/JS memory.
2. Mount and unmount the component ten times (route changes).
3. Memory should return near baseline; the count of `requestAnimationFrame` loops (instrument with a counter) must be zero after unmount.
