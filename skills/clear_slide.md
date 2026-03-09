# clear_slide
Remove every element from a slide so the LLM can start fresh before drawing a new plan.

Arguments:
- `presentation_id` (string)
- `slide_index` (int)

Output:
- `status`: `"ok"` with a message or the API response describing the deleted objects.

Do not call this unless the user wants to wipe the slide. Use `read_slide` first to confirm what will be deleted.
