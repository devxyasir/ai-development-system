---
name: ui-animation
description: "Implements animation for common interface components: buttons, menus, dialogs, drawers, tooltips, tabs, accordions, loaders and progress, toasts, validation feedback, list changes, expandable content and route transitions, consistent with the design system. Use when animating a specific UI component or transition in CSS, Web Animations API or a framework."
metadata:
  category: motion
  version: "0.1.0"
  related: "motion-design, micro-interactions, animation-performance, reduced-motion-accessibility, component-engineering"
---

# UI animation

Build component-level animation that matches the project's motion tokens, survives interruption, and respects reduced motion. Start with CSS; reach for scripting or a library only when CSS cannot express the behavior.

## When to use
- Animating or reviewing a specific component or screen transition.
- Not for: deciding whether and why to animate (motion-design, do that first), micro-feedback details (micro-interactions), scroll-linked effects (scroll-animation).

## Procedure
1. **Get the motion spec** for the component (motion-design). If absent, write a short one now: purpose, duration token, easing token, reduced-motion behavior.
2. **Inspect the project:** which styling approach (plain CSS, Tailwind, CSS-in-JS), which animation library if any, existing motion tokens, existing component primitives. Reuse them. Do not add a library for one animation.
3. **Choose the technique** with the table below.
4. **Animate transform and opacity.** Replace position, size and margin animation with transforms (FLIP for layout changes).
5. **Handle both directions:** enter and exit are separate designs (exit shorter, accelerating). Elements removed from the DOM need the exit to finish before removal (use an exit-aware mechanism of your framework or the `transitionend`/`animationend` event with a timeout fallback).
6. **Make it interruptible:** use transitions driven by state, or cancel and retarget scripted animations.
7. **Preserve semantics and focus:** animation must not change focus order, hide content from assistive technology while visible, or delay when controls become usable.
8. **Add the reduced-motion variant** and check it.
9. **Test repeated and rapid triggering,** then verify visually.

## Choosing a technique
| Need | Technique |
| --- | --- |
| Hover, focus, open/close of already-present elements | CSS `transition` on a state class or attribute |
| Appear/disappear (display none to block, dialog, popover) | `@starting-style` with `transition-behavior: allow-discrete`, or an exit-aware framework mechanism; check browser support |
| Height auto expand/collapse | `grid-template-rows: 0fr` to `1fr`, or measure and animate; do not animate `height: auto` directly |
| Reordering or moving elements | FLIP with the Web Animations API, or a library's layout animation |
| Sequence or choreography | CSS animation with delays, WAAPI, or a timeline library |
| Route transitions | View Transitions API with a non-animated fallback; or framework transitions |

## Component recipes
Code for dialog, drawer, menu, accordion, toast, list reorder and route transitions: [component recipes](references/component-recipes.md). Key rules per component:
| Component | Rule |
| --- | --- |
| Button | Press feedback 80-120 ms; never delay the click action |
| Menu, dropdown, tooltip | Scale and fade 4-8% from the anchor, 120-200 ms; tooltips appear after a short intent delay, hide instantly |
| Dialog, drawer | Fade plus 8-16 px translate (dialog) or edge slide (drawer); backdrop fades; focus moves in immediately |
| Tabs, accordion | Cross-fade or grid-row expand; keep layout from jumping |
| Loader, progress | Determinate: width via `transform: scaleX`; indeterminate loops stay subtle and pause when reduced motion |
| Toast | Slide/fade in, auto-dismiss pausable on hover and focus, errors persist, `role="status"` or `aria-live` |
| Validation | Message fades in next to the field; shake is optional and must have a reduced-motion alternative |
| Lists | Insert with a short fade and height reveal; reorder with FLIP |

## Common mistakes
- Animating `height`, `top`, `left` or `box-shadow` blur per frame.
- Removing the element from the DOM before the exit finishes, or leaving invisible elements focusable.
- Different durations for the same component in different screens.
- Fixed `setTimeout` delays that drift from CSS durations; read durations from tokens or events.

## Verification
- Slow the animation (inspector or temporary multiplier) and check start, end and mid-way reversal.
- Trigger rapidly five times; the final state is correct.
- Tab through while it plays; focus and screen-reader order are unchanged.
- Enable reduced motion and re-check; run the performance check in animation-performance if the component is large or frequently used.
- State what was not visually verified if no browser was available.

## Deliverables
Component animation implemented with tokens, reduced-motion variant, short note on technique chosen and why.

## References
- [Component recipes](references/component-recipes.md): working CSS and JavaScript patterns.
