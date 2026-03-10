---
name: clear-slide
description: This skill should be used when the user asks to "clear the slide", "delete everything on the slide", "wipe the slide", "start fresh", "remove all elements", or wants to reset a slide before redrawing.
version: 0.1.0
---

# clear-slide

Delete all page elements from a slide.

## Command

```json
{
  "tool": "clear_slide",
  "presentation_id": "1abc...",
  "slide_index": 0
}
```

Send via:
```bash
python scripts/send_command.py '{"tool":"clear_slide","presentation_id":"...","slide_index":0}'
```

## Response

```json
{ "status": "ok", "response": { ... } }
```

If the slide is already empty:
```json
{ "status": "ok", "message": "slide already empty" }
```

## Typical Workflow

1. `clear_slide` — remove existing elements
2. `read_slide` — confirm empty, get fresh `slide_id`
3. `batch_draw` — draw the new layout
