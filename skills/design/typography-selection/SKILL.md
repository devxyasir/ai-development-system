---
name: typography-selection
description: "Selects typefaces and builds a type system: pairing, modular scale, line height and measure, weights, numerals, code, font loading and fallbacks, and multilingual or right-to-left support (Arabic, Urdu, CJK). Use when choosing fonts, fixing hard-to-read text, building a type scale, adding a language, or fixing layout shift from font loading."
metadata:
  category: design
  version: "0.1.0"
  related: "visual-design-direction, design-system-creation, layout-and-responsive-design, frontend-performance"
---

# Typography selection

Type carries most of an interface. Choose fonts for the audience, languages and content, then set a scale and loading strategy that keeps text readable and stable.

## When to use
- Picking fonts, building a type scale, or fixing readability (cramped lines, long lines, tiny text).
- Adding a language or a right-to-left script, or fixing layout shift caused by web fonts.
- Not for: palette (color-palette-selection) or overall direction (visual-design-direction).

## Procedure
1. **List the content and scripts.** Reading text, UI labels, data tables, code, headings, and every language and script the product must support. Check that each candidate font covers all required scripts and symbols; a default or fallback font mixed in mid-line looks broken.
2. **Choose roles, not fonts.** Decide the roles needed (UI/body, display, mono). One family with several weights is a valid answer. Add a second family only for a stated reason.
3. **Shortlist two or three candidates per role** that suit the direction (see visual-design-direction). Evaluate with real content at real sizes: long paragraph, numbers in a table, a button, a small caption, the longest label.
4. **Check licensing and delivery.** Prefer fonts with a clear license; self-host with `woff2`; subset to needed scripts; use a variable font when you need many weights.
5. **Set the scale.** Base 16 px (1rem) for body. Use a ratio from 1.125 to 1.333 and round to a handful of steps ([scale reference](references/type-system.md)). Use `clamp()` for fluid headings only; keep body text fixed or nearly so.
6. **Set rhythm.** Body line height about 1.4-1.6; headings about 1.1-1.3; measure (line length) about 45-75 characters via `max-width: 65ch`; paragraph spacing from the spacing scale.
7. **Set details.** `font-variant-numeric: tabular-nums` for tables and counters; avoid more than three weights; never use all-caps for long text; use real italics and bold.
8. **Load safely.** `font-display: swap` (or `optional` for non-critical fonts), preload only the one or two critical files, define a metric-matched fallback to limit layout shift (see reference), and test with the network throttled.
9. **Handle other scripts:** logical CSS properties and `dir="rtl"`; no letter-spacing on Arabic-script text; give Nastaliq-style Urdu fonts much more line height than Latin; test CJK with `lang` set so the right glyph forms are chosen.

## Decision rules
| Situation | Do this |
| --- | --- |
| Dense data UI | Compact sans with tabular numerals, 13-14 px minimum for secondary text |
| Long-form reading | 17-20 px body, 1.5-1.7 line height, measure under 75 characters |
| Mixed Latin and Arabic or Urdu | Choose a Latin font and an Arabic-script font designed to pair; size-adjust so x-heights look equal |
| Need identity but little budget | One characterful display face for headings, a system or neutral face for UI |
| Performance-critical page | System font stack for UI, one web font for headings |

## Common mistakes
- Picking a font from a favorites list without checking script coverage.
- Using several near-identical sans families.
- Body text under 16 px on mobile, or tiny gray captions that fail contrast.
- Loading eight weights and blocking render on them.
- Letter-spacing or uppercase transforms applied to Arabic-script text.

## Verification
- Render real content in each role at the smallest and largest sizes, in every supported language and direction; if no browser tool is available, state that rendering was not checked.
- Contrast passes for all text colors (see color-palette-selection).
- Throttle the network and reload: no invisible text for long, and layout shift is small.
- Zoom to 200% and enlarge text-only: nothing clips or overlaps.

## Deliverables
Font choices with reasons and licenses, scale tokens, loading snippet, fallback stack, per-script notes.

## References
- [Type system reference](references/type-system.md): scale table, loading code, fallback metrics, multilingual notes.
