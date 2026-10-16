# Type system reference

## Scale (base 16 px, ratio 1.25, rounded)
| Step | rem | px | Typical use |
| --- | --- | --- | --- |
| -1 | 0.8 | 12.8 | Captions, legal (avoid below this) |
| 0 | 1 | 16 | Body |
| 1 | 1.25 | 20 | Lead text, small headings |
| 2 | 1.563 | 25 | h3 |
| 3 | 1.953 | 31 | h2 |
| 4 | 2.441 | 39 | h1 |
| 5 | 3.052 | 49 | Display (use sparingly) |
Ratios: 1.125 (tight, dense UI), 1.25 (general), 1.333 (editorial), higher for marketing display only.

## Fluid headings (only where useful)
```css
h1 { font-size: clamp(2rem, 1.2rem + 3vw, 3.5rem); line-height: 1.1; }
.prose { max-width: 65ch; line-height: 1.6; }
```
Avoid fluid sizing that prevents users from enlarging text; include `rem` in the clamp so user font-size settings still scale it.

## Loading
```css
@font-face {
  font-family: "Brand Sans";
  src: url("/fonts/brand-sans-var.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
}
/* Metric-matched fallback reduces layout shift when the web font swaps in. Tune the numbers by measurement. */
@font-face {
  font-family: "Brand Sans Fallback";
  src: local("Arial");
  size-adjust: 104%;
  ascent-override: 92%;
  descent-override: 24%;
}
body { font-family: "Brand Sans", "Brand Sans Fallback", system-ui, sans-serif; }
```
```html
<link rel="preload" href="/fonts/brand-sans-var.woff2" as="font" type="font/woff2" crossorigin>
```
- The override values above are illustrative; derive real ones from the font's metrics with a tool or by measurement.
- Preload only fonts used above the fold. Subset to required scripts and use `unicode-range` for large multi-script families.

## Numerals and code
- `font-variant-numeric: tabular-nums;` for columns, prices, timers. `slashed-zero` helps in code and IDs.
- Monospace for code only; match its apparent size to body (many monospace faces look smaller, so adjust with `font-size-adjust` or a manual ratio).

## Multilingual and right-to-left
- Set `lang` and `dir` on the document or the element; use logical properties (`margin-inline-start`, `padding-inline`, `text-align: start`) so layouts mirror correctly.
- Arabic-script text: do not apply letter-spacing (it breaks the joining of letters); avoid synthetic bold and italic; test shaping with real words, not Latin sample text.
- Urdu in Nastaliq style needs generous line height (often much larger than Latin text) and enough vertical room so diacritics and tall letterforms do not clip; verify in a real rendering.
- Numerals: decide on Western or Arabic-Indic digits per audience and be consistent.
- CJK: set `lang` (ja, ko, zh-Hans, zh-Hant) so the browser picks correct glyph variants; avoid italics; allow line breaking without spaces.
- Mixed-direction strings (RTL text containing Latin names or numbers) need `bdi` or `unicode-bidi: isolate` for user-generated content.

## Checks that catch most problems
1. Paste the longest real label and the longest real paragraph; look for clipping and awkward wraps.
2. Increase the browser's default font size; confirm the layout reflows.
3. Disable the web font; confirm the fallback is still readable and similarly sized.
