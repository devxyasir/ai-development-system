# Motion spec: <animation name>

| Question | Answer |
| --- | --- |
| 1. What is changing? | <element and state change> |
| 2. Why does it need to move? | <spatial relationship / continuity / attention / feedback / progress / brand> |
| 3. What should it communicate? | <one sentence> |
| 4. What moves first, and what follows? | <order and stagger, e.g. panel then items at 30 ms> |
| 5. How does it start and end? | <enter ease-out / exit ease-in / move ease-in-out / linear> |
| 6. Duration and easing | <token names, e.g. dur-base + ease-out> |
| 7. Interruption, cancel, repeat | <reverse from current state / replace / ignore duplicate input> |
| 8. Mobile and low-power behavior | <properties animated, simplifications> |
| 9. Reduced motion | <replacement: fade / instant / none; what feedback stays> |
| 10. Verification | <how and where it will be checked> |

## Implementation choice
<CSS transition / CSS animation / Web Animations API / SVG / canvas / library> because <reason tied to the requirements>.

## Properties animated
<transform, opacity only | other properties and why>

## Acceptance criteria
- [ ] Runs at the stated duration and easing
- [ ] Reverses cleanly when interrupted
- [ ] Reduced-motion variant verified
- [ ] No layout shift or dropped frames in the profiled scenario: <scenario>
