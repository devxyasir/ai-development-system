# Library selection criteria

Check these before adding any animation dependency. Record the decision.

| Criterion | Question |
| --- | --- |
| Need | Can CSS transitions, CSS animations or the Web Animations API meet it? If yes, no library. |
| Existing stack | Does the project already include an animation library or framework transition API? Use it. |
| API fit | Does it work with your framework's lifecycle (mount, unmount, exit animations)? Read the official docs for the installed version; do not rely on memory of the API. |
| Size and loading | Bundle size added, tree-shaking support, lazy-loading possibility. |
| Performance model | Uses compositor properties and the Web Animations API where possible; supports cancellation and interruption. |
| Accessibility | Honors reduced motion or lets you branch on it easily; does not remove focusable elements mid-animation. |
| License and cost | License terms for your use (commercial, redistribution); verify on the official site because terms can change. |
| Maintenance | Recent releases, open issues, compatibility with your framework version. |
| Exit strategy | How hard is it to remove later? Keep usage behind a small wrapper. |

## Typical mapping (verify current status before choosing)
- React declarative animation and layout transitions: a maintained React motion library or framework-native transitions.
- Timelines and scroll scrubbing across frameworks: a timeline library with scroll plugin.
- Designer-authored vector or interactive animation: Lottie or Rive runtimes.
- 3D: three.js and a framework binding.

## Decision record template
Need: <what cannot be done with CSS or WAAPI>
Options considered: <list>
Chosen: <library, version> because <reasons>
Cost: <bundle size, license note>
Removal plan: <wrapper location>
