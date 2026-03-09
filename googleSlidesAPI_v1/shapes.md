# Shapes

### Shape


A
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.PageElement`
kind representing a generic shape that doesn't have a more specific classification. For more information, see
[Size and position page elements](https://developers.google.com/workspace/slides/api/guides/transform).

| JSON representation |
|---|
| ``` { "shapeType": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Type`), "text": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextContent`) }, "shapeProperties": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.ShapeProperties`) }, "placeholder": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Placeholder`) } } ``` |

| Fields ||
|---|---|
| `shapeType` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Type`)`` The type of the shape. |
| `text` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextContent`)`` The text content of the shape. |
| `shapeProperties` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.ShapeProperties`)`` The properties of the shape. |
| `placeholder` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Placeholder`)`` Placeholders are page elements that inherit from corresponding placeholders on layouts and masters. If set, the shape is a placeholder shape and any inherited properties can be resolved by looking at the parent placeholder identified by the `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Placeholder.FIELDS.parent_object_id` field. |

### Type


The shape types.


Many of these shapes correspond to predefined shapes from the ECMA-376 standard. For more information, see the description of the "ST_ShapeType" simple type in section 20.1.10.56 of "Office Open XML File Formats - Fundamentals and Markup Language Reference", part 1 of
[ECMA-376 5th edition](https://ecma-international.org/publications-and-standards/standards/ecma-376/).

| Enums ||
|---|---|
| `TYPE_UNSPECIFIED` | Default value. This value is unused. |
| `TEXT_BOX` | Text box shape. |
| `RECTANGLE` | Rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'rect' |
| `ROUND_RECTANGLE` | Round corner rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'roundRect' |
| `ELLIPSE` | Ellipse shape. Corresponds to ECMA-376 ST_ShapeType 'ellipse' |
| `ARC` | Curved arc shape. Corresponds to ECMA-376 ST_ShapeType 'arc' |
| `BENT_ARROW` | Bent arrow shape. Corresponds to ECMA-376 ST_ShapeType 'bentArrow' |
| `BENT_UP_ARROW` | Bent up arrow shape. Corresponds to ECMA-376 ST_ShapeType 'bentUpArrow' |
| `BEVEL` | Bevel shape. Corresponds to ECMA-376 ST_ShapeType 'bevel' |
| `BLOCK_ARC` | Block arc shape. Corresponds to ECMA-376 ST_ShapeType 'blockArc' |
| `BRACE_PAIR` | Brace pair shape. Corresponds to ECMA-376 ST_ShapeType 'bracePair' |
| `BRACKET_PAIR` | Bracket pair shape. Corresponds to ECMA-376 ST_ShapeType 'bracketPair' |
| `CAN` | Can shape. Corresponds to ECMA-376 ST_ShapeType 'can' |
| `CHEVRON` | Chevron shape. Corresponds to ECMA-376 ST_ShapeType 'chevron' |
| `CHORD` | Chord shape. Corresponds to ECMA-376 ST_ShapeType 'chord' |
| `CLOUD` | Cloud shape. Corresponds to ECMA-376 ST_ShapeType 'cloud' |
| `CORNER` | Corner shape. Corresponds to ECMA-376 ST_ShapeType 'corner' |
| `CUBE` | Cube shape. Corresponds to ECMA-376 ST_ShapeType 'cube' |
| `CURVED_DOWN_ARROW` | Curved down arrow shape. Corresponds to ECMA-376 ST_ShapeType 'curvedDownArrow' |
| `CURVED_LEFT_ARROW` | Curved left arrow shape. Corresponds to ECMA-376 ST_ShapeType 'curvedLeftArrow' |
| `CURVED_RIGHT_ARROW` | Curved right arrow shape. Corresponds to ECMA-376 ST_ShapeType 'curvedRightArrow' |
| `CURVED_UP_ARROW` | Curved up arrow shape. Corresponds to ECMA-376 ST_ShapeType 'curvedUpArrow' |
| `DECAGON` | Decagon shape. Corresponds to ECMA-376 ST_ShapeType 'decagon' |
| `DIAGONAL_STRIPE` | Diagonal stripe shape. Corresponds to ECMA-376 ST_ShapeType 'diagStripe' |
| `DIAMOND` | Diamond shape. Corresponds to ECMA-376 ST_ShapeType 'diamond' |
| `DODECAGON` | Dodecagon shape. Corresponds to ECMA-376 ST_ShapeType 'dodecagon' |
| `DONUT` | Donut shape. Corresponds to ECMA-376 ST_ShapeType 'donut' |
| `DOUBLE_WAVE` | Double wave shape. Corresponds to ECMA-376 ST_ShapeType 'doubleWave' |
| `DOWN_ARROW` | Down arrow shape. Corresponds to ECMA-376 ST_ShapeType 'downArrow' |
| `DOWN_ARROW_CALLOUT` | Callout down arrow shape. Corresponds to ECMA-376 ST_ShapeType 'downArrowCallout' |
| `FOLDED_CORNER` | Folded corner shape. Corresponds to ECMA-376 ST_ShapeType 'foldedCorner' |
| `FRAME` | Frame shape. Corresponds to ECMA-376 ST_ShapeType 'frame' |
| `HALF_FRAME` | Half frame shape. Corresponds to ECMA-376 ST_ShapeType 'halfFrame' |
| `HEART` | Heart shape. Corresponds to ECMA-376 ST_ShapeType 'heart' |
| `HEPTAGON` | Heptagon shape. Corresponds to ECMA-376 ST_ShapeType 'heptagon' |
| `HEXAGON` | Hexagon shape. Corresponds to ECMA-376 ST_ShapeType 'hexagon' |
| `HOME_PLATE` | Home plate shape. Corresponds to ECMA-376 ST_ShapeType 'homePlate' |
| `HORIZONTAL_SCROLL` | Horizontal scroll shape. Corresponds to ECMA-376 ST_ShapeType 'horizontalScroll' |
| `IRREGULAR_SEAL_1` | Irregular seal 1 shape. Corresponds to ECMA-376 ST_ShapeType 'irregularSeal1' |
| `IRREGULAR_SEAL_2` | Irregular seal 2 shape. Corresponds to ECMA-376 ST_ShapeType 'irregularSeal2' |
| `LEFT_ARROW` | Left arrow shape. Corresponds to ECMA-376 ST_ShapeType 'leftArrow' |
| `LEFT_ARROW_CALLOUT` | Callout left arrow shape. Corresponds to ECMA-376 ST_ShapeType 'leftArrowCallout' |
| `LEFT_BRACE` | Left brace shape. Corresponds to ECMA-376 ST_ShapeType 'leftBrace' |
| `LEFT_BRACKET` | Left bracket shape. Corresponds to ECMA-376 ST_ShapeType 'leftBracket' |
| `LEFT_RIGHT_ARROW` | Left right arrow shape. Corresponds to ECMA-376 ST_ShapeType 'leftRightArrow' |
| `LEFT_RIGHT_ARROW_CALLOUT` | Callout left right arrow shape. Corresponds to ECMA-376 ST_ShapeType 'leftRightArrowCallout' |
| `LEFT_RIGHT_UP_ARROW` | Left right up arrow shape. Corresponds to ECMA-376 ST_ShapeType 'leftRightUpArrow' |
| `LEFT_UP_ARROW` | Left up arrow shape. Corresponds to ECMA-376 ST_ShapeType 'leftUpArrow' |
| `LIGHTNING_BOLT` | Lightning bolt shape. Corresponds to ECMA-376 ST_ShapeType 'lightningBolt' |
| `MATH_DIVIDE` | Divide math shape. Corresponds to ECMA-376 ST_ShapeType 'mathDivide' |
| `MATH_EQUAL` | Equal math shape. Corresponds to ECMA-376 ST_ShapeType 'mathEqual' |
| `MATH_MINUS` | Minus math shape. Corresponds to ECMA-376 ST_ShapeType 'mathMinus' |
| `MATH_MULTIPLY` | Multiply math shape. Corresponds to ECMA-376 ST_ShapeType 'mathMultiply' |
| `MATH_NOT_EQUAL` | Not equal math shape. Corresponds to ECMA-376 ST_ShapeType 'mathNotEqual' |
| `MATH_PLUS` | Plus math shape. Corresponds to ECMA-376 ST_ShapeType 'mathPlus' |
| `MOON` | Moon shape. Corresponds to ECMA-376 ST_ShapeType 'moon' |
| `NO_SMOKING` | No smoking shape. Corresponds to ECMA-376 ST_ShapeType 'noSmoking' |
| `NOTCHED_RIGHT_ARROW` | Notched right arrow shape. Corresponds to ECMA-376 ST_ShapeType 'notchedRightArrow' |
| `OCTAGON` | Octagon shape. Corresponds to ECMA-376 ST_ShapeType 'octagon' |
| `PARALLELOGRAM` | Parallelogram shape. Corresponds to ECMA-376 ST_ShapeType 'parallelogram' |
| `PENTAGON` | Pentagon shape. Corresponds to ECMA-376 ST_ShapeType 'pentagon' |
| `PIE` | Pie shape. Corresponds to ECMA-376 ST_ShapeType 'pie' |
| `PLAQUE` | Plaque shape. Corresponds to ECMA-376 ST_ShapeType 'plaque' |
| `PLUS` | Plus shape. Corresponds to ECMA-376 ST_ShapeType 'plus' |
| `QUAD_ARROW` | Quad-arrow shape. Corresponds to ECMA-376 ST_ShapeType 'quadArrow' |
| `QUAD_ARROW_CALLOUT` | Callout quad-arrow shape. Corresponds to ECMA-376 ST_ShapeType 'quadArrowCallout' |
| `RIBBON` | Ribbon shape. Corresponds to ECMA-376 ST_ShapeType 'ribbon' |
| `RIBBON_2` | Ribbon 2 shape. Corresponds to ECMA-376 ST_ShapeType 'ribbon2' |
| `RIGHT_ARROW` | Right arrow shape. Corresponds to ECMA-376 ST_ShapeType 'rightArrow' |
| `RIGHT_ARROW_CALLOUT` | Callout right arrow shape. Corresponds to ECMA-376 ST_ShapeType 'rightArrowCallout' |
| `RIGHT_BRACE` | Right brace shape. Corresponds to ECMA-376 ST_ShapeType 'rightBrace' |
| `RIGHT_BRACKET` | Right bracket shape. Corresponds to ECMA-376 ST_ShapeType 'rightBracket' |
| `ROUND_1_RECTANGLE` | One round corner rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'round1Rect' |
| `ROUND_2_DIAGONAL_RECTANGLE` | Two diagonal round corner rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'round2DiagRect' |
| `ROUND_2_SAME_RECTANGLE` | Two same-side round corner rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'round2SameRect' |
| `RIGHT_TRIANGLE` | Right triangle shape. Corresponds to ECMA-376 ST_ShapeType 'rtTriangle' |
| `SMILEY_FACE` | Smiley face shape. Corresponds to ECMA-376 ST_ShapeType 'smileyFace' |
| `SNIP_1_RECTANGLE` | One snip corner rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'snip1Rect' |
| `SNIP_2_DIAGONAL_RECTANGLE` | Two diagonal snip corner rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'snip2DiagRect' |
| `SNIP_2_SAME_RECTANGLE` | Two same-side snip corner rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'snip2SameRect' |
| `SNIP_ROUND_RECTANGLE` | One snip one round corner rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'snipRoundRect' |
| `STAR_10` | Ten pointed star shape. Corresponds to ECMA-376 ST_ShapeType 'star10' |
| `STAR_12` | Twelve pointed star shape. Corresponds to ECMA-376 ST_ShapeType 'star12' |
| `STAR_16` | Sixteen pointed star shape. Corresponds to ECMA-376 ST_ShapeType 'star16' |
| `STAR_24` | Twenty four pointed star shape. Corresponds to ECMA-376 ST_ShapeType 'star24' |
| `STAR_32` | Thirty two pointed star shape. Corresponds to ECMA-376 ST_ShapeType 'star32' |
| `STAR_4` | Four pointed star shape. Corresponds to ECMA-376 ST_ShapeType 'star4' |
| `STAR_5` | Five pointed star shape. Corresponds to ECMA-376 ST_ShapeType 'star5' |
| `STAR_6` | Six pointed star shape. Corresponds to ECMA-376 ST_ShapeType 'star6' |
| `STAR_7` | Seven pointed star shape. Corresponds to ECMA-376 ST_ShapeType 'star7' |
| `STAR_8` | Eight pointed star shape. Corresponds to ECMA-376 ST_ShapeType 'star8' |
| `STRIPED_RIGHT_ARROW` | Striped right arrow shape. Corresponds to ECMA-376 ST_ShapeType 'stripedRightArrow' |
| `SUN` | Sun shape. Corresponds to ECMA-376 ST_ShapeType 'sun' |
| `TRAPEZOID` | Trapezoid shape. Corresponds to ECMA-376 ST_ShapeType 'trapezoid' |
| `TRIANGLE` | Triangle shape. Corresponds to ECMA-376 ST_ShapeType 'triangle' |
| `UP_ARROW` | Up arrow shape. Corresponds to ECMA-376 ST_ShapeType 'upArrow' |
| `UP_ARROW_CALLOUT` | Callout up arrow shape. Corresponds to ECMA-376 ST_ShapeType 'upArrowCallout' |
| `UP_DOWN_ARROW` | Up down arrow shape. Corresponds to ECMA-376 ST_ShapeType 'upDownArrow' |
| `UTURN_ARROW` | U-turn arrow shape. Corresponds to ECMA-376 ST_ShapeType 'uturnArrow' |
| `VERTICAL_SCROLL` | Vertical scroll shape. Corresponds to ECMA-376 ST_ShapeType 'verticalScroll' |
| `WAVE` | Wave shape. Corresponds to ECMA-376 ST_ShapeType 'wave' |
| `WEDGE_ELLIPSE_CALLOUT` | Callout wedge ellipse shape. Corresponds to ECMA-376 ST_ShapeType 'wedgeEllipseCallout' |
| `WEDGE_RECTANGLE_CALLOUT` | Callout wedge rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'wedgeRectCallout' |
| `WEDGE_ROUND_RECTANGLE_CALLOUT` | Callout wedge round rectangle shape. Corresponds to ECMA-376 ST_ShapeType 'wedgeRoundRectCallout' |
| `FLOW_CHART_ALTERNATE_PROCESS` | Alternate process flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartAlternateProcess' |
| `FLOW_CHART_COLLATE` | Collate flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartCollate' |
| `FLOW_CHART_CONNECTOR` | Connector flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartConnector' |
| `FLOW_CHART_DECISION` | Decision flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartDecision' |
| `FLOW_CHART_DELAY` | Delay flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartDelay' |
| `FLOW_CHART_DISPLAY` | Display flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartDisplay' |
| `FLOW_CHART_DOCUMENT` | Document flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartDocument' |
| `FLOW_CHART_EXTRACT` | Extract flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartExtract' |
| `FLOW_CHART_INPUT_OUTPUT` | Input output flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartInputOutput' |
| `FLOW_CHART_INTERNAL_STORAGE` | Internal storage flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartInternalStorage' |
| `FLOW_CHART_MAGNETIC_DISK` | Magnetic disk flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartMagneticDisk' |
| `FLOW_CHART_MAGNETIC_DRUM` | Magnetic drum flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartMagneticDrum' |
| `FLOW_CHART_MAGNETIC_TAPE` | Magnetic tape flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartMagneticTape' |
| `FLOW_CHART_MANUAL_INPUT` | Manual input flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartManualInput' |
| `FLOW_CHART_MANUAL_OPERATION` | Manual operation flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartManualOperation' |
| `FLOW_CHART_MERGE` | Merge flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartMerge' |
| `FLOW_CHART_MULTIDOCUMENT` | Multi-document flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartMultidocument' |
| `FLOW_CHART_OFFLINE_STORAGE` | Offline storage flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartOfflineStorage' |
| `FLOW_CHART_OFFPAGE_CONNECTOR` | Off-page connector flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartOffpageConnector' |
| `FLOW_CHART_ONLINE_STORAGE` | Online storage flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartOnlineStorage' |
| `FLOW_CHART_OR` | Or flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartOr' |
| `FLOW_CHART_PREDEFINED_PROCESS` | Predefined process flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartPredefinedProcess' |
| `FLOW_CHART_PREPARATION` | Preparation flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartPreparation' |
| `FLOW_CHART_PROCESS` | Process flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartProcess' |
| `FLOW_CHART_PUNCHED_CARD` | Punched card flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartPunchedCard' |
| `FLOW_CHART_PUNCHED_TAPE` | Punched tape flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartPunchedTape' |
| `FLOW_CHART_SORT` | Sort flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartSort' |
| `FLOW_CHART_SUMMING_JUNCTION` | Summing junction flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartSummingJunction' |
| `FLOW_CHART_TERMINATOR` | Terminator flow shape. Corresponds to ECMA-376 ST_ShapeType 'flowChartTerminator' |
| `ARROW_EAST` | East arrow shape. |
| `ARROW_NORTH_EAST` | Northeast arrow shape. |
| `ARROW_NORTH` | North arrow shape. |
| `SPEECH` | Speech shape. |
| `STARBURST` | Star burst shape. |
| `TEARDROP` | Teardrop shape. Corresponds to ECMA-376 ST_ShapeType 'teardrop' |
| `ELLIPSE_RIBBON` | Ellipse ribbon shape. Corresponds to ECMA-376 ST_ShapeType 'ellipseRibbon' |
| `ELLIPSE_RIBBON_2` | Ellipse ribbon 2 shape. Corresponds to ECMA-376 ST_ShapeType 'ellipseRibbon2' |
| `CLOUD_CALLOUT` | Callout cloud shape. Corresponds to ECMA-376 ST_ShapeType 'cloudCallout' |
| `CUSTOM` | Custom shape. |

### ShapeProperties


The properties of a
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Shape`.


