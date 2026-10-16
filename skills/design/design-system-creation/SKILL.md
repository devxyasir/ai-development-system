---
name: design-system-creation
description: "Creates or extends a design system: tiered design tokens (primitive, semantic, component), spacing, radius, elevation, motion tokens, component variants, theming and documentation, enforced by lint-style checks. Use when starting a UI codebase, when styles are hard-coded and inconsistent, when adding dark mode or themes, or when a component library needs rules."
metadata:
  category: design
  version: "0.1.0"
  related: "visual-design-direction, color-palette-selection, typography-selection, component-engineering, motion-design"
---

# Design system creation

A design system is a small set of decisions encoded as tokens and components so screens stay consistent without every author re-deciding. Keep it as small as the product needs.

## When to use
- A new front end needs a style foundation, or existing CSS is full of one-off values.
- Adding dark mode, theming, density modes or a second brand.
- Not for: choosing the look itself (visual-design-direction) or building a single component (component-engineering).

## Procedure
1. **Audit what exists.** Search the code for distinct colors, font sizes, spacings and radii (for example `grep -rhoE "#[0-9a-fA-F]{3,8}" src | sort | uniq -c | sort -rn`). Count them. If a design system or tokens already exist, extend them; do not create a second one.
2. **Read the design rationale** from visual-design-direction. If none exists, run that skill first.
3. **Define primitives** (raw values): palette ramps, spacing steps, radii, font sizes. Primitives are never used directly in components.
4. **Define semantic tokens** (meaning): `color-bg`, `color-surface`, `color-text`, `color-text-muted`, `color-border`, `color-action`, `color-on-action`, `color-focus`, `color-success`, `color-warning`, `color-danger`. Themes remap semantic tokens only.
5. **Define scales:** spacing on a 4 px base (4, 8, 12, 16, 24, 32, 48, 64, 96), a type scale, one radius scale, an elevation scale (borders or tone before shadows), and motion durations and easings.
6. **Define component tokens only where needed** (for example `button-bg`) when a component needs to diverge from the semantic layer.
7. **Inventory components** that actually appear in the product. For each: variants, sizes, states (default, hover, focus-visible, active, disabled, loading, error), and what it must never contain.
8. **Write the tokens file** (see [tokens template](templates/tokens.css) and [architecture notes](references/token-architecture.md)). Check every text/background pair with the contrast tool in color-palette-selection.
9. **Enforce.** Add a check that fails on hard-coded colors and pixel spacings outside the tokens file (a grep in CI is enough to start).
10. **Document** in one page: how to add a token, how to add a component, what is deprecated.

## Decision rules
| Situation | Do this |
| --- | --- |
| Value appears once and is not part of the scale | Keep it local and comment why; do not add a token |
| Same value appears three or more times | Promote it to a token |
| Two near-identical values (14px and 15px) | Pick one, replace both |
| New theme requested | Remap semantic tokens; do not touch components |
| Existing UI library in the project | Theme it with your tokens; do not add a second library |

## Common mistakes
- Naming tokens by appearance (`blue-button`) instead of role (`color-action`).
- Skipping the semantic layer, so dark mode requires editing every component.
- Building 40 components before one real screen uses them.
- Dark mode made by inverting colors rather than designing surfaces and contrast.

## Verification
- No hard-coded colors or off-scale spacing remain outside the tokens file (run the grep from step 1 again).
- Toggle every theme and look at one representative screen per theme; if no browser tool is available, state that themes were not visually checked.
- Contrast passes for all semantic text/background pairs in every theme.
- Every component in the inventory renders each of its states.

## Deliverables
Tokens file, component inventory with states, one-page usage doc, enforcement check.

## References
- [Token architecture](references/token-architecture.md): tiers, naming, theming patterns, platform notes.
- [Illustrative tokens file](templates/tokens.css): structure to copy; every value must be replaced by your own decisions.
