# read_slide
Observe the current contents of a slide before making a plan.

Arguments:
- `presentation_id` (string): the target presentation.
- `slide_index` (int): zero-based index of the slide to inspect.

Response:
- `slide_id`: the object ID of the inspected slide.
- `title`: the presentation title.
- `elements`: array of objects describing each element (`objectId`, `type`, optional `text` for shapes).

Usage:
Call this skill first so you know what already exists. Use the returned elements to guide your next batch drawing plan.
