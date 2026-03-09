---
name: draw-text
description: This skill should be used when the user asks to "add text", "add a label", "write on the slide", "add a title", "add a text box", "format text", "add a banner with text", "set font size", "make text bold", or needs to compose text operations for a Google Slides batch-draw command.
version: 0.1.0
---

# draw-text

Compose text box operations for `batch-draw`.

## Operation Structure

```json
{
  "type": "text",
  "id": "unique_id",
  "x": 100,
  "y": 80,
  "w": 180,
  "h": 60,
  "text": "Hello World",
  "shape_type": "TEXT_BOX",
  "fill_color": null,
  "outline_color": null,
  "text_style": {
    "font_family": "Arial",
    "font_size": 14,
    "bold": false,
    "italic": false,
    "foreground_color": "#000000",
    "alignment": "CENTER"
  }
}
```

| Field | Required | Default | Notes |
|---|---|---|---|
| `type` | yes | — | `"text"` |
| `id` | yes | — | Unique, 5–50 chars |
| `x`, `y`, `w`, `h` | yes | — | Bounding box in PT |
| `text` | no | — | Text content (`\n` for line breaks) |
| `shape_type` | no | `TEXT_BOX` | Any shape type works as a text container |
| `fill_color` | no | transparent | Background fill |
| `outline_color` | no | none | Border color |
| `text_style` | no | — | Text formatting options |

## Text Style Fields

| Field | Values |
|---|---|
| `font_family` | `"Arial"`, `"Roboto"`, `"Georgia"`, `"Dancing Script"`, etc. |
| `font_size` | Number in points (e.g. `12`, `18`, `36`) |
| `bold` | `true` / `false` |
| `italic` | `true` / `false` |
| `foreground_color` | Any color spec (see `colors` skill) |
| `alignment` | `"LEFT"`, `"CENTER"`, `"RIGHT"`, `"JUSTIFIED"` |

## Labelling Shapes

To put a label inside a shape, use the **same `x/y/w/h`** as the shape. The text box is transparent by default:

```json
[
  { "type": "shape", "id": "decision1",
    "x": 280, "y": 100, "w": 160, "h": 80,
    "shape_type": "FLOW_CHART_DECISION", "fill_color": "#F9A825" },
  { "type": "text", "id": "dlbl1",
    "x": 280, "y": 100, "w": 160, "h": 80,
    "text": "Valid?",
    "text_style": { "bold": true, "alignment": "CENTER", "font_size": 14 } }
]
```

## Banner Example

```json
{
  "type": "text", "id": "banner",
  "x": 0, "y": 490, "w": 720, "h": 50,
  "text": "CONFIDENTIAL",
  "fill_color": { "hex": "#B71C1C", "alpha": 0.9 },
  "text_style": {
    "font_family": "Roboto", "font_size": 18,
    "bold": true, "foreground_color": "#FFFFFF", "alignment": "CENTER"
  }
}
```

## Multi-line Text

```json
"text": "Line one\nLine two\nLine three"
```

## Tips

- Text is always inserted at index 0 (beginning of the text box).
- Only one `text` field per operation.
- For dark fills, use `foreground_color: "#FFFFFF"` (white text).
- For slide titles: `y: 30–60`, large `font_size` (28–40), `bold: true`.
- Vertical centering is not controllable via API — adjust `y` and `h` to visually center.
