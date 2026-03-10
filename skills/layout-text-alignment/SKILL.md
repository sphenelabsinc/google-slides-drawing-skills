---
name: layout-text-alignment
description: Use when placing labels or annotations beside shapes and ensuring text alignment makes the layout legible.
version: 0.1.0
---

# layout-text-alignment

This skill focuses on keeping labels/annotations aligned, choosing font sizes, and positioning them beside visual elements so they appear clearly tied to the target shape.

## When to use
- Labels should sit to the side of a shape rather than overlapping it.
- You need to set `alignment`/`left_indent` values so the text lines up with connectors or region edges.
- Annotations rely on bullet points and need paragraph spacing.

## Tips
- Place text boxes near the edge of a shape and use `alignment: "START"` for left-aligned explanatory text.
- Pair each text box with a subtle connector or line to show the relationship when the label floats away from the shape.
- Always note the font size (10–12 pt for annotations, 14 pt bold for node labels) so the slides stay readable.
