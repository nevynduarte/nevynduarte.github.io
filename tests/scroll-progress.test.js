/**
 * Regression tests for the scroll progress calculation.
 *
 * Bug: when documentHeight <= windowHeight (no scrollable content), the
 * original formula `scrollTop / (documentHeight - windowHeight)` computed
 * `0 / 0 = NaN`, which then set the CSS custom property to "NaN%" — an
 * invalid value that silently broke the progress indicator.
 *
 * Run with: node tests/scroll-progress.test.js
 */

/**
 * Pure implementation of the fixed scroll-progress calculation, mirroring
 * updateScrollProgress() in index.html.
 */
function calcScrollPercent(scrollTop, documentHeight, windowHeight) {
    const scrollable = documentHeight - windowHeight;
    return scrollable > 0 ? Math.min((scrollTop / scrollable) * 100, 100) : 0;
}

let passed = 0;
let failed = 0;

function assert(name, actual, expected) {
    const ok = Number.isNaN(expected)
        ? Number.isNaN(actual)
        : Math.abs(actual - expected) < 1e-9;

    if (ok) {
        console.log(`  PASS  ${name}`);
        passed++;
    } else {
        console.error(`  FAIL  ${name}`);
        console.error(`        expected: ${expected}`);
        console.error(`        received: ${actual}`);
        failed++;
    }
}

// --- Regression: non-scrollable pages must not produce NaN ---
assert(
    'equal height (no scroll possible) → 0, not NaN',
    calcScrollPercent(0, 800, 800),
    0
);
assert(
    'content shorter than viewport → 0, not NaN',
    calcScrollPercent(0, 600, 900),
    0
);

// --- Normal scrolling behaviour ---
assert(
    'beginning of scrollable page → 0%',
    calcScrollPercent(0, 1000, 500),
    0
);
assert(
    '50% through scrollable page',
    calcScrollPercent(250, 1000, 500),
    50
);
assert(
    'fully scrolled → 100%',
    calcScrollPercent(500, 1000, 500),
    100
);

// --- Clamping ---
assert(
    'overscroll (e.g. bounce) clamps to 100%',
    calcScrollPercent(600, 1000, 500),
    100
);

// --- Ensure result is always a finite number ---
const result = calcScrollPercent(0, 800, 800);
assert(
    'result is always a finite number',
    Number.isFinite(result),
    true
);

// Summary
console.log(`\n${passed} passed, ${failed} failed`);
process.exit(failed > 0 ? 1 : 0);
