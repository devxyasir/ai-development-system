---
name: color-palette-selection
description: "Selects and verifies a color palette: brand and neutral ramps, semantic roles, interactive states, chart colors, dark theme, with measured WCAG contrast and color-blind safety. Use when choosing or changing colors, fixing low contrast, adding dark mode, picking chart colors, or when a palette feels random. Includes a contrast-ratio script."
compatibility: "The bundled scripts/contrast.py uses only the Python 3 standard library (tested on 3.12)."
metadata:
  category: design
  version: "0.1.0"
  related: "visual-design-direction, design-system-creation, accessibility-review"
---

# Color palette selection

Colors carry identity, hierarchy and state. Choose them from context, build them as ramps and roles, and measure contrast instead of eyeballing it.

## When to use
- Choosing a palette, changing a brand color, fixing contrast failures, adding a dark theme, or coloring charts and status states.
- Not for: typography (typography-selection) or deciding the overall direction (visual-design-direction).

## Procedure
1. **Start from the rationale.** Read the visual direction. Decide the strategy: neutral plus one accent, duotone, or categorical.
2. **Pick the brand seed(s)** from the product's domain and audience, not from a trending palette. Record the reason.
3. **Build neutrals first.** A 9-11 step ramp tinted slightly toward the brand hue. Most of the interface is neutral; get these right before accents.
4. **Build the accent ramp** by varying lightness at similar chroma (working in OKLCH makes steps perceptually even; hex output is fine for delivery).
5. **Assign roles** (see design-system-creation): background, surface, text, muted text, border, action, on-action, focus, success, warning, danger. Use the accent only for primary actions and key state, so it keeps its meaning.
6. **Define interactive states:** hover and active steps one or two ramp steps away; disabled lowers contrast on purpose but keeps shape; focus is a high-contrast ring that is not color alone.
7. **Measure contrast** with `python scripts/contrast.py FOREGROUND BACKGROUND` for every text/background and UI/background pair, in every theme. Required minimums are in the table below.
8. **Check color-blind safety:** never encode meaning in red versus green alone; add an icon, label or pattern. For charts follow [the palette method](references/palette-method.md).
9. **Design dark theme as its own surface set:** lighter surfaces for elevation, slightly desaturated accents, re-measured contrast.

## Required contrast (WCAG 2.x ratios)
| Pair | Minimum (AA) | Stronger (AAA) |
| --- | --- | --- |
| Normal text (under 24 px, or under 18.66 px bold) | 4.5:1 | 7:1 |
| Large text (24 px+, or 18.66 px+ bold) | 3:1 | 4.5:1 |
| UI components, icons, focus indicators, chart marks against adjacent colors | 3:1 | n/a |

## Decision rules
- Text on a colored button: measure against the button color, not the page background.
- Placeholder, disabled and decorative text: placeholders still need 4.5:1 if they carry meaning; disabled controls are exempt but must stay recognizable.
- Accent fails contrast as text on the background: use it for fills and borders, and use a darker step for text links.
- More than one accent hue competing for attention: remove one or demote it to a neutral.

## Common mistakes
- Pure gray neutrals beside a saturated accent.
- Using the accent for decoration, so it no longer signals "click here".
- Checking contrast only in light mode.
- Picking 10 chart colors with no way to tell them apart; direct labels beat legends.

## Verification
- Run the contrast script on every role pair and record the ratios; all required pairs pass.
- Simulate color blindness if tools exist (browser rendering emulation or a simulator); otherwise state it was reasoned, not simulated.
- Render one dense screen and one sparse screen in each theme if a browser tool is available.

## Deliverables
Ramps, role table with measured ratios, state colors, chart palette, dark-theme mapping.

## References
- [Palette method](references/palette-method.md): ramp construction, chart palettes, dark theme notes.
- `scripts/contrast.py`: run `python scripts/contrast.py "#1f1b16" "#faf6ef"`; exit code 0 means the pair meets AA for normal text, `--large` and `--ui` change the threshold. See [palette method](references/palette-method.md) for scripted checks over a whole role table.
