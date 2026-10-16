# Web Vitals playbook

## Diagnose LCP
1. Identify the LCP element (Performance panel or Lighthouse). It is usually a hero image, a large heading or a poster.
2. Break the time into: server response (TTFB), resource discovery delay, resource load time, render delay.
3. Fix the largest part:
| Largest part | Fix |
| --- | --- |
| TTFB | Cache or statically generate; reduce server work; use a CDN |
| Discovery delay | Put the image in the HTML (not set by JavaScript); preload; `fetchpriority="high"` |
| Load time | Smaller, correctly sized image; modern format; compress |
| Render delay | Remove render-blocking CSS and scripts; inline critical CSS; avoid client-only rendering of the main content |

## Diagnose INP
1. Record the slow interaction in the Performance panel.
2. Look at input delay (main thread busy), processing time (handlers), presentation delay (rendering).
3. Fixes:
- Split long tasks (more than 50 ms) with yielding (`await` a scheduler yield, `setTimeout`, or `requestIdleCallback` for non-critical work).
- Move heavy computation to a Web Worker.
- Reduce component re-renders and DOM size; virtualize long lists.
- Debounce or throttle high-frequency handlers; keep handlers light and defer the rest.

## Diagnose CLS
- Images and embeds: set `width` and `height` or `aspect-ratio`.
- Ads, banners, cookie notices: reserve their space or overlay them without moving content.
- Web fonts: `font-display` plus a metric-matched fallback.
- Late-injected content: insert below the viewport or after user action, or reserve space.
- Animations: use transform, not layout properties.

## Bundle analysis
- Generate a bundle report with your build tool's analyzer.
- Find the top three largest dependencies and ask: is it needed on first load? Is there a smaller alternative or native API?
- Check for duplicate versions of the same package, unused polyfills, and unshaken imports (importing a whole library for one function).
- Split by route and by feature; lazy-load modals, charts, editors and maps.

## Images
- Use `srcset` and `sizes` for responsive images; compress; use modern formats where the audience's browsers support them; lazy-load below the fold with `loading="lazy"`; set dimensions.
- Hero or LCP image: never lazy-loaded; high fetch priority.

## Third parties
- Audit tags, analytics, chat widgets. Load after interaction or idle time; use facades (a static placeholder that loads the real widget on click).

## Caching and delivery
- Long-lived cache headers for hashed assets; revalidation for HTML; compression (Brotli or gzip); HTTP/2 or HTTP/3 via the host or CDN.

## Budgets (example structure, set your own numbers from measurement)
| Resource | Budget | How enforced |
| --- | --- | --- |
| JavaScript per route (compressed) | <set after baseline> | CI bundle check |
| LCP in lab | <set after baseline> | Lighthouse CI |
| CLS | 0.1 | Lighthouse CI |
