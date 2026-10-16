# Layout patterns

## Structures and when to use them
| Structure | Use when | CSS starting point |
| --- | --- | --- |
| Single column stack | Reading, forms, mobile default | `display: grid; gap: var(--space-4); max-width: 65ch;` |
| Sidebar + main | App navigation, filters beside results | `grid-template-columns: minmax(14rem, 18rem) 1fr;` collapse below a breakpoint |
| Master-detail | Lists with a selected item | Two columns on wide screens; separate routes on narrow ones |
| Equal grid | Browsing comparable visual items | `grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));` |
| Holy grail (header, nav, main, aside, footer) | Documentation, portals | Named grid areas |
| Canvas | Editors, maps, diagrams | Toolbars as overlays or panels around a flexible stage |
| Timeline | Sequential events | Single axis with consistent date column |

## Recipes
```css
/* Constrained, centered content with full-bleed backgrounds possible */
.wrap { width: min(100% - 2rem, 72rem); margin-inline: auto; }

/* Responsive grid without media queries */
.grid { display: grid; gap: var(--space-4); grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr)); }

/* Component-level responsiveness */
.card-host { container-type: inline-size; }
@container (min-width: 32rem) { .card { display: grid; grid-template-columns: 8rem 1fr; } }

/* Scrolling table inside a container so the page never scrolls sideways */
.table-scroll { overflow-x: auto; max-width: 100%; }

/* Full-height mobile layout */
.app { min-height: 100dvh; }
```

## Spacing logic
- Inside a component: 4-12 px steps. Between components: 16-32 px. Between sections: 48-96 px.
- Increase space around the most important element rather than adding borders.
- Optical alignment: icons next to text often need a 1-2 px nudge; check visually.

## Responsive checks by width
| Width | Look for |
| --- | --- |
| 320 | No horizontal page scroll, text readable, tap targets not overlapping |
| 375-430 | Primary action reachable by thumb, forms usable with the keyboard open |
| 768 | Awkward in-between layouts (two columns too narrow, nav overflowing) |
| 1024-1440 | Line length, empty space, content not stretched |
| 1920+ | Content constrained with `max-width`, backgrounds still fill |

## Right-to-left
- Replace `left/right` with logical properties; test with `dir="rtl"` and a real RTL string.
- Keep numbers, code and brand names readable inside RTL text with `bdi` or isolation.
