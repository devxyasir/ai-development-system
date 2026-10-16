# Rendering and state reference

## Rendering vocabulary
- **Static generation (SSG):** HTML built ahead of time. Fast, cacheable, cheap. Needs a rebuild or revalidation for updates.
- **Server rendering (SSR):** HTML produced per request. Fresh and SEO-friendly; costs server time per request.
- **Client rendering (CSR):** the browser builds the UI from JavaScript. Good for authenticated apps; slower first paint and weaker SEO without extra work.
- **Streaming:** the server sends HTML in chunks so fast parts appear before slow data resolves.
- **Hydration:** JavaScript attaches behavior to server-rendered HTML. Cost grows with how much of the page is interactive; limit it to the parts that need it.
- **Islands / partial hydration:** only interactive components ship and run JavaScript.
Use the terms and APIs of your actual framework and version; read its official docs for specifics.

## State decision order (stop at the first that fits)
1. **Derive it** from existing props, state or URL.
2. **URL state** (path, search params) for anything shareable or restorable: filters, sort, tab, page, selected item.
3. **Server state** (data owned by the backend) in the framework's data layer or a query cache with keys, staleness and invalidation. Not in a global store.
4. **Local component state** for UI-only concerns: open/closed, hover, draft input.
5. **Shared client state** (context or a small store) for cross-cutting UI state: theme, current user, multi-step wizard progress.
6. **Form state** with a form library or the browser's native form handling; validate on the server too.

## Effects checklist
Use an effect only to synchronize with something outside the component system (subscriptions, timers, imperative libraries, the document title). Do not use it to: compute values, copy props to state, respond to user events, or fetch data when the framework offers a loader or query hook.

## Forms and validation
- Native `form` with `onSubmit`; labels, `name`, `autocomplete`.
- Client validation for fast feedback; server validation as the authority.
- Show errors next to fields and in a summary; preserve input on failure.
- Disable duplicate submits during a request; handle network errors with retry.

## Routing
- Route-level code splitting and data loading; prefetch likely next routes.
- Unknown route: friendly not-found page. Auth-gated route: redirect with a return path.
- Scroll and focus management on navigation (move focus to the new page heading or main region).

## Error and loading states
- Route-level error boundary with a retry action and a way home.
- Skeletons for predictable layout; spinners for short unknown waits; keep layout stable to avoid shift.
- Optimistic updates only for reversible actions with rollback.

## Folder structure sketch (adapt to the framework)
```
src/
  features/<feature>/   components, hooks, api, tests, index (public exports)
  shared/               ui primitives, utils, design tokens
  routes/ or app/       route entries wiring features together
```

## Security notes
- Treat all data from APIs and URLs as untrusted when rendering; avoid raw HTML injection APIs, or sanitize with a maintained library.
- Do not put secrets in environment variables that the build exposes to the browser.
- Store session tokens in HttpOnly cookies when the architecture allows; understand the trade-offs of storing tokens in web storage.
