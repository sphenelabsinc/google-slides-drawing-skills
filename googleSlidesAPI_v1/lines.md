# Lines

### Line


A
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.PageElement`
kind representing a non-connector line, straight connector, curved connector, or bent connector.

| JSON representation |
|---|
| ``` { "lineProperties": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.LineProperties`) }, "lineType": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.Type_4`), "lineCategory": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.LineCategory`) } ``` |

| Fields ||
|---|---|
| `lineProperties` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.LineProperties`)`` The properties of the line. |
| `lineType` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.Type_4`)`` The type of the line. |
| `lineCategory` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.LineCategory`)`` The category of the line. It matches the `category` specified in `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/request#CreateLineRequest`, and can be updated with `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/request#UpdateLineCategoryRequest`. |

### LineProperties


The properties of the
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.Line`.


When unset, these fields default to values that match the appearance of new lines created in the Slides editor.

| JSON representation |
|---|
| ``` { "lineFill": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.LineFill`) }, "weight": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "dashStyle": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.DashStyle`), "startArrow": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.ArrowStyle`), "endArrow": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.ArrowStyle`), "link": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Link`) }, "startConnection": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.LineConnection`) }, "endConnection": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.LineConnection`) } } ``` |

| Fields ||
|---|---|
| `lineFill` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.LineFill`)`` The fill of the line. The default line fill matches the defaults for new lines created in the Slides editor. |
| `weight` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` The thickness of the line. |
| `dashStyle` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.DashStyle`)`` The dash style of the line. |
| `startArrow` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.ArrowStyle`)`` The style of the arrow at the beginning of the line. |
| `endArrow` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.ArrowStyle`)`` The style of the arrow at the end of the line. |
| `link` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Link`)`` The hyperlink destination of the line. If unset, there is no link. |
| `startConnection` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.LineConnection`)`` The connection at the beginning of the line. If unset, there is no connection. Only lines with a `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.Type_4` indicating it is a "connector" can have a `startConnection`. |
| `endConnection` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.LineConnection`)`` The connection at the end of the line. If unset, there is no connection. Only lines with a `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.Type_4` indicating it is a "connector" can have an `endConnection`. |

### LineFill


The fill of the line.

| JSON representation |
|---|
| ``` { "solidFill": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.SolidFill`) } } ``` |

| Fields ||
|---|---|
| Union field `kind`. The kind of line fill. `kind` can be only one of the following: ||
| `solidFill` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.SolidFill`)`` Solid color fill. |

### ArrowStyle


The kinds of start and end forms with which linear geometry can be rendered. Some values are based on the "ST_LineEndType" simple type described in section 20.1.10.33 of "Office Open XML File Formats - Fundamentals and Markup Language Reference", part 1 of
[ECMA-376 5th edition](https://ecma-international.org/publications-and-standards/standards/ecma-376/).

| Enums ||
|---|---|
| `ARROW_STYLE_UNSPECIFIED` | An unspecified arrow style. |
| `NONE` | No arrow. |
| `STEALTH_ARROW` | Arrow with notched back. Corresponds to ECMA-376 ST_LineEndType value 'stealth'. |
| `FILL_ARROW` | Filled arrow. Corresponds to ECMA-376 ST_LineEndType value 'triangle'. |
| `FILL_CIRCLE` | Filled circle. Corresponds to ECMA-376 ST_LineEndType value 'oval'. |
| `FILL_SQUARE` | Filled square. |
| `FILL_DIAMOND` | Filled diamond. Corresponds to ECMA-376 ST_LineEndType value 'diamond'. |
| `OPEN_ARROW` | Hollow arrow. |
| `OPEN_CIRCLE` | Hollow circle. |
| `OPEN_SQUARE` | Hollow square. |
| `OPEN_DIAMOND` | Hollow diamond. |

### LineConnection


The properties for one end of a
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.Line`
connection.

| JSON representation |
|---|
| ``` { "connectedObjectId": string, "connectionSiteIndex": integer } ``` |

| Fields ||
|---|---|
| `connectedObjectId` | `string` The object ID of the connected page element. Some page elements, such as `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.Group`, `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.Table`, and `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.Line` do not have connection sites and therefore cannot be connected to a connector line. |
| `connectionSiteIndex` | `integer` The index of the connection site on the connected page element. In most cases, it corresponds to the predefined connection site index from the ECMA-376 standard. More information on those connection sites can be found in both the description of the "cxn" attribute in section 20.1.9.9 and "Annex H. Example Predefined DrawingML Shape and Text Geometries" of "Office Open XML File Formats - Fundamentals and Markup Language Reference", part 1 of [ECMA-376 5th edition](https://ecma-international.org/publications-and-standards/standards/ecma-376/). The position of each connection site can also be viewed from Slides editor. |

### Type


The line types.


Many of these shapes correspond to predefined shapes from the ECMA-376 standard. For more information, see the description of the "ST_ShapeType" simple type in section 20.1.10.56 of "Office Open XML File Formats - Fundamentals and Markup Language Reference", part 1 of
[ECMA-376 5th edition](https://ecma-international.org/publications-and-standards/standards/ecma-376/).

| Enums ||
|---|---|
| `TYPE_UNSPECIFIED` | An unspecified line type. |
| `STRAIGHT_CONNECTOR_1` | Straight connector 1 form. Corresponds to ECMA-376 ST_ShapeType 'straightConnector1'. |
| `BENT_CONNECTOR_2` | Bent connector 2 form. Corresponds to ECMA-376 ST_ShapeType 'bentConnector2'. |
| `BENT_CONNECTOR_3` | Bent connector 3 form. Corresponds to ECMA-376 ST_ShapeType 'bentConnector3'. |
| `BENT_CONNECTOR_4` | Bent connector 4 form. Corresponds to ECMA-376 ST_ShapeType 'bentConnector4'. |
| `BENT_CONNECTOR_5` | Bent connector 5 form. Corresponds to ECMA-376 ST_ShapeType 'bentConnector5'. |
| `CURVED_CONNECTOR_2` | Curved connector 2 form. Corresponds to ECMA-376 ST_ShapeType 'curvedConnector2'. |
| `CURVED_CONNECTOR_3` | Curved connector 3 form. Corresponds to ECMA-376 ST_ShapeType 'curvedConnector3'. |
| `CURVED_CONNECTOR_4` | Curved connector 4 form. Corresponds to ECMA-376 ST_ShapeType 'curvedConnector4'. |
| `CURVED_CONNECTOR_5` | Curved connector 5 form. Corresponds to ECMA-376 ST_ShapeType 'curvedConnector5'. |
| `STRAIGHT_LINE` | Straight line. Corresponds to ECMA-376 ST_ShapeType 'line'. This line type is not a connector. |

### LineCategory


The category of a
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/lines#Page.Line`.

| Enums ||
|---|---|
| `LINE_CATEGORY_UNSPECIFIED` | Unspecified line category. |
| `STRAIGHT` | Straight connectors, including straight connector 1. |
| `BENT` | Bent connectors, including bent connector 2 to 5. |
| `CURVED` | Curved connectors, including curved connector 2 to 5. |