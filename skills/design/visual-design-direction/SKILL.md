---
name: visual-design-direction
description: "Chooses a deliberate visual direction (identity, color strategy, type pairing, shape, density, imagery, motion language) from the product's audience and context so interfaces do not default to generic AI-template looks. Use when starting or redesigning a UI, when output looks generic, or when asked for a distinctive look or brand feel. Produces a one-page design rationale."
metadata:
  category: design
  version: "0.1.0"
  related: "product-design, design-system-creation, color-palette-selection, typography-selection, motion-design"
---

# Visual design direction

Pick the look from the product's real context, write down why, and only then build tokens. The failure this prevents: the same purple gradient, navy background, default sans, glass cards and pill buttons on every project.

## When to use
- A new interface, a redesign, or feedback that the result "looks generic".
- Before running design-system-creation, color-palette-selection or typography-selection.
- Not for: screen structure (product-design) or implementing an existing mockup (design-to-code).

## Procedure
1. **Gather context.** Audience, domain, tone, device and environment (glare, one hand, dark room), content type (data, reading, media), brand constraints, language and direction (RTL, CJK).
2. **State the direction in words.** Three adjectives and one "not" (for example: precise, calm, editorial; not playful). Everything later must match these words.
3. **Collect three references by description.** Name what each does well (a printed timetable's density, a lab instrument's labelling, a newspaper's hierarchy). Describe, do not copy.
4. **Decide the eight identity choices:** color strategy, type pairing, shape language (radius scale), density, layout rhythm, imagery and illustration style, icon style (stroke weight, fill), motion language. Use [the method](references/direction-method.md) for the options of each.
5. **Run the anti-default check.** For each item in [anti-generic defaults](references/anti-generic-defaults.md), either avoid it or write a one-line justification tied to the context.
6. **Write the rationale** using the [template](templates/design-rationale.md): one page, with the decisions, the reason for each, and what you deliberately rejected.
7. **Hand off:** tokens go to design-system-creation, palette to color-palette-selection, fonts to typography-selection.

## Starting points by context (not rules)
| Context | Direction to test first |
| --- | --- |
| Finance, compliance, admin tools | Restrained, high contrast, tabular numerals, conservative motion |
| Developer tools | Dense, keyboard-first, monospaced accents, minimal chrome |
| Healthcare, public services | Calm, large targets, plain language, strong accessibility margins |
| Creative portfolio, campaign sites | Expressive type, asymmetric layout, cinematic motion (see cinematic-motion) |
| Long-form reading | Serif or humanist body, generous leading, narrow measure |
| E-commerce | Product imagery first, fast, visible trust signals |
| Children, education | Warm and bright but accessible, larger targets, simple language |

## Common mistakes
- Choosing colors first and calling it a direction.
- Using a trend (glassmorphism, neon glow) because it is current rather than because it fits.
- Decorating task software with hero sections, stock illustrations and meaningless metrics.
- Writing a rationale after building, which only justifies what already exists.

## Verification
- Every identity choice has a stated reason that refers to the audience or context.
- Each default in the anti-default list is avoided or justified in one line.
- A reviewer can answer "why this palette and these fonts?" from the rationale alone.
- If screens exist: render them and confirm they read as the stated adjectives; otherwise state that the direction is unverified visually.

## Deliverables
Design rationale (one page), initial token decisions, list of rejected defaults.

## References
- [Direction method](references/direction-method.md): the option set for each identity choice.
- [Anti-generic defaults](references/anti-generic-defaults.md): what to avoid by default and when it is justified.
- [Design rationale template](templates/design-rationale.md)
