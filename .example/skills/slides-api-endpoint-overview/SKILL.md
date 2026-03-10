---
name: slides-api-endpoint-overview
description: Use when you want a quick sense of the main Slides API endpoints (create, read, batchUpdate, delete) and how their request/response shapes relate to the local skills.
version: 0.1.0
---

# slides-api-endpoint-overview

This skill is your entry point into the API reference. `skills/reference-digests/endpoints-summary.md` condenses each endpoint’s purpose so you can decide whether to dive into shapes, lines, tables, or page metadata.

## Why it exists
- The endpoint documentation is large; this skill summarizes each request/response structure so you can pick the right digest to load next.
- It keeps the context small—read nothing but the digest to recall which endpoints accept `shape`, `text`, `line`, or `table` payloads.

## Next steps
1. Open `skills/reference-digests/endpoints-summary.md` to identify which endpoint matches your goal (e.g., creating shapes vs. reading the slide).
2. Jump to the digest linked in `reference-digests` that matches the payload you plan to send (shapes/types, text, lines, etc.).
