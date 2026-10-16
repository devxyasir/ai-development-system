# Visual QA checklist

Mark each item Pass, Issue or Not checked, per screen and width.

## Layout and alignment
- Elements align to a consistent set of edges; gutters equal where intended.
- No overlap, clipping, or elements hidden under fixed bars.
- Content width constrained on wide screens; backgrounds fill correctly.
- Vertical rhythm follows the spacing scale.

## Typography
- Hierarchy is clear: one dominant heading, distinct subheadings, readable body.
- Line length about 45-75 characters for reading text; line height comfortable.
- No orphaned single words in headings where avoidable; no awkward breaks in buttons or labels.
- Correct fonts loaded (no fallback flash that stays); numbers tabular where needed.

## Color and contrast
- Text and UI contrast meet the target (measure; do not guess).
- Accent used only for primary actions and key states.
- States distinguishable without color alone.
- Dark theme (if present) has separate checks for surfaces, borders and shadows.

## Responsive behavior
- 320 px: no horizontal page scroll, controls reachable and large enough.
- Intermediate widths: no awkward two-column squeeze.
- Wide screens: not stretched.
- Orientation change and 200-400% zoom handled.

## Components and states
- Default, hover, focus-visible, active, disabled, loading, error, success, empty exist where relevant.
- Forms: labels, validation messages, help text, long values, autofill.
- Tables and lists: long text, many rows, zero rows, sorting and filtering states.
- Overlays: open, close, focus handling, scroll lock, stacking order.

## Motion
- Animations start, end and interrupt cleanly; no layout shift.
- Reduced-motion variant verified.
- No animation blocks input.

## Content realism
- Real-length names, addresses, numbers, translated strings, user-generated content.
- Images: loading placeholder, missing image, wrong aspect ratio.

## Loading, empty and error
- Initial load, slow network, offline (if supported), API error, permission denied, not found.

## Consistency across screens
- Same component looks and behaves the same everywhere; spacing and type scale consistent.

## Accessibility spot checks
- Keyboard tab order and visible focus on every screen.
- Page title, headings, landmarks make sense.
- Run accessibility-review for the full pass.
