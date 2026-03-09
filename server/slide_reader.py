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

        if element_type == "shape":
            text_runs = element["shape"].get("text", {}).get("textElements", [])
            text_content = "".join(
                [run["textRun"]["content"] for run in text_runs if "textRun" in run]
            ).strip()
            if text_content:
                element_summary["text"] = text_content

        elements.append(element_summary)

    return {
        "slide_id": slide["objectId"],
        "elements": elements,
        "title": presentation.get("title"),
    }
