# Before deployment

Size this to the risk. For small changes to low-risk environments a few lines are enough; for production and risky changes complete all of it. See the deployment workflow.

- [ ] I have explicit authorization for this environment.
- [ ] The artifact was built from the tested commit (commit id: ______).
- [ ] Required configuration and secrets exist in the target environment; no secrets are in the repository or logs.
- [ ] Database migrations are tested on a copy, compatible with both old and new code, and a backup is current (destructive steps need explicit authorization).
- [ ] Health checks exist (liveness and readiness) and I know how to read them.
- [ ] I have a rollback plan and know the exact commands; I know what makes rollback impossible (for example a destructive migration).
- [ ] Monitoring, logs and alerts are available; someone is watching during the rollout.
- [ ] The rollout strategy fits the risk (staged, canary, rolling, blue-green, feature flag).
- [ ] I know which smoke tests prove it works (key user flows).
- [ ] I will capture evidence after deployment (version served, status codes, logs), and will not claim success without it.
- [ ] Costs and resource limits were considered (instances, storage, external API usage).
