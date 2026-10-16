# Component recipes

All durations and easings come from motion tokens (`--dur-*`, `--ease-*`). Verify browser support for newer features (`@starting-style`, `allow-discrete`, View Transitions) against your audience; each recipe lists its fallback.

## Dialog with native `<dialog>`
```css
dialog {
  opacity: 0;
  transform: translateY(var(--distance-small));
  transition:
    opacity var(--dur-base) var(--ease-out),
    transform var(--dur-base) var(--ease-out),
    overlay var(--dur-base) allow-discrete,
    display var(--dur-base) allow-discrete;
}
dialog[open] { opacity: 1; transform: none; }
@starting-style { dialog[open] { opacity: 0; transform: translateY(var(--distance-small)); } }

dialog::backdrop {
  background: rgb(0 0 0 / 0);
  transition: background var(--dur-base) linear, overlay var(--dur-base) allow-discrete, display var(--dur-base) allow-discrete;
}
dialog[open]::backdrop { background: rgb(0 0 0 / 0.4); }
@starting-style { dialog[open]::backdrop { background: rgb(0 0 0 / 0); } }
```
Fallback: browsers without these features open and close instantly, which is acceptable. Use `dialog.showModal()` and `dialog.close()`; focus handling and Escape come built in.

## Accordion / expandable content
```css
.panel { display: grid; grid-template-rows: 0fr; transition: grid-template-rows var(--dur-base) var(--ease-out); }
.panel[data-open="true"] { grid-template-rows: 1fr; }
.panel > .inner { overflow: hidden; min-height: 0; }
```
Set `aria-expanded` on the trigger and `hidden` or `inert` on collapsed content so it is not focusable while closed (toggle `inert` after the collapse transition ends).

## Menu / popover (scale from anchor)
```css
.menu { transform-origin: top left; opacity: 0; transform: scale(0.96); transition: opacity var(--dur-fast) var(--ease-out), transform var(--dur-fast) var(--ease-out); }
.menu[data-open="true"] { opacity: 1; transform: none; }
```
Set `transform-origin` from the trigger's position (a CSS custom property set in script, or anchor positioning where supported).

## Drawer
```css
.drawer { transform: translateX(100%); transition: transform var(--dur-slow) var(--ease-out); }
.drawer[data-open="true"] { transform: none; }
.drawer[data-open="false"] { transition-timing-function: var(--ease-in); transition-duration: var(--dur-base); }
```
Exit uses ease-in and a shorter duration. For right-to-left layouts mirror the translate direction using logical logic in script or `:dir(rtl)`.

## Toast stack
```js
function showToast(el, ms = 5000) {
  el.classList.add('is-in');                     // CSS handles slide+fade
  let remaining = ms, started = performance.now(), timer;
  const start = () => { started = performance.now(); timer = setTimeout(hide, remaining); };
  const pause = () => { clearTimeout(timer); remaining -= performance.now() - started; };
  const hide = () => { el.classList.remove('is-in'); el.addEventListener('transitionend', () => el.remove(), { once: true }); };
  el.addEventListener('mouseenter', pause); el.addEventListener('mouseleave', start);
  el.addEventListener('focusin', pause); el.addEventListener('focusout', start);
  start();
}
```
Markup: container `aria-live="polite"` (`role="status"`); error toasts should not auto-dismiss without a way to review them.

## List reorder with FLIP (Web Animations API)
```js
function flipReorder(container, mutate) {
  const items = [...container.children];
  const first = new Map(items.map(el => [el, el.getBoundingClientRect()]));
  mutate();                                      // change DOM order or classes
  for (const el of container.children) {
    const a = first.get(el); if (!a) continue;
    const b = el.getBoundingClientRect();
    const dx = a.left - b.left, dy = a.top - b.top;
    if (!dx && !dy) continue;
    el.animate([{ transform: `translate(${dx}px, ${dy}px)` }, { transform: 'none' }],
               { duration: 220, easing: 'cubic-bezier(0.65, 0, 0.35, 1)' });
  }
}
```
Skip when `matchMedia('(prefers-reduced-motion: reduce)').matches`. For large lists limit to visible items.

## Route / view transitions
```js
function transition(update) {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!document.startViewTransition || reduce) { update(); return; }
  document.startViewTransition(() => update());
}
```
```css
::view-transition-old(root) { animation: fade-out var(--dur-base) var(--ease-in) both; }
::view-transition-new(root) { animation: fade-in var(--dur-base) var(--ease-out) both; }
```
Give shared elements `view-transition-name` values that are unique per page. Fallback is an immediate update. Frameworks often provide their own wrapper; use it instead of calling the API by hand.

## Progress bar without layout cost
```css
.bar { transform-origin: left center; transform: scaleX(var(--progress, 0)); transition: transform var(--dur-base) linear; }
```
Update `--progress` (0 to 1) from script. In right-to-left layouts set `transform-origin: right center`.

## Interruption-safe scripted animation
```js
let current;
function animateTo(el, keyframes, options) {
  if (current) { current.commitStyles(); current.cancel(); }  // keep where we are, then retarget
  current = el.animate(keyframes, { fill: 'both', ...options });
  return current.finished.catch(() => {});                   // cancel() rejects; ignore it
}
```
`commitStyles()` requires the element to be rendered; guard against that in components that may unmount.
