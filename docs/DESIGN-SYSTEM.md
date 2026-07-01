# Design System — nevyn.tech

This site uses a **pure CSS custom-property token stack** built on top of
[Open Props](https://open-props.style/) (MIT) values inlined directly into
`css/style.css`. No build tooling is required — every token is a native CSS
variable, and every layer is additive.

## Architecture

```
Layer 0  Colors            — palette + semantic aliases, alpha variants via color-mix()
Layer 1  Transitions       — --transition-fast / base / slow
Layer 2  Spacing           — --section-padding, --container-max
Layer 3  Font families     — --font-display, --font-mono
Layer 4  Font-weight scale — --weight-* (this layer, see below)
```

Future layers in open PRs (not yet on main):
- Fluid spacing tokens (`--size-fluid-*` from Open Props)
- Fluid font-size tokens (`--font-size-fluid-*`)
- Display-type tokens (`--text-display-*` for hero/section headings)
- Easing tokens (`--ease-*` from Open Props, replacing bare `ease`)
- Border-radius scale (`--radius-xs` through `--radius-pill`)
- Z-index stacking scale (`--z-*`)
- Shadow / glow tokens (`--shadow-*`, `--shadow-glow-*`)
- Leading (line-height) scale (`--leading-*`)
- Tracking (letter-spacing) scale (`--tracking-*`)
- Font-size scale (`--font-size-0` through `--font-size-7`)
- Color tokens + `color-mix()` alpha variants

---

## Layer 0 — Colors

All colors live in `:root` at the top of `css/style.css`.

### Raw palette

| Token | Value | Role |
|---|---|---|
| `--bg-primary` | `#0a0a0b` | Page background |
| `--bg-secondary` | `#111113` | Alternate surface |
| `--bg-tertiary` | `#18181b` | Elevated surface |
| `--bg-card` | `#1c1c1f` | Card background |
| `--text-primary` | `#fafafa` | Body text |
| `--text-secondary` | `#d4d4d8` | Secondary text |
| `--text-tertiary` | `#a1a1aa` | Muted / labels |
| `--accent` | `#3b82f6` | Primary accent (blue) |
| `--accent-hover` | `#60a5fa` | Accent hover state |
| `--accent-subtle` | `rgba(59,130,246,0.1)` | Accent background tint |
| `--accent-purple` | `#a78bfa` | Secondary accent (violet) |
| `--accent-purple-hover` | `#c4b5fd` | Violet hover state |
| `--accent-purple-subtle` | `rgba(167,139,250,0.1)` | Violet background tint |
| `--border` | `#27272a` | Default border |
| `--border-light` | `#3f3f46` | Lighter border |

---

## Layer 1 — Transitions

```css
--transition-fast: 150ms ease;   /* micro-interactions, hover states */
--transition-base: 250ms ease;   /* standard UI state changes */
--transition-slow: 400ms ease;   /* large layout animations */
```

Use `var(--transition-fast)` in `transition:` shorthands everywhere — never
hard-code `150ms ease` or similar magic numbers.

---

## Layer 2 — Spacing

```css
--section-padding: clamp(2rem, 5vw, 4rem);  /* vertical section breathing room */
--container-max:   1200px;                  /* max content width */
```

---

## Layer 3 — Font families

```css
--font-display: 'Instrument Serif', Georgia, serif;  /* headings, hero text */
--font-mono:    'IBM Plex Mono', 'SF Mono', monospace; /* body, labels, code */
```

Both fonts load from Google Fonts CDN in `<head>`.

---

## Layer 4 — Font-weight scale

Six named weights covering the full OpenType range used on this site.
Numeric values are intentional — CSS `font-weight` accepts integers directly.

```css
--weight-light:    300;   /* thin decorative text */
--weight-regular:  400;   /* body copy, heading base weight */
--weight-medium:   500;   /* labels, nav links, sub-headings */
--weight-semibold: 600;   /* (reserved for future use) */
--weight-bold:     700;   /* section callouts, emphasis */
--weight-black:    900;   /* hero super-title, max impact */
```

### Usage guide

| Element | Token |
|---|---|
| `h1`–`h4` (display serif) | `--weight-regular` |
| Nav logo, hero name | `--weight-regular` |
| Nav links, role labels, card headings | `--weight-medium` |
| Hero title | `--weight-bold` |
| Hero title `strong` (brand mark) | `--weight-black` |
| `.pfp-hint__title` | `--weight-bold` |

### Why not Open Props `--font-weight-*`?

Open Props v1 does not ship a `--font-weight-*` scale; its font tokens focus on
size and line-height. This custom 6-step scale follows the same naming convention
and will alias to Open Props tokens if they are added upstream.

---

## Accessibility notes

- All interactive elements must have a visible `:focus-visible` ring. The
  site-wide reset (`outline: none`) is intentional — a full focus-ring section
  at the bottom of `css/style.css` reinstates it with consistent styling.
- Color contrast: `--text-primary` (#fafafa) on `--bg-primary` (#0a0a0b) is
  **21:1** — WCAG AAA.
- `--accent` (#3b82f6) on `--bg-primary` is approximately **3.6:1** — meets WCAG AA
  for large text / UI components.

---

## How to extend

1. Add new tokens to `:root` in `css/style.css`, grouped with a comment header.
2. Replace the raw literal everywhere it appears with `var(--token-name)`.
3. Document the new layer in this file (add a "Layer N" section above).
4. Keep the layers additive — do not remove a token once it is used; deprecate
   by aliasing to the replacement first.
