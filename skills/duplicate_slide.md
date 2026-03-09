# duplicate_slide
Create a copy of an existing slide so the user can clearly see the result of AI-generated edits while the original remains unchanged.

Arguments:
- `presentation_id` (string)
- `slide_index` (int): zero-based index of the slide to duplicate.

Output:
- Returns the API response for the duplication request.

Use this when the user explicitly asks to preserve a visible history of changes.
