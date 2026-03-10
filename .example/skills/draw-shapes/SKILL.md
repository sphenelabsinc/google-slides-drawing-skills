---
name: draw-shapes
description: This skill should be used when the user asks to "draw a shape", "add a rectangle", "draw a diamond", "add a process box", "draw a flowchart", "add a callout", "draw an arrow shape", "add an ellipse", "draw a decision box", "add a terminator", or needs to compose shape operations for a Google Slides batch-draw command.
version: 0.1.0
---

# draw-shapes

Compose shape operations for `batch-draw`.

## Operation Structure

```json
{
  "type": "shape",
  "id": "unique_id",
  "x": 100,
  "y": 80,
  "w": 160,
  "h": 60,
  "shape_type": "RECTANGLE",
  "fill_color": "#4285F4",
  "outline_color": "#1A237E",
  "outline_width": 2
}
```

| Field | Required | Default | Notes |
|---|---|---|---|
| `type` | yes | — | `"shape"` or `"rectangle"` |
| `id` | yes | — | Unique, 5–50 chars `[a-zA-Z0-9_-:]` |
| `x`, `y` | yes | — | Top-left corner in PT |
| `w`, `h` | yes | — | Width/height in PT |
| `shape_type` | no | `RECTANGLE` | See shape catalog |
| `fill_color` | no | transparent | See `colors` skill |
| `outline_color` | no | none | Omit for no border |
| `outline_width` | no | none | Border thickness in PT |

## Essential Shape Types

### General Shapes
`RECTANGLE`, `ROUND_RECTANGLE`, `ELLIPSE`, `DIAMOND`, `PARALLELOGRAM`, `TRAPEZOID`, `TRIANGLE`, `HEXAGON`, `PENTAGON`, `CHEVRON`, `FRAME`, `CLOUD`

### Flowchart Shapes
| Type | Symbol |
|---|---|
| `FLOW_CHART_PROCESS` | Rectangle — process step |
| `FLOW_CHART_TERMINATOR` | Pill — start/end |
| `FLOW_CHART_DECISION` | Diamond — yes/no |
| `FLOW_CHART_DATA` | Parallelogram — input/output |
| `FLOW_CHART_DOCUMENT` | Wavy-bottom rect — document |
| `FLOW_CHART_PREDEFINED_PROCESS` | Striped rect — subroutine |
| `FLOW_CHART_MAGNETIC_DISK` | Cylinder — database |
| `FLOW_CHART_PREPARATION` | Hexagon — initialization |
| `FLOW_CHART_DELAY` | D-shape — delay |
| `FLOW_CHART_CONNECTOR` | Circle — on-page connector |

### Arrow Shapes
`RIGHT_ARROW`, `LEFT_ARROW`, `UP_ARROW`, `DOWN_ARROW`, `LEFT_RIGHT_ARROW`, `UP_DOWN_ARROW`, `BENT_ARROW`, `PENTAGON`

### Callouts
`WEDGE_RECT_CALLOUT`, `WEDGE_ROUND_RECT_CALLOUT`, `WEDGE_ELLIPSE_CALLOUT`, `CLOUD_CALLOUT`

## Labelling Shapes

Overlay a `text` operation with the same bounding box to label a shape:

```json
[
  { "type": "shape", "id": "proc1", "x": 100, "y": 80, "w": 160, "h": 60,
    "shape_type": "FLOW_CHART_PROCESS", "fill_color": "#4285F4" },
  { "type": "text",  "id": "lbl1",  "x": 100, "y": 80, "w": 160, "h": 60,
    "text": "Validate Input",
    "text_style": { "bold": true, "foreground_color": "#FFFFFF", "alignment": "CENTER" } }
]
```

The text box is transparent by default — the shape fill shows through.

## Typical Sizes (720 × 540 PT slide)

| Element | w | h |
|---|---|---|
| Process box | 160 | 60 |
| Decision diamond | 120 | 80 |
| Terminator | 140 | 50 |
| Database cylinder | 100 | 80 |
| Wide banner | 720 | 60 |

## Additional Resources

- **`references/shape-catalog.md`** — Full shape type catalog with all variants (arrows, stars, callout variants, all FLOW_CHART_* types)
