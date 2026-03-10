---
name: layout-consistency
description: Use when you need to lock in a palette, stroke weight, or size system so the diagram feels cohesive.
version: 0.1.0
---

# layout-consistency

This skill helps you define and reuse color, size, and spacing constants so nodes and connectors come from the same visual system.

## When to use
- You need to ensure every pill has the same radius, height, or color fill.
- A new section should mirror the previous one, sharing `outline_width`, font sizes, and spacing.
- You are documenting the legend so future nodes can reuse the existing tokens.

## Tips
- Pick a small palette (two to three colors) and reference it whenever you describe fill colors in `batch_draw` operations.
- Decide the standard height for process nodes, and reuse that height for all nodes in the same row.
- Keep `outline_width` the same across shapes to avoid depth illusions.
