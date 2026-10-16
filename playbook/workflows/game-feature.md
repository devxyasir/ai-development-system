# Workflow: Building a game feature

Requires: [core principles](../core/00-core-principles.md)

## When to use
Adding or changing gameplay, game systems, rendering, input, UI, saves, networking or builds in a game project.

## Inspect first
- The engine or framework, version and project structure
- The core loop and how the feature fits it
- Existing systems for input, state, saving and scenes
- Target platforms and frame budget
- How to run the game and whether a headless or automated test mode exists

## Load
Load only these. "Always" skills are mandatory; load the others only when their condition is true.

| Skill | When |
| --- | --- |
| [game-development](../../skills/specialist/game-development/SKILL.md) | Always |
| [testing-strategy](../../skills/engineering/testing-strategy/SKILL.md) | Always |
| [architecture-decisions](../../skills/engineering/architecture-decisions/SKILL.md) | The feature introduces a new subsystem or changes how state is structured |
| [performance-analysis](../../skills/engineering/performance-analysis/SKILL.md) | There are frame drops, hitches or a budget to meet |
| [svg-canvas-3d-animation](../../skills/motion/svg-canvas-3d-animation/SKILL.md) | The game runs in a browser with canvas or WebGL rendering |
| [accessibility-review](../../skills/design/accessibility-review/SKILL.md) | The feature adds menus, HUD or a web build |
| [ci-cd-and-deployment](../../skills/delivery/ci-cd-and-deployment/SKILL.md) | Builds, packaging or release pipelines are affected |

## Steps
1. Describe the player-facing behavior and how it supports the core loop; define acceptance criteria.
2. Prototype the behavior in the simplest form that can be played.
3. Separate rules and state from presentation where practical; use delta time or a fixed step as appropriate.
4. Implement with attention to per-frame allocations and the frame budget.
5. Add automated tests for rules and simulation (seeded, headless if possible).
6. Run the game and play the feature; exercise edge cases (pause, restart, save and load, rapid input).
7. Capture a performance profile on target hardware if it matters.
8. Note the playtest results or that none occurred.

## Decisions
| Situation | Do this |
| --- | --- |
| Behavior differs by frame rate | Move to a fixed time step |
| Scope growing | Cut features, not the polish of the core loop |
| Multiplayer involved | Decide authority and latency handling first |

## Artifacts
- Feature implementation
- Simulation tests
- Performance and playtest notes

## Verify
- The feature was actually run and played; platform and build type stated
- Automated tests pass
- Frame time checked on target hardware, or stated as not measured
- Save and load still work

## If verification fails
1. Hitches: look for allocations and loading on the main thread; pool and preload.
2. Rule bug only in play: reproduce with a seeded headless run and add a test.

## Final report
- What the feature does and how it was played
- Tests and measurements
- Not verified (platforms, balance, fun)
- Risks

Use the four-part format from [quality gate and reporting](../core/03-quality-gate-and-reporting.md); run the [final verification checklist](../checklists/final-verification.md) first.

## Related workflows
- [release](release.md): to ship a build
