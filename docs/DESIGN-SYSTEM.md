# Design System

Pure vanilla HTML/CSS/JS portfolio site. No build tooling — all tokens and
components are plain CSS and inline `<script>` blocks.

---

## Layer architecture

```
Layer 1 — FOUNDATION   Open Props v1.7 (MIT)  → via CDN, provides --ease-*, --radius-*, --shadow-* etc.
Layer 2 — TOKENS       css/style.css :root     → semantic aliases + custom brand tokens
Layer 3 — BASE         css/style.css globals   → html, body, h1–h4, a, ul, ::selection
Layer 4 — COMPONENTS   css/style.css sections  → .nav, .hero, .experience-item, .project-card …
```

The CDN link is placed **before** the custom stylesheet in every HTML file so
Open Props variables are defined first. The `:root` block in `style.css` then
either reuses those variables or overrides them with identical local fallbacks —
ensuring the design works even when the CDN is unavailable.

---

## Foundation — Open Props (MIT)

```html
<link rel="stylesheet" href="https://unpkg.com/open-props/open-props.min.css">
```

### Easing curves in use

| Token | Curve | Used for |
|---|---|---|
| `--ease-1` | `cubic-bezier(.25,0,.5,1)` | `--transition-slow` (scroll reveals) |
| `--ease-2` | `cubic-bezier(.25,0,.4,1)` | `--transition-base` (hover states) |
| `--ease-out-2` | `cubic-bezier(0,0,.5,1)` | `<details>` open animation |
| `--ease-out-3` | `cubic-bezier(0,0,.3,1)` | `--transition-fast`, `<details>` close |
| `--ease-elastic-out-1` | `cubic-bezier(.5,.75,.75,1.25)` | (available; not yet used) |

### Border-radius scale

```
--radius-1: 2px   --radius-2: 4px   --radius-3: 8px
--radius-4: 12px  --radius-round: 1e5px
```

### Shadow tokens

Dark-mode shadows use HSL with a near-black hue:

```css
--shadow-color: 220 3% 5%;
--shadow-strength: 1%;

--shadow-2: /* 2-layer lift — used on .experience-item:hover */
--shadow-3: /* 3-layer lift — used on .project-card:hover   */
```

---

## Token layer (`css/style.css :root`)

### Colour palette

| Token | Value | Role |
|---|---|---|
| `--bg-primary` | `#0a0a0b` | Page background |
| `--bg-secondary` | `#111113` | Alternate section background |
| `--bg-card` | `#1c1c1f` | Card surfaces |
| `--text-primary` | `#fafafa` | Headlines, body |
| `--text-secondary` | `#d4d4d8` | Supporting text |
| `--text-tertiary` | `#a1a1aa` | Meta, timestamps |
| `--accent` | `#3b82f6` | Primary interactive / Tailwind blue-500 |
| `--accent-purple` | `#a78bfa` | Secondary accent / Tailwind violet-400 |
| `--border` | `#27272a` | Default border |
| `--border-light` | `#3f3f46` | Hover border |

### Typography

| Token | Value |
|---|---|
| `--font-display` | `'Instrument Serif', Georgia, serif` |
| `--font-mono` | `'IBM Plex Mono', 'SF Mono', monospace` |

### Transition aliases

```css
--transition-fast: 150ms var(--ease-out-3);   /* focus, micro-interactions */
--transition-base: 250ms var(--ease-2);        /* hover states */
--transition-slow: 400ms var(--ease-1);        /* scroll-reveal entrance animations */
```

---

## Component notes

### `<details>` / `<summary>` — Education specialization cards

The collapsible course lists in the Education section are animated via the
**Web Animations API** (`element.animate()`). Key design decisions:

- **Chevron icon** (`▸`) rotates 90° on open via `transform: rotate(90deg)` — no
  `content` change, so the transition is CSS-animatable.
- **Height animation** uses `scrollHeight` measured after `details.open = true` to
  get the exact target height, avoiding the `max-height: 999px` snap-back
  anti-pattern.
- **Respects `prefers-reduced-motion`**: the script exits early if the media
  query matches; the native browser toggle is used instead.
- **Graceful degradation**: the script only runs if `Element.prototype.animate`
  exists; older browsers see the default instant toggle behaviour.

```
Open → content.style.overflow='hidden'; content.style.maxHeight='0px';
        details.open=true; animate(0px → scrollHeight px)
Close → animate(scrollHeight px → 0px); onfinish: details.open=false
```

### Cards — hover depth

Experience and project cards gain a perceptible lift on hover using the shadow
token layer:

```css
.experience-item:hover { box-shadow: var(--shadow-2); }
.project-card:hover    { box-shadow: var(--shadow-3); transform: translateY(-4px); }
```

### Accessibility notes

- Focus rings: use the default browser focus ring via `:focus-visible`. The accent
  colour provides sufficient contrast against `--bg-card` surfaces.
- Reduced-motion: all entrance animations and the `<details>` script are gated on
  `prefers-reduced-motion: reduce`.
- No-JS fallback: `.no-js .experience-item` etc. override the `opacity: 0` entrance
  state so content is visible without JavaScript.

---

## Adding a new component

1. Use `var(--radius-*)` for `border-radius` — never magic-number `px`.
2. Use `var(--transition-*)` for `transition` timing — pick the speed tier that
   matches the interaction weight.
3. Add hover depth with `var(--shadow-2)` or `var(--shadow-3)`.
4. Gate any JS animation on `prefers-reduced-motion` and `Element.prototype.animate`.
