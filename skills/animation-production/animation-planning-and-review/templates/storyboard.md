# Animation storyboard: <name>

## Goal
<what the viewer should understand or feel> | Motion language: <e.g. quick and quiet / slow and cinematic>

## Beats
| # | Time range | Visual (what is on screen) | Motion (what moves, how far) | Easing / duration token | Trigger | Sound | Reduced-motion version |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0-400 ms | <e.g. headline mask reveal> | <translateY 16px to 0, opacity 0 to 1> | <ease-out / dur-slow> | <page load> | <none> | <fade only> |
| 2 | 400-900 ms | <...> | <...> | <...> | <...> | <...> | <...> |

## Timing review
- Total duration: <ms>; time to usable content: <ms>
- Primary motion per beat: <one per row?>
- Stagger step and cap: <ms, ms>
- Holds or pauses: <where>

## Assets and dependencies
| Asset or library | Why needed | Size / license note |
| --- | --- | --- |
| <file or package> | <reason> | <note> |

## Implementation per beat
| Beat | Technique | Reason |
| --- | --- | --- |
| 1 | <CSS / WAAPI / SVG / canvas / library> | <reason> |

## Acceptance criteria
- [ ] Durations and easings match the table
- [ ] Interruption and repeat handled: <behavior>
- [ ] Reduced-motion version implemented and checked
- [ ] No layout shift; frame budget met on <device or throttling profile>
- [ ] Skip or pause control present (if over 5 s or autoplaying)
