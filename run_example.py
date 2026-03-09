import json

from scripts.send_command import send_command


def load_config():
    with open("config.json") as config_file:
        return json.load(config_file)


def banner_text_style():
    return {
        "font_family": "Dancing Script",
        "font_size": 40,
        "foreground_color": {"hex": "#FF8C00"},
        "bold": True,
        "italic": True,
        "alignment": "CENTER",
    }


def smiley_operations():
    face = {
        "type": "rectangle",
        "id": "smiley_face",
        "x": 260,
        "y": 80,
        "w": 400,
        "h": 400,
        "fill_color": {"hex": "#FFF176"},
        "outline_color": {"hex": "#F0A000"},
        "outline_width": 4,
    }
    left_eye = {
        "type": "rectangle",
        "id": "left_eye",
        "x": 320,
        "y": 180,
        "w": 60,
        "h": 60,
        "fill_color": {"hex": "#212121"},
    }
    right_eye = {
        "type": "rectangle",
        "id": "right_eye",
        "x": 500,
        "y": 180,
        "w": 60,
        "h": 60,
        "fill_color": {"hex": "#212121"},
    }
    mouth = {
        "type": "rectangle",
        "id": "mouth",
        "x": 360,
        "y": 350,
        "w": 200,
        "h": 25,
        "fill_color": {"hex": "#212121"},
    }
    connectors = [
        {
            "type": "connector",
            "id": "eye_to_mouth_left",
            "x": 330,
            "y": 250,
            "w": 220,
            "h": 60,
            "lineCategory": "BENT",
            "line_color": {"hex": "#424242"},
            "line_weight": 3,
        },
        {
            "type": "connector",
            "id": "eye_to_mouth_right",
            "x": 480,
            "y": 250,
            "w": 220,
            "h": 60,
            "lineCategory": "BENT",
            "line_color": {"hex": "#424242"},
            "line_weight": 3,
        },
        {
            "type": "line",
            "id": "smile_curve",
            "x": 330,
            "y": 360,
            "w": 200,
            "h": 40,
            "lineCategory": "BENT",
            "line_color": {"hex": "#212121"},
            "line_weight": 5,
        },
    ]
    banner = {
        "type": "rectangle",
        "id": "banner",
        "x": 0,
        "y": 470,
        "w": 720,
        "h": 70,
        "fill_color": {"hex": "#D32F2F"},
    }
    banner_text = {
        "type": "text",
        "id": "banner_text",
        "x": 140,
        "y": 485,
        "w": 680,
        "h": 55,
        "text": "Hello World",
        "text_style": banner_text_style(),
    }

    return [face, left_eye, right_eye, mouth] + connectors + [banner, banner_text]


if __name__ == "__main__":
    config = load_config()
    command = {
        "tool": "batch_draw",
        "presentation_id": config["presentation_id"],
        "slide_index": 0,
        "operations": smiley_operations(),
    }

    print("Sending smiley batch draw command")
    response = send_command(command)
    print("Response:", response)
