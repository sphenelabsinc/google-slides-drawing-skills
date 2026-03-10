---
name: draw-lines
description: This skill should be used when the user asks to "draw a line", "add a connector", "connect two shapes", "draw an arrow between", "add an elbow connector", "draw a curved connector", "connect flowchart boxes", "add a straight line", or needs to compose line/connector operations for a Google Slides batch-draw command.
version: 0.1.0
---

# draw-lines

Compose line and connector operations for `batch-draw`.

## Operation Structure

```json
{
  "type": "line",
  "id": "unique_id",
  "x": 100,
  "y": 140,
  "w": 1,
  "h": 80,
  "category": "STRAIGHT",
  "line_color": "#333333",
  "line_weight": 2,
  "start_arrow": "NONE",
  "end_arrow": "FILL_ARROW",
  "start_connection": {
    "connected_object_id": "box1",
    "connection_site_index": 2
  },
  "end_connection": {
    "connected_object_id": "box2",
    "connection_site_index": 0
  }
}
```

| Field | Required | Default | Notes |
|---|---|---|---|
| `type` | yes | — | `"line"`, `"connector"`, or `"arrow"` |
| `id` | yes | — | Unique, 5–50 chars |
| `x`, `y`, `w`, `h` | yes | — | Bounding box in PT |
| `category` | no | `STRAIGHT` | Line routing style |
| `line_color` | no | black | Stroke color |
| `line_weight` | no | 1 | Stroke thickness in PT |
| `start_arrow` | no | `NONE` | Arrowhead at start |
| `end_arrow` | no | `NONE` | Arrowhead at end |
| `start_connection` | no | — | Snap start to shape |
| `end_connection` | no | — | Snap end to shape |

## Line Categories

| Value | Style |
|---|---|
| `STRAIGHT` | Direct straight line (default) |
| `BENT` | Right-angle elbow routing (standard flowchart connector) |
| `CURVED` | Smooth S-curve routing |

> `ELBOW` is NOT valid — use `BENT` instead.

## Arrow Styles

| Value | Appearance |
|---|---|
| `NONE` | No arrowhead |
| `STEALTH` | Small filled stealth point |
| `FILL_ARROW` | Solid filled triangle |
| `OPEN` | Open (outline) triangle |
| `FILL_CIRCLE` | Filled circle |
| `OPEN_CIRCLE` | Open circle |
| `FILL_SQUARE` | Filled square |
| `OPEN_SQUARE` | Open square |
| `FILL_DIAMOND` | Filled diamond |
| `OPEN_DIAMOND` | Open diamond |

## Connection Sites

Standard connection site indices (clockwise from top):
- `0` = top center
- `1` = right center
- `2` = bottom center
- `3` = left center

## Connecting Shapes

Set `start_connection` and `end_connection` to snap a connector to shapes. The API auto-routes the line within its bounding box. After drawing, add a `reroute_line` operation to snap to the closest sites:

```json
{ "type": "reroute_line", "id": "conn1" }
```

## Common Patterns

### Flowchart downward arrow (box1 bottom → box2 top)
```json
{ "type": "connector", "id": "flow1",
  "x": 180, "y": 140, "w": 1, "h": 60,
  "category": "BENT", "end_arrow": "FILL_ARROW",
  "line_weight": 2,
  "start_connection": { "connected_object_id": "proc1", "connection_site_index": 2 },
  "end_connection":   { "connected_object_id": "proc2", "connection_site_index": 0 } }
```

### Bidirectional relationship line
```json
{ "type": "line", "id": "rel1",
  "x": 200, "y": 80, "w": 120, "h": 1,
  "category": "STRAIGHT",
  "start_arrow": "OPEN_DIAMOND", "end_arrow": "FILL_ARROW",
  "line_color": "#1565C0", "line_weight": 2 }
```

## Additional Resources

- **`references/connector-reference.md`** — Full connector type details, dash styles, connection site mapping by shape
