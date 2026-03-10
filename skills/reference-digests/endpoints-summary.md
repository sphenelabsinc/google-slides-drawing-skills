# Endpoints Digest

Short summary of key Slides API REST endpoints and their request/response patterns from the `googleSlidesAPI_v1` collection.

- **presentations.create**: `POST /v1/presentations` with optional `presentationId`, `title`, `pageSize`, `slides`, `layouts`, and `masters`. The response returns the new presentation object with `presentationId`, `revisionId`, and `slides` metadata.
- **presentations.pages**: The page resource documents `pageElements`, `pageProperties`, and type-specific subproperties (`slideProperties`, `notesProperties`, etc.). `read_slide` mimics `presentations.get` followed by slicing to the desired `slide_index`.
- **batchUpdate**: Accepts an array of requests (`createShape`, `insertText`, `createLine`, `deleteObjects`, `updateShapeProperties`, etc.). Each request’s response is usually `Empty`, but the overarching `batchUpdate` response includes `replies` and `presentationId` so you can capture created `objectId`s.
- **deleteObjects**: The server wraps this to remove listed `objectId`s with a single call.

Keep this digest as the entry point before inspecting other digests; it tells you which endpoint to go to next (shapes, tables, text, etc.).
