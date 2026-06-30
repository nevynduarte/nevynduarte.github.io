# Design System — nevynduarte.github.io

**Stack:** Pure vanilla HTML5/CSS3/JS · GitHub Pages · No build tooling  
**Foundation:** Open Props tokens (inlined as CSS custom properties) + site-specific semantic tokens  
**Files:** `css/style.css` (`:root` token layers) · `index.html` · `about/index.html`

---

## Combination

This site uses a layered token architecture — no React, no npm, no build step. All tokens are plain CSS custom properties inlined into `:root`.

| Layer | What | Source |
|-------|------|--------|
| 0 | Color scale (raw palette) | Tailwind zinc/blue/violet values |
| 1 | Semantic color + alpha variants | `color-mix()` on Layer 0 tokens |
| 2 | Fluid spacing | Open Props v1.7 `--size-fluid-*` |
| 3 | Fluid font-size | Open Props v1.7 `--font-size-fluid-*` |
| 4 | Display-type tokens | Site-specific `--text-display-*` aliases |
| 5 | Easing | Open Props `--ease-3` / `--ease-4` curves |
| 6 | Transitions | `--transition-fast/base/slow` (use Layer 5 easing) |
| 7 | Radius | `--radius-sm` through `--radius-pill` |
| 8 | Shadow + glow | `--shadow-sm/md` + accent glow tokens |
| 9 | Focus ring | `--focus-ring-width/offset/color` + `:focus-visible` |
| 10 | Line-height / leading | `--leading-none` through `--leading-loose` |
| 11 | Letter-spacing / tracking | `--tracking-tight` through `--tracking-display` |
| 12 | Z-index stacking | `--z-ground` through `--z-nav` |

---

## Layer 0 — Color Scale

Raw palette tier. Named after Tailwind's convention for familiarity. Only change these when the brand palette changes.

```css
--color-blue-400:   #60a5fa;   /* accent hover */
--color-blue-500:   #3b82f6;   /* accent */
--color-violet-300: #c4b5fd;   /* accent-purple hover */
--color-violet-400: #a78bfa;   /* accent-purple */
--color-violet-500: #8b5cf6;   /* hero/research/status gradients */
```

Background and text colors use the Tailwind zinc scale (hardcoded in `:root` color section):

| Token | Value | Usage |
|-------|-------|-------|
| `--bg-primary` | `#0a0a0b` | page background |
| `--bg-secondary` | `#111113` | alternate sections |
| `--bg-tertiary` | `#18181b` | inputs, sub-panels |
| `--bg-card` | `#1c1c1f` | card backgrounds |
| `--text-primary` | `#fafafa` | headings, body |
| `--text-secondary` | `#d4d4d8` | supporting text |
| `--text-tertiary` | `#a1a1aa` | labels, metadata |
| `--border` | `#27272a` | card borders |
| `--border-light` | `#3f3f46` | hover / focus borders |

---

## Layer 1 — Semantic Colors + Alpha Variants

Semantic tokens alias the scale. Alpha variants use `color-mix()` so all glow/border/gradient opacities are automatically derived from the live token — rebranding requires changing only Layer 0.

`color-mix()` browser support: Chrome 111+, Firefox 113+, Safari 16.2+.

### Blue accent

```css
--accent:        var(--color-blue-500);
--accent-hover:  var(--color-blue-400);
--accent-subtle: var(--accent-a10);        /* 10% opacity */

--accent-a03  …  --accent-a50              /* 3%–50% opacity steps */
```

### Purple accent

```css
--accent-purple:        var(--color-violet-400);
--accent-purple-hover:  var(--color-violet-300);
--accent-purple-subtle: var(--accent-purple-a10);

--accent-purple-a10  …  --accent-purple-a50
```

### Violet-500 accent (hero + easter-egg)

```css
--accent-violet-a12  --accent-violet-a20  --accent-violet-a30
--accent-violet-a40  --accent-violet-a50
```

All derived from `var(--color-violet-500)`. Used for `drop-shadow`, `box-shadow`, and gradient stops in the hero section, profile image effects, and research cover images.

---

## Layers 2–12 (in-flight, not yet on master)

These layers have been authored in separate PRs and document the intended final state of the system.

### Layer 2 — Fluid Spacing (Open Props v1.7)
`--size-fluid-1` through `--size-fluid-6` — viewport-responsive spacing steps.

### Layer 3 — Fluid Font-size (Open Props v1.7)
`--font-size-fluid-1` through `--font-size-fluid-3`.

### Layer 4 — Display-type Tokens
`--text-display-xl/lg/md/sm` — semantic aliases for all raw `clamp()` font-size calls.

### Layer 5 — Easing (Open Props)
`--ease-ui: var(--ease-3)`, `--ease-fast: var(--ease-4)` — deceleration curves.

### Layer 6 — Transitions
`--transition-fast/base/slow` composed from Layer 5 easing tokens.

### Layer 7 — Radius
`--radius-sm/md/lg/line/pill` — consistent border-radius scale.

### Layer 8 — Shadow + Glow
`--shadow-sm/md` (elevation) + `--shadow-glow-accent/purple/violet` (colored glow).

### Layer 9 — Focus Ring
`--focus-ring-width/offset/color` + comprehensive `:focus-visible` rules. Skip-to-content `.skip-link` on both pages.

### Layer 10 — Leading (Line-height)
`--leading-none/tight/normal/body/loose` — named scale, Tailwind convention.

### Layer 11 — Tracking (Letter-spacing)
`--tracking-tight/normal/wide/wider/widest/display`.

### Layer 12 — Z-index
`--z-ground/base/raised/elevated/higher/indicator/mobile-menu/nav`.

---

## Adding a new color

1. Add the raw hex to Layer 0 (e.g. `--color-emerald-500: #10b981`)
2. Alias a semantic token: `--accent-success: var(--color-emerald-500)`
3. Generate alpha variants: `--accent-success-a20: color-mix(in srgb, var(--accent-success) 20%, transparent)`
4. Use the semantic/alpha tokens in component CSS — never the raw hex

## Rebranding accent color

Change `--color-blue-500` (and optionally `--color-blue-400`). All `--accent-a*` tokens, every glow, border, gradient, text-shadow, and box-shadow that references them updates automatically.
