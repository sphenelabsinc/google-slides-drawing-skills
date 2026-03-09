# Tables

### Table


A
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.PageElement`
kind representing a table.

| JSON representation |
|---|
| ``` { "rows": integer, "columns": integer, "tableRows": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableRow`) } ], "tableColumns": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableColumnProperties`) } ], "horizontalBorderRows": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderRow`) } ], "verticalBorderRows": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderRow`) } ] } ``` |

| Fields ||
|---|---|
| `rows` | `integer` Number of rows in the table. |
| `columns` | `integer` Number of columns in the table. |
| `tableRows[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableRow`)`` Properties and contents of each row. Cells that span multiple rows are contained in only one of these rows and have a `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCell.FIELDS.row_span` greater than 1. |
| `tableColumns[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableColumnProperties`)`` Properties of each column. |
| `horizontalBorderRows[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderRow`)`` Properties of horizontal cell borders. A table's horizontal cell borders are represented as a grid. The grid has one more row than the number of rows in the table and the same number of columns as the table. For example, if the table is 3 x 3, its horizontal borders will be represented as a grid with 4 rows and 3 columns. |
| `verticalBorderRows[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderRow`)`` Properties of vertical cell borders. A table's vertical cell borders are represented as a grid. The grid has the same number of rows as the table and one more column than the number of columns in the table. For example, if the table is 3 x 3, its vertical borders will be represented as a grid with 3 rows and 4 columns. |

### TableRow


Properties and contents of each row in a table.

| JSON representation |
|---|
| ``` { "rowHeight": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "tableRowProperties": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableRowProperties`) }, "tableCells": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCell`) } ] } ``` |

| Fields ||
|---|---|
| `rowHeight` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` Height of a row. |
| `tableRowProperties` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableRowProperties`)`` Properties of the row. |
| `tableCells[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCell`)`` Properties and contents of each cell. Cells that span multiple columns are represented only once with a `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCell.FIELDS.column_span` greater than 1. As a result, the length of this collection does not always match the number of columns of the entire table. |

### TableRowProperties


Properties of each row in a table.

| JSON representation |
|---|
| ``` { "minRowHeight": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) } } ``` |

| Fields ||
|---|---|
| `minRowHeight` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` Minimum height of the row. The row will be rendered in the Slides editor at a height equal to or greater than this value in order to show all the text in the row's cell(s). |

### TableCell


Properties and contents of each table cell.

| JSON representation |
|---|
| ``` { "location": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCellLocation`) }, "rowSpan": integer, "columnSpan": integer, "text": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextContent`) }, "tableCellProperties": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCellProperties`) } } ``` |

| Fields ||
|---|---|
| `location` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCellLocation`)`` The location of the cell within the table. |
| `rowSpan` | `integer` Row span of the cell. |
| `columnSpan` | `integer` Column span of the cell. |
| `text` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text#Page.TextContent`)`` The text content of the cell. |
| `tableCellProperties` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCellProperties`)`` The properties of the table cell. |

### TableCellLocation


A location of a single table cell within a table.

| JSON representation |
|---|
| ``` { "rowIndex": integer, "columnIndex": integer } ``` |

| Fields ||
|---|---|
| `rowIndex` | `integer` The 0-based row index. |
| `columnIndex` | `integer` The 0-based column index. |

### TableCellProperties


The properties of the
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCell`.

| JSON representation |
|---|
| ``` { "tableCellBackgroundFill": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCellBackgroundFill`) }, "contentAlignment": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ContentAlignment`) } ``` |

| Fields ||
|---|---|
| `tableCellBackgroundFill` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCellBackgroundFill`)`` The background fill of the table cell. The default fill matches the fill for newly created table cells in the Slides editor. |
| `contentAlignment` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ContentAlignment`)`` The alignment of the content in the table cell. The default alignment matches the alignment for newly created table cells in the Slides editor. |

### TableCellBackgroundFill


The table cell background fill.

| JSON representation |
|---|
| ``` { "propertyState": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.PropertyState`), "solidFill": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.SolidFill`) } } ``` |

| Fields ||
|---|---|
| `propertyState` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.PropertyState`)`` The background fill property state. Updating the fill on a table cell will implicitly update this field to `RENDERED`, unless another value is specified in the same request. To have no fill on a table cell, set this field to `NOT_RENDERED`. In this case, any other fill fields set in the same request will be ignored. |
| Union field `kind`. The kind of background fill. `kind` can be only one of the following: ||
| `solidFill` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.SolidFill`)`` Solid color fill. |

### TableColumnProperties


Properties of each column in a table.

| JSON representation |
|---|
| ``` { "columnWidth": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) } } ``` |

| Fields ||
|---|---|
| `columnWidth` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` Width of a column. |

### TableBorderRow


Contents of each border row in a table.

| JSON representation |
|---|
| ``` { "tableBorderCells": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderCell`) } ] } ``` |

| Fields ||
|---|---|
| `tableBorderCells[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderCell`)`` Properties of each border cell. When a border's adjacent table cells are merged, it is not included in the response. |

### TableBorderCell


The properties of each border cell.

| JSON representation |
|---|
| ``` { "location": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCellLocation`) }, "tableBorderProperties": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderProperties`) } } ``` |

| Fields ||
|---|---|
| `location` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableCellLocation`)`` The location of the border within the border table. |
| `tableBorderProperties` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderProperties`)`` The border properties. |

### TableBorderProperties


The border styling properties of the
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderCell`.

| JSON representation |
|---|
| ``` { "tableBorderFill": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderFill`) }, "weight": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "dashStyle": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.DashStyle`) } ``` |

| Fields ||
|---|---|
| `tableBorderFill` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/tables#Page.TableBorderFill`)`` The fill of the table border. |
| `weight` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` The thickness of the border. |
| `dashStyle` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.DashStyle`)`` The dash style of the border. |

### TableBorderFill


The fill of the border.

| JSON representation |
|---|
| ``` { "solidFill": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.SolidFill`) } } ``` |

| Fields ||
|---|---|
| Union field `kind`. The kind of fill. `kind` can be only one of the following: ||
| `solidFill` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.SolidFill`)`` Solid fill. |