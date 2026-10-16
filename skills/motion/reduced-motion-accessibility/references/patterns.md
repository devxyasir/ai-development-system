# Reduced-motion patterns

## Design the alternative, per component
```css
.panel { transform: translateX(100%); transition: transform var(--dur-slow) var(--ease-out); }
.panel[data-open="true"] { transform: none; }

@media (prefers-reduced-motion: reduce) {
  .panel { transform: none; opacity: 0; transition: opacity var(--dur-fast) linear; }
  .panel[data-open="true"] { opacity: 1; }
}
```
The panel still appears and disappears, now by fading.

## Blanket safety net (use in addition to designed alternatives)
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
Trade-offs: this removes feedback transitions too, and scripts that wait for `transitionend` still receive it only when a transition actually runs; code that waits for an event on a zero-length transition should also use a timeout.

## Opt-in pattern (animate only when motion is allowed)
```css
@media (prefers-reduced-motion: no-preference) {
  .reveal { animation: rise var(--dur-slow) var(--ease-out) both; }
}
```
Writing motion inside `no-preference` makes the safe path the default.

## JavaScript
```js
const mq = window.matchMedia('(prefers-reduced-motion: reduce)');
let reduceMotion = mq.matches;
mq.addEventListener('change', (e) => { reduceMotion = e.matches; applyPreference(); });

function animateIn(el) {
  if (reduceMotion) { el.style.opacity = 1; return; }
  el.animate([{ opacity: 0, transform: 'translateY(12px)' }, { opacity: 1, transform: 'none' }], { duration: 250, easing: 'ease-out', fill: 'both' });
}
```
Libraries: use their reduced-motion option or config where one exists (check official docs); otherwise branch with the variable above. For canvas and WebGL render a still or slow version (see svg-canvas-3d-animation).

## In-app toggle that adds to the system preference
```css
:root[data-motion="reduce"] { --dur-fast: 1ms; --dur-base: 1ms; --dur-slow: 1ms; --dur-page: 1ms; }
```
```js
const saved = localStorage.getItem('motion');               // 'reduce' or null; wrap in try/catch in real code
if (saved === 'reduce' || mq.matches) document.documentElement.dataset.motion = 'reduce';
```

## Auto-playing media
```html
<video muted playsinline loop preload="metadata" poster="hero.jpg"></video>
```
```js
const v = document.querySelector('video');
if (!reduceMotion) v.play().catch(() => {});
// provide a visible pause/play button in all cases
```

## Pause, stop, hide control for carousels and tickers
- A button with an accessible name ("Pause carousel") that toggles auto-advance.
- Auto-advance stops on hover and keyboard focus within the region.
- Do not auto-advance at all when reduced motion is requested.

## Flashing safety
- Avoid content that flashes more than three times per second; avoid large high-contrast red flashes. If video or animated content is user-supplied or third-party, state that limits cannot be guaranteed and provide controls.

## Test matrix
| Setting | Check |
| --- | --- |
| Default | Animation runs as designed |
| Reduced motion on | Alternatives apply; feedback intact; nothing waits for animation events |
| Toggle changed while page is open | The `change` listener updates behavior without reload |
| Autoplay disabled by the browser | Controls still work |
