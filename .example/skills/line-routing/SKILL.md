---
name: line-routing
description: Use when you need to route connectors so they avoid overlapping objects, exit cleanly, and align with the visual hierarchy.
version: 0.1.0
---

# line-routing

This skill captures best practices for routing connectors so lines do not cut through shapes, they hug the edges, and arrowheads stay legible.

## When to use
- A diagram has dense nodes and connectors; you need to avoid the line intersecting an unrelated shape.
- Several connectors share the same start or end node and should fan out neatly.
- A return flow needs a curved path that doesn’t bisect the working zone.

## Tips
- Use `startConnection` and `endConnection` alongside `layout-avoid-overlap` so the API automatically anchors connectors to the perimeter of the shape.
- When connectors bend around shapes, tilt the bounding box (`x`, `y`, `w`, `h`) to cover only the gap between objects to prevent overlapping other nodes.
- Curved connectors (`category: "CURVED"`) keep the visual hierarchy clean when multiple flows move in parallel.
