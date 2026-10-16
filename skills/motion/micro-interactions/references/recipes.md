# Micro-interaction recipes

## Press and release
```css
.btn { transition: transform var(--dur-fast) var(--ease-out), background-color var(--dur-fast) var(--ease-out); }
.btn:active { transform: scale(0.97); }
.btn:focus-visible { outline: 2px solid var(--color-focus); outline-offset: 2px; }
@media (hover: hover) { .btn:hover { background-color: var(--color-action-hover); } }
```
The hover guard avoids sticky hover on touch devices.

## Toggle switch
```html
<button type="button" role="switch" aria-checked="false" class="switch"><span class="knob"></span><span class="sr-only">Notifications</span></button>
```
```css
.knob { transform: translateX(0); transition: transform var(--dur-fast) var(--ease-out); }
.switch[aria-checked="true"] .knob { transform: translateX(1.25rem); }
.switch[aria-checked="true"] { background: var(--color-action); }
```
```js
document.querySelectorAll('.switch').forEach(s => s.addEventListener('click', () =>
  s.setAttribute('aria-checked', String(s.getAttribute('aria-checked') !== 'true'))));
```
In right-to-left layouts mirror the translate direction.

## Copy confirmation
```js
async function copy(btn, text) {
  await navigator.clipboard.writeText(text);   // requires a secure context and user gesture
  const label = btn.textContent;
  btn.textContent = 'Copied';
  document.getElementById('live').textContent = 'Copied to clipboard';
  setTimeout(() => { btn.textContent = label; document.getElementById('live').textContent = ''; }, 1800);
}
```
Handle rejection (permissions, insecure context) with a visible failure message.

## Form field feedback
```css
.field[aria-invalid="true"] input { border-color: var(--color-danger); }
.field .error { opacity: 0; transform: translateY(-4px); transition: opacity var(--dur-fast) var(--ease-out), transform var(--dur-fast) var(--ease-out); }
.field[aria-invalid="true"] .error { opacity: 1; transform: none; }
```
Link the message with `aria-describedby`. Validate on blur, then on input after the first error so the message clears as soon as it is fixed.

## Optional shake (with reduced-motion alternative)
```css
@keyframes shake { 20%, 60% { transform: translateX(-4px); } 40%, 80% { transform: translateX(4px); } }
.field.shake { animation: shake 220ms var(--ease-in-out); }
@media (prefers-reduced-motion: reduce) { .field.shake { animation: none; outline: 2px solid var(--color-danger); } }
```

## Drag with a keyboard alternative
- Pointer: use Pointer Events; apply `transform: translate(...)` while dragging; `touch-action: none` on the handle; show a placeholder at the drop position.
- Keyboard: focus the item, Space to lift, arrow keys to move, Space to drop, Escape to cancel; announce position changes in a live region ("Item 3 of 8, moved to position 2").
- Provide a non-drag alternative for reordering (move up and move down buttons) for pointer users who cannot drag precisely (WCAG 2.5.7).

## Optimistic update with undo
```js
async function archive(item) {
  const snapshot = store.snapshot(item);
  store.archiveLocal(item);                     // immediate
  showUndoToast('Archived', () => store.restore(snapshot));
  try { await api.archive(item.id); }
  catch { store.restore(snapshot); showError('Could not archive. Restored.'); }
}
```
Undo must also cancel or reverse the server request. If the action cannot be reversed server-side, do not offer undo; use confirmation instead.

## Progress and completion
1. Immediately: pressed state and disabled-while-busy (but keep focus on the button).
2. After about 300 ms: show a spinner or progress inside the button.
3. On success: state change (check icon, text) for 1-2 s, announce via live region.
4. On failure: restore the control, show the error where the user is looking.
