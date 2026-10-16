---
name: design-to-code
description: "Turns design references (screenshots, mockups, Figma exports, existing interfaces) into working front-end code that matches the intended visual identity: inventory of regions, type, color, spacing and states, component boundaries, implementation in the existing stack, rendered comparison and fixes. Use when asked to build or match a UI from an image, mockup or reference site."
metadata:
  category: frontend
  version: "0.1.0"
  related: "visual-qa, component-engineering, design-system-creation, layout-and-responsive-design, accessibility-review, typography-selection"
---

# Design to code

Reproduce the intent of a reference faithfully in the project's own stack, verify it by comparing renders, and keep the interface real: working interactions and states, not a flat screenshot.

## When to use
- A screenshot, mockup, design file export or live page is the source of truth for a new or changed UI.
- Not for: designing without a reference (product-design, visual-design-direction).

## Procedure
1. **Inspect the reference.** Identify the major regions (header, navigation, content, side panels, footer), the hierarchy, and which parts repeat. Note anything you cannot see (hover, error, empty, mobile) and decide how to handle it ([inventory template](templates/reference-inventory.md)).
2. **Extract the visual system.** Fonts (identify by shape or ask; if unavailable choose the closest licensed alternative and say so), type sizes and weights, colors (sample from the image or file; do not guess hex values by eye when you can read them), spacing rhythm, radius, borders, shadows.
3. **Do not invent exact measurements.** If a value cannot be read, estimate from proportions (for example the ratio of heading height to body height), then compare the render against the reference and adjust.
4. **Inspect the project:** framework, styling method, existing tokens and components. Reuse them. Map reference values to existing tokens when they match; add new tokens when they are genuinely new (see design-system-creation). Do not replace the intended identity with a component library's defaults.
5. **Split into components** with component-engineering rules: shared pieces first (buttons, inputs, cards), then regions, then the page.
6. **Build the layout first** (structure, spacing, alignment at the reference width), then typography and color, then details (borders, shadows, icons, images).
7. **Add behavior:** hover, focus, active, disabled and loading states; real navigation, form handling, menus; responsive behavior for narrower widths (infer sensibly; note assumptions); right-to-left if required.
8. **Use real content shapes:** realistic text lengths, images with intrinsic sizes, data in lists and tables.
9. **Compare with the reference** at the same viewport: overlay or side by side if tools permit; list every difference; fix the largest first (layout, then type, then color, then details). Repeat until the remaining differences are intentional.
10. **Check accessibility and functionality** (accessibility-review) and run visual-qa for the rendered review.

## Decision rules
| Situation | Do this |
| --- | --- |
| Reference font unavailable | Closest licensed match; record the substitution |
| Colors read from a compressed image | Sample several pixels, take the consistent value, snap to a token if within a small tolerance |
| Reference only shows desktop | Design mobile deliberately; do not just shrink |
| Icons in the reference | Use the project's icon set if close; otherwise extract as SVG if you have the asset, never trace by eye as a final result |
| Reference contains dummy copy | Use realistic content of similar length |
| Reference conflicts with accessibility (low contrast) | Keep the look where possible, adjust values to meet contrast, and tell the user |

## Common mistakes
- Building a static replica with no interactions or states.
- Guessing pixel values and never comparing the render.
- Replacing the reference's type and color with library defaults.
- Missing the narrow-width and error states.
- Claiming a match without rendering it.

## Verification
- Render at the reference viewport and compare; record remaining differences and why they remain.
- Check at least one narrower and one wider width.
- Test keyboard operation and interactive states.
- If no browser or screenshot tool is available, say plainly that the match was not verified visually and list what was checked from code only.

## Deliverables
Working UI, reference inventory with assumptions and substitutions, list of remaining differences.

## References
- [Reference inventory template](templates/reference-inventory.md)
