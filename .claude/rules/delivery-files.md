---
paths:
  - ".github/workflows/**"
  - "**/Dockerfile*"
  - "**/docker-compose*.{yml,yaml}"
  - "**/*.tf"
---

# When editing pipelines, containers or infrastructure

- Follow [deployment](../../playbook/workflows/deployment.md) for anything that changes what runs in an environment.
- Never put secrets in these files. Use the platform's secret store.
- Do not deploy, publish or apply infrastructure changes without explicit authorization; provide the commands instead.
