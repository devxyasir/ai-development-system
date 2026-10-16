# Engine selection

Check each engine's current license, pricing, platform support and documentation before committing; terms change.

## Questions that decide
1. Platforms: web, mobile, desktop, consoles?
2. 2D or 3D, and how demanding is the rendering?
3. Team languages and experience.
4. Budget and licensing tolerance.
5. Need for built-in tools (editor, animation, UI, networking)?
6. Scope: prototype, jam game, commercial release?

## Typical fits (verify current status)
| Option | Good fit | Considerations |
| --- | --- | --- |
| Godot | 2D and moderate 3D, indie projects, open-source preference | Scripting in its own language or C#; exports to multiple platforms; consoles need extra work |
| Unity | 2D and 3D, mobile and many platforms, large asset ecosystem | C#; read current licensing and runtime terms; heavier editor |
| Unreal Engine | High-end 3D visuals | C++ and visual scripting; heavy; read current royalty and license terms |
| Phaser or other HTML5 frameworks | 2D browser games, quick sharing | JavaScript or TypeScript; web performance constraints; pair with the web skills |
| Raylib, SDL, MonoGame, LibGDX and similar frameworks | Code-first control, small games, learning | You build tools and structure yourself |
| Custom engine | A specific technical need or a learning goal | Large cost; justify with a requirement the above cannot meet |

## Decision rule
Pick the engine that lets the team ship the first playable fastest on the target platforms. Switching engines mid-project is expensive; prototype the core loop in the candidate before committing.

## 2D versus 3D notes
- 2D: tilemaps, sprite atlases, pixel-perfect scaling, camera smoothing, per-layer parallax.
- 3D: LOD, culling, baked lighting where possible, texture compression, draw-call batching, shader complexity budgets.
