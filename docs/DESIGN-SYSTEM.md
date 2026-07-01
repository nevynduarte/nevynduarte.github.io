# Design System

This site uses a **layered design-token approach** for a pure vanilla HTML/CSS/JS stack (no build tooling).

## Layer stack

```
┌──────────────────────────────────────────────┐
│  3. Component CSS  (css/style.css)            │
│     Hardcoded values are replaced by          │
│     semantic tokens from layer 2.             │
├──────────────────────────────────────────────┤
│  2. Site token layer  (css/style.css :root)   │
│     Semantic aliases:                         │
│       --radius-sm, --radius-md, --radius-pill │
│       --space-1 … --space-7                   │
│       --text-xs … --text-3xl                  │
│       --leading-tight … --leading-relaxed     │
│       --transition-fast/base/slow             │
│     These reference layer 1 primitives where  │
│     Open Props has a matching value, and use  │
│     site-specific values where it does not.   │
├──────────────────────────────────────────────┤
│  1. Foundations  (Open Props — MIT)           │
│     https://unpkg.com/open-props              │
│     Provides the primitive scale:             │
│       --size-1 … --size-15  (spacing)         │
│       --font-size-0 … --font-size-9           │
│       --font-lineheight-1 … -5                │
│       --radius-1 … --radius-round             │
│       --ease-1 … --ease-5                     │
│       --layer-1 … --layer-5  (z-index)        │
│       --shadow-1 … --shadow-6                 │
└──────────────────────────────────────────────┘
```

## How to use tokens

Always use **layer-2 site tokens** in component CSS — never use Open Props primitives directly and never write raw pixel values for things the token system covers.

```css
/* ✓ correct */
.some-card  { border-radius: var(--radius-md); }
.some-badge { border-radius: var(--radius-pill); }
.some-btn   { transition: all var(--transition-fast); }

/* ✗ wrong — leaks primitives into components */
.some-card  { border-radius: var(--radius-3); }

/* ✗ wrong — hardcodes a value the token system owns */
.some-card  { border-radius: 8px; }
```

## Token reference

### Border radius

| Token            | Value                        | Use                     |
|------------------|------------------------------|-------------------------|
| `--radius-xs`    | `var(--radius-1)` = 2px      | Micro-elements          |
| `--radius-sm`    | 4px                          | Buttons, tags, chips    |
| `--radius-md`    | 8px                          | Cards, containers       |
| `--radius-lg`    | `var(--radius-3)` = 1rem     | Large panels            |
| `--radius-pill`  | `var(--radius-round)` ≈ ∞    | Pills, badge, slider    |
| `--radius-circle`| 50%                          | Circular avatars        |

### Transitions

| Token               | Value                    |
|---------------------|--------------------------|
| `--transition-fast` | `150ms var(--ease-3)`    |
| `--transition-base` | `250ms var(--ease-2)`    |
| `--transition-slow` | `400ms var(--ease-1)`    |

The timing functions come from Open Props' curated ease scale; `--ease-3` is a
brisk ease-out well-suited to hover states, while `--ease-1` is a gentle curve
suited to entrance animations.

### Spacing

Maps to Open Props `--size-*`. Use these via the site wrapper tokens when you want
semantic names, or reference `var(--size-N)` directly for ad-hoc values.

| Token      | Open Props ref | Value   |
|------------|---------------|---------|
| `--space-1`| `--size-1`    | 0.25rem |
| `--space-2`| `--size-2`    | 0.5rem  |
| `--space-3`| `--size-3`    | 1rem    |
| `--space-4`| `--size-5`    | 1.5rem  |
| `--space-5`| `--size-7`    | 2rem    |
| `--space-6`| `--size-8`    | 3rem    |
| `--space-7`| `--size-9`    | 4rem    |

### Typography scale

| Token        | Open Props ref    | Value    |
|--------------|-------------------|----------|
| `--text-xs`  | `--font-size-0`   | 0.75rem  |
| `--text-sm`  | —                 | 0.8125rem|
| `--text-base`| `--font-size-1`   | 1rem     |
| `--text-lg`  | `--font-size-3`   | 1.25rem  |
| `--text-xl`  | `--font-size-4`   | 1.5rem   |
| `--text-2xl` | `--font-size-5`   | 2rem     |
| `--text-3xl` | `--font-size-6`   | 2.5rem   |

### Line heights

| Token               | Open Props ref         | Value |
|---------------------|------------------------|-------|
| `--leading-tight`   | `--font-lineheight-1`  | 1.1   |
| `--leading-snug`    | `--font-lineheight-2`  | 1.25  |
| `--leading-normal`  | `--font-lineheight-4`  | 1.5   |
| `--leading-relaxed` | `--font-lineheight-5`  | 1.75  |

## Color tokens

Brand colors are defined directly in `:root` (not derived from Open Props),
since the site uses a custom dark palette that does not match Open Props'
semantic color ramps:

| Token                   | Use                          |
|-------------------------|------------------------------|
| `--bg-primary`          | Page background              |
| `--bg-secondary`        | Alternate section background |
| `--bg-tertiary`         | Subtle tints                 |
| `--bg-card`             | Card surface                 |
| `--text-primary`        | Body copy                    |
| `--text-secondary`      | Supporting text              |
| `--text-tertiary`       | De-emphasised metadata       |
| `--accent`              | Blue interactive accent      |
| `--accent-purple`       | Purple accent                |
| `--border`              | Default divider              |
| `--border-light`        | Elevated divider             |

## Next steps

- Adopt the spacing tokens (`--space-*`) in padding/gap/margin values throughout component CSS
- Adopt the typography tokens (`--text-*`, `--leading-*`) for font-size and line-height
- Add a focus-ring token layer (`--focus-ring`, `--focus-ring-offset`) sourced from Open Props `--shadow-*`
- Evaluate accessible color contrast for all token pairs at AA / AAA levels
