# Principles and timing

## Why the numbers work
- People perceive responses under roughly 100 ms as immediate; feedback motion in that range reads as a direct reaction.
- Longer motion is acceptable only when it explains something (where something went, how two states relate). Past about 400 ms on ordinary UI actions, users start waiting.
- Decelerating (ease-out) entrances feel responsive because most of the movement happens at the start. Accelerating exits feel like things leaving. Symmetric easing (ease-in-out) suits objects that travel between two visible places.
- These are heuristics. Validate with real devices and real users; do not cite them as measured standards.

## Motion purposes (choose one primary)
| Purpose | Example | Signals success when |
| --- | --- | --- |
| Spatial relationship | Menu grows from its button | Users can say where it came from |
| Continuity | List item moves to a new position after sorting | Users do not lose track of the item |
| Attention | New message nudges in | Users notice without being startled |
| Feedback | Button presses in on click | Users know the click registered |
| Progress | Bar fills, skeleton shimmers | Users understand waiting is in progress |
| Brand expression | Logo reveal | Matches the stated visual direction |

## Choreography patterns
- **Parent then children:** container settles first, children stagger in.
- **Shared element:** one element visually travels from state A to B (FLIP or View Transitions).
- **Cross-fade with slight offset:** content swaps in place without losing layout.
- **Reveal with mask:** clipping reveals content to give direction without large travel.
- **Dismiss by direction:** swipe or slide out toward where it came from.

## Motion language by product type
| Product | Character | Typical choices |
| --- | --- | --- |
| Data-dense professional tools | Quiet, instant | 100-180 ms, opacity and small translate, no bounce |
| Consumer apps | Friendly, responsive | 150-300 ms, gentle spring, shared-element transitions |
| Editorial and portfolio | Expressive, paced | Longer reveals, scroll storytelling (see cinematic-motion) |
| Games and playful UI | Energetic | Overshoot, squash and stretch, sound-synchronized |
| Safety-critical (medical, finance) | Calm | Minimal, no surprise movement near critical data |

## Interruption model
- State-driven changes (open/close, expand/collapse, hover): use CSS transitions so reversing mid-way retargets from the current value.
- Scripted sequences (Web Animations API or library timelines): on interruption, read the current state (`getComputedStyle` or `commitStyles()`), cancel, then start the new animation from there.
- Never stack unfinished animations on the same property; cancel or replace them.

## Review questions that catch most problems
1. Could you remove this and lose nothing? Then remove it.
2. Is it faster than the user's patience for this action?
3. Does it use the same tokens as the same kind of change elsewhere?
4. What does the user see if it is cut off at 50%?
