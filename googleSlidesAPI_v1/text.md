# Text

### TextContent


The general text content. The text must reside in a compatible shape (e.g. text box or rectangle) or a table cell in a page.

| JSON representation |
|---|
| ``` { "textElements": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextElement`) } ], "lists": { string: { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.List`) }, ... } } ``` |

| Fields ||
|---|---|
| `textElements[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextElement`)`` The text contents broken down into its component parts, including styling information. This property is read-only. |
| `lists` | ``map (key: string, value: object ( `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.List`))`` The bulleted lists contained in this text, keyed by list ID. |

### TextElement


A TextElement describes the content of a range of indices in the text content of a Shape or TableCell.

| JSON representation |
|---|
| ``` { "startIndex": integer, "endIndex": integer, "paragraphMarker": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.ParagraphMarker`) }, "textRun": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextRun`) }, "autoText": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.AutoText`) } } ``` |

| Fields ||
|---|---|
| `startIndex` | `integer` The zero-based start index of this text element, in Unicode code units. |
| `endIndex` | `integer` The zero-based end index of this text element, exclusive, in Unicode code units. |
| Union field `kind`. The kind of text that this element represents. `kind` can be only one of the following: ||
| `paragraphMarker` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.ParagraphMarker`)`` A marker representing the beginning of a new paragraph. The `startIndex` and `endIndex` of this TextElement represent the range of the paragraph. Other TextElements with an index range contained inside this paragraph's range are considered to be part of this paragraph. The range of indices of two separate paragraphs will never overlap. |
| `textRun` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextRun`)`` A TextElement representing a run of text where all of the characters in the run have the same `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle`. The `startIndex` and `endIndex` of TextRuns will always be fully contained in the index range of a single `paragraphMarker` TextElement. In other words, a TextRun will never span multiple paragraphs. |
| `autoText` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.AutoText`)`` A TextElement representing a spot in the text that is dynamically replaced with content that can change over time. |

### ParagraphMarker


A TextElement kind that represents the beginning of a new paragraph.

| JSON representation |
|---|
| ``` { "style": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.ParagraphStyle`) }, "bullet": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.Bullet`) } } ``` |

| Fields ||
|---|---|
| `style` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.ParagraphStyle`)`` The paragraph's style |
| `bullet` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.Bullet`)`` The bullet for this paragraph. If not present, the paragraph does not belong to a list. |

### ParagraphStyle


Styles that apply to a whole paragraph.


If this text is contained in a shape with a parent
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Placeholder`, then these paragraph styles may be inherited from the parent. Which paragraph styles are inherited depend on the nesting level of lists:

- A paragraph not in a list will inherit its paragraph style from the paragraph at the 0 nesting level of the list inside the parent placeholder.
- A paragraph in a list will inherit its paragraph style from the paragraph at its corresponding nesting level of the list inside the parent placeholder.


Inherited paragraph styles are represented as unset fields in this message.

| JSON representation |
|---|
| ``` { "lineSpacing": number, "alignment": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.Alignment`), "indentStart": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "indentEnd": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "spaceAbove": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "spaceBelow": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "indentFirstLine": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "direction": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextDirection`), "spacingMode": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.SpacingMode`) } ``` |

| Fields ||
|---|---|
| `lineSpacing` | `number` The amount of space between lines, as a percentage of normal, where normal is represented as 100.0. If unset, the value is inherited from the parent. |
| `alignment` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.Alignment`)`` The text alignment for this paragraph. |
| `indentStart` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` The amount indentation for the paragraph on the side that corresponds to the start of the text, based on the current text direction. If unset, the value is inherited from the parent. |
| `indentEnd` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` The amount indentation for the paragraph on the side that corresponds to the end of the text, based on the current text direction. If unset, the value is inherited from the parent. |
| `spaceAbove` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` The amount of extra space above the paragraph. If unset, the value is inherited from the parent. |
| `spaceBelow` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` The amount of extra space below the paragraph. If unset, the value is inherited from the parent. |
| `indentFirstLine` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` The amount of indentation for the start of the first line of the paragraph. If unset, the value is inherited from the parent. |
| `direction` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextDirection`)`` The text direction of this paragraph. If unset, the value defaults to `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextDirection` since text direction is not inherited. |
| `spacingMode` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.SpacingMode`)`` The spacing mode for the paragraph. |

### Alignment


The types of text alignment for a paragraph.

| Enums ||
|---|---|
| `ALIGNMENT_UNSPECIFIED` | The paragraph alignment is inherited from the parent. |
| `START` | The paragraph is aligned to the start of the line. Left-aligned for LTR text, right-aligned otherwise. |
| `CENTER` | The paragraph is centered. |
| `END` | The paragraph is aligned to the end of the line. Right-aligned for LTR text, left-aligned otherwise. |
| `JUSTIFIED` | The paragraph is justified. |

