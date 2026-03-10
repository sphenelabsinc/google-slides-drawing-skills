# Connector Reference

## Line Categories (API `category` field)

The `category` field in `createLine` determines routing style. Valid values:
- `STRAIGHT` — straight connector 1; direct line between endpoints
- `BENT` — bent connectors 2–5; right-angle routing (elbow joints)
- `CURVED` — curved connectors 2–5; smooth Bézier routing

The API determines the exact connector sub-type based on routing between connected elements.

**Important:** `ELBOW` is deprecated and invalid. Use `BENT`.

## Arrow Styles (full list)

`NONE`, `STEALTH`, `FILL_ARROW`, `OPEN`, `FILL_CIRCLE`, `OPEN_CIRCLE`, `FILL_SQUARE`, `OPEN_SQUARE`, `FILL_DIAMOND`, `OPEN_DIAMOND`, `SHORT`

## Dash Styles (not yet exposed in skill — raw API)

If building raw requests: `SOLID`, `DOT`, `DASH`, `DASH_DOT`, `LONG_DASH`, `LONG_DASH_DOT`

## Connection Sites by Shape Type

Most shapes have 4 connection sites:
- `0` = top center, `1` = right center, `2` = bottom center, `3` = left center

Shapes with more sites (typically have side midpoints too):
- Callout shapes: may have 4–8 sites including the tail anchor
- Star shapes: site per point
- Arrow shapes: sites at each tip

To discover actual site indices for a specific element, call `read_slide` and inspect `connectionSites` on the element.

## Rerouting

After creating a connected line, add a `reroute_line` operation to automatically snap it to the two closest connection sites:

```json
{ "type": "reroute_line", "id": "conn1" }
```

This is equivalent to the API's `rerouteLine` request. Most useful after:
- Moving shapes to new positions
- Changing shape sizes
- Creating connectors without specifying exact site indices

## updateLineCategory

To change a line's category after creation (not yet exposed as skill operation — use `batch_draw` raw if needed):
```json
{
  "updateLineCategory": {
    "objectId": "conn1",
    "lineCategory": "BENT"
  }
}
```

## Line Weight Guide

| Weight (PT) | Use case |
|---|---|
| 1 | Reference/annotation lines |
| 2 | Standard flowchart connectors |
| 3 | Emphasis connectors |
| 4–6 | Bold callout lines |
