/**
 * Tests for back-to-top button behavior.
 * Run with: node tests/back-to-top.test.js
 */

'use strict';

// Minimal DOM stubs
function makeButton() {
    return {
        classList: (() => {
            const classes = new Set();
            return {
                toggle(name, force) {
                    if (force === true) classes.add(name);
                    else if (force === false) classes.delete(name);
                    else if (classes.has(name)) classes.delete(name);
                    else classes.add(name);
                },
                has: name => classes.has(name),
            };
        })(),
    };
}

// Logic extracted from index.html (no DOM dependency)
function makeUpdateBackToTop(btn, getScrollY) {
    return function updateBackToTop() {
        if (btn) {
            btn.classList.toggle('visible', getScrollY() > 400);
        }
    };
}

let passed = 0;
let failed = 0;

function assert(label, condition) {
    if (condition) {
        console.log(`  PASS  ${label}`);
        passed++;
    } else {
        console.error(`  FAIL  ${label}`);
        failed++;
    }
}

console.log('\nback-to-top button\n');

// Hidden below threshold
{
    const btn = makeButton();
    let scrollY = 0;
    const update = makeUpdateBackToTop(btn, () => scrollY);

    scrollY = 0;
    update();
    assert('not visible at scroll 0', !btn.classList.has('visible'));

    scrollY = 399;
    update();
    assert('not visible at scroll 399', !btn.classList.has('visible'));
}

// Visible at and above threshold
{
    const btn = makeButton();
    let scrollY = 401;
    const update = makeUpdateBackToTop(btn, () => scrollY);

    update();
    assert('visible at scroll 401', btn.classList.has('visible'));

    scrollY = 1000;
    update();
    assert('still visible at scroll 1000', btn.classList.has('visible'));
}

// Exactly at threshold
{
    const btn = makeButton();
    let scrollY = 400;
    const update = makeUpdateBackToTop(btn, () => scrollY);
    update();
    assert('not visible at exactly 400 (> required, not >=)', !btn.classList.has('visible'));
}

// Hides again after scrolling back up
{
    const btn = makeButton();
    let scrollY = 800;
    const update = makeUpdateBackToTop(btn, () => scrollY);

    update();
    assert('visible at 800', btn.classList.has('visible'));

    scrollY = 100;
    update();
    assert('hidden after scrolling back to 100', !btn.classList.has('visible'));
}

// Null-safe: no btn element
{
    let threw = false;
    try {
        const update = makeUpdateBackToTop(null, () => 500);
        update();
    } catch (e) {
        threw = true;
    }
    assert('does not throw when btn is null', !threw);
}

console.log(`\n${passed} passed, ${failed} failed\n`);
if (failed > 0) process.exit(1);
