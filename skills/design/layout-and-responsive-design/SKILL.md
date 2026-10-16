---
name: layout-and-responsive-design
description: "Designs layout, spacing, alignment, composition and responsive behavior: grids, spacing scales, breakpoints, container queries, fluid sizing, touch targets, reflow at narrow widths, and right-to-left mirroring. Use when building or fixing a page layout, when a UI breaks on mobile or large screens, when content overflows, or when spacing looks inconsistent."
metadata:
  category: design
  version: "0.1.0"
  related: "product-design, design-system-creation, visual-qa, accessibility-review, typography-selection"
---

# Layout and responsive design

Layouts should follow the content and the task, hold their structure across screen sizes, and use one spacing system. Decide the structure first, then the breakpoints the content forces.

## When to use
- Building or repairing a page or component layout; mobile or very wide screens look wrong; content overflows or wraps badly; spacing feels arbitrary.
- Not for: choosing colors or fonts, or deciding what belongs on a screen (product-design).

## Procedure
1. **Start from content and task.** Which region is primary? What must stay visible? Sketch the structure at the smallest width first (single column), then add structure as space allows.
2. **Choose the structure** per region: stack, split (list plus detail), sidebar plus main, grid of equals, canvas. Use cards only for items that are equal and browsable; see [layout patterns](references/layout-patterns.md).
3. **Apply one spacing scale** (4 px base: 4, 8, 12, 16, 24, 32, 48, 64). Related items sit closer than unrelated ones (proximity); repeat gaps consistently.
4. **Align to a few visible lines.** Pick left edges and baselines; avoid items that almost align. Use CSS grid or flexbox with `gap`, not margins stacked by hand.
5. **Let content set breakpoints.** Widen the viewport until the layout looks stretched, add a breakpoint there. Typical stops are 480, 768, 1024 and 1280 px, but follow the content. Prefer `min-width` media queries (mobile first).
6. **Use container queries for components** that appear in different-width slots: `@container (min-width: 32rem) { ... }` with `container-type: inline-size` on the parent. Check browser support for your audience.
7. **Size fluidly** with `clamp()`, `min()`, `max()`, `fr`, `minmax()` and `auto-fit`; avoid fixed pixel widths on containers. Use `dvh`/`svh` rather than `vh` for full-height mobile layouts.
8. **Make touch usable:** primary touch targets about 44x44 CSS px (WCAG 2.2 minimum is 24x24), spacing between targets, no hover-only functionality, thumb-reachable primary actions on phones.
9. **Handle overflow deliberately:** long words (`overflow-wrap: anywhere` where needed), wide tables (scroll inside their own container), images (`max-width: 100%`), text that grows (no fixed heights on text containers).
10. **Mirror for right-to-left:** use logical properties (`margin-inline`, `inset-inline-start`, `border-inline-end`) and flex/grid direction that follows `dir`; flip directional icons (arrows, chevrons) but not logos or media controls with universal meaning.

## Decision rules
| Situation | Do this |
| --- | --- |
| Component appears in sidebar and main area | Container query, not viewport query |
| Data table on phone | Horizontal scroll in a container, or reflow to labeled rows for few columns |
| Navigation with many items | Priority+ pattern or menu; never shrink touch targets |
| Full-bleed hero plus constrained text | Full-width wrapper, inner `max-width` container |
| Need an equal-height row of cards | Grid with `align-items: stretch`; do not set fixed heights |

## Common mistakes
- Designing at one desktop width and "making it responsive" later.
- Fixed heights on text containers; hover-only menus; 100vh on mobile.
- Stacking margins and paddings by eye instead of using gap and the scale.
- Testing only the exact widths of popular devices.

## Verification
- Check at 320, 375, 768, 1024, 1440 and one very wide width, plus 200% and 400% zoom (no horizontal scrolling of the page at 320 CSS px, WCAG reflow). If no browser tool is available, state which widths were reasoned rather than rendered.
- Resize slowly between breakpoints; nothing overlaps, clips or jumps.
- Try longest labels, translated text (about 30-40% longer), and RTL if supported.
- Keyboard and touch targets reachable and not obscured by fixed headers.

## Deliverables
Layout structure per breakpoint, spacing and grid decisions in tokens, notes on overflow and RTL handling.

## References
- [Layout patterns](references/layout-patterns.md): structures, CSS recipes, responsive checks.
