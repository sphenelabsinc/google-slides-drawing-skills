# Text Digest

Highlights from `googleSlidesAPI_v1/text.md` for when you style or insert text.

- **Page.TextContent** is a hierarchy: `textElements[]` include `TextRun`, `AutoText`, and `ParagraphMarker` entries; use them to insert raw text or mix styles.
- **TextStyle** fields: `fontFamily`, `fontSize`, `bold`, `italic`, `foregroundColor`, `baselineOffset`, `weightedFontFamily`, and `link` give you granular control over formatting.
- **ParagraphStyle** supports `alignment` (START/CENTER/END), `lineSpacing`, `direction`, `indent`, and bullet options (`TextBullet` with `ListStyle`).
- **AutoText & lists**: `AutoText` entries can pull placeholders like slide numbers; `ListStyle` and `NestingLevel` let you shape bullet hierarchies.

Keep this digest open when making `insertText`, `updateTextStyle`, or `updateParagraphStyle` calls so you can remember the main fields without scanning the full docs.
