# Design System

nevynduarte.github.io uses a layered, token-based design system built from
inlined [Open Props](https://open-props.style) (MIT) primitives and
site-specific semantic aliases. There is no npm/build tooling — every token is a
plain CSS custom property in `css/style.css`'s `:root` block.

---

## Layer 0 — Brand colors

```
--bg-primary / --bg-secondary / --bg-tertiary / --bg-card
--text-primary / --text-secondary / --text-tertiary
--accent / --accent-hover / --accent-subtle
--accent-purple / --accent-purple-hover / --accent-purple-subtle
--border / --border-light
```

All values are hand-tuned for the dark (#0a0a0b) base. Do not add new raw hex
values — add a semantic token instead.

---

## Layer 1 — Typography

```
--font-display   'Instrument Serif', Georgia, serif
--font-mono      'IBM Plex Mono', 'SF Mono', monospace
```

Fonts are loaded via Google Fonts CDN in each HTML file's `<head>`.

---

## Layer 2 — Layout

```
--section-padding   clamp(2rem, 5vw, 4rem)
--container-max     1200px
```

---

## Layer 3 — Transitions

```
--transition-fast   150ms ease
--transition-base   250ms ease
--transition-slow   400ms ease
```

**In-flight (branches 19/20/31):** These will be upgraded to use Open Props
easing curves (`--ease-out-3`, `--ease-2`) once those branches merge.

---

## Layer 4 — Line-height / leading scale

Named after Tailwind's `leading-*` convention for familiarity.

| Token            | Value | Usage                                   |
|------------------|-------|-----------------------------------------|
| `--leading-none` | `1`   | Stat numerals, tight display figures    |
| `--leading-tight`| `1.2` | Headings (h1–h4), hint overlay text     |
| `--leading-normal`| `1.6`| Content paragraphs, course/activity lists|
| `--leading-body` | `1.7` | Global body text (`<body>`)             |
| `--leading-loose`| `1.8` | Hero description (short, airy copy)     |

---

## Layer 5 — Letter-spacing / tracking scale

Named after Tailwind's `tracking-*` convention.

| Token                 | Value    | Usage                                        |
|-----------------------|----------|----------------------------------------------|
| `--tracking-tight`    | `0.02em` | Nav links, buttons, role text, filter label  |
| `--tracking-normal`   | `0.04em` | Status-tag badges (moderate separation)      |
| `--tracking-wide`     | `0.05em` | Section numbers (`.section-number`)          |
| `--tracking-wider`    | `0.08em` | Tech-stack tags (`.exp-tech`), blog status   |
| `--tracking-widest`   | `0.1em`  | ALL-CAPS labels: stat labels, skill headers, project labels, research headers |
| `--tracking-display`  | `0.2em`  | PFP hint title (maximum spread, 10px)        |

---

## Layer 6 — Z-index stacking scale

Named layers prevent stacking collisions. Always use these tokens — never bare
integers — so the full layer order stays visible in one place.

| Token              | Value  | Element / usage                         |
|--------------------|--------|-----------------------------------------|
| `--z-ground`       | `0`    | `.grid-bg` — fixed grid behind all UI  |
| `--z-base`         | `1`    | Decorative pfp overlay layers (color, glow, scanlines, shimmer) |
| `--z-raised`       | `2`    | Slightly higher pfp layers (grain, vignette) |
| `--z-elevated`     | `5`    | `.pfp-overlay` — easter-egg overlay     |
| `--z-higher`       | `10`   | Scroll-progress caption gradient        |
| `--z-indicator`    | `100`  | Scroll-progress pill (`.scroll-indicator`) |
| `--z-mobile-menu`  | `999`  | Mobile nav drawer (`.mobile-menu`)      |
| `--z-nav`          | `1000` | Top navigation bar (`.nav`)             |

---

## In-flight token layers (not yet on master)

The following layers exist on open branches and will extend this file once merged:

| Layer | Branch(es) | Tokens |
|-------|-----------|--------|
| Easing curves | 19, 20, 31 | `--ease-1` … `--ease-out-3`, `--ease-elastic-out-1` |
| Border radius | 19, 20, 31 | `--radius-sm` / `--radius-md` / `--radius-pill` (or `--radius-1` … `--radius-round`) |
| Shadow / glow | 20, 34 | `--shadow-sm`, `--shadow-md`, `--shadow-glow-*` |
| Focus ring | 33 | `--focus-ring-width`, `--focus-ring-offset`, `--focus-ring-color` |
| Fluid spacing | 21 | `--size-fluid-1` … `--size-fluid-6` |
| Fluid font-size | 21 | `--font-size-fluid-1` … `--font-size-fluid-3` |
| Display type | 21 | `--text-display-xl` … `--text-display-sm` |

---

## Conventions

- **Add a token before adding a literal.** If a new value appears more than once,
  it belongs in `:root`.
- **Token names** follow `--category-scale` (e.g. `--leading-tight`,
  `--tracking-wider`, `--z-nav`).
- **No React, no npm, no build step.** All tokens must work as plain CSS custom
  properties consumed by vanilla CSS rules.
- **Dark theme only.** All color tokens are calibrated for the `#0a0a0b`
  background. A light theme is not planned.
