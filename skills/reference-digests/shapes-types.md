# Shapes Types Digest

Summaries of the major `shapeType` families as documented in `googleSlidesAPI_v1/shapes.md` so you can reach for the right primitive without rereading the entire file.

## Basics
- `TEXT_BOX`, `RECTANGLE`, `ROUND_RECTANGLE`, `ELLIPSE`, `ARC`, `BEVEL`, `BLOCK_ARC`, `FRAME`, and `DIAMOND` cover the standard UI primitives you reach for most often.
- Rounded rectangles come in variants (`ROUND_1_RECTANGLE`, `ROUND_2_DIAGONAL_RECTANGLE`, `SNIP_*`, `FLOW_CHART_ROUNDED_RECTANGLE`) so you can fine-tune which corners curve and by how much.

## Flowchart / connectors
- Flowchart shapes (`FLOW_CHART_*`) span process, decision, input/output, offline/online storage, terminator, summing junction, etc.; use these when emulating process diagrams.
- Connector silhouettes (`FLOW_CHART_CONNECTOR`, `BENT_ARROW`, `CURVED_*`, `ELBOW`-like shapes) are the ones you choose when you want pre-routed arrows or bent paths.

## Specialty symbols
- Arrows in cardinal directions, guards (brace/bracket), math symbols (`MATH_PLUS`, `MATH_MINUS`), stars (`STAR_*`), and callouts (`WEDGE_*`, `CLOUD_CALLOUT`) are all enumerated; pick the name that matches your visual language.
- Misc shapes (`HEART`, `SUN`, `MOON`, `CLOUD`, `SPEECH`) serve decorative needs and have predictable ECMA-376 equivalents.

This digest lets you pick the right `shapeType` enum quickly instead of scrolling a five-hundred-line table.
