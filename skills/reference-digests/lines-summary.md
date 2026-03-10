# Lines Digest

The `Page.Line` fields described in `googleSlidesAPI_v1/lines.md` are summarized here so you can route connectors without reading the full reference.

- **Categories**: `category` can be `STRAIGHT`, `BENT`, or `CURVED`; choose based on whether you want elbow connectors or smooth curves.
- **Line properties**: `lineFill` (with `solidFill`) sets the stroke color, `weight` gives the thickness, and `lineCategory` describes the visual style.
- **Arrows**: Set `startArrow`/`endArrow` to enums like `FILL_ARROW` or `CHEVRON_ARROW` when you need arrowheads.
- **Connections**: `startConnection`/`endConnection` attach to shapes using `connectedObjectId` plus `connectionSiteIndex` (0–3 typically on a rectangle).
- **Rerouting**: Use `rerouteLine` operations after `batchUpdate` if you move shapes and want the connector to snap to nearby points.

Refer to this digest before building connectors so you don’t have to read the longer API file every time.
