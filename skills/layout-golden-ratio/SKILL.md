---
name: layout-golden-ratio
description: Use when you need visually appealing proportions—widths, heights, or spacing—based on the golden ratio.
version: 0.1.0
---

# layout-golden-ratio

This skill encourages using the golden ratio (≈1.618) to size and space elements so the canvas feels natural and balanced.

## When to use
- You want a heading or node to dominate the panel without overwhelming the rest of the layout.
- Two adjacent panels should split the slide with a subtle emphasis (one at 61.8% width, the other at 38.2%).
- You are sizing pills or annotations to align with the golden ratio relative to a guiding shape.

## Tips
- When sizing a pill, divide the height by 1.618 to get the width or vice versa; round to prevent fractional points.
- Use `layout-consistency` to keep every pill using the same golden-ratio computation so groups feel related.
- Pair golden-ratio spacing with `layout-avoid-overlap` so proportions do not inadvertently intersect existing shapes.
