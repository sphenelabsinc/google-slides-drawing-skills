---
name: layout-avoid-overlap
description: Use when you need to place new shapes without overlapping existing elements and keep the canvas legible.
version: 0.1.0
---

# layout-avoid-overlap

This skill focuses on spacing, collision avoidance, and repositioning so new shapes don’t obscure existing content.

## When to use
- Introducing a new node into a crowded diagram and needing to avoid the bounding boxes of nearby objects.
- Planning connectors that must leave enough horizontal/vertical real estate for labels.
- You want to cascade icons or labels without stacking them on top of each other.

## Tips
- After `read_slide`, record every element’s `x`, `y`, `w`, `h` and leave 10–12 pt of breathing room before drawing the next object.
- Use grid snapping (multiples of 10) so related elements align and collisions stand out quickly.
- Drop a temporary helper shape before the final one so you can test collisions without committing.
