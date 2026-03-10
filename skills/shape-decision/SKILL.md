---
name: shape-decision
description: Use when you need diamond/decision shapes or other flowchart-specific shapes that carry branching logic.
version: 0.1.0
---

# shape-decision

Pick `FLOW_CHART_DECISION`, `DIAMOND`, or other angular shapes when you need to show splits, approvals, or guard rails. The diamond geometry must stay balanced so branch labels can sit along each connector.

## When to use
- A decision point requires a label on every outbound connector.
- You want a tight diamond with vents on each direction rather than a freeform polygon.
- The node should be visually distinct from your pill-style states but align with the same palette.

## Tips
- Keep the diamond roughly square so connector anchors sit midpoints; adjust `x`/`y` to center it before wiring lines.
- Use `layout-avoid-overlap` to ensure connectors exit cleanly—avoid overloaded connectors across the center.
- Use the `colors` skill to keep the diamond fill gray/white so it remains legible even with multiple labels.

## Reference
`googleSlidesAPI_v1/shapes.md` for `FLOW_CHART_DECISION`, `shapeProperties`, and placeholder inheritance.
