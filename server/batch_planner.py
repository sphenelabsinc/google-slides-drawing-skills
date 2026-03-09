def execute_batch(api, cmd):
    presentation_id = cmd["presentation_id"]
    slide_index = cmd["slide_index"]

    presentation = api.get_presentation(presentation_id)
    slides = presentation.get("slides", [])

    if slide_index >= len(slides):
        raise IndexError("slide_index is out of bounds for the presentation")

    slide_id = slides[slide_index]["objectId"]
    requests = []

    for op in cmd.get("operations", []):
        op_type = op.get("type", "rectangle")
        if op_type in {"rectangle", "shape"}:
            requests.extend(_shape_requests(op, slide_id))
        elif op_type == "text":
            requests.extend(_text_requests(op, slide_id))
        elif op_type in {"line", "connector", "arrow"}:
            requests.extend(_line_request(op, slide_id))
        elif op_type == "table":
            requests.extend(_table_requests(op, slide_id))
        elif op_type == "insert_text":
            requests.append(_insert_table_text(op))
        elif op_type == "update_table_cell":
            requests.extend(_update_table_cell(op))
        elif op_type == "merge_table_cells":
            requests.append(_merge_table_cells(op))
        elif op_type == "reroute_line":
            requests.append({"rerouteLine": {"objectId": op["id"]}})
        else:
            raise ValueError(f"unknown operation type: {op_type}")

    if not requests:
        return {"status": "ok", "message": "no operations to execute"}

    api.batch_update(presentation_id, requests)

    return {"status": "ok", "requests_sent": len(requests)}


def _shape_requests(op, slide_id):
    shape_type = op.get("shape_type", "RECTANGLE")
    requests = [
        {
            "createShape": {
                "objectId": op["id"],
                "shapeType": shape_type,
                "elementProperties": _element_properties(op, slide_id),
            }
        }
    ]

    requests.extend(_style_requests(op, op["id"]))

    return requests


def _text_requests(op, slide_id):
    requests = [
        {
            "createShape": {
                "objectId": op["id"],
                "shapeType": op.get("shape_type", "TEXT_BOX"),
                "elementProperties": _element_properties(op, slide_id),
            }
        }
    ]

    requests.extend(_style_requests(op, op["id"]))

    text = op.get("text")
    if text:
        requests.append(
            {
                "insertText": {
                    "objectId": op["id"],
                    "insertionIndex": 0,
                    "text": text,
                }
            }
        )

        text_style = op.get("text_style", {})
        if text_style:
            style_payload = {}
            fields = []

            if "font_family" in text_style:
                style_payload["fontFamily"] = text_style["font_family"]
                fields.append("fontFamily")

            if "font_size" in text_style:
                style_payload["fontSize"] = {
                    "magnitude": text_style["font_size"],
                    "unit": "PT",
                }
                fields.append("fontSize")

            if "bold" in text_style:
                style_payload["bold"] = text_style["bold"]
                fields.append("bold")

            if "italic" in text_style:
                style_payload["italic"] = text_style["italic"]
                fields.append("italic")

            if "foreground_color" in text_style:
                color, _ = _color_payload(text_style["foreground_color"])
                if color:
                    style_payload["foregroundColor"] = {"opaqueColor": color}
                    fields.append("foregroundColor")

            if fields:
                requests.append(
                    {
                        "updateTextStyle": {
                            "objectId": op["id"],
                            "textRange": {"type": "ALL"},
                            "style": style_payload,
                            "fields": ",".join(fields),
                        }
                    }
                )

            if "alignment" in text_style:
                alignment = text_style["alignment"]
                requests.append(
                    {
                        "updateParagraphStyle": {
                            "objectId": op["id"],
                            "style": {"alignment": alignment},
                            "fields": "alignment",
                        }
                    }
                )

    return requests


def _line_request(op, slide_id):
    requests = [
        {
            "createLine": {
                "objectId": op["id"],
                "category": op.get("lineCategory", op.get("category", "STRAIGHT")),
                "elementProperties": _element_properties(op, slide_id),
            }
        }
    ]

    line_props = {}
    color, _ = _color_payload(op.get("line_color"))
    if color:
        line_props["lineFill"] = {"solidFill": {"color": color}}

    weight = op.get("line_weight")
    if weight:
        line_props["weight"] = {"magnitude": weight, "unit": "PT"}

    if "start_arrow" in op:
        line_props["startArrow"] = op["start_arrow"]

    if "end_arrow" in op:
        line_props["endArrow"] = op["end_arrow"]

    if "start_connection" in op:
        sc = op["start_connection"]
        line_props["startConnection"] = {
            "connectedObjectId": sc["connected_object_id"],
            "connectionSiteIndex": sc.get("connection_site_index", 0),
        }

    if "end_connection" in op:
        ec = op["end_connection"]
        line_props["endConnection"] = {
            "connectedObjectId": ec["connected_object_id"],
            "connectionSiteIndex": ec.get("connection_site_index", 2),
        }

    if line_props:
        fields = []
        if "lineFill" in line_props:
            fields.append("lineFill.solidFill.color")
        if "weight" in line_props:
            fields.append("weight")
        if "startArrow" in line_props:
            fields.append("startArrow")
        if "endArrow" in line_props:
            fields.append("endArrow")
        if "startConnection" in line_props:
            fields.append("startConnection")
        if "endConnection" in line_props:
            fields.append("endConnection")

        requests.append(
            {
                "updateLineProperties": {
                    "objectId": op["id"],
                    "lineProperties": line_props,
                    "fields": ",".join(fields),
                }
            }
        )

    return requests


