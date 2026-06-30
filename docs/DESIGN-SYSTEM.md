# Design System — nevynduarte.github.io

Pure vanilla HTML/CSS/JS site on GitHub Pages. No npm, no build tooling.
All design-system value comes from inlined CSS custom properties.

## Combination

| Layer | Source | Approach |
|-------|--------|----------|
| Foundations / tokens | [Open Props v1.7](https://open-props.style/) (MIT) | Values inlined into `:root`; no CDN import needed |
| Behavior / accessibility | ARIA HTML attributes + CSS `:focus-visible` | Native browser primitives; no JS framework required |
| CSS framework | Vanilla CSS with semantic token aliases | Tailored to the dark, mono-serif aesthetic |

---

## Token Layers in `css/style.css`

All tokens live in `:root`. Layers are listed in cascade order (each layer may
reference tokens from earlier layers).

### Layer 1 — Colors

Brand-specific palette; not derived from Open Props.

| Token | Value | Role |
|-------|-------|------|
| `--bg-primary` | `#0a0a0b` | Page background |
| `--bg-secondary` | `#111113` | Alternate section bg |
| `--bg-tertiary` | `#18181b` | Input / select bg |
| `--bg-card` | `#1c1c1f` | Card surfaces |
| `--text-primary` | `#fafafa` | Body copy |
| `--text-secondary` | `#d4d4d8` | Secondary labels |
| `--text-tertiary` | `#a1a1aa` | Muted / caption |
| `--accent` | `#3b82f6` | Blue accent (CTA, focus) |
| `--accent-hover` | `#60a5fa` | Blue hover |
| `--accent-subtle` | `rgba(59,130,246,0.1)` | Tinted bg tint |
| `--accent-purple` | `#a78bfa` | Soft violet accent |
| `--accent-purple-hover` | `#c4b5fd` | Soft violet hover |
| `--accent-purple-subtle` | `rgba(167,139,250,0.1)` | Violet tinted bg tint |
| `--border` | `#27272a` | Default border |
| `--border-light` | `#3f3f46` | Hover border |

### Layer 2 — Typography

| Token | Value | Role |
|-------|-------|------|
| `--font-display` | `'Instrument Serif', Georgia, serif` | Headings, logo |
| `--font-mono` | `'IBM Plex Mono', 'SF Mono', monospace` | Body, code |

### Layer 3 — Layout

| Token | Value | Role |
|-------|-------|------|
| `--section-padding` | `clamp(2rem, 5vw, 4rem)` | Vertical section padding |
| `--container-max` | `1200px` | Max content width |

### Layer 4 — Transitions

| Token | Value | Role |
|-------|-------|------|
| `--transition-fast` | `150ms ease` | Micro-interactions |
| `--transition-base` | `250ms ease` | Standard state changes |
| `--transition-slow` | `400ms ease` | Entrance / exit |

> **Upgrade path (in-flight PRs):** Replace bare `ease` keyword with
> Open Props easing curves (`--ease-3`, `--ease-4`) for more
> perceptually correct deceleration.

### Layer 5 — Shadow Tokens _(this pass)_

Open Props-inspired two-tier shadow system tuned for the dark theme:
**elevation** (neutral dark) and **brand glow** (accent-tinted).

#### Elevation

| Token | Value | Used on |
|-------|-------|---------|
| `--shadow-sm` | `0 2px 8px rgba(0,0,0,0.20)` | Filter select, input cards at rest |
| `--shadow-md` | `0 4px 20px rgba(0,0,0,0.30)` | Floating UI (scroll indicator, tooltips) |

#### Accent glow — blue (`#3b82f6`)

| Token | Value | Used on |
|-------|-------|---------|
| `--shadow-glow-accent` | `0 4px 12px rgba(59,130,246,0.15)` | Hover state on selects |
| `--shadow-glow-accent-strong` | `0 4px 12px rgba(59,130,246,0.20)` | Focus compound (with ring) |
| `--shadow-glow-accent-bar` | `0 0 10px rgba(59,130,246,0.50)` | Scroll-progress bar fill |

#### Purple glow — deep violet (`#8b5cf6`)

| Token | Value | Used on |
|-------|-------|---------|
| `--shadow-glow-purple` | `0 0 20px rgba(139,92,246,0.30)` | Research cover images (rest) |
| `--shadow-glow-purple-strong` | `0 0 30px rgba(139,92,246,0.50)` | Research cover images (hover) |

#### Violet glow — soft violet (`#a78bfa` = `--accent-purple`)

| Token | Value | Used on |
|-------|-------|---------|
| `--shadow-glow-violet` | `0 0 20px rgba(167,139,250,0.30)` | Blog card images (rest) |
| `--shadow-glow-violet-strong` | `0 0 30px rgba(167,139,250,0.50)` | Blog card images (hover) |

**Intentionally left as literals:** easter-egg `fx-glow` / `pulseGlow`
keyframe animations and the `scrollHighlight` pulse (all are animated
one-off effects that don't benefit from a shared token).

---

## Accessibility

- `:focus-visible` rings on all interactive elements use `--accent` (in-flight PR #33).
- Skip-to-content `.skip-link` on both pages (WCAG 2.4.1 — in-flight PR #33).
- `@media (prefers-reduced-motion: reduce)` collapses all transitions and animations.
- `aria-hidden` / `aria-controls` on the mobile menu toggle (in-flight PR #33).

---

## Extending this system

Next recommended passes (not yet started):
- **Fluid spacing** — inline Open Props `--size-fluid-1` through `--size-fluid-6`; replace
  hardcoded `gap` / `padding` literals.
- **Fluid type scale** — inline `--font-size-fluid-1` through `--font-size-fluid-3`; replace
  hardcoded `font-size` literals in body copy.
- **Easing tokens** — wire `--transition-*` to Open Props `--ease-3` / `--ease-4`.
- **Radius tokens** — `--radius-sm`, `--radius-md`, `--radius-pill` etc.; replace `border-radius`
  literals (partially done in PR #31).
