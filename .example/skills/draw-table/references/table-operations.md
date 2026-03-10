# Table Operations Reference

## createTable

```json
{
  "type": "table",
  "id": "tbl1",
  "x": 60, "y": 100, "w": 600, "h": 240,
  "rows": 4,
  "columns": 3
}
```

- Max 20 rows or columns in a single table
- Table auto-distributes column widths evenly across `w`
- Table auto-distributes row heights evenly across `h`
- If no size provided the API auto-sizes, but always provide `x/y/w/h`

## insertText (into table cell)

```json
{
  "type": "insert_text",
  "id": "tbl1",
  "text": "Cell content",
  "cell_row": 0,
  "cell_col": 0,
  "insertion_index": 0
}
```

- `insertion_index` defaults to 0 (beginning)
- Use `\n` for line breaks within a cell
- Call once per cell — subsequent inserts append

## updateTableCellProperties

```json
{
  "type": "update_table_cell",
  "id": "tbl1",
  "cell_row": 0,
  "cell_col": 0,
  "fill_color": "#4285F4",
  "row_span": 1,
  "col_span": 1
}
```

- `fill_color` supports all color formats (see `colors` skill)
- `row_span`/`col_span` default to 1 (single cell)
- To style a range, send one operation per cell in the range

## mergeTableCells

```json
{
  "type": "merge_table_cells",
  "id": "tbl1",
  "row": 0,
  "col": 0,
  "row_span": 1,
  "col_span": 3
}
```

- Merges the range `(row, col)` spanning `row_span × col_span`
- Text from merged cells is combined
- Cannot merge cells that span across already-merged regions

## Patterns

### Header row (full-width merge + fill)
```json
[
  { "type": "merge_table_cells", "id": "tbl1", "row": 0, "col": 0, "row_span": 1, "col_span": 3 },
  { "type": "insert_text", "id": "tbl1", "text": "Section Title", "cell_row": 0, "cell_col": 0 },
  { "type": "update_table_cell", "id": "tbl1", "cell_row": 0, "cell_col": 0, "fill_color": "#1A237E" }
]
```

### Alternating row stripes
Apply `fill_color: "#F5F5F5"` to even rows (row indices 2, 4, 6...) and no fill to odd rows.

### Column headers (frozen style)
Apply `fill_color: "#E3F2FD"` to column header row (row 0) and bold text via separate `updateTextStyle` if needed.
