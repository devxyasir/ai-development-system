---
name: frontend-architecture
description: "Decides front-end structure: rendering strategy (static, server, client, streaming, hydration), state placement, routing, data fetching, forms, error boundaries, loading states, folder structure, build tooling and security basics, for new apps and existing codebases. Use when starting a web front end, adding a feature that spans routes and data, or when state, effects or rendering are tangled."
metadata:
  category: frontend
  version: "0.1.0"
  related: "component-engineering, frontend-performance, frontend-testing, backend-api-design, accessibility-review"
---

# Frontend architecture

Choose the smallest structure that meets the requirements, follow the framework the project already uses, and keep state, data and rendering decisions explicit.

## When to use
- Starting a front end, adding a multi-route feature, or untangling state and effects.
- Choosing between static, server and client rendering.
- Not for: component API details (component-engineering) or measuring speed (frontend-performance).

## Procedure
1. **Inspect first:** framework and version, router, state and data libraries, folder conventions, build tool, lint and test setup. Follow them. Do not introduce a second framework or state library.
2. **List requirements that drive structure:** SEO and first-load speed, personalization, offline needs, real-time data, size of the team and app, target devices.
3. **Pick a rendering strategy** with the table below; use what the framework supports and what the content's freshness requires.
4. **Place state** with the [state decision order](references/rendering-and-state.md): URL, server cache, local component, shared client, form. Derive values instead of storing them.
5. **Design data flow:** one place fetches (route loader, server component, query hook); components receive data via props or context. Handle loading, error, empty and stale states at the boundary.
6. **Define routes and error boundaries:** one per route group; unexpected errors show a recoverable message, never a blank page.
7. **Structure folders** by feature (a feature folder holds components, hooks, API calls, tests) with a small shared layer; avoid circular imports between features.
8. **Set build and quality tooling** the project already uses: type checking, lint, formatting, test runner, bundle analysis.
9. **Apply security basics:** no secrets in the client bundle, escape or sanitize untrusted HTML, validate on the server as well as the client, careful token storage (see security-review).
10. **Write down decisions** that are costly to reverse (framework mode, state library, routing approach) in a short decision record.

## Choosing a rendering strategy
| Situation | Prefer |
| --- | --- |
| Content rarely changes, public, SEO matters | Static generation |
| Content per request or per user, SEO matters | Server rendering (with streaming for slow parts) |
| Authenticated app behind login, heavy interactivity | Client rendering, with server-rendered shell if the framework offers it |
| Mostly static page with a few interactive widgets | Islands or partial hydration if supported |
| Content updates periodically | Static with revalidation |
Do not ship client-side JavaScript for content that never changes after load.

## Decision rules
| Situation | Do this |
| --- | --- |
| Value can be computed from props or state | Compute it during render; do not store it |
| State needed by two siblings | Lift to the nearest common parent first; use context or a store only when prop passing becomes painful |
| Data from the server | Use the framework's data layer or a query cache; do not copy it into local state |
| Effect that sets state from props | Replace with derived value or event handler |
| Large app, many teams | Strict feature boundaries and public entry points per feature |
| Small app | Flat structure; resist premature abstraction |

## Common mistakes
- Duplicate state (server data copied into local state and drifting).
- Effects used for data flow that belongs in event handlers or derived values.
- Client rendering everything for SEO-critical pages.
- Global store for state that belongs in the URL or a component.
- No error boundary or loading state at route level.

## Verification
- The app builds and type checks; run existing tests and add tests for new routes or data flows (see frontend-testing).
- Load, error and empty states each exercised manually or in tests.
- View page source or rendered HTML where SEO matters to confirm what is server-rendered; state if it was not checked.
- No secrets in the built bundle (search the output for known key prefixes or variable names).

## Deliverables
Short architecture note (strategy, state placement, data flow, folder layout, risks), implemented structure, tests.

## References
- [Rendering and state reference](references/rendering-and-state.md)
