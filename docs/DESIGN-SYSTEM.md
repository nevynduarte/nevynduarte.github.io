# Design System

This site uses a layered design-system approach built entirely on **vanilla CSS custom properties** — no framework or build step required. The combination follows the three-layer pattern:

```
Foundation tokens  →  Open Props (easing + radius)
Accessibility      →  WAI-ARIA focus-visible conventions
Component styles   →  hand-crafted CSS referencing the tokens above
```

---

## Layer 1 — Foundation tokens (Open Props, MIT)

Source: <https://open-props.style>

The `css/style.css` `:root` block inlines a curated subset of Open Props v1.7 tokens. Using the Open Props names directly means future maintainers can swap in the full CDN build (`<link rel="stylesheet" href="https://unpkg.com/open-props@1.7.6/open-props.min.css">`) without any renaming.

### Easing tokens

| Token | Value | Used for |
|-------|-------|----------|
| `--ease-1` | `cubic-bezier(.25, 0, .5, 1)` | slow entrance animations (`--transition-slow`) |
| `--ease-2` | `cubic-bezier(.25, 0, .4, 1)` | standard UI interactions (`--transition-base`) |
| `--ease-3` | `cubic-bezier(.25, 0, .3, 1)` | quick interactions |
| `--ease-out-1` | `cubic-bezier(0, 0, .75, 1)` | decelerate out |
| `--ease-out-2` | `cubic-bezier(0, 0, .50, 1)` | moderate decelerate |
| `--ease-out-3` | `cubic-bezier(0, 0, .30, 1)` | snappy hover/focus (`--transition-fast`) |
| `--ease-elastic-out-1` | `cubic-bezier(.5, .75, .75, 1.25)` | available for spring effects |

The semantic transition aliases:

```css
--transition-fast: 150ms var(--ease-out-3);   /* hover, focus ring */
--transition-base: 250ms var(--ease-2);        /* button, link states */
--transition-slow: 400ms var(--ease-1);        /* scroll-reveal fade-in */
```

### Border-radius tokens

| Token | Value | Semantic use |
|-------|-------|--------------|
| `--radius-1` | `2px` | subtle rounding (scroll line, focus `border-radius`) |
| `--radius-2` | `4px` | buttons, tags, images |
| `--radius-3` | `8px` | cards (experience, project, blog, research, edu) |
| `--radius-4` | `12px` | logo placeholders |
| `--radius-5` | `16px` | (available) |
| `--radius-round` | `1e5px` | pill badges, scroll indicator |

---

## Layer 2 — Accessibility primitives

No third-party library is needed for a static site; the accessibility behavior layer is implemented as CSS `:focus-visible` rules that mirror the intent of headless component libraries (Radix UI Primitives, React Aria).

### Focus-visible ring

A single global rule provides a consistent 2 px outline in `--accent` (`#3b82f6`) for every interactive element, activated only by keyboard or programmatic focus (`:focus-visible`), not by pointer clicks:

```css
:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 3px;
    border-radius: var(--radius-1);
}
```

Element-specific overrides handle special shapes:

- **`.pfp-wrap`** — circular photo gets `border-radius: 50%` and `outline-offset: 5px`
- **`.filter-dropdown`** — reduced offset + inner glow supplement
- **`summary.specialization-title`** — tighter offset for inline text
- **`.scroll-nav` buttons** — square radius matches shape

### sr-only pattern

```css
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0;
}
```

This follows the standard Bootstrap/Tailwind convention (1 px clip) rather than `width: 0; height: 0`, which some screen readers handle inconsistently.

---

## Layer 3 — Component styles

All component CSS lives in `css/style.css` and references the tokens above. Key semantic aliases:

| Custom property | Value |
|-----------------|-------|
| `--accent` | `#3b82f6` (blue — CTA, focus, accent labels) |
| `--accent-purple` | `#a78bfa` (purple — role titles, alt section numbers) |
| `--bg-primary` | `#0a0a0b` |
| `--bg-card` | `#1c1c1f` |
| `--font-display` | `Instrument Serif` |
| `--font-mono` | `IBM Plex Mono` |

---

## Extending this system

**To add more Open Props tokens** (colors, shadows, sizes):

```html
<!-- Replace the inlined subset with the full CDN build -->
<link rel="stylesheet" href="https://unpkg.com/open-props@1.7.6/open-props.min.css">
```

Then remove the manually-inlined token block from `:root` in `style.css`.

**To add interactive component behavior** (e.g. a disclosure widget, tabs):

Consider the [Radix UI Primitives](https://www.radix-ui.com/primitives) mental model even in plain HTML — use `details`/`summary` for disclosure, `role="tab"` + `aria-selected` for tabs, and pair with `:focus-visible` CSS already defined here.

**Next design-system steps for future passes:**

- Adopt Open Props `--shadow-*` tokens to replace the inline `box-shadow` values
- Add Open Props `--size-*` spacing tokens to replace the `clamp()` values
- Extract component-specific CSS into separate partials (e.g. `css/nav.css`, `css/cards.css`)
