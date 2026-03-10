---
name: colors
description: This skill should be used when the user asks about "what color format to use", "how to set fill color", "use a hex color", "specify RGB color", "set text color", "color a shape", or needs to understand color specification for Google Slides batch-draw operations.
version: 0.1.0
---

# colors

Color specification reference for all `fill_color`, `outline_color`, `line_color`, and `text_style.foreground_color` fields.

## Formats

### Hex string
```json
"fill_color": "#4285F4"          // 6-digit RGB
"fill_color": "#4285F4CC"        // 8-digit RGBA (CC = 80% opacity)
"fill_color": "#FFF"             // 3-digit shorthand
```

### RGB dict
```json
"fill_color": { "r": 66, "g": 133, "b": 244 }           // 0–255 range
"fill_color": { "r": 0.259, "g": 0.522, "b": 0.957 }    // 0.0–1.0 range
```

### No color / transparent
```json
"fill_color": null
```
Or omit the field.

## Where Colors Apply

| Field | Context |
|---|---|
| `fill_color` | Shape/text box background |
| `outline_color` + `outline_width` | Shape border |
| `line_color` + `line_weight` | Line/connector stroke |
| `text_style.foreground_color` | Text fill |

## Quick Palette

| Color | Hex | Usage |
|---|---|---|
| Google Blue | `#4285F4` | Primary shapes |
| Google Red | `#EA4335` | Alerts, terminators |
| Google Yellow | `#FBBC05` | Decisions, warnings |
| Google Green | `#34A853` | Success, start nodes |
| Dark Blue | `#1A237E` | Headers, banners |
| Blue Grey | `#455A64` | Borders, subdued |
| Light Grey | `#EEEEEE` | Alternating rows |
| Dark Grey | `#424242` | Text, connectors |
| White | `#FFFFFF` | Text on dark bg |
| Transparent blue | `{ "hex": "#1565C0", "alpha": 0.15 }` | Swim-lane tints |

## Tips

- Dark fills → use `foreground_color: "#FFFFFF"` for readable text.
- Swim-lane backgrounds → `alpha: 0.1–0.2` for subtle tinting.
- Borders → pair `outline_color` with `outline_width` (PT); omit both for borderless.
- Connector strokes → `line_color` + `line_weight`.

## Additional Resources

- **`references/palette.md`** — Extended palette with Material Design colors and semantic usage guide
