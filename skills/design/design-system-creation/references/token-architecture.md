# Token architecture

## Three tiers
1. **Primitive**: `--p-vermilion-600: #b8400f;` Raw, named by hue and step. No meaning.
2. **Semantic**: `--color-action: var(--p-vermilion-600);` Named by role. Components use only this tier.
3. **Component**: `--button-bg: var(--color-action);` Optional; use when a component needs its own knob.

Rule: components reference semantic or component tokens, never primitives.

## Naming
- `category-role-variant-state`: `color-text-muted`, `space-4`, `radius-md`, `dur-fast`.
- Use roles (`danger`, `surface-raised`), not appearances (`red`, `light-gray`).
- Numeric scales use steps (`space-1..space-12`), not t-shirt sizes mixed with numbers.

## Theming patterns
- **`light-dark()`** with `color-scheme: light dark;` lets one declaration hold both values: `--color-bg: light-dark(#faf6ef, #17140f);`. It is part of recent CSS; verify browser support for your audience before relying on it and provide a fallback block if needed.
- **Attribute override:** `:root[data-theme="dark"] { color-scheme: dark; }` lets users override the system setting.
- **Alternative (wide support):** define dark values inside `@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { ... } }` and repeat them under `:root[data-theme="dark"]`.
- Dark mode is designed, not inverted: lower saturation of accents, raise surface lightness to show elevation, re-check contrast.

## Spacing and sizing
- 4 px base unit, 8 px as the common step; use `rem` for type and spacing that should scale with user font size.
- Touch targets at least 24x24 CSS px (WCAG 2.2 minimum); 44x44 is a better default for primary touch controls.

## Elevation
- Prefer tone and 1 px borders for layering in flat styles; if shadows are used, define 2-3 levels and never invent new ones per component.

## Motion tokens
- Durations: `--dur-fast`, `--dur-base`, `--dur-slow`. Easings: `--ease-out`, `--ease-in`, `--ease-in-out`. Define once; see the motion-design skill for values and reasons.

## Platform notes
- Tailwind: put tokens in the theme configuration and map utilities to semantic names; avoid raw palette utilities in components.
- CSS-in-JS or component libraries: export tokens as a typed object generated from one source of truth.
- Multiple platforms (web and native): keep tokens in a neutral JSON file and generate platform outputs; do not hand-copy values.

## Enforcement ideas
- CI grep for `#[0-9a-fA-F]{3,8}` and `\b\d+px\b` outside the tokens file (allow-list exceptions with a comment).
- Lint rule or code review checklist item: "no new token without three uses or a written reason".
