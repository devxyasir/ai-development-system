# WCAG 2.2 AA review checklist

Use as a working list. "How to test" is a manual or tool check you can actually do. Criterion numbers are WCAG 2.x identifiers.

## Perceivable
| Check | Criterion | How to test |
| --- | --- | --- |
| Images have text alternatives; decorative images have empty `alt` | 1.1.1 | Inspect `img`, SVG `title`/`aria-label`; screen reader |
| Video has captions; audio has transcript | 1.2.x | Play without sound |
| Headings, lists, landmarks use real elements | 1.3.1 | Outline view or screen reader headings list |
| Reading order matches visual order | 1.3.2 | Tab and read order with CSS disabled |
| Inputs identify purpose (`autocomplete`) | 1.3.5 | Inspect attributes on name, email, address fields |
| Information not conveyed by color alone | 1.4.1 | Grayscale view |
| Text contrast 4.5:1 (3:1 large) | 1.4.3 | contrast tool |
| Text resizes to 200% without loss | 1.4.4 | Browser zoom, text-only zoom |
| No horizontal scroll at 320 CSS px; 400% zoom | 1.4.10 | Narrow window or zoom |
| UI component and graphic contrast 3:1 | 1.4.11 | contrast tool on borders, icons, focus rings |
| Layout survives text-spacing overrides | 1.4.12 | Apply spacing bookmarklet or CSS |
| Hover/focus content dismissible, hoverable, persistent | 1.4.13 | Tooltips and popovers by mouse and keyboard |

## Operable
| Check | Criterion | How to test |
| --- | --- | --- |
| Everything usable by keyboard; no traps | 2.1.1, 2.1.2 | Tab, Shift+Tab, Enter, Space, arrows, Escape |
| Single-key shortcuts can be turned off or remapped | 2.1.4 | Review shortcut implementation |
| Time limits adjustable; moving content pausable | 2.2.1, 2.2.2 | Check timers, carousels, auto-updating regions |
| No content flashes more than three times per second | 2.3.1 | Review animations and video |
| Skip link or landmarks to bypass repeated blocks | 2.4.1 | First Tab press |
| Page titles and focus order are meaningful | 2.4.2, 2.4.3 | Read titles; Tab order |
| Link purpose clear from text or context | 2.4.4 | Links list in screen reader |
| Visible focus indicator | 2.4.7 | Tab through everything |
| Focus is not hidden by sticky or fixed content | 2.4.11 | Tab to elements near sticky headers and footers |
| Pointer gestures have simple alternatives (no path-only drag) | 2.5.1, 2.5.7 | Try each gesture with single taps or clicks |
| Visible label is contained in accessible name | 2.5.3 | Compare label text with accessible name |
| Targets at least 24x24 CSS px (or spaced) | 2.5.8 | Measure in dev tools |

## Understandable
| Check | Criterion | How to test |
| --- | --- | --- |
| Page language set; language changes marked | 3.1.1, 3.1.2 | `lang` attributes |
| Focus or input does not cause unexpected context change | 3.2.1, 3.2.2 | Interact with each control |
| Help and navigation in consistent places | 3.2.3, 3.2.6 | Compare pages |
| Errors identified and described in text; suggestions given | 3.3.1, 3.3.3 | Submit invalid data |
| Labels or instructions present | 3.3.2 | Inspect forms |
| Important submissions reversible, checked or confirmed | 3.3.4 | Review destructive flows |
| Users are not asked to re-enter information already provided | 3.3.7 | Walk multi-step flows |
| Authentication does not rely on a cognitive test (paste allowed, password managers work) | 3.3.8 | Try password manager and paste |

## Robust
| Check | Criterion | How to test |
| --- | --- | --- |
| Name, role, value exposed for custom controls | 4.1.2 | Accessibility tree in dev tools; screen reader |
| Status messages announced without moving focus | 4.1.3 | Trigger toasts and validation with a screen reader |

## Patterns that need the full keyboard contract
Dialog (focus trap, Escape, return focus), menu/menubar, tabs (arrow keys, roving tabindex), combobox, tree, slider. Use native elements or a tested library for these; if you build one, follow the published authoring practices for that pattern and test with a screen reader.
