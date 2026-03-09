---
name: read-slide
description: This skill should be used when the user asks to "read the slide", "inspect the slide", "what's on the slide", "get slide elements", "check the current slide", "list shapes on slide", or before planning any drawing operation on a Google Slides presentation.
version: 0.1.0
---

# read-slide

Inspect the current contents of a slide before planning or drawing.

## Always Call First

Call `read-slide` before any drawing operation to:
- Discover existing element IDs (avoid ID collisions)
- Understand current layout and occupied space
- Confirm the correct `slide_index`

## Command

```json
{
  "tool": "read_slide",
  "presentation_id": "1abc...",
  "slide_index": 0
}
```

Send via:
```bash
python scripts/send_command.py '{"tool":"read_slide","presentation_id":"...","slide_index":0}'
```

## Response

```json
{
  "slide_id": "g1234abcd",
  "title": "My Presentation",
  "elements": [
    { "objectId": "p1", "type": "SHAPE", "text": "Hello" },
    { "objectId": "p2", "type": "LINE" },
    { "objectId": "p3", "type": "TABLE" }
  ]
}
```

## Using the Response

- Use `slide_id` if any operation needs the page object ID directly.
- Check `elements[].objectId` to avoid using IDs that already exist.
- Empty `elements` array means the slide is blank — safe to draw freely.
- For a 720 × 540 PT slide, plan positions so shapes don't overlap unless intentional.
