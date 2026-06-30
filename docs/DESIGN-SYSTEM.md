# Design System — nevyn.tech

This file documents the CSS custom-property design-token layers defined in
`css/style.css`. Tokens are pure CSS custom properties — no build step, no
npm dependency, zero runtime cost.

All tokens are inlined from or modelled on
[Open Props v1.7](https://open-props.style) (MIT licence) unless noted.

---

## Token layers

### Layer 0 — Brand colors

Defined at the top of `:root`.

| Token | Value | Usage |
|---|---|---|
| `--bg-primary` | `#0a0a0b` | Page background |
| `--bg-secondary` | `#111113` | Secondary surfaces |
| `--bg-tertiary` | `#18181b` | Tertiary surfaces |
| `--bg-card` | `#1c1c1f` | Card backgrounds |
| `--text-primary` | `#fafafa` | Body text |
| `--text-secondary` | `#d4d4d8` | Secondary text |
| `--text-tertiary` | `#a1a1aa` | Muted / placeholder text |
| `--accent` | `#3b82f6` | Blue accent — interactive elements |
| `--accent-hover` | `#60a5fa` | Blue accent hover state |
| `--accent-subtle` | `rgba(59,130,246,.1)` | Faint blue fill |
| `--accent-purple` | `#a78bfa` | Violet accent — decorative |
| `--accent-purple-hover` | `#c4b5fd` | Violet hover state |
| `--accent-purple-subtle` | `rgba(167,139,250,.1)` | Faint violet fill |
| `--border` | `#27272a` | Default border |
| `--border-light` | `#3f3f46` | Lighter border (hover) |

### Layer 1 — Font stacks

| Token | Value | Usage |
|---|---|---|
| `--font-display` | `'Instrument Serif', Georgia, serif` | Headings and display text |
| `--font-mono` | `'IBM Plex Mono', 'SF Mono', monospace` | Body copy and UI chrome |

### Layer 2 — Layout / spacing

| Token | Value | Usage |
|---|---|---|
| `--section-padding` | `clamp(2rem, 5vw, 4rem)` | Vertical padding on all sections |
| `--container-max` | `1200px` | Max-width of `.section-inner` |

### Layer 3 — Transitions

| Token | Value | Usage |
|---|---|---|
| `--transition-fast` | `150ms ease` | Hover colour changes, button states |
| `--transition-base` | `250ms ease` | Card lift, dropdown open |
| `--transition-slow` | `400ms ease` | Scroll-triggered entry animations |

> **Future:** easing tokens from Open Props (`--ease-out-3` etc.) will
> replace the bare `ease` keyword in a later pass, giving the site a
> coherent deceleration curve.

### Layer 4 — Body-copy font-size scale

Fixed sizes for UI chrome and body copy, following Open Props
`--font-size-*` naming convention. Fluid display sizes (hero title,
section headings, contact heading) are handled separately via
`--text-display-*` tokens added in a later pass.

| Token | rem | px equiv | Primary usage |
|---|---|---|---|
| `--font-size-0` | `0.75rem` | 12 px | Timestamps, stat legend labels, tiny badges |
| `--font-size-1` | `0.8125rem` | 13 px | Nav links, filter dropdown, date chips |
| `--font-size-2` | `0.875rem` | 14 px | Secondary body copy, card descriptions |
| `--font-size-3` | `0.9375rem` | 15 px | Primary body copy (`body` element) |
| `--font-size-4` | `1rem` | 16 px | Standard size (hero description, misc) |
| `--font-size-5` | `1.125rem` | 18 px | Card sub-headings, section sub-labels |
| `--font-size-6` | `1.25rem` | 20 px | Section numbers, nav logo |
| `--font-size-7` | `1.5rem` | 24 px | Card headings (research, blog, education) |

**Intentionally excluded from the scale** (context-specific):

| Value | Where | Reason |
|---|---|---|
| `0.6rem` | Mobile stat label | Extreme small at mobile breakpoint only |
| `0.6875rem` | Project / research / blog tags | Mid-scale; left as literal |
| `0.7rem` | Blog read-time | Unique tiny label |
| `0.8rem` | Blog image caption | Between `--font-size-0` and `--font-size-2` |
| `0.85rem` / `0.85em` | Research/blog body copy | Between `--font-size-1` and `--font-size-2` |
| `0.95rem` | Research/contact descriptions | Between `--font-size-3` and `--font-size-4` |
| `1.2rem` | Experience time range | Between `--font-size-5` and `--font-size-6` |
| `1.75rem` | Mobile stat value | Display range; handled by `--text-display-*` |
| `2rem`+ | Stat values, section numbers | Display range; handled by `--text-display-*` |

---

## Planned future layers

The following token layers are being introduced in separate branches and
will be documented here once merged:

- **Easing tokens** — Open Props `--ease-1` through `--ease-out-3` curves,
  replacing the bare `ease` keyword in `--transition-*`
- **Radius tokens** — `--radius-sm` through `--radius-pill`
- **Fluid spacing scale** — Open Props `--size-fluid-1` through `-6`
- **Fluid font-size scale** — Open Props `--font-size-fluid-1` through `-3`
- **Display-type tokens** — `--text-display-xl/lg/md/sm` for `clamp()`
  heading sizes
- **Focus-ring tokens** — `--focus-ring-width/offset/color` + WCAG
  `:focus-visible` policy
- **Shadow tokens** — elevation (`--shadow-sm/md`) and brand-glow variants
- **Leading / tracking / z-index scales**
- **Color-scale tokens** — named palette with `color-mix()` alpha variants

---

## Accessibility baseline

- `prefers-reduced-motion: reduce` collapses all `animation-duration` and
  `transition-duration` to `0.01ms` via the `*` selector (lines 2059–2068
  of `css/style.css`).
- A targeted earlier block (around line 597) also zeroes transitions on the
  profile image easter-egg components.
- `scroll-behavior: smooth` is set on `html` but not yet overridden under
  `prefers-reduced-motion`. **TODO** — add `scroll-behavior: auto` to the
  reduced-motion block.

## File locations

| File | Role |
|---|---|
| `css/style.css` | All tokens live in `:root`; stylesheet is the single source of truth |
| `index.html` | Main portfolio page |
| `about/index.html` | About page — shares the same `css/style.css` |
| `docs/DESIGN-SYSTEM.md` | This file — design token documentation |
