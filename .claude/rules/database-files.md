---
paths:
  - "**/migrations/**"
  - "**/*.sql"
  - "**/schema.*"
---

# When editing migrations or SQL

- Follow [database-migration](../../playbook/workflows/database-migration.md).
- Never edit a migration that may already have been applied. Add a new one.
- Destructive statements (drop, truncate, delete without a narrow condition) need a verified backup and explicit authorization.
