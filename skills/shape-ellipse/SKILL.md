---
name: shape-ellipse
description: Use when composing circular or ellipse shapes (dots, aggregators, icons) that anchor connectors or call out points.
version: 0.1.0
---

# shape-ellipse

Ellipses and circles (`ELLIPSE`, `CIRCLE`) are great for junctions, aggregator dots, and small accent markers. They should remain proportional so the stroke feels balanced.

## When to use
- You want a tiny anchor point where multiple connectors converge (aggregator dot) or a callout bubble.
- You need a rounded badge for annotations or icons and must keep it perfectly circular.
- A state should stand out as a node while remaining minimal.

## Tips
- Keep `w` = `h` to enforce circularity; if you need a horizontal pill, switch to `FLOW_CHART_ROUNDED_RECTANGLE` instead.
- Pair a thin outline with a lightly saturated fill so dots never dominate the page’s hierarchy.
- Use `layout-round-corners` when you want every shape to share the same corner radius language.

## Reference
`googleSlidesAPI_v1/shapes.md` for `shapeType`, `shapeProperties`, and autofit rules when the ellipse contains text.
