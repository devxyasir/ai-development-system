# Migrations and indexing reference

Statements below use PostgreSQL-style syntax as examples. Behavior (especially locking) differs by database and version; check your database's documentation for the exact statement.

## Expand and contract example: rename a column
1. Expand: `ALTER TABLE users ADD COLUMN full_name text;`
2. Deploy code that writes both `name` and `full_name`.
3. Backfill in batches:
```sql
UPDATE users SET full_name = name
WHERE id IN (SELECT id FROM users WHERE full_name IS NULL ORDER BY id LIMIT 1000);
```
Repeat until zero rows are updated; pause between batches under load.
4. Deploy code that reads `full_name`.
5. Contract in a later release: drop `name` after confirming nothing reads it.

## Adding a NOT NULL column safely
- Add as nullable (or with a constant default if your database does this cheaply), backfill, then add the constraint after verifying no nulls. In PostgreSQL, add a `CHECK (col IS NOT NULL) NOT VALID`, validate it separately, then set `NOT NULL`.

## Indexes
- Create without blocking writes where supported (`CREATE INDEX CONCURRENTLY` in PostgreSQL; it cannot run inside a transaction block).
- Composite index order: equality columns first, then range column, then sort column.
- Covering or partial indexes for hot queries on a subset: `CREATE INDEX ... WHERE status = 'open'`.
- Verify use: `EXPLAIN (ANALYZE, BUFFERS) SELECT ...` shows an index scan and lower cost; remove indexes that are never used (check usage statistics) because they slow writes.

## Reading an execution plan
| Observation | Meaning | Action |
| --- | --- | --- |
| Sequential scan on a large table with a selective filter | Missing or unusable index | Add an index matching the filter; avoid wrapping the column in functions |
| Estimated rows far from actual | Stale or insufficient statistics | Update statistics; consider extended statistics |
| Sort with external disk usage | Not enough memory or missing index for order | Index for the sort or add a limit |
| Nested loop over many rows | Join order or missing index on join key | Index the join key |

## Pagination
```sql
-- keyset: stable, fast at any depth
SELECT id, created_at, title FROM posts
WHERE (created_at, id) < ($1, $2)
ORDER BY created_at DESC, id DESC LIMIT 50;
```

## Transactions and isolation
- Keep transactions short; no network calls inside them.
- Know the default isolation level of your database; use stronger levels or explicit locks only for the specific invariants that need them; retry serialization failures.

## Connection pooling
- Pool size is bounded by database capacity across all application instances; more connections is not faster. Set acquisition timeouts and handle pool exhaustion as an error, not a hang.

## Backups and restore
- Automated backups with a retention policy; periodic restore tests to a scratch environment; point-in-time recovery if the data requires it. A backup that has never been restored is unproven.

## Document databases
- Embed data that is read together and bounded in size; reference data that grows without bound or is shared. Define indexes for query paths; validate documents with a schema; plan for schema evolution with version fields.

## Data quality and retention
- Constraints and validation at write time; checks (counts, duplicates, nulls, referential integrity) after migrations and pipelines; documented retention periods and deletion jobs; personal data inventory.

## Pipelines (ETL) basics
- Idempotent loads, incremental processing with watermarks, schema validation at ingestion, quarantine for bad records, row-count and checksum reconciliation, monitoring for lateness and failures.
