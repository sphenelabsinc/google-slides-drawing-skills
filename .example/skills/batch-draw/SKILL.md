---
name: batch-draw
description: This skill should be used when the user asks to "draw on a slide", "add shapes to a slide", "create a diagram", "draw a flowchart", "add connectors", "place text on a slide", "draw a table", "create a layout", "render elements", or wants to execute any composed drawing operations on a Google Slides presentation.
version: 0.1.0
---

# batch-draw

Send a batch of pre-composed drawing operations to a Google Slides presentation in a single API call via the local socket server.

## Role

This skill is the **executor**. It does not compose operations — it sends them. Use the composing skills first:
- **`draw-shapes`** — rectangles, ellipses, flowchart symbols, arrows, callouts
- **`draw-lines`** — straight lines, bent connectors, curved connectors, shape connections
- **`draw-text`** — text boxes, labels, banners, styled text
- **`draw-table`** — tables with rows, columns, cell styling, merges
- **`colors`** — color specification for all fill, stroke, and text properties

## Workflow

1. Call `read-slide` to inspect the current slide (get element IDs and layout).
2. Plan the full set of operations: shapes → text labels → connectors → tables.
3. Compose each operation dict using the composing skill references.
4. Send one `batch_draw` command to the server.

**Always create shapes before connectors that reference them** — operations are executed in order.

## Sending a Command

Use `scripts/send_command.py` at the project root:

```bash
python scripts/send_command.py '{"tool":"batch_draw","presentation_id":"...","slide_index":0,"operations":[...]}'
```

Or pipe JSON:
```bash
echo '{ ... }' | python scripts/send_command.py
```

## Command Structure

```json
{
  "tool": "batch_draw",
  "presentation_id": "1abc_PRESENTATION_ID",
  "slide_index": 0,
  "operations": [ ... ]
}
```

## Operation Types Summary

| type | Description |
|---|---|
| `shape` / `rectangle` | Create a shape (requires `id`, `x`, `y`, `w`, `h`) |
| `text` | Create a text box with content |
| `line` / `connector` / `arrow` | Create a line or connector |
| `table` | Create a table |
| `insert_text` | Insert text into a table cell |
| `update_table_cell` | Set table cell background |
| `merge_table_cells` | Merge a range of table cells |
| `reroute_line` | Reroute a connected line to closest sites |

All coordinates and sizes are in **points (PT)**. Standard slide: **720 × 540 PT**.

Object IDs must be unique across the whole presentation, **5–50 chars**, starting with `[a-zA-Z0-9_]`.

## Minimal Example

```json
{
  "tool": "batch_draw",
  "presentation_id": "1c-z-5s1Ofu0MPb2bad...",
  "slide_index": 0,
  "operations": [
    {
      "type": "shape", "id": "proc1",
      "x": 100, "y": 80, "w": 160, "h": 60,
      "shape_type": "FLOW_CHART_PROCESS",
      "fill_color": "#4285F4"
    },
    {
      "type": "text", "id": "lbl1",
      "x": 100, "y": 80, "w": 160, "h": 60,
      "text": "Process A",
      "text_style": { "bold": true, "foreground_color": "#FFFFFF", "alignment": "CENTER" }
    }
  ]
}
```

## Additional Resources

- **`references/server-protocol.md`** — Socket server details, config.json, error handling
- **`scripts/send_command.py`** (project root) — Shared TCP client utility
