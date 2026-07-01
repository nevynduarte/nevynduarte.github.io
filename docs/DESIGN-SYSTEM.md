# Design System — nevyn.tech

Pure-CSS token layer built on Open Props v1.7 conventions. No build step; all tokens are inline
CSS custom properties in `css/style.css (:root)`. Extend, never replace.

---

## Stack

| Role | Choice | License |
|---|---|---|
| Design token foundations | **Open Props v1.7** conventions (inlined) | MIT |
| CSS framework | Vanilla CSS (no framework) | — |
| Behavior / accessibility | Native HTML + vanilla JS | — |

React / Vue component kits are out of scope — the site is plain HTML/CSS/JS deployed on GitHub Pages.

---

## Token layers

Tokens are defined in `:root` in `css/style.css`. The layers below are cumulative; later passes add
layers without changing earlier ones.

### Layer 1 — Transition shorthands

```css
--transition-fast: 150ms ease;
--transition-base: 250ms ease;
--transition-slow: 400ms ease;
```

Used everywhere with `transition: <property> var(--transition-fast)`.

---

### Layer 7 — Border-radius scale

Seven named steps cover every rounding use-case on the site.

| Token | Value | Used for |
|---|---|---|
| `--radius-xs` | `2px` | Progress-bar indicators, underline accents |
| `--radius-sm` | `4px` | Buttons, nav CTA, small chips |
| `--radius-md` | `6px` | Dropdown items, medium cards |
| `--radius-lg` | `8px` | Cards, panels, modals |
| `--radius-xl` | `12px` | Large feature cards |
| `--radius-circle` | `50%` | Avatar / circular images |
| `--radius-pill` | `999px` | Pill tags, scroll-nav badge |

**Migration:** 27 raw `border-radius` literals replaced (4px × 7, 8px × 8, 50% × 9, 999px × 3, plus single occurrences of 2px, 6px, 12px).

---

### Layer 8 — Z-index stacking scale

Named semantic levels prevent arbitrary stacking magic-numbers.

| Token | Value | Layer |
|---|---|---|
| `--z-ground` | `0` | `.grid-bg` fixed background |
| `--z-base` | `1` | Base element context |
| `--z-raised` | `2` | Slightly elevated UI (pfp overlays) |
| `--z-elevated` | `5` | `.pfp-overlay` absolute layer |
| `--z-higher` | `10` | `.pfp-hint` hover label |
| `--z-indicator` | `100` | Scroll-down nav badge |
| `--z-mobile-menu` | `999` | Full-screen mobile menu overlay |
| `--z-nav` | `1000` | Sticky top navigation bar |

**Migration:** 12 raw `z-index` literals replaced.

---

## Conventions

- **Token names follow Open Props**: `--font-size-*`, `--size-fluid-*`, `--radius-*`, etc.
- **No raw literals** for any tokenised property. If you add a new `border-radius` value that isn't
  on the scale, add a token first.
- **`!important` is preserved** when the selector requires specificity override (e.g. pfp easter-egg
  layers); only the numeric value is replaced with the token.
- **Keyframe / animated shadows** are intentionally kept as literals because the animation values
  are contextual and not part of the repeatable scale.

---

## Adding tokens (future passes)

Planned layers:

- **Layer 2–3** — Fluid spacing (`--size-fluid-1…6`) and fluid font-size (`--font-size-fluid-1…3`)
  from Open Props
- **Layer 4** — Display-type tokens (`--text-display-xl/lg/md`) for all `clamp()` font-size calls
- **Layer 5** — Focus-ring tokens (`--focus-ring-width/offset/color`) + `.skip-link` accessibility
- **Layer 6** — Shadow / glow tokens (`--shadow-sm/md`, `--shadow-glow-*`)
- **Layer 9** — Easing tokens (`--ease-out-3` etc. from Open Props, replacing bare `ease`)
- **Layer 10** — Color palette + semantic aliases + `color-mix()` alpha variants
- **Layer 11** — Body font-size scale (`--font-size-0…7`)
