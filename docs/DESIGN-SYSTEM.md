# Design System — nevyn.tech

A pure CSS design system for a static HTML/CSS/JS portfolio site (no npm, no build step).
All tokens are CSS custom properties inlined into `css/style.css`.

---

## Combination

| Layer | System | License |
|---|---|---|
| **Foundations / tokens** | Open Props v1.7 (inlined values) | MIT |
| **Accessibility primitives** | Native HTML + ARIA + `:focus-visible` policy | — |
| **Component / CSS** | Hand-authored semantic classes on top of the token layer | — |

> **React component kits are out of scope.** The site has no build tooling;
> CDN-only or inlined CSS/HTML approaches are used throughout.

---

## Token Layers (all in `css/style.css :root`)

### Layer 0 — Primitive color palette
```
--bg-primary / --bg-secondary / --bg-tertiary / --bg-card
--text-primary / --text-secondary / --text-tertiary
--accent / --accent-hover / --accent-subtle
--accent-purple / --accent-purple-hover / --accent-purple-subtle
--border / --border-light
```
Hand-authored to match the dark, sophisticated palette.

### Layer 1 — Typography tokens
```
--font-display   →  'Instrument Serif', Georgia, serif
--font-mono      →  'IBM Plex Mono', 'SF Mono', monospace
```

### Layer 2 — Spacing tokens
```
--section-padding: clamp(2rem, 5vw, 4rem)   (unique viewport band)
--container-max:   1200px
```

### Layer 3 — Transition tokens
```
--transition-fast:  150ms ease
--transition-base:  250ms ease
--transition-slow:  400ms ease
```

### Layer 4 — Focus Ring Tokens (added this pass)
WCAG 2.1 AA — Success Criterion 2.4.7 Focus Visible.
```
--focus-ring-width:  2px
--focus-ring-offset: 3px
--focus-ring-color:  var(--accent)   /* #3b82f6 blue */
```
Used by every `:focus-visible` rule in the stylesheet. Changing `--accent`
automatically updates every focus ring across the site.

---

## Accessibility Patterns

### Skip-to-content link
`index.html` and `about/index.html` both open with:
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```
`.skip-link` is visually hidden (`top: -100%`) until it receives keyboard focus,
at which point it slides in from the top (WCAG 2.4.1 Bypass Blocks).

### `:focus-visible` policy
A focused section at the **end of `css/style.css`** defines consistent rings
for every interactive element:

| Selector | `border-radius` applied |
|---|---|
| `:focus-visible` (universal baseline) | `2px` |
| `a:focus-visible` | `2px` |
| `.nav-links a:focus-visible`, `.mobile-menu a:focus-visible` | `2px` |
| `.nav-links a.nav-cta:focus-visible` | `4px` (matches button shape) |
| `.nav-toggle:focus-visible` | `4px` |
| `.btn:focus-visible` | `4px` (matches `.btn` border-radius) |
| `.pfp-wrap:focus-visible` | `50%` (circular) |
| `.scroll-nav:focus-visible` | `50%` |
| `.filter-dropdown:focus-visible` | `6px` (matches select shape) |
| `.contact-link:focus-visible` | `6px` |

Using `:focus-visible` (not `:focus`) means mouse users are never shown rings
for pointer interactions, preserving the clean visual aesthetic.

### Mobile menu ARIA
The hamburger toggle and mobile overlay keep ARIA state in sync:
```html
<button class="nav-toggle" aria-label="Toggle menu"
        aria-expanded="false" aria-controls="mobile-menu">
<div class="mobile-menu" id="mobile-menu" aria-hidden="true">
```
JavaScript toggles both `aria-expanded` on the button and `aria-hidden` on the
menu, including when links inside the menu are clicked.

---

## What to do next

- **Fluid spacing tokens** — inline Open Props `--size-fluid-1` through
  `--size-fluid-6` and replace hard-coded margin/padding literals.
- **Fluid font-size tokens** — `--font-size-fluid-1` through `-3` for body copy.
- **Display-type tokens** — semantic aliases for all the raw `clamp()` font-size
  calls (hero title, section title, contact title).
- **Easing tokens** — Open Props `--ease-out-3`, `--ease-elastic-3`, etc. to
  replace the bare `ease` keyword in transition values.
- **Radius + shadow tokens** — `--radius-*` and `--shadow-*` from Open Props to
  replace the hard-coded values scattered through the component CSS.
- **Color tokens — semantic tier** — map primitive colors to intent-named aliases
  (`--color-surface`, `--color-on-surface`, `--color-interactive`, etc.).
