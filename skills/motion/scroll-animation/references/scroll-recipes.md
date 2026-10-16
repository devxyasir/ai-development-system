# Scroll recipes

## 1. Reveal on enter (IntersectionObserver)
```html
<script>document.documentElement.classList.add('js');</script>
```
```css
.js [data-reveal] { opacity: 0; transform: translateY(16px); transition: opacity var(--dur-slow) var(--ease-out), transform var(--dur-slow) var(--ease-out); }
.js [data-reveal].is-visible { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { .js [data-reveal] { opacity: 1; transform: none; transition: none; } }
```
```js
const io = new IntersectionObserver((entries) => {
  for (const e of entries) if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); }
}, { rootMargin: '0px 0px -10% 0px', threshold: 0.1 });
document.querySelectorAll('[data-reveal]').forEach(el => io.observe(el));
// cleanup when the view is destroyed: io.disconnect();
```
Stagger siblings with `style="transition-delay: calc(var(--i) * var(--stagger-step))"` and a capped index.

## 2. Reading progress bar (CSS scroll timeline with fallback)
```css
.progress { position: fixed; inset: 0 0 auto 0; height: 3px; background: var(--color-action); transform-origin: left; transform: scaleX(0); }
@supports (animation-timeline: scroll()) {
  .progress { animation: grow linear both; animation-timeline: scroll(root block); }
  @keyframes grow { to { transform: scaleX(1); } }
}
```
Fallback script for unsupported browsers:
```js
if (!CSS.supports('animation-timeline: scroll()')) {
  const bar = document.querySelector('.progress'); let ticking = false;
  addEventListener('scroll', () => {
    if (ticking) return; ticking = true;
    requestAnimationFrame(() => {
      const max = document.documentElement.scrollHeight - innerHeight;
      bar.style.transform = `scaleX(${max > 0 ? scrollY / max : 0})`; ticking = false;
    });
  }, { passive: true });
}
```
Right-to-left pages: use `transform-origin: right`.

## 3. View-based fade and rise (CSS only, progressive enhancement)
```css
@supports (animation-timeline: view()) {
  .rise { animation: rise linear both; animation-timeline: view(); animation-range: entry 0% entry 60%; }
  @keyframes rise { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: none; } }
}
```
Elements are fully visible in browsers without support. Browser support for scroll-driven animations is still uneven; check current compatibility data before depending on it.

## 4. Sticky sidebar or header
```css
.toc { position: sticky; top: calc(var(--header-h, 0px) + 1rem); align-self: start; }
html { scroll-padding-top: calc(var(--header-h, 0px) + 1rem); } /* anchor jumps are not hidden under the header */
```
`position: sticky` fails if an ancestor has `overflow: hidden/auto` unintentionally; check the ancestors.

## 5. Pinned section driven by steps (observer-driven state)
```js
const steps = document.querySelectorAll('[data-step]');
const stepIO = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) chart.setState(e.target.dataset.step); });
}, { rootMargin: '-45% 0px -45% 0px' });   // fires when a step crosses the middle
steps.forEach(s => stepIO.observe(s));
```
The pinned chart is `position: sticky; top: 10vh`. Each step stays readable text; the chart update uses a short transition.

## 6. Parallax (use sparingly)
```js
const layers = [...document.querySelectorAll('[data-depth]')];
let y = 0, queued = false;
addEventListener('scroll', () => { y = scrollY; if (!queued) { queued = true; requestAnimationFrame(apply); } }, { passive: true });
function apply() { layers.forEach(l => l.style.transform = `translate3d(0, ${y * parseFloat(l.dataset.depth)}px, 0)`); queued = false; }
```
Depth values small (0.05-0.3), decorative layers only, disabled for reduced motion and small screens. Remove the listener in cleanup. Prefer a CSS scroll timeline where supported.

## 7. Scroll snapping
```css
.slides { scroll-snap-type: y proximity; overflow-y: auto; height: 100dvh; }
.slides > section { scroll-snap-align: start; }
```
`mandatory` can trap users in tall sections; use it only when every snap target fits the viewport.

## 8. Timeline libraries
When using a scroll timeline library: create triggers in a single setup function, store them, and kill them on teardown; call its refresh method after images, fonts or layout changes; pin only when the pinned content fits the viewport; check the library's current license and API from its official documentation before adding it.
