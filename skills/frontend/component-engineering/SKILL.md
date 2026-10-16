---
name: component-engineering
description: "Designs and builds reusable UI components: deciding reuse versus new, API design (props, slots, variants), composition, state ownership, accessibility, styling with tokens, and documentation, in the project's existing framework. Use when creating or refactoring a component, building a component library, or when components have grown into unmaintainable conditional logic."
metadata:
  category: frontend
  version: "0.1.0"
  related: "frontend-architecture, design-system-creation, accessibility-review, frontend-testing, ui-animation"
---

# Component engineering

Build components that are small, composable, accessible and styled from tokens. Reuse what exists before writing anything new.

## When to use
- Creating or changing a component; deciding whether to reuse, extend or create.
- A component has dozens of props or nested conditionals.
- Not for: page-level structure or data flow (frontend-architecture).

## Procedure
1. **Search the codebase** for an existing component or primitive that does the job (names, props, usage). Prefer reuse; extend with a new variant only if the change is general.
2. **Decide reuse versus new** with the table below.
3. **Define the API from the caller's view:** write two or three real usages first, then derive props. Names describe intent (`variant="danger"`), not appearance (`color="red"`).
4. **Choose composition over configuration:** accept children or named slots instead of adding a prop for every possible content shape.
5. **Own state in one place:** controlled (value and onChange from parent) or uncontrolled (internal state with a default), and document which. Do not mirror props into state.
6. **Use native elements and correct semantics** (`button`, `a`, `label`, `dialog`); forward refs and rest props (class, aria attributes, data attributes) to the root element.
7. **Style from tokens** (see design-system-creation); implement every state: default, hover, focus-visible, active, disabled, loading, error, empty.
8. **Handle edge content:** very long text, empty lists, missing images, right-to-left, large font sizes.
9. **Test and document:** a test per behavior (not per prop), plus a short usage example; add to the project's component documentation or story tool if one exists.

## Reuse versus new
| Situation | Do this |
| --- | --- |
| Existing component fits | Reuse |
| Fits with one general new variant | Add the variant |
| Needs different behavior or structure | New component, share primitives |
| One-off layout used once | Local markup, not a shared component |
| Third copy of the same markup | Extract |

## Common mistakes
- Boolean prop explosion (`primary`, `large`, `outlined`, `rounded` combinations); use a variant union instead.
- Components that fetch their own data and render it, making reuse and testing hard.
- Spreading props onto the wrong element or dropping `className`/`aria-*` support.
- Hard-coded colors and spacing instead of tokens.
- A "generic" component that every caller works around.

## Verification
- Keyboard: operate the component without a mouse; focus is visible.
- Screen-reader name, role and state are correct for each variant (accessibility tree in dev tools).
- Every listed state renders; long and empty content do not break layout.
- Unit or component tests pass; types compile; lint passes.
- If a browser tool is available, render each variant; otherwise state that visual states were reasoned from code.

## Deliverables
Component, tests, usage example, notes on props and state ownership.

## References
This skill is self-contained. For interactive patterns such as dialogs, tabs and menus, also load the accessibility-review skill; for tokens and variants, design-system-creation.
