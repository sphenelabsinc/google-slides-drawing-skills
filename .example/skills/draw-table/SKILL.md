---
name: draw-table
description: This skill should be used when the user asks to "draw a table", "add a table", "create a data table", "add rows and columns", "insert a table", "add a comparison table", or needs to compose table operations for a Google Slides batch-draw command.
version: 0.1.0
---

# draw-table

Compose table operations for `batch-draw`. Tables require a specific **create → populate → style** order.

## Workflow

1. `table` — create the table (sets position, size, row/column count)
2. `insert_text` — populate each cell with text
3. `update_table_cell` — apply background fills (optional)
4. `merge_table_cells` — merge cell ranges (optional)

All four operation types go in the same `batch_draw` `operations` array.

## 1. Create Table

```json
{
  "type": "table",
  "id": "tbl1",
  "x": 60,
  "y": 100,
  "w": 600,
  "h": 240,
  "rows": 4,
  "columns": 3
}
```

## 2. Insert Text into a Cell

```json
{
  "type": "insert_text",
  "id": "tbl1",
  "text": "Header A",
  "cell_row": 0,
  "cell_col": 0
}
```

## 3. Style a Cell

```json
{
  "type": "update_table_cell",
  "id": "tbl1",
  "cell_row": 0,
  "cell_col": 0,
  "fill_color": "#1A73E8"
}
```

## 4. Merge Cells

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

## Full Example — 3-column Table

```json
[
  { "type": "table", "id": "tbl1", "x": 60, "y": 80, "w": 600, "h": 220, "rows": 3, "columns": 3 },

  { "type": "insert_text", "id": "tbl1", "text": "Name",  "cell_row": 0, "cell_col": 0 },
  { "type": "insert_text", "id": "tbl1", "text": "Role",  "cell_row": 0, "cell_col": 1 },
  { "type": "insert_text", "id": "tbl1", "text": "Team",  "cell_row": 0, "cell_col": 2 },

  { "type": "insert_text", "id": "tbl1", "text": "Alice", "cell_row": 1, "cell_col": 0 },
  { "type": "insert_text", "id": "tbl1", "text": "Engineer", "cell_row": 1, "cell_col": 1 },
  { "type": "insert_text", "id": "tbl1", "text": "Backend", "cell_row": 1, "cell_col": 2 },

  { "type": "update_table_cell", "id": "tbl1", "cell_row": 0, "cell_col": 0, "fill_color": "#1A73E8" },
  { "type": "update_table_cell", "id": "tbl1", "cell_row": 0, "cell_col": 1, "fill_color": "#1A73E8" },
  { "type": "update_table_cell", "id": "tbl1", "cell_row": 0, "cell_col": 2, "fill_color": "#1A73E8" }
]
```

## Sizing Guide

| Use case | w | h | rows |
|---|---|---|---|
| Small summary | 400 | 180 | 3–4 |
| Standard data | 600 | 240 | 4–6 |
| Wide comparison | 660 | 300 | 5–8 |

Leave ~60 PT margin; slide is 720 × 540 PT.

## Additional Resources

- **`references/table-operations.md`** — All table operation fields, multi-row operations, merge rules
