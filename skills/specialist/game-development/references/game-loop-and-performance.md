# Game loop and performance

## Fixed time step with interpolation
```text
accumulator += frame_time (clamped, e.g. to 0.25 s)
while accumulator >= STEP:
    previous_state = current_state
    update(STEP)              # physics, rules, AI at a constant rate
    accumulator -= STEP
alpha = accumulator / STEP
render(lerp(previous_state, current_state, alpha))
```
- Use a fixed step (for example 1/60 or 1/120 s) for simulation and a variable rate for rendering.
- Clamp frame time to avoid a spiral of death after a stall.
- Frame-based versus time-based: anything that changes over time uses seconds, not frames.

## Separating simulation from presentation
- Simulation owns state and rules and emits events ("enemy died"); presentation (animation, particles, sound, UI) subscribes. This allows headless tests and replays.

## Input
- Poll or receive events into an input-state layer; map to actions (`jump`, `fire`), not keys; buffer actions for a short window; support rebinding and multiple devices.

## Performance budget
| Item | Guidance |
| --- | --- |
| Frame time | 16.6 ms for 60 fps; 8.3 ms for 120 fps; track worst frames, not only average |
| Allocations | None in per-frame code; pool bullets, particles, enemies |
| Draw calls | Batch with atlases and instancing; measure with the engine's profiler |
| Physics | Limit active bodies; use simple colliders; sleep inactive bodies |
| AI and pathfinding | Time-slice updates; cache paths; limit queries per frame |
| Loading | Preload assets; stream large assets asynchronously; show progress |
| Memory | Compress textures and audio; unload unused assets |

## Common simulation systems
- **Collision:** broad phase (grid or tree) then narrow phase; use layers and masks; continuous detection for fast objects.
- **Animation:** state machines for characters; blend by time; separate gameplay hitboxes from visuals.
- **Camera:** smoothing with delta-time-aware damping; clamp to level bounds; screen shake with reduced-motion option.
- **Audio:** pooled voices, priority limits, mixer buses, volume settings saved.
- **Save systems:** versioned schema, atomic writes (write temp then rename), validation on load, backup of previous save, no executable data.
- **Procedural generation:** seeded RNG, validation of results (reachability, difficulty), reproducible from seed for bug reports.

## Multiplayer basics
- Choose authority: server-authoritative for competitive games; client prediction with server reconciliation for responsiveness; interpolation for remote entities.
- Send inputs or compact state deltas; handle packet loss and reordering; test with simulated latency and loss.
- Cheating, matchmaking, and privacy needs shape the architecture early.

## Testing
- Headless simulation tests with seeded inputs; replay tests comparing state hashes for determinism.
- Soak tests for memory growth; performance captures on target hardware.
- Playtest checklist: can a new player complete the first minutes without help; where do they get stuck; is the difficulty curve fair; are controls comfortable.

## Packaging
- Per-platform build configuration; test the installed build, not only the editor; check permissions, storage paths, window and resolution handling, controller support, and store requirements (read the platform's current submission rules).
