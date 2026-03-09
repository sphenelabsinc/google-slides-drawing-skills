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
            requests.append(_line_request(op, slide_id))
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
                color = _color_payload(text_style["foreground_color"])
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
                "lineCategory": op.get("lineCategory", "STRAIGHT"),
                "elementProperties": _element_properties(op, slide_id),
            }
        }
    ]

    line_props = {}
    color, alpha = _color_payload(op.get("line_color"))
    if color:
        line_fill = {"color": color}
        if alpha is not None:
            line_fill["alpha"] = alpha
        line_props["lineFill"] = {"solidFill": line_fill}

    weight = op.get("line_weight")
    if weight:
        line_props["weight"] = {"magnitude": weight, "unit": "PT"}

    if "start_arrow" in op:
        line_props["startArrow"] = {"arrowHead": op["start_arrow"]}

    if "end_arrow" in op:
        line_props["endArrow"] = {"arrowHead": op["end_arrow"]}

    if line_props:
        fields = []
        if "lineFill" in line_props:
            fields.append("lineFill.solidFill.color")
            fields.append("lineFill.solidFill.alpha")
        if "weight" in line_props:
            fields.append("weight")
        if "startArrow" in line_props:
            fields.append("startArrow")
        if "endArrow" in line_props:
            fields.append("endArrow")

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

    fill_color, fill_alpha = _color_payload(op.get("fill_color"))
    if fill_color:
        solid_fill = {"color": fill_color}
        if fill_alpha is not None:
            solid_fill["alpha"] = fill_alpha
        requests.append(
            {
                "updateShapeProperties": {
                    "objectId": object_id,
                    "shapeProperties": {
                        "shapeBackgroundFill": {
                            "solidFill": solid_fill
                        }
                    },
                    "fields": "shapeBackgroundFill.solidFill.color,shapeBackgroundFill.solidFill.alpha",
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
