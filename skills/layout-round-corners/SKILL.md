---
name: layout-round-corners
description: Use when you need to round corners uniformly or emphasize a specific rounded-corner language.
version: 0.1.0
---

# layout-round-corners

This skill explains how to keep corner radii consistent across shapes or adjust them per object without breaking the diagram’s feel.

## When to use
- You want every shape to share the same rounded radius so the diagram feels soft.
- One object should stand out with a sharper or softer radius without clashing.
- You are switching between rectangles and `FLOW_CHART_ROUNDED_RECTANGLE` shapes.

## Tips
- For a uniform experience, max out the radius on `FLOW_CHART_ROUNDED_RECTANGLE` by using corner radius values (e.g., 0.4–0.5 of the height) for pill shapes.
- Document the radius you use (e.g., `corner_radius: 20`) so any future shape can copy the value in its `shapeProperties`.
- When only one shape gets a different radius, describe the reason in the chat so the human understands the visual cue.
