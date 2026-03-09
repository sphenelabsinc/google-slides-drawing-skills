---
name: duplicate-slide
description: This skill should be used when the user asks to "duplicate the slide", "copy this slide", "make a copy of slide", or wants to create a backup before modifying a slide.
version: 0.1.0
---

# duplicate-slide

Duplicate a slide. The copy is inserted immediately after the original.

## Command

```json
{
  "tool": "duplicate_slide",
  "presentation_id": "1abc...",
  "slide_index": 0
}
```

Send via:
```bash
python scripts/send_command.py '{"tool":"duplicate_slide","presentation_id":"...","slide_index":0}'
```

## Response

```json
{ "status": "ok", "response": { ... } }
```

## Typical Workflow

1. `duplicate_slide` — create a backup copy
2. Work on the duplicate (now at index 1)
3. Or: modify the original knowing the backup exists at index+1
