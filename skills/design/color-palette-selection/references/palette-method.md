# Palette method

## Neutral ramp
- 9-11 steps from near-white to near-black. Tint every step toward the brand hue with low chroma so surfaces feel related to the accent.
- Use lighter steps for backgrounds and raised surfaces, mid steps for borders, dark steps for text. Keep body text at least a few steps darker than muted text.

## Accent and status ramps
- Build ramps by changing lightness in even steps at roughly constant chroma (OKLCH). Convert to hex or `oklch()` for delivery; `oklch()` is supported by current browsers, verify for your audience.
- Status colors (success, warning, danger, info) need their own ramps so each has a text-safe dark step and a fill-safe light step.
- Keep hue families distinguishable by lightness as well as hue, so they survive color-vision differences and grayscale printing.

## Scripted check of a whole role table
```bash
python scripts/contrast.py "#1f1b16" "#faf6ef"            # text on background
python scripts/contrast.py "#faf6ef" "#b8400f"            # text on action fill
python scripts/contrast.py "#b8400f" "#faf6ef" --ui       # icon or border against background
```
Record each ratio next to its role in the palette table.

## Chart palettes
- Categorical: at most 6-8 hues; vary lightness too; label directly on the marks where possible.
- Sequential (ordered values): single hue, lightness from light to dark.
- Diverging (above/below a midpoint): two hues meeting at a neutral midpoint.
- Always give charts a non-color cue (direct labels, patterns, markers) for accessibility.

## Dark theme
- Surface steps get lighter with elevation (the opposite of drop shadows).
- Reduce accent saturation slightly; very saturated colors on dark backgrounds vibrate.
- Re-measure every pair; do not assume light-theme ratios carry over.

## Restraint heuristic
Roughly 60% neutral surfaces, 30% secondary/neutral emphasis, 10% accent is a starting heuristic, not a rule. The test is whether the accent still means "act here".
