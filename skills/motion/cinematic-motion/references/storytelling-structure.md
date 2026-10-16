# Storytelling structure for motion

## Three-beat structure
| Beat | Purpose | Visual idea examples |
| --- | --- | --- |
| Setup | Establish tone and subject | Slow fade from black, a single line of type, a held establishing image |
| Development | Show the idea or features | Parallax pan across layers, sequential reveals tied to scroll, a diagram that builds step by step |
| Payoff | Resolve and prompt action | The full composition settles, a clear call to action, the quietest moment of the page |

## Pacing patterns
- **Hold:** keep a frame still for 300-800 ms after a reveal so it registers.
- **Build and release:** accelerate the rhythm of reveals, then give one still moment.
- **Contrast:** a slow scene after a fast one reads as significant.
- **Silence:** not every moment needs movement; stillness is a tool.

## Camera-like movement
- Push-in: scale a layer slowly (a few percent over seconds) to add attention without distraction.
- Pan: translate layers horizontally at different rates for depth.
- Rack focus: fade or blur background layers while the subject sharpens (blur is expensive; use it on small areas or pre-rendered assets).
- Keep camera moves slow and eased; abrupt motion reads as an error on the web.

## Depth and layering
- Three layers are usually enough: background (slowest), midground, foreground (fastest).
- Differences in speed of 5-30% between layers create depth without nausea; avoid large movements for vestibular safety (see reduced-motion-accessibility).
- Keep text on the most stable layer.

## Typography reveals
- Line-by-line or mask reveals keep text readable; per-letter animation is slow to read and hard on assistive technology (keep the real text in the DOM and avoid splitting it in ways that break reading order; add an `aria-label` if you must split).

## Transitions between scenes
- Match cut: an element persists across scenes while the surroundings change.
- Crossfade: neutral and safe.
- Wipe or mask: gives direction; keep the direction consistent with the story.
- Choose one or two and repeat.

## Sound (optional)
- Off by default; user-initiated; accessible controls; short cues synchronized to visual events; never required to understand content.

## Production checks
1. Total sequence length and time to usable content.
2. Asset weight and loading order.
3. Behavior on a slow device.
4. A version with no motion that still tells the story in layout and type.
