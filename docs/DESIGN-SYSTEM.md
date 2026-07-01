# Design System — nevynduarte.github.io

Pure vanilla HTML/CSS/JS portfolio. No npm, no build step.
All design system work lands as CSS custom properties in the `:root` block of `css/style.css`.

## Chosen combination

| Layer | System | License | Status |
|---|---|---|---|
| **Foundations / tokens** | Open Props v1.7 (inlined) | MIT | Layer 1 ✅ |
| **CSS framework** | Custom utility tokens over the Open Props foundation | — | ongoing |
| **Behavior / accessibility** | Native HTML semantics + ARIA attributes | — | ongoing |

**Why no React/component kit?** The site is pure static HTML/CSS — no build pipeline exists.
Open Props tokens are inlined directly as CSS custom properties: zero runtime cost, no CDN dependency.

---

## Layer 1 — Easing (Open Props v1.7)

**File:** `css/style.css` — `:root` block, lines 37–71

Inlines the complete Open Props easing token set as CSS custom properties.
Every raw `ease`, `ease-out`, and `ease-in-out` keyword in the stylesheet has been replaced with a specific token.

### Token families

| Family | Tokens | Use case |
|---|---|---|
| `--ease-1` … `--ease-5` | General deceleration (slows into final state) | Default UI interactions |
| `--ease-in-1` … `--ease-in-5` | Acceleration (fast out of start) | Elements exiting the viewport |
| `--ease-out-1` … `--ease-out-5` | Deceleration (fast into final state) | Elements entering / hover effects |
| `--ease-in-out-1` … `--ease-in-out-5` | Symmetric S-curve | Longer transitions, infinite animations |
| `--ease-elastic-out-1` … `--ease-elastic-out-5` | Overshoot and settle | Springy feedback effects |
| `--ease-squish-1` … `--ease-squish-5` | Squish-and-release | Playful interactive elements |
| `--ease-step-1` … `--ease-step-5` | Discrete steps | Progress indicators, stepped reveals |

### Semantic transition aliases

The three site-wide transition shorthands are now wired to specific easing tokens:

```css
--transition-fast: 150ms var(--ease-out-2);   /* hover/focus, tight interactions  */
--transition-base: 250ms var(--ease-out-2);   /* most UI state changes            */
--transition-slow: 400ms var(--ease-in-out-2); /* layout shifts, page-level motion */
```

**Why `--ease-out-2` for fast/base?** Most interactions (hover, focus, tap) feel snappier when
they decelerate into their end state — the element "lands" quickly. `--ease-out-2` (`cubic-bezier(0, 0, .5, 1)`)
is a moderate deceleration that works for both fast and medium durations.

**Why `--ease-in-out-2` for slow?** Longer transitions feel natural with a symmetric curve that
accelerates out of and decelerates into the resting state.

### Non-tokenised exceptions

Two Easter-egg / spring animations keep literal `cubic-bezier` values intentionally:

| Selector | Value | Reason |
|---|---|---|
| `.pfp-overlay.fx-sheen` | `cubic-bezier(0.4, 0, 0.2, 1)` | Material Design 3 standard curve — explicit design intent |
| `.fx-wobble` | `cubic-bezier(0.36, 0.07, 0.19, 0.97)` | Tuned spring — doesn't map to any Open Props family |

---

## Adding more layers

Next passes should extend this foundation rather than introduce a second design system.
Recommended order:

1. **Fluid spacing** — inline `--size-fluid-1` … `--size-fluid-6` from Open Props; replace raw layout gaps and paddings
2. **Fluid font-size** — inline `--font-size-fluid-1` … `--font-size-fluid-3`; replace raw `clamp()` body-copy sizes
3. **Display-type tokens** — semantic aliases (`--text-display-xl` etc.) for all heading `clamp()` calls
4. **Border-radius scale** — `--radius-sm` … `--radius-pill`; replace all raw `border-radius` literals
5. **Z-index scale** — `--z-nav`, `--z-mobile-menu`, `--z-indicator`, etc.
6. **Shadow tokens** — `--shadow-sm/md` plus glow variants for accent colors
7. **Color-scale tokens** — raw named palette → semantic aliases → `color-mix()` alpha variants
8. **Body font-size scale** — `--font-size-0` … `--font-size-7` step scale

**Rule:** once a token layer exists, all new CSS must use the token — never write a raw literal for
a value that already has a token.