If the shape is a placeholder shape as determined by the
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Placeholder`
field, then these properties may be inherited from a parent placeholder shape. Determining the rendered value of the property depends on the corresponding
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.PropertyState`
field value.


Any text autofit settings on the shape are automatically deactivated by requests that can impact how text fits in the shape.

| JSON representation |
|---|
| ``` { "shapeBackgroundFill": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.ShapeBackgroundFill`) }, "outline": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Outline`) }, "shadow": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Shadow`) }, "link": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Link`) }, "contentAlignment": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ContentAlignment`), "autofit": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Autofit`) } } ``` |

| Fields ||
|---|---|
| `shapeBackgroundFill` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.ShapeBackgroundFill`)`` The background fill of the shape. If unset, the background fill is inherited from a parent placeholder if it exists. If the shape has no parent, then the default background fill depends on the shape type, matching the defaults for new shapes created in the Slides editor. |
| `outline` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Outline`)`` The outline of the shape. If unset, the outline is inherited from a parent placeholder if it exists. If the shape has no parent, then the default outline depends on the shape type, matching the defaults for new shapes created in the Slides editor. |
| `shadow` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Shadow`)`` The shadow properties of the shape. If unset, the shadow is inherited from a parent placeholder if it exists. If the shape has no parent, then the default shadow matches the defaults for new shapes created in the Slides editor. This property is read-only. |
| `link` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Link`)`` The hyperlink destination of the shape. If unset, there is no link. Links are not inherited from parent placeholders. |
| `contentAlignment` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ContentAlignment`)`` The alignment of the content in the shape. If `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ContentAlignment`, the alignment is inherited from a parent placeholder if it exists. If the shape has no parent, the default alignment matches the alignment for new shapes created in the Slides editor. |
| `autofit` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Autofit`)`` The autofit properties of the shape. This property is only set for shapes that allow text. |

