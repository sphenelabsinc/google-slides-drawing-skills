---
name: shape-pill
description: Use when you need to craft pill-shaped or rounded rectangle shapes, keeping widths, radii, and color consistent for UI nodes.
version: 0.1.0
---

# shape-pill

This skill explains how to pick the right shape types (`ROUND_RECTANGLE`, `FLOW_CHART_ROUNDED_RECTANGLE`, `RECTANGLE`) and size ratios when you want pill-shaped nodes that pair well with bold text or data pills.

## When to use
- Drawing states, concepts, or data pills that should be wider than they are tall.
- You need to match the legend’s palette without shifting type readability (dark fill + light text).
- A new node should have the same radius as the existing process-orientated pills so the panel feels cohesive.

## Tips
- Keep width-to-height ratios in the 3:1 to 4:1 range so the pill doesn’t look too stubby—apply `layout-golden-ratio` if you need extra polish.
- If text wraps, place `text` operations inside the same object and center the alignment; use `shape_text_style` so the label stays legible.
- When reusing the same color, keep the outline subtle (`outline_width` 0.5–1) or omit it to avoid visual noise.

## Reference
`googleSlidesAPI_v1/shapes.md` for `shapeType`, `shapeProperties`, fills, and outlines.

## Sample script
`skills/shape-pill/create_shape.py` shows how to send a `batch_draw` request that creates a `FLOW_CHART_PROCESS` pill with a solid fill and outline.
