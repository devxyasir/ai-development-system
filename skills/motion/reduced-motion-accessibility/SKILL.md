---
name: reduced-motion-accessibility
description: "Makes animation safe and accessible: honoring prefers-reduced-motion with designed alternatives, pause and stop controls, seizure-safe flashing limits, vestibular-safe motion, and motion that does not block tasks. Use whenever adding or reviewing animation, parallax, auto-playing media, carousels or page transitions, and when asked about motion accessibility."
metadata:
  category: motion
  version: "0.1.0"
  related: "motion-design, accessibility-review, scroll-animation, ui-animation"
---

# Reduced motion and motion accessibility

Some users get dizziness, nausea or distraction from movement, some can have seizures from flashing, and some simply need to focus. The operating system's reduced-motion setting is an explicit request; treat it as a requirement, not a nicety.

## When to use
- Any new or changed animation, parallax, auto-playing video or carousel, page transitions, or large movement.
- A review or audit of motion; questions about `prefers-reduced-motion`.

## Procedure
1. **Inventory the motion** in the change: what moves, how far, how long, whether it loops or autoplays.
2. **Classify each item:**
| Class | Examples | Reduced-motion treatment |
| --- | --- | --- |
| Essential feedback | Focus ring, pressed state, validation message, progress | Keep, as color, text or instant change |
| Functional movement | Menu opens, panel slides | Replace slide and scale with a fade or an instant change |
| Large or vestibular-triggering | Parallax, zooming, spinning, full-screen slides, scroll-jacking | Remove; show static layout |
| Decorative loops and autoplay | Background video, particle fields | Stop or show a still frame |
3. **Implement the media query** per component or via tokens ([patterns](references/patterns.md)). A blanket reset that zeroes all durations is a safety net, not a design; it also removes useful feedback and can break scripts waiting on `transitionend`.
4. **Handle scripted animation:** read `matchMedia('(prefers-reduced-motion: reduce)')`, listen for changes, and branch in libraries and canvas loops.
5. **Apply the timing rules:** moving, blinking or auto-updating content that starts automatically, lasts over 5 seconds and runs alongside other content needs a pause, stop or hide control (WCAG 2.2.2). Nothing flashes more than three times in any one second (WCAG 2.3.1). Avoid motion triggered by interaction that users cannot disable (WCAG 2.3.3 is Level AAA, still a good target).
6. **Offer an in-app control** when motion is a core part of the experience (for example a "Reduce animations" toggle that sets a root attribute), and let it add to, not override, the system preference.
7. **Make sure nothing depends on animation finishing:** state changes, focus movement and event handlers must not wait on a transition that is disabled.

## Decision rules
| Situation | Do this |
| --- | --- |
| Slide-in panel | Keep a short fade (or none) under reduced motion |
| Parallax or scroll-linked transforms | Disable and render static |
| Autoplaying hero video | Do not autoplay under reduced motion; show a poster with a play button |
| Spinner | Keep, but use a non-rotating or pulsing indicator if rotation is large; keep it small |
| Shake on error | Replace with outline plus message |

## Common mistakes
- Adding the media query only to CSS and forgetting JavaScript, canvas, video and libraries.
- Disabling motion by setting `display: none` on content that should still be visible.
- Treating "reduce" as "remove every cue", leaving users without feedback.
- Testing only the default setting.

## Verification
- Turn on the system or browser reduced-motion setting (or emulate it in dev tools) and walk every changed flow.
- Confirm essential feedback survives, large motion is gone, and no state depends on a transition event.
- Check flashing content frequency and pause controls for anything over 5 seconds.
- State if emulation was not possible and what was reviewed in code only.

## Deliverables
Motion inventory with reduced-motion treatment per item, implementation, test notes.

## References
- [Patterns](references/patterns.md): CSS and JavaScript patterns, library hooks, toggle implementation.
