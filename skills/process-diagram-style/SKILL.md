# process-diagram-style — Process Diagram Visual Language

## Purpose
Capture the single visual style currently in use on slide 0: the process diagram vocabulary. Follow these rules whenever the human explicitly asks for this style or when you and the human agree you should continue in the same language.

- After reading slide 0 on March 9, 2026, the process diagram style was distilled directly from that canvas. The diagram is sprawling (≈3000×2000 PT) and divided into sections, with a legend near the top that defines each role.
- All core nodes (concept, process, data pills, etc.) use flowchart primitives (`FLOW_CHART_*`) so you can dial in the radius and keep line work consistent. Aim for a rectangular aspect ratio (wider than tall) for these shapes, then max out the corner radius on `FLOW_CHART_ROUNDED_RECTANGLE` so the node appears pill-shaped—this keeps the text area readable while preserving the pill silhouette.
- Colors stay restrained: reuse the legend palette (soft blues, the dark construction for data pills, and muted grays) or describe any new palette before introducing it. If you need an additional concept that the legend doesn’t cover, pick one or two muted hues, state the mapping, and ask the user to confirm.
- Text labels inside the shapes remain 12–14 pt bold and centered; longer explanations live in floating text boxes (10–11 pt regular) with bullet points, positioned close to their target so the reader can draw the connection without overlap.

## Shape vocabulary
| Role | Shape type | Size / behavior | Notes |
|---|---|---|---|
| Concept / state pill | `FLOW_CHART_ROUNDED_RECTANGLE` | Rectangular area (wider than tall, typically ≈60–80 PT wide × 42.5 PT high) with maxed radius | Light blue fill, dark text; push the corner radius all the way so the rectangle becomes a pill while keeping enough room for the label and optionally overlay a transparent text box for precise text placement.
| Data record pill | `FLOW_CHART_ROUNDED_RECTANGLE` | Rectangular area similar to concept pills (wider than tall) with radius maximized | Dark blue (`#1565C0`) fill, white text. Keep the same pill proportions as concept nodes so the color differentiates role while the shape language stays consistent.
| Process node | `ELLIPSE` | Tiny dot (≈25 EMU raw) | Invisible or filled with a neutral color; floating text sits beside it to explain the stage.
| Decision diamond | `FLOW_CHART_DECISION` | Small (≈12×12 PT) | White fill, dark text. Place each path label outside the diamond next to the connector it controls.
| Circle aggregator | `ELLIPSE` | ≈8 PT diameter dot | Filled circle for junctions with 3+ connectors; keeps overlapping connectors tidy.
| Process rectangle / sub-process | `FLOW_CHART_PROCESS` | Sized to content | A structured block that can stretch vertically; tweak the corner radius so the interior text stays legible.
| Pill label / section header | `FLOW_CHART_ROUNDED_RECTANGLE` | Height 20–28 PT, wider for long titles | Track headers and legend entries. Match the legend’s colors when possible but pick a neutral tone if describing a new grouping.
| Zone divider | `line` with `category: "STRAIGHT"` | Full width/height | Light gray (`#CCCCCC`) line segments give a dashed impression when needed; the legend indicates whether the divider should run horizontally or vertically.

## Connections & arrow policy
- Connectors are elbow (`BENT`) or smooth (`CURVED`) rather than straight lines so the routing mirrors the reference slide. If the flow is left-to-right with two adjacent nodes, snap the start site `1` (right of the source) to the end site `3` (left of the target) so the path hugs the shape edges.
- Use black strokes (`#000000`) with a weight of 2 pt. Dashes are acceptable when you need to imply a different relationship; set them consistently per connection and mention the intent if it deviates from solid.
- Arrowheads are welcome when they add clarity (loops, ambiguous splits, or return flows). Add them sparingly and explain why you added them if a human asks.
- When >2 connectors meet, insert a small `ELLIPSE` aggregator (`≈8 PT`) and connect every line to it to avoid overlapping.
- Decision paths get labeled text boxes near the connector termini, not inside the diamond.

## Color system
- If the slide includes a legend, match the documented fills/text colors — treat it as the contract for the diagram.
- When no legend exists or you need a new concept, keep the palette simple (one or two muted hues plus grayscale outlines) and describe the role-to-color mapping before drawing.
- Feel free to reuse the current blue/orange/gray tokens when they match the concept you are drawing, but don't lock yourself in; the user can pick a different color set if they prefer.

## Text hierarchy & annotations
- Node labels inside pills are 12–14 pt bold, centered, and uppercase if the human prefers emphasis.
- Detail text boxes (floating text) are 10–11 pt regular, aligned left, and use bullet points to break up information.
- Keep annotation boxes close to the object they describe, with just enough space so the text doesn’t bump into connectors.
- Avoid paragraph-style text inside small shapes; if more explanation is needed, write it in a nearby floating box.

## Process tips
- Sketch a multi-step plan in `tmp-step-1.md`, `tmp-step-2.md`, etc., before writing scripts that change the slide. Each file should describe one phase of the work so you and the human can iterate on the plan.
- Prefer smaller `scripts/tmp-*.py` jobs that draw a few elements at a time so the human sees updates quickly and can redirect if needed.
- Always double-check the legend when assigning colors or roles; the legend is the contract for this visual language.

## Expanding the style library
When the human needs a new visual approach, copy this skill into a new `skills/<style-name>/SKILL.md` folder and describe the new rules there. Update AGENT.md to point to the available style skills and prompt the user for the one they want before executing commands.