def _style_requests(op, object_id):
    requests = []

    fill_color, _ = _color_payload(op.get("fill_color"))
    if fill_color:
        solid_fill = {"color": fill_color}
        requests.append(
            {
                "updateShapeProperties": {
                    "objectId": object_id,
                    "shapeProperties": {
                        "shapeBackgroundFill": {
                            "solidFill": solid_fill
                        }
                    },
                    "fields": "shapeBackgroundFill.solidFill.color",
                }
            }
        )

    outline_color, _ = _color_payload(op.get("outline_color"))
    outline_width = op.get("outline_width")
    if outline_color or outline_width:
        outline = {"outlineFill": {"solidFill": {"color": outline_color}}} if outline_color else {}
        if outline_width:
            outline["weight"] = {"magnitude": outline_width, "unit": "PT"}

        requests.append(
            {
                "updateShapeProperties": {
                    "objectId": object_id,
                    "shapeProperties": {"outline": outline},
                    "fields": "outline",
                }
            }
        )

    return requests


def _element_properties(op, slide_id):
    return {
        "pageObjectId": slide_id,
        "size": {
            "height": {"magnitude": op["h"], "unit": "PT"},
            "width": {"magnitude": op["w"], "unit": "PT"},
        },
        "transform": {
            "scaleX": 1,
            "scaleY": 1,
            "translateX": op["x"],
            "translateY": op["y"],
            "unit": "PT",
        },
    }


def _color_payload(spec):
    if not spec:
        return None, None

    if isinstance(spec, str):
        spec = {"hex": spec}

    if not isinstance(spec, dict):
        return None, None

    alpha = spec.get("a") or spec.get("alpha")
    alpha = max(0.0, min(1.0, float(alpha))) if alpha is not None else None

    if "hex" in spec:
        hex_value = spec["hex"].lstrip("#")
        if len(hex_value) == 3:
            hex_value = "".join(ch * 2 for ch in hex_value)
        if len(hex_value) not in {6, 8}:
            return None, None
        r = int(hex_value[0:2], 16)
        g = int(hex_value[2:4], 16)
        b = int(hex_value[4:6], 16)
        if len(hex_value) == 8 and alpha is None:
            alpha = int(hex_value[6:8], 16) / 255.0

        return _build_color_dict(r, g, b), alpha

    r = spec.get("r")
    g = spec.get("g")
    b = spec.get("b")
    if r is None or g is None or b is None:
        return None, alpha

    return _build_color_dict(r, g, b), alpha


def _build_color_dict(r, g, b):
    def normalize(value):
        value = float(value)
        return value / 255.0 if value > 1 else max(0.0, min(1.0, value))

    return {
        "rgbColor": {
            "red": normalize(r),
            "green": normalize(g),
            "blue": normalize(b),
        }
    }


def _table_requests(op, slide_id):
    return [
        {
            "createTable": {
                "objectId": op["id"],
                "elementProperties": _element_properties(op, slide_id),
                "rows": op["rows"],
                "columns": op["columns"],
            }
        }
    ]


def _insert_table_text(op):
    req = {
        "insertText": {
            "objectId": op["id"],
            "text": op["text"],
            "insertionIndex": op.get("insertion_index", 0),
        }
    }
    row = op.get("cell_row")
    col = op.get("cell_col")
    if row is not None and col is not None:
        req["insertText"]["cellLocation"] = {"rowIndex": row, "columnIndex": col}
    return req


def _update_table_cell(op):
    requests = []
    fill_color, _ = _color_payload(op.get("fill_color"))
    if fill_color:
        requests.append(
            {
                "updateTableCellProperties": {
                    "objectId": op["id"],
                    "tableRange": {
                        "location": {
                            "rowIndex": op["cell_row"],
                            "columnIndex": op["cell_col"],
                        },
                        "rowSpan": op.get("row_span", 1),
                        "columnSpan": op.get("col_span", 1),
                    },
                    "tableCellProperties": {
                        "tableCellBackgroundFill": {"solidFill": {"color": fill_color}}
                    },
                    "fields": "tableCellBackgroundFill.solidFill.color",
                }
            }
        )
    return requests


def _merge_table_cells(op):
    return {
        "mergeTableCells": {
            "objectId": op["id"],
            "tableRange": {
                "location": {
                    "rowIndex": op["row"],
                    "columnIndex": op["col"],
                },
                "rowSpan": op.get("row_span", 1),
                "columnSpan": op.get("col_span", 1),
            },
        }
    }