### ShapeBackgroundFill


The shape background fill.

| JSON representation |
|---|
| ``` { "propertyState": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.PropertyState`), "solidFill": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.SolidFill`) } } ``` |

| Fields ||
|---|---|
| `propertyState` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.PropertyState`)`` The background fill property state. Updating the fill on a shape will implicitly update this field to `RENDERED`, unless another value is specified in the same request. To have no fill on a shape, set this field to `NOT_RENDERED`. In this case, any other fill fields set in the same request will be ignored. |
| Union field `kind`. The kind of background fill. `kind` can be only one of the following: ||
| `solidFill` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.SolidFill`)`` Solid color fill. |

### Autofit


The autofit properties of a
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Shape`. This property is only set for shapes that allow text.

| JSON representation |
|---|
| ``` { "autofitType": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType`), "fontScale": number, "lineSpacingReduction": number } ``` |

| Fields ||
|---|---|
| `autofitType` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType`)`` The autofit type of the shape. If the autofit type is `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType`, the autofit type is inherited from a parent placeholder if it exists. The field is automatically set to `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType` if a request is made that might affect text fitting within its bounding text box. In this case, the `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Autofit.FIELDS.font_scale` is applied to the `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle.FIELDS.font_size` and the `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Autofit.FIELDS.line_spacing_reduction` is applied to the `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.ParagraphStyle.FIELDS.line_spacing`. Both properties are also reset to default values. |
| `fontScale` | `number` The font scale applied to the shape. For shapes with `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Autofit.FIELDS.autofit_type` `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType` or `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType`, this value is the default value of 1. For `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType`, this value multiplied by the `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextStyle.FIELDS.font_size` gives the font size that's rendered in the editor. This property is read-only. |
| `lineSpacingReduction` | `number` The line spacing reduction applied to the shape. For shapes with `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Autofit.FIELDS.autofit_type` `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType` or `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType`, this value is the default value of 0. For `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType`, this value subtracted from the `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.ParagraphStyle.FIELDS.line_spacing` gives the line spacing that's rendered in the editor. This property is read-only. |

### AutofitType


The autofit types of a
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Shape`.


Note that while all values are valid for read requests, only
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType`
and
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.AutofitType`
are valid for write requests.

| Enums ||
|---|---|
| `AUTOFIT_TYPE_UNSPECIFIED` | The autofit type is unspecified. |
| `NONE` | Do not autofit. |
| `TEXT_AUTOFIT` | Shrink text on overflow to fit the shape. |
| `SHAPE_AUTOFIT` | Resize the shape to fit the text. |