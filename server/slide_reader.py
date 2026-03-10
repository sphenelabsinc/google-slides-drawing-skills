def read_slide(api, cmd):
    presentation_id = cmd["presentation_id"]
    slide_index = cmd["slide_index"]

    presentation = api.get_presentation(presentation_id)
    slides = presentation.get("slides", [])

    if slide_index >= len(slides):
        raise IndexError("slide_index is out of bounds for the presentation")

    slide = slides[slide_index]
    elements = []

    page_elements = slide.get("pageElements", [])
    for element in page_elements:
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
            shape_props = element["shape"].get("shapeProperties")
            if shape_props:
                element_summary["shape_properties"] = shape_props
            placeholder = element["shape"].get("placeholder")
            if placeholder:
                element_summary["placeholder"] = placeholder
        elif element_type == "line":
            element_summary["line_category"] = element["line"].get("lineCategory")
            line_props = element["line"].get("lineProperties", {})
            if line_props:
                element_summary["line_weight"] = line_props.get("weight")
                element_summary["line_fill"] = line_props.get("lineFill", {}).get("solidFill", {}).get("color", {})
                element_summary["line_properties"] = line_props

        elements.append(element_summary)

    return {
        "slide_id": slide["objectId"],
        "slide_index": slide_index,
        "title": presentation.get("title"),
        "revision_id": slide.get("revisionId"),
        "page_type": slide.get("pageType"),
        "page_properties": slide.get("pageProperties"),
        "slide_properties": slide.get("slideProperties"),
        "layout_properties": slide.get("layoutProperties"),
        "notes_properties": slide.get("notesProperties"),
        "master_properties": slide.get("masterProperties"),
        "page_background": slide.get("pageProperties", {}).get("pageBackgroundFill"),
        "page_elements": page_elements,
        "element_details": {element.get("objectId"): element for element in page_elements if element.get("objectId")},
        "element_count": len(page_elements),
        "elements": elements,
    }
