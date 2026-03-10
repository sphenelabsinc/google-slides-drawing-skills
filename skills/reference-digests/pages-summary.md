# Pages Digest

High-level bullet points from `googleSlidesAPI_v1/pages.md` so you understand the `Page` and `PageElement` structure quickly.

- **Page resource**: Has `objectId`, `pageType` (`SLIDE`, `MASTER`, `LAYOUT`, `NOTES`, `NOTES_MASTER`), `revisionId`, `pageElements`, and specific `slideProperties`, `layoutProperties`, `notesProperties`, or `masterProperties` depending on type.
- **PageElement union**: Each element can be a `shape`, `image`, `line`, `table`, `wordArt`, `sheetsChart`, or `speakerSpotlight`. Check `size`, `transform`, `title`, `description`, and the type-specific payload (`shape`, `line`, etc.).
- **Transform/Size**: `AffineTransform` defines `scaleX`, `scaleY`, translations; `Size` uses EMUs and PT units—they get converted automatically by the server.
- **Theme/background**: `pageProperties` contain the `pageBackgroundFill`, `colorScheme`, and `themeColorPair` that new shapes inherit.

Use this digest to orient yourself on which page-level metadata you can read or write before diving into element-specific docs.
