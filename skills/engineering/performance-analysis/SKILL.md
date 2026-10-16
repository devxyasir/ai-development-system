---
name: performance-analysis
description: "Investigates and improves performance of back-end code, queries, services and scripts by measuring first: define the metric, capture a baseline, profile, find the bottleneck, change one thing, re-measure and report real numbers. Use when code or an endpoint is slow, memory or CPU is high, a regression appeared, or capacity needs checking. For web page speed use frontend-performance."
metadata:
  category: engineering
  version: "0.1.0"
  related: "database-engineering, frontend-performance, debugging, observability-and-incident-response, architecture-decisions"
---

# Performance analysis

Optimize what you have measured. Intuition about bottlenecks is often wrong, and unmeasured "optimizations" add complexity without benefit.

## When to use
- Slow endpoints, jobs, queries or scripts; high CPU or memory; regressions; capacity questions.
- Not for: browser page speed (frontend-performance) or animation smoothness (animation-performance).

## Procedure
1. **Define the problem as a metric:** latency (percentiles such as p50 and p95), throughput, memory, CPU, cost; the scenario; and the target.
2. **Make it reproducible:** a script or benchmark with realistic data and load; fixed environment; warm-up runs; repeated measurements. Record versions and hardware.
3. **Capture a baseline** with several runs and note variance. If you cannot measure, say so and give analysis as hypotheses, not facts.
4. **Profile to find where time goes:** language profiler (CPU and memory), query plans and slow-query logs, traces across services, system metrics. Rank costs by share of total time.
5. **Form a hypothesis** about the largest cost and the smallest change that would reduce it.
6. **Change one thing,** re-run the same benchmark, compare against the baseline and the variance.
7. **Keep or revert:** keep only changes with a measurable gain that justify their complexity; revert the rest.
8. **Consider the common wins first:** remove N+1 queries and repeated work, add an index, batch I/O, cache results with a clear invalidation rule, stream instead of loading everything, choose a better algorithm or data structure, move slow work off the request path.
9. **Check for regressions** in correctness (tests) and other metrics (memory, error rate).
10. **Report** with before and after numbers, method, environment, and limits.

## Decision rules
| Situation | Do this |
| --- | --- |
| Tail latency matters | Look at p95 or p99, not the average |
| Cache proposed | Define what is cached, the key, expiry or invalidation, and behavior on stampedes |
| Parallelism proposed | Check that the work is independent and the bottleneck is not shared (database, lock) |
| Rewrite in a faster language proposed | Profile first; the bottleneck is usually algorithmic or I/O |
| Premature optimization risk | Skip if the code is not on a measured critical path |

## Common mistakes
- Optimizing without a baseline, or against unrealistic data.
- Reporting averages only, or a single run.
- Inventing benchmark results or numbers from memory.
- Caching without invalidation.
- Several changes at once.

## Verification
- Baseline and after numbers come from the same benchmark and environment; variance noted.
- Tests pass; memory and error rate did not regress.
- Anything not measured is labeled as an estimate or hypothesis.

## Deliverables
Benchmark script or method, profile findings, the change, before and after results, recommendations.

## References
This skill is self-contained. Load database-engineering for query plans and indexing details.
