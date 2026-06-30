# Design System — nevyn.tech

Pure vanilla HTML/CSS/JS site (no build step). The design system is implemented via CSS custom properties in `css/style.css`.

## Stack

| Layer | System | License |
|---|---|---|
| Foundation — easing | Open Props v1.7 (inlined) | MIT |
| Foundation — radius | Site-specific tokens (Open Props scale) | — |
| Foundation — shadows | Site-specific dark-theme tokens | — |
| Accessibility | WAI-ARIA focus-visible patterns | — |

## Layer 1 — Easing (Open Props)

Eight easing curves inlined from Open Props into `:root`. Use these in `transition` and `animation` properties instead of bare CSS keywords.

| Token | Curve | Use for |
|---|---|---|
| `--ease-1` | `cubic-bezier(.25,0,.5,1)` | General purpose |
| `--ease-2` | `cubic-bezier(.25,0,.4,1)` | Slightly snappier |
| `--ease-3` | `cubic-bezier(.25,0,.3,1)` | Precise controls |
| `--ease-out-1` | `cubic-bezier(0,0,.75,1)` | Exits / slow ease-out |
| `--ease-out-2` | `cubic-bezier(0,0,.5,1)` | Default ease-out (used in `--transition-*`) |
| `--ease-out-3` | `cubic-bezier(0,0,.3,1)` | Crisp scroll animations |
| `--ease-elastic-1` | `cubic-bezier(.5,.75,.75,1.25)` | Subtle spring / bounce |
| `--ease-squish-1` | `cubic-bezier(.5,-.1,.1,1.5)` | Playful press effects |

The site-level transition shorthands use `--ease-out-2`:
```css
--transition-fast: 150ms var(--ease-out-2);
--transition-base: 250ms var(--ease-out-2);
--transition-slow: 400ms var(--ease-out-1);
```

## Layer 2 — Border-radius tokens

Six tokens covering the full range used across components. Prefer these over hardcoded `px` values.

| Token | Value | Example use |
|---|---|---|
| `--radius-1` | `2px` | Progress bar ends |
| `--radius-2` | `4px` | Tags, badges, small chips |
| `--radius-3` | `6px` | Form inputs |
| `--radius-4` | `8px` | Cards, panels |
| `--radius-5` | `12px` | Large logo containers |
| `--radius-round` | `1e5px` | Pills, status tags |

Do **not** replace `border-radius: 50%` — that's always a semantic circle, not a size token.

## Layer 3 — Shadow tokens

Dark-theme elevation + glow shadows. Pure elevation uses `--shadow-*`; accent glow uses `--shadow-glow-*`.

| Token | Value | Use |
|---|---|---|
| `--shadow-1` | `0 1px 2px rgba(0,0,0,.25)` | Subtle lift |
| `--shadow-2` | `0 2px 8px rgba(0,0,0,.2)` | Form elements |
| `--shadow-3` | `0 4px 20px rgba(0,0,0,.3)` | Floating UI (scroll indicator) |
| `--shadow-4` | `0 8px 32px rgba(0,0,0,.4)` | Modals / drawers |
| `--shadow-glow-blue` | `0 0 10px rgba(59,130,246,.5)` | Progress line active state |
| `--shadow-glow-blue-lg` | `0 0 20px rgba(59,130,246,.3)` | Blue accent hover |
| `--shadow-glow-purple` | `0 0 20px rgba(167,139,250,.3)` | Research covers, blog images |
| `--shadow-glow-purple-lg` | `0 0 30px rgba(167,139,250,.5)` | Hover state of purple glows |

Leave keyframe-animation `box-shadow` values (e.g. `scrollHighlight`) as raw literals — CSS variable interpolation in keyframes does not animate smoothly.

## Accessibility

- Global `:focus-visible` outline on all interactive elements.
- `.pfp-wrap:focus-visible` shows the hover hint overlay.
- `.filter-dropdown:focus` uses a compound focus ring `0 0 0 3px var(--accent-subtle)`.
- `.sr-only` uses the 1×1 px clipping pattern (WCAG-compliant).
- `@media (prefers-reduced-motion: reduce)` collapses all animations to instant.

## Next steps

- Add Open Props `--size-*` fluid spacing tokens and replace `clamp()` patterns for `--section-padding` and similar.
- Introduce `--shadow-inset-*` tokens for the pfp glow effects (lines 670, 777, 781 in `css/style.css`).
- Extend token vocabulary if a new component needs a radius or shadow outside the existing scale.
