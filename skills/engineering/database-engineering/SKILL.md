---
name: database-engineering
description: "Designs and changes databases safely: relational and document schema modeling, keys and constraints, indexes and query tuning with EXPLAIN, transactions and isolation, pagination, connection pooling, migrations with rollback, backups and restore, data retention and data quality. Use when creating or altering a schema, writing migrations, fixing slow queries, choosing a database, or handling large datasets."
metadata:
  category: engineering
  version: "0.1.0"
  related: "backend-api-design, security-review, performance-analysis, architecture-decisions, testing-strategy"
---

# Database engineering

Protect data integrity first, then performance. Schemas encode rules; migrations change live data and need a plan to apply, verify and reverse.

## When to use
- Designing or altering tables or collections, writing migrations, tuning queries, choosing a database, handling large data volumes.
- Not for: API behavior (backend-api-design).

## Procedure: schema design
1. **List entities, relationships and the main queries** (reads and writes, with frequency). The access patterns decide the model.
2. **Choose the database** by data shape, consistency needs, query patterns, scale and operational burden; prefer what the project and team already run. A relational database is the default for structured data with relationships and transactions; document stores fit self-contained, hierarchical records with simple access paths. Do not adopt a new database because it is popular.
3. **Model relational data** to a sound normal form (usually third) and denormalize deliberately with a measured reason. Every table has a primary key; relationships have foreign keys; enforce rules with `NOT NULL`, `UNIQUE`, `CHECK` and foreign key constraints, not only application code.
4. **Pick types carefully:** timestamps with time zone stored in UTC; money as exact decimals or integer minor units; identifiers as UUIDs or bigints by need; text lengths and enums intentional.
5. **Plan indexes from queries:** index columns used in `WHERE`, `JOIN`, `ORDER BY`; composite index column order follows equality conditions first, then range, then sort; do not index everything (writes and storage cost).
6. **Plan retention, deletion and privacy:** what is deleted when, soft versus hard delete, personal data handling, audit needs.

## Procedure: migrations
1. **Write migrations as versioned files** in the project's migration tool; never edit a migration that has been applied elsewhere; prefer additive changes.
2. **Use expand and contract** for risky changes: add the new column or table (nullable or with default), deploy code that writes both, backfill in batches, switch reads, then remove the old structure in a later release.
3. **Avoid long locks:** check how your database locks for each statement; use online or concurrent index creation where supported; batch backfills; set statement and lock timeouts.
4. **Write the rollback or forward-fix plan** before applying; destructive steps (drop, truncate) require a verified backup and explicit authorization.
5. **Test the migration** on a copy with realistic data volume, applying and (where reversible) reverting, and run the application tests against the migrated schema.
6. **Apply with checks:** record row counts and constraint results before and after.

## Procedure: query performance
1. **Find the slow query** with the slow-query log, monitoring or an application trace. Capture the real query and parameters.
2. **Read the plan** with `EXPLAIN` (and `EXPLAIN ANALYZE` on a safe copy; it executes the query). Look for full scans on large tables, wrong join order, sorts spilling to disk, row estimate errors.
3. **Fix the cause:** add or correct an index, rewrite the query (avoid functions on indexed columns, select only needed columns, remove N+1 patterns by batching), update statistics, fix the pagination approach.
4. **Measure again** with the same data; report actual timings, not predictions.

## Decision rules
| Situation | Do this |
| --- | --- |
| Large table pagination | Keyset (seek) pagination, not deep `OFFSET` |
| Many small queries in a loop | Batch with `IN`, joins or a data loader |
| Concurrent updates to the same row | Constraints and optimistic locking or `SELECT ... FOR UPDATE` in a short transaction |
| Need to change a column type on a big table | Expand and contract with backfill, not an in-place alter at peak time |
| Connection exhaustion | Pool connections, size the pool to the database's capacity, close on error paths |
| Analytics on a transactional database | Read replica or separate store; avoid heavy queries on the primary |

## Common mistakes
- Missing constraints (duplicates, orphans appear later).
- Running destructive migrations without a tested backup and restore.
- Indexes added by guess and never verified with the plan.
- Storing money in floating point.
- Long transactions holding locks across network calls.

## Verification
- Migration applied and tested on a copy; application tests pass against the new schema; rollback or forward-fix plan documented.
- Constraints enforce the stated rules (try inserting invalid data).
- For performance work: before and after plans and timings recorded.
- Backup exists and a restore has been tested for production-impacting changes; state if it was not.

## Deliverables
Schema or migration files, index rationale, rollback plan, performance evidence, notes on data retention.

## References
- [Migrations and indexing reference](references/migrations-and-indexing.md)
