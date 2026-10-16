# Animation quality review rubric

Score each area as Pass, Issue (with severity) or Not checked. Evidence is a recording, screenshot, profile or "reasoned only".

## 1. Purpose
- Each animation has a recorded purpose; nothing moves "just because".
- The primary focal motion is clear at every moment.

## 2. Timing and rhythm
- Durations fit the kind of change (see motion-design table); exits shorter than enters.
- Easing suits direction: ease-out in, ease-in out, ease-in-out between positions, linear for constant change.
- Stagger is capped; total sequence not longer than needed.

## 3. Continuity and spatial logic
- Elements enter and leave from logical directions.
- Shared elements stay identifiable across states.
- No teleporting, flicker or content jumps at the start or end.

## 4. Interaction
- Responds within about 100 ms to input.
- Interrupt, reverse and rapid repeat behave correctly.
- Does not block input or delay actions.
- Focus order and focus visibility unaffected.

## 5. Consistency
- Same tokens for the same kind of change throughout the product.
- Motion language matches the visual direction.

## 6. Performance
- Animates transform and opacity where possible.
- Frame budget met on the target device profile (state the profile).
- No layout shift or leaked loops, listeners, textures after unmount.

## 7. Accessibility
- Reduced-motion version exists and was exercised.
- No flashing over three per second; pause control for long autoplay.
- Nothing essential depends on the animation completing.

## 8. Robustness
- Works with slow networks and missing assets (placeholder, fallback).
- Works with scripting disabled for core content where applicable.
- Behaves across the supported browsers; unsupported features have fallbacks.

## Report format
| Area | Result | Severity | Evidence | Fix |
| --- | --- | --- | --- | --- |
| <area> | <Pass / Issue / Not checked> | <Blocker / Major / Minor> | <link or note> | <change> |