### TextDirection


The directions text can flow in.

| Enums ||
|---|---|
| `TEXT_DIRECTION_UNSPECIFIED` | The text direction is inherited from the parent. |
| `LEFT_TO_RIGHT` | The text goes from left to right. |
| `RIGHT_TO_LEFT` | The text goes from right to left. |

### SpacingMode


The different modes for paragraph spacing.

| Enums ||
|---|---|
| `SPACING_MODE_UNSPECIFIED` | The spacing mode is inherited from the parent. |
| `NEVER_COLLAPSE` | Paragraph spacing is always rendered. |
| `COLLAPSE_LISTS` | Paragraph spacing is skipped between list elements. |

### Bullet


Describes the bullet of a paragraph.

| JSON representation |
|---|
| ``` { "listId": string, "nestingLevel": integer, "glyph": string, "bulletStyle": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle`) } } ``` |

| Fields ||
|---|---|
| `listId` | `string` The ID of the list this paragraph belongs to. |
| `nestingLevel` | `integer` The nesting level of this paragraph in the list. |
| `glyph` | `string` The rendered bullet glyph for this paragraph. |
| `bulletStyle` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle`)`` The paragraph specific text style applied to this bullet. |

### TextStyle


Represents the styling that can be applied to a TextRun.


If this text is contained in a shape with a parent
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Placeholder`, then these text styles may be inherited from the parent. Which text styles are inherited depend on the nesting level of lists:

- A text run in a paragraph that is not in a list will inherit its text style from the the newline character in the paragraph at the 0 nesting level of the list inside the parent placeholder.
- A text run in a paragraph that is in a list will inherit its text style from the newline character in the paragraph at its corresponding nesting level of the list inside the parent placeholder.


Inherited text styles are represented as unset fields in this message. If text is contained in a shape without a parent placeholder, unsetting these fields will revert the style to a value matching the defaults in the Slides editor.

| JSON representation |
|---|
| ``` { "backgroundColor": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.OptionalColor`) }, "foregroundColor": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.OptionalColor`) }, "bold": boolean, "italic": boolean, "fontFamily": string, "fontSize": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "link": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Link`) }, "baselineOffset": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.BaselineOffset`), "smallCaps": boolean, "strikethrough": boolean, "underline": boolean, "weightedFontFamily": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.WeightedFontFamily`) } } ``` |

| Fields ||
|---|---|
| `backgroundColor` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.OptionalColor`)`` The background color of the text. If set, the color is either opaque or transparent, depending on if the `opaqueColor` field in it is set. |
| `foregroundColor` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.OptionalColor`)`` The color of the text itself. If set, the color is either opaque or transparent, depending on if the `opaqueColor` field in it is set. |
| `bold` | `boolean` Whether or not the text is rendered as bold. |
| `italic` | `boolean` Whether or not the text is italicized. |
| `fontFamily` | `string` The font family of the text. The font family can be any font from the Font menu in Slides or from [Google Fonts](https://fonts.google.com/). If the font name is unrecognized, the text is rendered in `Arial`. Some fonts can affect the weight of the text. If an update request specifies values for both `fontFamily` and `bold`, the explicitly-set `bold` value is used. |
| `fontSize` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` The size of the text's font. When read, the `fontSize` will specified in points. |
| `link` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Link`)`` The hyperlink destination of the text. If unset, there is no link. Links are not inherited from parent text. Changing the link in an update request causes some other changes to the text style of the range: - When setting a link, the text foreground color will be set to `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ThemeColorType` and the text will be underlined. If these fields are modified in the same request, those values will be used instead of the link defaults. - Setting a link on a text range that overlaps with an existing link will also update the existing link to point to the new URL. - Links are not settable on newline characters. As a result, setting a link on a text range that crosses a paragraph boundary, such as `"ABC\n123"`, will separate the newline character(s) into their own text runs. The link will be applied separately to the runs before and after the newline. - Removing a link will update the text style of the range to match the style of the preceding text (or the default text styles if the preceding text is another link) unless different styles are being set in the same request. |
| `baselineOffset` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.BaselineOffset`)`` The text's vertical offset from its normal position. Text with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically rendered in a smaller font size, computed based on the `fontSize` field. The `fontSize` itself is not affected by changes in this field. |
| `smallCaps` | `boolean` Whether or not the text is in small capital letters. |
| `strikethrough` | `boolean` Whether or not the text is struck through. |
| `underline` | `boolean` Whether or not the text is underlined. |
| `weightedFontFamily` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.WeightedFontFamily`)`` The font family and rendered weight of the text. This field is an extension of `fontFamily` meant to support explicit font weights without breaking backwards compatibility. As such, when reading the style of a range of text, the value of `weightedFontFamily#fontFamily` will always be equal to that of `fontFamily`. However, when writing, if both fields are included in the field mask (either explicitly or through the wildcard `"*"`), their values are reconciled as follows: - If `fontFamily` is set and `weightedFontFamily` is not, the value of `fontFamily` is applied with weight `400` ("normal"). - If both fields are set, the value of `fontFamily` must match that of `weightedFontFamily#fontFamily`. If so, the font family and weight of `weightedFontFamily` is applied. Otherwise, a 400 bad request error is returned. - If `weightedFontFamily` is set and `fontFamily` is not, the font family and weight of `weightedFontFamily` is applied. - If neither field is set, the font family and weight of the text inherit from the parent. Note that these properties cannot inherit separately from each other. If an update request specifies values for both `weightedFontFamily` and `bold`, the `weightedFontFamily` is applied first, then `bold`. If `weightedFontFamily#weight` is not set, it defaults to `400`. If `weightedFontFamily` is set, then `weightedFontFamily#fontFamily` must also be set with a non-empty value. Otherwise, a 400 bad request error is returned. |

