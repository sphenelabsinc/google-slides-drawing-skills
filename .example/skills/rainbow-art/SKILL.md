---
name: rainbow-art
description: Use this skill when composing playful, blocky art—especially the rainbow block cat—that sits beside the calculator output rather than adhering to the process-diagram rules.
version: 0.1.0
---

# rainbow-art

This skill documents how to build the rainbow block cat (and other similar art pieces) that live on the left side of the calculator plot. It prioritizes stacked rectangles, rounded blocks, circles, and short lines rather than flowchart primitives.

## Color legend

When describing the rainbow cat, cite this palette:

| Role | Hex |
|---|---|
| Stripe Red | `#FF5252` |
| Stripe Orange | `#FF9800` |
| Stripe Yellow | `#FFEB3B` |
| Stripe Green | `#76FF03` |
| Stripe Blue | `#448AFF` |
| Stripe Purple | `#7C4DFF` |
| Head Pink | `#FFC1E3` |
| Accent White | `#FFFFFF` |
| Pupil/Mouth | `#212121` |
| Nose | `#EF5350` |

Mention the palette entries you are honoring whenever you describe which part of the cat you are adding—this serves as the legend contract for the art.

## Shape guidelines

- Build the body from horizontal `RECTANGLE` shapes whose widths line up to create the stacked rainbow body.
- Use `ELLIPSE` shapes for eyes, pupils, and nose, and set `outline_color`/`outline_width` only when you need a dark border.
- Add whiskers with `line` operations (category `STRAIGHT`) whose `line_color` matches `#212121`.
- Place the cat so its left edge hugs the slide margin (≤ 40 PT) and it sits left of the plot area, leaving the main drawing math intact.
- Prefix every object ID with `cat_` so later scripts can target the art for cleanup.

## Execution example

Compose a `batch_draw` that combines stripes, the head, ears, eyes, nose, whiskers, tail blocks, and paws—each shape referencing the legend above. When running such a job, delete existing `cat_` objects first so repeated runs stay tidy.
