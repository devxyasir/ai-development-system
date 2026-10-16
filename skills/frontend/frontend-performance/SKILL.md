---
name: frontend-performance
description: "Measures and improves web front-end performance: Core Web Vitals (LCP, INP, CLS), bundle size, code splitting, images, fonts, rendering and hydration cost, caching and long-task reduction, always measured before and after. Use when a page feels slow, scores poorly, bundles are large, or before launching a content-heavy or public page."
metadata:
  category: frontend
  version: "0.1.0"
  related: "animation-performance, frontend-architecture, performance-analysis, typography-selection"
---

# Frontend performance

Performance work follows the measurement loop: define the problem, measure a baseline, change one thing, measure again. Never report numbers you did not measure.

## When to use
- Slow load or interactions, poor Web Vitals, large bundles, layout shift, janky scrolling.
- Pre-launch review of a public page.
- Not for: animation smoothness specifically (animation-performance) or server and database speed (performance-analysis).

## Procedure
1. **Define the target user and page:** device and network class, the key page or interaction, and what "good" means.
2. **Measure a baseline** with lab tools (Lighthouse or the browser Performance panel, with CPU and network throttling) and, if available, field data (real-user monitoring, Chrome UX Report). Record LCP, INP (or Total Blocking Time in the lab), CLS, transfer size, JavaScript size, and long tasks.
3. **Find the biggest cost first** with [the playbook](references/web-vitals-playbook.md): what is the LCP element, what blocks it, what runs on the main thread, what shifts.
4. **Apply the fix for that cause,** one at a time:
   - Slow LCP: optimize the LCP image or text (correct size and format, `fetchpriority="high"`, preload, no lazy-loading it), reduce server response time, remove render-blocking resources.
   - Poor INP: break up long tasks, defer non-critical work, reduce hydration and re-render cost, debounce expensive handlers.
   - CLS: reserve space (width and height or `aspect-ratio`), avoid inserting content above existing content, stabilize font loading.
   - Large bundles: analyze the bundle, remove or replace heavy dependencies, split by route, lazy-load below-the-fold and rarely used features, avoid shipping JavaScript for static content.
5. **Re-measure** in the same conditions; keep the change only if the metric improved and nothing regressed.
6. **Add a guard:** a performance budget or CI check (bundle size limit, Lighthouse threshold) so regressions are noticed.
7. **Report** before and after values, device and throttling profile, and what was not measured.

## Reference thresholds (good, at the 75th percentile of real users)
| Metric | Good |
| --- | --- |
| Largest Contentful Paint | 2.5 s or less |
| Interaction to Next Paint | 200 ms or less |
| Cumulative Layout Shift | 0.1 or less |
Thresholds come from the Core Web Vitals program; confirm current values on web.dev if precision matters.

## Decision rules
| Situation | Do this |
| --- | --- |
| Large third-party script | Load async or defer, or after interaction; consider removing |
| Images | Responsive sizes (`srcset`), modern formats where supported, lazy-load below the fold, explicit dimensions |
| Fonts | Subset, preload only critical, `font-display`, metric-matched fallback |
| Heavy component only on some routes | Dynamic import on that route |
| Re-render storms | Fix state placement before reaching for memoization |

## Common mistakes
- Optimizing without a baseline or on a fast development machine only.
- Lazy-loading the LCP image.
- Adding memoization everywhere instead of fixing the cause.
- Counting a Lighthouse score as the goal rather than user-visible speed.

## Verification
- Before and after metrics recorded under the same throttling.
- No new layout shift, functional regression or accessibility regression (run tests and a quick keyboard pass).
- Budget or CI guard added, or recommended with reason.
- Clearly mark any figure that was estimated rather than measured.

## Deliverables
Findings ranked by impact, changes made, before and after measurements, guard.

## References
- [Web Vitals playbook](references/web-vitals-playbook.md)
