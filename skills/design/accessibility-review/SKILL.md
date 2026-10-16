---
name: accessibility-review
description: "Reviews and fixes accessibility of web interfaces against WCAG 2.2 AA: keyboard operation, focus, names and roles, forms and errors, contrast, reflow, target size, motion, and screen-reader behavior, with severity ratings. Use when building or auditing UI, before release, when asked about accessibility, ARIA, keyboard support or screen readers."
metadata:
  category: design
  version: "0.1.0"
  related: "visual-qa, color-palette-selection, reduced-motion-accessibility, frontend-testing"
---

# Accessibility review

Make the interface usable by keyboard, screen reader, zoom and reduced-motion users. Automated tools find only part of the problems; manual checks are required.

## When to use
- Building or changing interactive UI, reviewing before release, or answering a question about ARIA, focus, forms or screen readers.
- Not for: legal compliance advice; state the standard checked and what was not verified.

## Procedure
1. **Fix the target:** WCAG 2.2 Level AA unless the project states otherwise. Record it.
2. **Run automated checks** if available (axe-core, Lighthouse, linters such as eslint-plugin-jsx-a11y). Treat results as a starting list; they catch a minority of real issues.
3. **Keyboard pass:** put the mouse away. Tab through the page: every control reachable, order matches reading order, focus indicator always visible and not hidden under sticky headers, no keyboard traps, modals trap focus while open and return it on close, Escape closes overlays.
4. **Semantics pass:** use native elements first (`button`, `a`, `input`, `label`, `dialog`, `nav`, `main`, headings in order). Add ARIA only when no native element fits, and follow the pattern's full keyboard contract. Every control has an accessible name; icons-only buttons have `aria-label` or visually hidden text.
5. **Forms pass:** visible labels tied by `for`/`id`, errors identified in text and linked (`aria-describedby`), required state exposed, `autocomplete` on personal data, no re-asking for data already given in the same flow.
6. **Visual pass:** contrast (4.5:1 text, 3:1 UI), not color alone, reflow at 320 CSS px and 400% zoom, text spacing overrides do not break layout, targets at least 24x24 CSS px.
7. **Motion and media pass:** `prefers-reduced-motion` honored (see reduced-motion-accessibility), nothing flashes more than three times per second, moving content over 5 seconds can be paused, captions or transcripts for media.
8. **Screen reader pass** with at least one real reader when possible (NVDA, VoiceOver, TalkBack): headings and landmarks navigable, dynamic updates announced (`role="status"`, `aria-live="polite"`), names and states read sensibly.
9. **Record issues** with severity (below), the WCAG criterion, the location, and a concrete fix; apply fixes and recheck.

## Severity
| Level | Meaning | Example |
| --- | --- | --- |
| Blocker | A user group cannot complete a core task | Checkout button not keyboard reachable |
| Major | Task possible but with serious difficulty | No visible focus; error not announced |
| Minor | Annoyance or best-practice gap | Redundant link text, heading skipped a level |

## Common mistakes
- `div` with click handlers instead of `button`; positive `tabindex` values.
- ARIA that contradicts native semantics (`role="button"` on a link that navigates).
- Focus lost when content is removed or a route changes; focus not moved into new dialogs.
- Placeholder as the only label; error shown only as red text.
- Claiming "accessible" after an automated scan alone.

## Verification
- Keyboard pass completed for every changed flow.
- Automated scan has zero new violations, and manual findings are listed with status.
- State exactly what was and was not checked (for example "no screen reader available; keyboard and automated checks only").

## Deliverables
Findings list with severity and fixes, list of checks performed, remaining risks.

## References
- [WCAG review checklist](references/wcag-review-checklist.md): criteria grouped by check, with how to test each.
