def read_slide(api, cmd):
    presentation_id = cmd["presentation_id"]
    slide_index = cmd["slide_index"]

    presentation = api.get_presentation(presentation_id)
    slides = presentation.get("slides", [])

    if slide_index >= len(slides):
        raise IndexError("slide_index is out of bounds for the presentation")

    slide = slides[slide_index]
    elements = []

    for element in slide.get("pageElements", []):
        element_type = (
            "shape"
            if "shape" in element
            else "image"
            if "image" in element
            else "line"
            if "line" in element
            else "unknown"
        )

        element_summary = {"objectId": element.get("objectId"), "type": element_type}

        transform = element.get("transform", {})
        size = element.get("size", {})
        if transform or size:
            element_summary["x"] = round(transform.get("translateX", 0), 1)
            element_summary["y"] = round(transform.get("translateY", 0), 1)
            element_summary["w"] = round(size.get("width", {}).get("magnitude", 0), 1)
            element_summary["h"] = round(size.get("height", {}).get("magnitude", 0), 1)

        if element_type == "shape":
            element_summary["shape_type"] = element["shape"].get("shapeType")
            text_runs = element["shape"].get("text", {}).get("textElements", [])
            text_content = "".join(
                [run["textRun"]["content"] for run in text_runs if "textRun" in run]
            ).strip()
            if text_content:
                element_summary["text"] = text_content
        elif element_type == "line":
            element_summary["line_category"] = element["line"].get("lineCategory")
            line_props = element["line"].get("lineProperties", {})
            if line_props:
                element_summary["line_weight"] = line_props.get("weight")
                element_summary["line_fill"] = line_props.get("lineFill", {}).get("solidFill", {}).get("color", {})

        elements.append(element_summary)

    return {
        "slide_id": slide["objectId"],
        "elements": elements,
        "title": presentation.get("title"),
    }