### OptionalColor


A color that can either be fully opaque or fully transparent.

| JSON representation |
|---|
| ``` { "opaqueColor": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.OpaqueColor`) } } ``` |

| Fields ||
|---|---|
| `opaqueColor` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.OpaqueColor`)`` If set, this will be used as an opaque color. If unset, this represents a transparent color. |

### BaselineOffset


The ways in which text can be vertically offset from its normal position.

| Enums ||
|---|---|
| `BASELINE_OFFSET_UNSPECIFIED` | The text's baseline offset is inherited from the parent. |
| `NONE` | The text is not vertically offset. |
| `SUPERSCRIPT` | The text is vertically offset upwards (superscript). |
| `SUBSCRIPT` | The text is vertically offset downwards (subscript). |

### WeightedFontFamily


Represents a font family and weight used to style a TextRun.

| JSON representation |
|---|
| ``` { "fontFamily": string, "weight": integer } ``` |

| Fields ||
|---|---|
| `fontFamily` | `string` The font family of the text. The font family can be any font from the Font menu in Slides or from [Google Fonts](https://fonts.google.com/). If the font name is unrecognized, the text is rendered in `Arial`. |
| `weight` | `integer` The rendered weight of the text. This field can have any value that is a multiple of `100` between `100` and `900`, inclusive. This range corresponds to the numerical values described in the CSS 2.1 Specification, [section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with non-numerical values disallowed. Weights greater than or equal to `700` are considered bold, and weights less than `700` are not bold. The default value is `400` ("normal"). |

### TextRun


A TextElement kind that represents a run of text that all has the same styling.

| JSON representation |
|---|
| ``` { "content": string, "style": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle`) } } ``` |

| Fields ||
|---|---|
| `content` | `string` The text of this run. |
| `style` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle`)`` The styling applied to this run. |

### AutoText


A TextElement kind that represents auto text.

| JSON representation |
|---|
| ``` { "type": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.Type_1`), "content": string, "style": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle`) } } ``` |

| Fields ||
|---|---|
| `type` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.Type_1`)`` The type of this auto text. |
| `content` | `string` The rendered content of this auto text, if available. |
| `style` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle`)`` The styling applied to this auto text. |

### Type


The types of auto text

| Enums ||
|---|---|
| `TYPE_UNSPECIFIED` | An unspecified autotext type. |
| `SLIDE_NUMBER` | Type for autotext that represents the current slide number. |

### List


A List describes the look and feel of bullets belonging to paragraphs associated with a list. A paragraph that is part of a list has an implicit reference to that list's ID.

| JSON representation |
|---|
| ``` { "listId": string, "nestingLevel": { integer: { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.NestingLevel`) }, ... } } ``` |

| Fields ||
|---|---|
| `listId` | `string` The ID of the list. |
| `nestingLevel` | ``map (key: integer, value: object ( `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.NestingLevel`))`` A map of nesting levels to the properties of bullets at the associated level. A list has at most nine levels of nesting, so the possible values for the keys of this map are 0 through 8, inclusive. |

### NestingLevel


Contains properties describing the look and feel of a list bullet at a given level of nesting.

| JSON representation |
|---|
| ``` { "bulletStyle": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle`) } } ``` |

| Fields ||
|---|---|
| `bulletStyle` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle`)`` The style of a bullet at this level of nesting. |