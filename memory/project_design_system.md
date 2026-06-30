---
name: project-design-system
description: Design system state — what layers exist, what's been adopted, what's next
metadata:
  type: project
---

## Current State (as of 2026-06-30)

Three-layer design token architecture is in place:

**Layer 1 — Open Props (MIT, CDN)**  
Loaded via `https://unpkg.com/open-props/open-props.min.css` in both `index.html` and `about/index.html`.  
Used primitives: `--radius-1`, `--radius-round`, `--ease-3`, `--ease-4`.

**Layer 2 — Semantic tokens in `css/style.css :root`**  
- Border-radius: `--radius-sm` (4px), `--radius-md` (8px), `--radius-input` (6px), `--radius-btn` (4px), `--radius-lg` (12px), `--radius-line` (Open Props), `--radius-pill` (Open Props)  
- Easing: `--ease-ui` (Open Props ease-3), `--ease-fast` (Open Props ease-4)  
- Transitions: `--transition-fast/base/slow` now use Open Props easing curves  
- Colors and typography remain brand-specific custom tokens (not yet from Open Props)

**Layer 3 — Component styles**  
All inline `border-radius: Npx` replaced with semantic tokens. No raw pixel values remain for radius in component rules.

**Documentation**  
`docs/DESIGN-SYSTEM.md` documents the full architecture including token tables and roadmap.

## Why

Establishes a foundation so future passes can consistently reference named tokens rather than magic numbers. Easing upgrade from CSS `ease` to Open Props decel curves improves perceived responsiveness.

## How to apply

When adding new components, always reference semantic tokens (`--radius-md`, `--transition-base`, etc.) — never hardcode px values for radius or easing. When extending the design system, update `docs/DESIGN-SYSTEM.md`.

## Roadmap

1. Map background colors to Open Props `--gray-*` oklch scale
2. Adopt Bootstrap utility classes for responsive grid sections
3. Add Open Props animation speed tokens to profile easter egg keyframes
