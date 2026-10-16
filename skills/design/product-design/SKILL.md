---
name: product-design
description: "Designs the user journey, information architecture, screen structure and every screen state before any visual styling. Use when planning a new app, dashboard, form flow, onboarding or navigation, when a UI feels confusing, or when asked how a screen or feature should work. Not for choosing colors, fonts or animation."
metadata:
  category: design
  version: "0.1.0"
  related: "visual-design-direction, accessibility-review, requirements-and-research, design-to-code"
---

# Product design

Turn a request into a task-focused structure: who is doing what, in which order, and what they see in every state. Styling comes afterwards (see visual-design-direction).

## When to use
- Starting a screen, flow or product, or deciding what belongs on a page.
- Navigation or a form feels confusing, or a request names a layout ("add a dashboard") without naming the user's task.
- Not for: visual styling (visual-design-direction) or building from an existing mockup (design-to-code).

## Procedure
1. **Name the user and the job.** Write one sentence: "<role> needs to <task> so that <outcome>." If you cannot, ask one question or record the assumption in the brief.
2. **Rank tasks.** List the top three by frequency x importance. Everything else is secondary and must not compete for space or attention.
3. **Map the journey.** Entry point, steps, success state, next action. Count the steps. Remove any step that asks for data you can derive or already have.
4. **Define information architecture.** Group by the user's mental model, not the database. Label with the user's words. Keep top-level navigation to roughly seven items or fewer.
5. **Pick a structure per task** using the table below.
6. **Specify every state:** empty, loading, partial, error, success, no-permission, and offline where relevant. A screen without its states is unfinished.
7. **Write the copy.** Buttons are specific verbs ("Save changes"). Errors say what happened and how to fix it. Empty states say what belongs here and offer the primary action.
8. **Write the brief** ([template](templates/design-brief.md)), including acceptance criteria a tester can check.

## Choosing a structure
| Task | Prefer | Avoid |
| --- | --- | --- |
| Compare many items on many attributes | Sortable, filterable table | Cards |
| Browse visual items | Grid of thumbnails/cards | Dense table |
| Edit one record | Single-column form in labeled groups | Multi-column forms |
| Monitor status | The 3-5 numbers that trigger action | Decorative metrics |
| Linear multi-step process | Stepper with saved progress | One very long form |
| Explore a hierarchy | Tree or master-detail | Nested modals |
| Time-based events | Timeline or calendar | Arbitrarily sorted list |

## Decision rules
- Destructive or irreversible action: state the consequence in the confirmation, or prefer undo to confirm.
- More than about seven required fields on one screen: split with progressive disclosure.
- Users return daily: optimize repeat use (shortcuts, saved filters, remembered state) over first-run delight.
- A dashboard number stays only if you can finish the sentence "if this changes, the user will ___".
- Task-focused software gets no oversized hero; the working surface is the first thing visible.

## Common mistakes
- Designing from the sitemap or database tables instead of the user's task.
- Forgetting empty, error and permission states, then discovering them in production.
- Jargon labels, and icon-only controls with no accessible name.
- Treating "looks modern" as a requirement.

## Verification
- Walk each top task using only the written spec: no dead ends, step count noted.
- Every screen lists its states; every state has copy.
- If a UI exists and a browser tool is available, render it and walk the flow; otherwise state that the flow was reviewed on paper only.

## Deliverables
Design brief, flow description, state matrix per screen, acceptance criteria.

## References
- [UX patterns](references/ux-patterns.md): forms, search and filters, dashboards, empty states, onboarding, destructive actions, error recovery, content design. Read when a task involves one of these.
- [Design brief template](templates/design-brief.md)
