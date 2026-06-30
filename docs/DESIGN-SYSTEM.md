# Design System

This portfolio site uses a three-layer design token architecture that combines
[Open Props](https://open-props.style/) (MIT) as the primitive foundation with
brand-specific semantic tokens consumed by all component styles.

---

## Architecture

```
Layer 1: Primitives  ←  Open Props (open-props.min.css via CDN)
    │
Layer 2: Semantic    ←  :root in css/style.css
    │
Layer 3: Components  ←  Component selectors in css/style.css
```

### Layer 1 — Primitives (Open Props, MIT)

Open Props is loaded via CDN and provides raw design tokens as CSS custom
properties. The site currently uses the following Open Props primitives:

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-1` | `2px` | Source for `--radius-line` |
| `--radius-round` | `1e5px` | Source for `--radius-pill` |
| `--ease-3` | `cubic-bezier(.25, 0, .3, 1)` | Source for `--ease-ui` |
| `--ease-4` | `cubic-bezier(.25, 0, .2, 1)` | Source for `--ease-fast` |

All references include CSS fallback values so the site degrades gracefully
if the CDN is unavailable.

### Layer 2 — Semantic Tokens (`css/style.css :root`)

Semantic tokens give brand meaning to the primitives. Component styles consume
only these tokens — never raw values.

#### Colors (brand-specific — not from Open Props)

| Token | Value | Role |
|-------|-------|------|
| `--bg-primary` | `#0a0a0b` | Page background |
| `--bg-secondary` | `#111113` | Alternate section background |
| `--bg-tertiary` | `#18181b` | Input / inline element background |
| `--bg-card` | `#1c1c1f` | Card surface |
| `--text-primary` | `#fafafa` | Body text |
| `--text-secondary` | `#d4d4d8` | Secondary text |
| `--text-tertiary` | `#a1a1aa` | Muted / caption text |
| `--accent` | `#3b82f6` | Primary accent (blue) |
| `--accent-hover` | `#60a5fa` | Blue hover state |
| `--accent-subtle` | `rgba(59,130,246,0.1)` | Blue tinted fill |
| `--accent-purple` | `#a78bfa` | Secondary accent (purple) |
| `--accent-purple-hover` | `#c4b5fd` | Purple hover state |
| `--accent-purple-subtle` | `rgba(167,139,250,0.1)` | Purple tinted fill |
| `--border` | `#27272a` | Default border |
| `--border-light` | `#3f3f46` | Hover / active border |

#### Typography

| Token | Value |
|-------|-------|
| `--font-display` | `'Instrument Serif', Georgia, serif` |
| `--font-mono` | `'IBM Plex Mono', 'SF Mono', monospace` |

#### Border Radius

| Token | Value | Source | Used on |
|-------|-------|--------|---------|
| `--radius-sm` | `4px` | custom | tags, image corners, small UI |
| `--radius-md` | `8px` | custom | cards, containers |
| `--radius-input` | `6px` | custom | form inputs |
| `--radius-btn` | `4px` | custom | buttons |
| `--radius-lg` | `12px` | custom | large decorative elements |
| `--radius-line` | `var(--radius-1, 2px)` | Open Props | progress bars |
| `--radius-pill` | `var(--radius-round, 1e5px)` | Open Props | badges, status tags |

#### Easing & Transitions

| Token | Value | Source |
|-------|-------|--------|
| `--ease-ui` | `var(--ease-3, cubic-bezier(.25,0,.3,1))` | Open Props |
| `--ease-fast` | `var(--ease-4, cubic-bezier(.25,0,.2,1))` | Open Props |
| `--transition-fast` | `150ms var(--ease-fast)` | semantic |
| `--transition-base` | `250ms var(--ease-ui)` | semantic |
| `--transition-slow` | `400ms var(--ease-ui)` | semantic |

### Layer 3 — Components

All component styles in `css/style.css` reference only Layer 2 semantic tokens.
No raw numeric values for radius, easing, or timing appear in component rules.

---

## Fonts

Both fonts are loaded from Google Fonts with `display=swap`.

- **Display** — `Instrument Serif` (ital variants) — section titles, hero tagline, identity
- **Mono** — `IBM Plex Mono` (400/500/600) — body text, labels, nav links, code-like UI

---

## Roadmap

Future passes should extend the combination further:

1. **Color tokens from Open Props** — map background palette to Open Props `--gray-*`
   oklch scale for perceptually-uniform darks and a consistent dark-mode story.
2. **Bootstrap utility layer** — adopt `col-*` / `d-flex` utilities for responsive
   grid sections rather than custom `display:grid` rules, reducing per-section CSS.
3. **Accessible interactive primitives** — any future dialog, tooltip, or dropdown
   should use Radix UI Primitives or React Aria behaviors once/if a build step is added.
4. **Open Props animation tokens** — replace the profile-picture easter egg's
   hardcoded keyframe timings with `--animation-speed-*` tokens.
