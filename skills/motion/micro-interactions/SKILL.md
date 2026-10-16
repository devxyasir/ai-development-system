---
name: micro-interactions
description: "Designs and builds small interaction details: hover, focus, press and release, selection, toggles, drag, copy confirmation, form success and error feedback, optimistic updates, undo and progress feedback that feel deliberate without slowing tasks. Use when polishing controls, adding feedback to user actions, or reviewing whether interface feedback is clear and fast."
metadata:
  category: motion
  version: "0.1.0"
  related: "motion-design, ui-animation, reduced-motion-accessibility, accessibility-review"
---

# Micro-interactions

A micro-interaction is one trigger, one response, and optionally a state change. Its job is to confirm, guide or prevent error. It must stay fast, clear and optional to notice.

## When to use
- Polishing buttons, toggles, inputs, selection, drag handles, copy buttons and similar controls.
- Reviewing whether the interface acknowledges user actions.
- Not for: page-level choreography (motion-design) or large component transitions (ui-animation).

## Procedure
1. **List the controls** the user touches most. Start with those; ignore rarely used ones.
2. **For each, define trigger, response, and result:** what the user does, what changes immediately, what state remains.
3. **Respond within 100 ms** for every action. If the real result takes longer, show immediate acknowledgement (pressed state, spinner on the control) and then the result.
4. **Pick the lightest cue** that is unambiguous: color or shadow change, small scale (about 0.96-0.98 on press), icon swap, check mark, short text change ("Copied"). Prefer one cue to three.
5. **Make states reachable without a pointer:** every hover cue has a `:focus-visible` equivalent; no information appears only on hover; touch has a pressed state through `:active`.
6. **Pair visual cues with non-visual ones** for important outcomes: update an `aria-live` region or `aria-pressed`/`aria-checked` state so assistive technology gets the same confirmation.
7. **Use optimistic updates for reversible actions** (like, archive, reorder): update the interface immediately, reconcile when the server answers, and roll back with a clear message on failure. Offer undo for destructive but reversible actions.
8. **Define the failure cue:** errors need text and an icon, not only shake or red. Shake is optional and needs a reduced-motion alternative.
9. **Test repeated use:** the hundredth click must not feel slow or annoying. Frequent actions get the quietest feedback.

## Recipes
Code and details for each pattern: [recipes](references/recipes.md).
| Pattern | Core idea |
| --- | --- |
| Press and release | Scale to about 0.97 on `:active`, return with ease-out in 100-150 ms |
| Toggle | Animate the knob with transform; also change color and text or icon; expose `role="switch"` and `aria-checked` |
| Copy confirmation | Swap label to "Copied" for 1.5-2 s, announce via live region, revert automatically |
| Form field feedback | Validate on blur; success is quiet (small check), error is explicit (message plus icon) |
| Drag | Lift on grab (shadow or scale), show drop targets, offer a keyboard alternative |
| Optimistic update + undo | Immediate change, "Undo" for about 5-8 s, rollback on failure |
| Progress and completion | Immediate pressed state, then spinner or progress, then a clear done state |

## Common mistakes
- Feedback that delays the action (waiting for an animation to end before applying the result).
- Hover-only cues, no focus equivalent.
- Celebration animations on frequent actions.
- Success shown before the server confirms, with no rollback path.
- Cues that rely on color alone.

## Verification
- Each control shows feedback within 100 ms on a throttled CPU profile where available.
- Keyboard users get the same feedback as pointer users.
- Failure and rollback paths were exercised, not only success.
- Reduced-motion mode keeps the confirmation (as color, text or instant change) without the movement.
- State which interactions were verified in a real browser.

## Deliverables
List of micro-interactions with trigger, response, state, accessibility mapping and reduced-motion behavior; implemented code.

## References
- [Recipes](references/recipes.md)
