---
name: game-development
description: "Guides game development: defining the core loop and player experience, choosing an engine, structuring scenes and entities, fixed versus variable time steps, input, physics and collision, animation, audio, UI, AI and pathfinding, save systems, asset pipelines, frame-time and memory budgets, multiplayer basics, testing and playtesting, and packaging. Use when planning or building a game or game feature in any engine or framework."
metadata:
  category: specialist
  version: "0.1.0"
  related: "svg-canvas-3d-animation, testing-strategy, performance-analysis, architecture-decisions, accessibility-review"
---

# Game development

A game is a loop of input, simulation and presentation that must feel good. A technically valid build is not proof that the game is fun, balanced or even playable; test by playing.

## When to use
- Planning a game or feature, choosing an engine, structuring game code, fixing game performance, preparing a build.
- Not for: web page animation (see motion skills) unless the project is a browser game, in which case use both.

## Procedure
1. **Define the core loop and the player fantasy** in a few sentences: what the player does moment to moment, why it feels good, what the goal and failure are. Build a rough prototype of that loop before anything else.
2. **Write a small design document:** pillars (three or fewer), mechanics, controls, progression, scope for the first playable, and what is cut.
3. **Choose the engine or framework** with the [engine guide](references/engine-selection.md): by platform, 2D or 3D, team skills, licensing terms (verify current terms), and ecosystem; custom engines only for a concrete reason.
4. **Structure the code:** separate simulation (rules, state) from presentation (rendering, audio, UI) where practical; use scenes, entities and components or the engine's native structure; centralize input mapping; keep content (data) separate from logic.
5. **Set the time model:** movement and timers scale with delta time; physics and deterministic simulation run on a fixed time step (accumulator loop) with interpolated rendering; avoid frame-count based logic.
6. **Handle input well:** remappable controls, dead zones, input buffering, coyote time or similar forgiveness where the genre needs it, gamepad, keyboard and touch support as required.
7. **Budget performance:** target frame time (16.6 ms at 60 fps); avoid allocations in per-frame code (pool objects), batch draw calls, limit physics bodies and active AI, profile with the engine's profiler ([loop and performance notes](references/game-loop-and-performance.md)).
8. **Design systems with their failure modes in mind:** save files versioned and validated; pathfinding with caching and budgets; procedural generation seeded and validated for solvability; networking with an authoritative server, client prediction and reconciliation if multiplayer.
9. **Add accessibility and localization early:** subtitles, remapping, color-blind safe cues, text scaling, string tables, right-to-left support if needed.
10. **Test:** automated tests for rules and simulation (headless where possible, seeded), smoke tests on each target platform, performance captures, and playtests with observers who are not the author.
11. **Package and verify the build** on real target hardware; check install, first launch, save and load, and settings persistence.

## Decision rules
| Situation | Do this |
| --- | --- |
| Physics behaves differently at different frame rates | Move to a fixed time step |
| Hitches every few seconds | Look for garbage-collection allocations or asset loading on the main thread; pool and preload |
| Multiplayer requested | Decide authority and latency model first; start with simple state replication |
| Scope growing | Cut to the core loop; cut features, not polish of the loop |
| Need determinism (replays, lockstep) | Fixed step, seeded RNG, ordered updates, no unordered iteration affecting state; test with replay hashes |

## Common mistakes
- Building systems before the core loop is fun.
- Frame-dependent movement and timers.
- Coupling game rules to rendering so they cannot be tested.
- Skipping real-device testing and playtests.
- Claiming balance or fun from reading code.

## Verification
- The game or feature was actually run (state platform, build type); controls, save and load, and the core loop exercised.
- Automated simulation tests pass; performance measured against the frame budget on target hardware, or stated as not measured.
- Playtest notes recorded, or explicit statement that no playtest occurred.

## Deliverables
Design document, implementation, tests, performance notes, build instructions, playtest findings.

## References
- [Engine selection](references/engine-selection.md)
- [Game loop and performance](references/game-loop-and-performance.md)
