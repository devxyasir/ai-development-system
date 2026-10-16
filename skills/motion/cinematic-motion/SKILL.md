---
name: cinematic-motion
description: "Designs expressive storytelling motion for creative websites, landing pages, portfolios, presentations and interactive experiences: opening sequences, camera-like movement, depth and layering, reveals, scene transitions, pacing, pauses and narrative progression. Use for portfolio, campaign or showcase pages, not for dashboards or ordinary product UI."
metadata:
  category: motion
  version: "0.1.0"
  related: "motion-design, scroll-animation, svg-canvas-3d-animation, animation-performance, reduced-motion-accessibility, animation-planning-and-review"
---

# Cinematic motion

Cinematic motion tells a story over time and space. It borrows from film (pacing, framing, reveals) and accepts longer durations than product UI, because the motion is the content. It still must stay usable, fast to load and accessible.

## When to use
- Creative portfolios, product launches, campaign and showcase pages, interactive stories, presentations.
- Not for: dashboards, forms, admin tools or any task-first interface; use motion-design and ui-animation there. Do not carry cinematic motion into the same product's functional screens.

## Procedure
1. **Define the story in three beats:** setup (who or what, establish tone), development (the feature or idea), payoff (call to action or emotional resolution). Each beat has one visual idea.
2. **Set the pacing:** where the viewer should linger (pauses of 300-800 ms or a held frame), where energy rises, and the total time before the content is usable. A visitor should reach real content or a clear action within a few seconds even if the sequence is richer.
3. **Choose the visual language:** camera moves (slow push-in, parallax pan), depth layers (foreground, midground, background moving at different rates), type reveals (mask, line by line), light and color shifts. Keep to a small vocabulary and repeat it.
4. **Storyboard** the sequence with the animation-planning-and-review skill when it is installed; otherwise use a table with columns time, visual, motion, sound, trigger.
5. **Pick the driver:** time-based intro, scroll-driven sequence, or interaction-triggered scenes. Time-based intros must be skippable; scroll-driven sequences follow scroll-animation rules (no scroll hijacking).
6. **Build in layers,** using the cheapest technique per layer: CSS transform and opacity for most, SVG for line work, canvas or WebGL only for the one or two moments that need them (see svg-canvas-3d-animation).
7. **Add sound only by consent:** muted by default, user-initiated, with a visible control; synchronize cues to motion events, not to guesses about time.
8. **Plan the fallback:** reduced motion gets a restrained version (stills, crossfades, no parallax); low-power and slow networks get lighter assets; the page works without the animation.
9. **Preload and sequence assets** so motion does not stutter on first play; show a designed loading state, not a blank screen.

## Decision rules
| Situation | Do this |
| --- | --- |
| Visitor returns often | Play the opening once per session, then skip |
| Long sequence | Provide a visible skip control and keyboard access to it |
| Heavy 3D asset | Show a poster image, load the scene when idle or on interest |
| Text must be read during motion | Slow or pause motion around it; never move body text while it is being read |
| Several scenes | One transition style between scenes; vary only with a story reason |

## Common mistakes
- Treating restraint as optional: constant movement means nothing stands out.
- Intros that delay the first useful content by many seconds.
- Autoplaying sound.
- Mixing six transition styles.
- Skipping the reduced-motion and slow-device versions.

## Verification
- Watch the whole sequence at normal speed, then with the sound off, then on a throttled device profile or slow network if tools exist.
- Time to first meaningful content and to a clear action is measured and acceptable.
- Skip control works by keyboard; reduced motion shows the restrained version; the page works with scripting disabled for core content.
- Contrast and text readability checked over moving or layered backgrounds.
- State what was only reasoned and not rendered.

## Deliverables
Story beats and storyboard, motion vocabulary, implementation with fallbacks and skip, performance notes.

## References
- [Storytelling structure](references/storytelling-structure.md): beats, pacing patterns, framing and layering ideas.
