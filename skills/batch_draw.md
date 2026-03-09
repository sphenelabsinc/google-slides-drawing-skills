# batch_draw
Draw multiple elements with a single batchUpdate call. This minimizes API traffic and keeps the slide state coherent.

Arguments:
- `presentation_id` (string): the target presentation.
- `slide_index` (int): zero-based index of the slide to modify.
- `operations` (array): each operation is a dictionary describing one shape.

Supported operation types:
- `type: "rectangle"` or `type: "shape"` (requires `id`, `x`, `y`, `w`, `h`, optional `shape_type`)
- `type: "text"` (requires `id`, `x`, `y`, `w`, `h`, must include `text`, optional `text_style` and `shape_type`)
- `type: "line"`, `type: "connector"` or `type: "arrow"` (requires `id`, `x`, `y`, `w`, `h`, optional `lineCategory`)

Common optional fields per operation:
- `shape_type`: Google Slides shape type (e.g., `RECTANGLE`, `ELLIPSE`, `TEXT_BOX`). Defaults to `RECTANGLE` for shapes and `TEXT_BOX` for text.
- `fill_color`: `{"hex": "#ff0000"}` or `{"r":255,"g":0,"b":0,"alpha":0.5}` or similar. Controls the shape background fill.
- `outline_color`, `outline_width`: controls border color and thickness. Omit for borderless shapes.
- `line_color`, `line_weight`: control the stroke color/width for line connectors. Colors follow the same format used for `fill_color`.
- `lineCategory`: the connector style (`STRAIGHT`, `ELBOW`, `BENT`). Use `ELBOW`/`BENT` to express curved or angled joins between features.
- `start_arrow`, `end_arrow`: arrowhead style names (e.g., `STEALTH`, `TRIANGLE`, `NONE`) when drawing connectors.
- `text_style`: used when `type: "text"`. Recognized keys: `font_family`, `font_size`, `bold`, `italic`, `foreground_color`, `alignment`. `foreground_color` uses the same color format.

Color notes:
- Channels in `fill_color`, `outline_color`, `line_color`, or `foreground_color` may be provided as hex strings (`#rrggbb` or `#rrggbbaa`) or dictionaries with `r`, `g`, `b` (0–255 or 0.0–1.0) plus optional `alpha`.

Connector guidance:
- After you understand the slide via `read_slide`, sketch relationships using `line`/`connector` operations to draw `ELBOW` or `BENT` segments and show how the new shapes link together. This keeps the batch update performant while maintaining visual logic.

Example workflow:
1. `read_slide` the target to capture existing elements.
2. Plan every rectangle, text box, connector, and banner you need.
3. Send a single `batch_draw` command containing all operations (shape + connector + text) so the server issues one `batchUpdate` instead of multiple round-trips.

Best practice:
1. Call `read_slide` to understand current elements.
2. Plan geometry and labels.
3. Send one `batch_draw` command with all operations to avoid repeated network calls.
