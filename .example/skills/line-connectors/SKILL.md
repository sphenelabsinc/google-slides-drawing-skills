---
name: line-connectors
description: Use when describing how to connect shapes with straight, bent, or curved lines while respecting connector categories and arrowheads.
version: 0.1.0
---

# line-connectors

`googleSlidesAPI_v1/lines.md` explains the `Page.Line` schema, line categories, arrow styles, and how to use `lineFill`. Use this skill when you need to wire up shapes cleanly and want to understand which connectors can attach where. Connector endpoints use `LineConnection` objects that reference a shape’s `connectionSiteIndex`, and the docs note that most standard shapes (rectangles, rounded rectangles, ellipses, diamonds, flowchart nodes) expose the ECMA-376 connection sites on their perimeters while groups, tables, and other non-graphical elements do not expose connection points at all.

## When to use
- Building a flow that requires precise arrowheads, line weights, or `lineFill` colors.
- You need to understand `LineConnection` payloads so connectors can attach to specific shapes without rerouting manually.
- You want to insert curved or bent lines to represent non-linear flows.

## Tips
- Always create the connector after the two shapes exist so you can reference their `objectId` in `startConnection`/`endConnection`.
- Set `line_weight` to 2–3 for readability and use `line_color` to reinforce the legend’s semantics.
- Favor shapes that expose the default ECMA-376 connection sites (top/middle/bottom/left) such as rectangles, rounded rectangles, ellipses, diamonds, and the `FLOW_CHART_*` primitives so wiring stays predictable.
- Use `line-routing` and `layout-avoid-overlap` to avoid messy intersections.
- When testing a new shape type, drop it onto the slide and run `read_slide` to see its `connectionSiteIndex` availability—if the summary lacks indexes, treat it as harder to connect and consider switching to a more connector-friendly primitive.

## Reference
`googleSlidesAPI_v1/lines.md` and `googleSlidesAPI_v1/shapes.md` for start/end anchor behavior.

## Sample script
`skills/line-connectors/draw_connector.py` builds two ellipses and a straight connector with arrowheads to show how line attributes map to a `batch_draw` payload.
