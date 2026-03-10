# Tables Digest

Condensed view of `googleSlidesAPI_v1/tables.md` for quick table planning.

- **Table structure**: A `Table` has `rows` × `columns`. Specify `tableProperties`, `tableBorderRows`, and `tableBorderCells` when you need custom styling.
- **Cells**: `TableCell` holds `tableCellProperties`, including `tableCellBackgroundFill`. Use `rowIndex`/`columnIndex` to target cells when inserting text or updating fills.
- **Borders**: `TableBorderRow` and `TableBorderCell` objects define `TableBorderProperties` (weight, dash style, color); use them to control per-side borders.
- **Operations**: `insert_text`, `update_table_cell`, and `merge_table_cells` are the operations you send via `batchDraw` after creating the table.

This digest keeps your focus on the key table concepts so you can script tables without rereading the entire API doc.
