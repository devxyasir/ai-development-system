---
name: desktop-and-mobile-development
description: "Guides desktop and mobile application development: choosing native, cross-platform or web-wrapper approaches, app lifecycle, offline behavior and sync, permissions, navigation, local storage and credentials, background work and battery, crash reporting, accessibility, packaging, signing, auto-update and store release. Use when building, structuring or releasing desktop or mobile apps."
metadata:
  category: specialist
  version: "0.1.0"
  related: "frontend-architecture, security-review, ci-cd-and-deployment, accessibility-review, architecture-decisions"
---

# Desktop and mobile development

Apps run on devices you do not control: intermittent networks, limited batteries, permission prompts, OS updates, and store review. Design for those realities.

## When to use
- Choosing an app technology; designing lifecycle, offline, permissions and storage; packaging, signing, updating and releasing apps.
- Not for: web-only front ends (frontend-architecture) or server APIs (backend-api-design).

## Procedure
1. **Establish requirements:** platforms and minimum OS versions, offline needs, device features (camera, location, files, notifications), performance expectations, distribution (stores or direct), update policy.
2. **Choose the approach** with the table below; follow the project's existing choice.
3. **Design the lifecycle:** apps can be suspended, killed and restored at any time; save state early and restore it; handle interruptions (calls, low memory, permission changes, network changes).
4. **Design for offline and poor networks:** local source of truth with a sync queue; retry with backoff; conflict resolution rules; clear offline and syncing indicators; cache with expiry.
5. **Handle permissions at the point of use:** explain why before asking, handle denial and "denied permanently" paths, never block core features unnecessarily, request the minimum.
6. **Store data securely:** use the platform's secure storage (keychain, keystore, credential vault) for tokens and secrets; encrypt sensitive local data; do not log sensitive values; clear data on sign-out.
7. **Respect resources:** batch network calls, avoid background wakeups, use platform background APIs correctly, release resources when backgrounded, test on low-end devices.
8. **Build native-feeling navigation and UI:** follow platform conventions, support text scaling, screen readers, dark mode and right-to-left; use appropriate touch target sizes.
9. **Handle failure and diagnostics:** crash reporting (without personal data), structured logs, remote configuration or feature flags for risky features.
10. **Package and release:** reproducible builds in CI; code signing and notarization (desktop) or app signing (mobile) with keys stored securely and backed up; versioning and changelog; auto-update that verifies signatures; staged rollout; store listing and policy checks (read current store guidelines).
11. **Test on real devices and OS versions** you claim to support; include upgrade-from-previous-version tests.

## Choosing an approach
| Situation | Prefer |
| --- | --- |
| Deep platform integration, best performance, one platform | Native |
| Two or more mobile platforms, shared logic, typical UI | A cross-platform framework the team knows |
| Web team, desktop app with web UI | A web-wrapper framework; weigh runtime size and security model (lighter frameworks use the system web view) |
| Simple content app | Progressive web app, if device features allow |

## Decision rules
| Situation | Do this |
| --- | --- |
| Need to store a token | Platform secure storage, never plain files or shared preferences |
| Feature needs a permission | Ask in context; provide a fallback when denied |
| Update mechanism | Signed updates over HTTPS; allow rollback; never download executable code from unverified sources |
| Data sync | Define conflict rules before building (last write wins, merge, ask user) |
| Desktop file access | Use sandboxed access and the user's file picker where available |

## Common mistakes
- Assuming the network is available or the app keeps running in the background.
- Requesting all permissions at launch.
- Storing secrets in plain text; ignoring certificate or signing key backup.
- Testing only on the newest device and OS.

## Verification
- Run on at least the minimum and the latest supported OS (emulator or device), and on a low-end profile if performance matters; state what was not available.
- Test offline start, offline edits and reconnect; permission denial; app kill and restore; upgrade from the previous version.
- Verify the signed artifact installs and the update path works.

## Deliverables
Architecture notes, implementation, test notes by platform, release checklist and signing plan.

## References
This skill is self-contained. Load ci-cd-and-deployment for build pipelines and release checklists, and security-review for storage and update risks.
