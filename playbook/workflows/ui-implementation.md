# Workflow: Building a user interface

Requires: [core principles](../core/00-core-principles.md)

## When to use
Building or changing screens, components or layouts, whether from a design reference (screenshot, mockup, existing site) or from a description.

## Inspect first
- The project's framework, styling method, tokens and existing components
- Whether a design reference exists and what it shows (and does not show)
- Supported browsers, devices, languages and text directions
- How to run the app and whether a browser or screenshot tool is available

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [component-engineering](../../skills/frontend/component-engineering/SKILL.md) | Always |
| [layout-and-responsive-design](../../skills/design/layout-and-responsive-design/SKILL.md) | Always |
| [accessibility-review](../../skills/design/accessibility-review/SKILL.md) | Always |
| [visual-qa](../../skills/frontend/visual-qa/SKILL.md) | Always |
| [design-to-code](../../skills/frontend/design-to-code/SKILL.md) | A design reference was supplied |
| [product-design](../../skills/design/product-design/SKILL.md) | New screens or flows must be designed, or the structure is unclear |
| [visual-design-direction](../../skills/design/visual-design-direction/SKILL.md) | No visual identity or design system exists yet |
| [design-system-creation](../../skills/design/design-system-creation/SKILL.md) | Tokens or shared styles must be created or extended |
| [color-palette-selection](../../skills/design/color-palette-selection/SKILL.md) | Colors must be chosen or contrast fixed |
| [typography-selection](../../skills/design/typography-selection/SKILL.md) | Fonts or a type scale must be chosen, or non-Latin scripts are needed |
| [frontend-architecture](../../skills/frontend/frontend-architecture/SKILL.md) | The change spans routes, data fetching or shared state |
| [ui-animation](../../skills/motion/ui-animation/SKILL.md) | Animation or transitions are requested |
| [frontend-testing](../../skills/frontend/frontend-testing/SKILL.md) | Tests for the interface are needed |

## Steps
1. Establish what the interface must let the user do (acceptance criteria) and which states it has.
2. If a reference exists, inventory it first (regions, type, color, spacing, missing states).
3. Reuse existing tokens and components; add new ones only when needed.
4. Build layout first at the smallest width, then widen; then typography, color and details.
5. Implement real behavior: interactions, forms, loading, empty and error states, keyboard use.
6. Run the app and look at it: capture at 320, 768 and 1440 px (and other widths that matter) and each important state.
7. Compare with the reference or the intended design; list differences; fix the largest first.
8. Run the accessibility pass and the tests.
9. Write the visual QA report.

## Decisions
| Situation | Do this |
| --- | --- |
| No design system exists | Create a small token set (design-system-creation) instead of scattering values |
| Reference conflicts with accessibility | Keep the look where possible, meet contrast and target size, tell the user |
| No browser tool | State that the interface was not rendered; review code against the visual QA checklist and give the user steps to verify |
| Generic output risk | Run the anti-default check in visual-design-direction |

## Artifacts
- Working interface and tests
- Visual QA report
- Notes on substitutions and assumptions

## Verify
- Rendered and inspected at the stated widths and states, or explicitly not rendered
- Keyboard operation and visible focus work
- Contrast measured for text and controls
- No horizontal scroll at 320 px; long and empty content handled

## If verification fails
1. Layout breaks at some width: fix the structure rather than hiding overflow.
2. Rendered result differs from the reference: continue comparison rounds; list remaining differences honestly.

## Final report
- What was built and where
- Verification level for visuals (rendered / code only)
- Widths, themes and states captured
- Open issues by severity

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [animation-implementation](animation-implementation.md): for motion
- [testing-and-verification](testing-and-verification.md): for test planning
