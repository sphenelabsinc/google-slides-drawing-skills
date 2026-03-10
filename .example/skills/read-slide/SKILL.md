---
name: read-slide
description: Use this skill whenever you are about to inspect the current slide contents, gather object IDs, or understand how the API models each element before planning drawing operations.
version: 0.1.0
---

# read-slide

Inspect every attribute that the Google Slides API exposes for the requested page before mutating it. `read-slide` is the first skill you should run: it sets expectations about what elements already exist, what `pageProperties` look like, and whether the page is really a slide, layout, master, or notes page.

## Always call this before mutating
- Discover every object ID on the slide so you avoid duplicate IDs.
- Understand the current layout, background, and template metadata (`pageProperties`, `slideProperties`, `masterProperties`) so you can inherit placeholder styles correctly.
- Confirm the `page_type` and `revision_id`—these describe whether the page is a slide, notes page, master, etc., and let you detect if someone edited the deck before you run your batch.

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
  "slide_index": 0,
  "title": "My Presentation",
  "revision_id": "r20260309",
  "page_type": "SLIDE",
  "page_properties": { "pageBackgroundFill": { "solidFill": { "color": { "rgbColor": { "red": 1 } } } } },
  "slide_properties": { "notes_page": { "objectId": "notes123" } },
  "layout_properties": null,
  "notes_properties": null,
  "master_properties": { "master_object_id": "master123" },
  "page_background": { "solidFill": { "color": { "rgbColor": { "red": 1 } } } },
  "element_count": 3,
  "elements": [
    { "objectId": "p1", "type": "shape", "text": "Title", "x": 100, "y": 80, "w": 200, "h": 60, "shape_type": "TEXT_BOX" },
    { "objectId": "p2", "type": "line", "x": 90, "y": 200, "w": 300, "h": 0, "line_category": "STRAIGHT" },
    { "objectId": "p3", "type": "shape", "shape_type": "RECTANGLE" }
  ],
  "page_elements": [
    {
      "objectId": "p1",
      "size": { "width": { "magnitude": 200, "unit": "PT" }, "height": { "magnitude": 60, "unit": "PT" } },
      "shape": { "shapeType": "TEXT_BOX" }
    },
    {
      "objectId": "p2",
      "line": { "lineCategory": "STRAIGHT" },
      "size": { "width": { "magnitude": 300, "unit": "PT" }, "height": { "magnitude": 0, "unit": "PT" } }
    }
  ],
  "element_details": {
    "p1": { "objectId": "p1", "shape": { "shapeType": "TEXT_BOX" } },
    "p2": { "objectId": "p2", "line": { "lineCategory": "STRAIGHT" } }
  }
}
```

## Using the response
- `elements` keeps delivering the quick summaries you already rely on (position, type, text) so you can plan new shapes without colliding with existing objects.
- `page_elements` holds the raw `PageElement` structures returned by the Slides API; inspect this when you need the `shapeProperties`, `textElements`, `table` cells, or `image` metadata for an object.
- `element_details` maps each `objectId` to its full payload; use it to look up a single shape or line without hunting the entire list.
- `element_count` tells you how many `pageElements` are present so you can verify whether a destructive operation (like `clear_slide`) actually removed every object.
- `page_properties`, `slide_properties`, `layout_properties`, `notes_properties`, and `master_properties` expose the template metadata that new shapes will inherit (fill, placeholders, theme colors, speaker notes linkage).
- `page_background` repeats `page_properties.pageBackgroundFill` so you can quickly see whether a background is a picture, gradient, or solid fill before adding new art.
- `page_type` clarifies whether you are looking at a `SLIDE`, `MASTER`, `LAYOUT`, `NOTES`, or `NOTES_MASTER` page; only `SLIDE` pages accept most drawing operations.
- `revision_id` lets you detect concurrent edits; refuse to send a `batch_draw` if the value changed between your `read-slide` and `batch_draw` calls.

For field-level definitions (e.g., `Page.Shape`, `Page.Line`, `ParagraphStyle`, `TableCellProperties`, etc.), consult the `reference-digests` skill for bite-sized summarizations of the underlying API files (`shapes.md`, `lines.md`, `text.md`, `tables.md`, `pages.md`). Each digest points back to the relevant raw document so you can copy the field name directly into a future `batch_draw` operation.
