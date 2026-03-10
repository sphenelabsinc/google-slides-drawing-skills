---
name: reference-digests
description: Use when you want bite-sized summaries of the Google Slides API reference files instead of loading the full documents.
version: 0.1.0
---

# reference-digests

This skill points to the digest files under `skills/reference-digests/` that chunk the large `googleSlidesAPI_v1/*.md` references into composable pieces.

## Digests
| Digest | Focus |
|---|---|
| `shapes-types.md` | Shape type enums split into rectangles/callouts, flowchart nodes, arrows, and specialty symbols.
| `shapes-properties.md` | Shape styling fields: fills, outlines, shadows, content alignment, and autofit.
| `lines-summary.md` | Line categories, arrowheads, weights, and connection payloads.
| `text-summary.md` | Text content hierarchy, styles, paragraph formatting, bullets, and auto text.
| `tables-summary.md` | Table structure, cell indexing, fills, and border properties.
| `pages-summary.md` | Overview of the `Page` resource, page elements unions, transforms, and background fills.
| `endpoints-summary.md` | Entry-level digest for each endpoint (create, read, batchUpdate, delete) so you know which detail digest to open next.

## How to use
1. Open `endpoints-summary.md` to orient yourself if you aren’t sure which endpoint you need.
2. Jump to the relevant digest (shapes, tables, text, lines, or pages) for a short summary before diving into the full `googleSlidesAPI_v1/*.md` file.
3. Keep the digest list short so you can load only the portion needed for your task; reference them with `rg` or by path when you forget a specific field name.
