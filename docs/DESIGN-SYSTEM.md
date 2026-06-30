# Design System — nevyn.tech

Pure vanilla HTML/CSS/JS site (no build step). The design system is implemented via CSS custom properties in `css/style.css`.

## Stack

| Layer | System | License |
|---|---|---|
| Foundation — easing | Open Props v1.7 (inlined) | MIT |
| Foundation — spacing | Open Props v1.7 fluid size scale (inlined) | MIT |
| Foundation — typography | Open Props v1.7 fluid font-size scale + site semantic tokens (inlined) | MIT |
| Accessibility | WAI-ARIA patterns, `.sr-only`, `:focus-visible` | — |

No npm, no build tooling. All design tokens are inlined as CSS custom properties in `:root`.

---

## Layer 1 — Transitions / Easing

Three site-level transition shorthands. All use standard CSS `ease` keyword today; future passes may wire in Open Props `--ease-out-*` curves here.

```css
--transition-fast: 150ms ease;
--transition-base: 250ms ease;
--transition-slow: 400ms ease;
```

---

## Layer 2 — Fluid spacing scale (Open Props `--size-fluid-*`)

Six fluid spacing tokens inlined from Open Props. Prefer these over bare `clamp()` calls in `padding`, `gap`, and `margin`. Values are unchanged from the upstream Open Props spec.

| Token | Value | Typical use |
|---|---|---|
| `--size-fluid-1` | `clamp(.5rem, 1vw, 1rem)` | Fine gaps, icon padding |
| `--size-fluid-2` | `clamp(1rem, 2vw, 1.5rem)` | Inline spacing |
| `--size-fluid-3` | `clamp(1.5rem, 3vw, 2rem)` | Small component padding |
| `--size-fluid-4` | `clamp(2rem, 4vw, 3rem)` | Card padding, section sub-gaps |
| `--size-fluid-5` | `clamp(4rem, 5vw, 5rem)` | Between-section rhythm |
| `--size-fluid-6` | `clamp(5rem, 6vw, 7.5rem)` | Page-level vertical rhythm |

`--section-padding: clamp(2rem, 5vw, 4rem)` is a site-specific token (slightly wider viewport band than `--size-fluid-4`) and intentionally kept as its own literal to preserve the exact rhythm established in the original design.

---

## Layer 3 — Fluid font-size scale (Open Props `--font-size-fluid-*`)

Three fluid font-size tokens from Open Props, covering body → sub-heading → heading ranges.

| Token | Value | Use |
|---|---|---|
| `--font-size-fluid-1` | `clamp(1rem, 4vw, 1.5rem)` | Lead text, large body |
| `--font-size-fluid-2` | `clamp(1.5rem, 6vw, 2.5rem)` | Sub-headings |
| `--font-size-fluid-3` | `clamp(2rem, 9vw, 3.5rem)` | Page headings (Open Props scale) |

---

## Layer 4 — Site display-type tokens (`--text-display-*`)

Four semantic aliases over bespoke `clamp()` values derived from the original design. Named by visual intent so every component references a token rather than duplicating a raw clamp literal.

| Token | Value | Used by |
|---|---|---|
| `--text-display-xl` | `clamp(2.5rem, 6vw, 4.5rem)` | `.hero-title` (desktop) |
| `--text-display-lg` | `clamp(2.5rem, 5vw, 4rem)` | `.contact-title`, about page heading |
| `--text-display-md` | `clamp(2rem, 4vw, 3rem)` | `.section-title` |
| `--text-display-sm` | `clamp(1.75rem, 8vw, 2.5rem)` | `.hero-title` (mobile breakpoint) |

The XL and LG tokens share the same `2.5rem` minimum — the difference is the viewport band (`6vw` vs `5vw`) and the cap (`4.5rem` vs `4rem`), giving the hero slightly more aggressive growth on wide screens.

---

## Accessibility

- `.sr-only` uses the standard 1×1 px clip pattern (WCAG 2.1 compatible).
- All interactive elements receive a visible `:focus-visible` outline.
- `@media (prefers-reduced-motion: reduce)` collapses all animations and transitions to instant.

---

## Extending this system

When adding a new component:

1. **Pick a spacing value** from `--size-fluid-*` before writing a bare `clamp()`.
2. **Pick a font size** from `--font-size-fluid-*` or `--text-display-*`; add a new `--text-display-*` token if the size is unique and reused in more than one place.
3. **Do not import a second design system.** This repo has no build step; React/Vue component kits are out of scope.
4. **Document new tokens** in this file under the appropriate layer.

## Next steps

- Wire `--transition-*` to Open Props `--ease-out-*` easing curves (parallel pass in flight).
- Add radius tokens (`--radius-1` … `--radius-round`) and shadow tokens (`--shadow-*`, `--shadow-glow-*`) to replace remaining raw literals (parallel pass in flight).
- Add inset-glow tokens (`--shadow-inset-blue`, etc.) for the pfp Easter egg effects.
