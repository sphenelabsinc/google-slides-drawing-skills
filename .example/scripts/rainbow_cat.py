#!/usr/bin/env python3
"""Job that draws the rainbow block cat art beside the calculator plot."""

import json
import socket
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config.json"


def load_config():
    with CONFIG_PATH.open() as fh:
        data = json.load(fh)
    return {
        "presentation_id": data["presentation_id"],
        "slide_index": data["slide_index"],
        "host": data.get("host", "127.0.0.1"),
        "port": data.get("port", 8765),
    }


def gen_id(name):
    return f"cat_{name}_{uuid.uuid4().hex[:6]}"


class SlideClient:
    def __init__(self, presentation_id, slide_index, host="127.0.0.1", port=8765):
        self.presentation_id = presentation_id
        self.slide_index = slide_index
        self.host = host
        self.port = port

    def send(self, payload):
        payload.update(
            {
                "presentation_id": self.presentation_id,
                "slide_index": self.slide_index,
            }
        )
        message = json.dumps(payload)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.sendall(message.encode("utf-8"))
            data = b""
            while True:
                chunk = sock.recv(65536)
                if not chunk:
                    break
                data += chunk
        if not data:
            raise ConnectionError("empty response from skill server")
        return json.loads(data.decode("utf-8"))

    def read_slide(self):
        return self.send({"tool": "read_slide"})

    def delete_objects(self, object_ids):
        return self.send({"tool": "delete_objects", "object_ids": object_ids})

    def batch_draw(self, operations):
        return self.send({"tool": "batch_draw", "operations": operations})


def build_cat_operations():
    body_left = 32
    body_width = 112
    body_top = 262
    stripe_height = 18
    stripe_colors = [
        ("red", "#FF5252"),
        ("orange", "#FF9800"),
        ("yellow", "#FFEB3B"),
        ("green", "#76FF03"),
        ("blue", "#448AFF"),
        ("purple", "#7C4DFF"),
    ]
    ops = []
    for idx, (name, color) in enumerate(stripe_colors):
        ops.append(
            {
                "type": "shape",
                "id": gen_id(f"stripe_{name}"),
                "x": body_left,
                "y": body_top + idx * stripe_height,
                "w": body_width,
                "h": stripe_height,
                "shape_type": "RECTANGLE",
                "fill_color": color,
                "outline_color": "#212121",
                "outline_width": 0.8,
            }
        )

    tail_left = body_left - 28
    tail_top = body_top + 8
    tail_width = 20
    tail_height = stripe_height * 4
    tail_bands = ["#7C4DFF", "#448AFF", "#76FF03"]
    band_height = tail_height / len(tail_bands)
    for idx, color in enumerate(tail_bands):
        ops.append(
            {
                "type": "shape",
                "id": gen_id(f"tail_{idx}"),
                "x": tail_left,
                "y": tail_top + idx * band_height,
                "w": tail_width,
                "h": band_height,
                "shape_type": "ROUND_RECTANGLE",
                "fill_color": color,
                "outline_color": "#212121",
                "outline_width": 0.6,
            }
        )

    head_width = 90
    head_height = 70
    head_x = body_left + (body_width - head_width) / 2
    head_y = body_top - head_height + 10
    ops.append(
        {
            "type": "shape",
            "id": gen_id("head"),
            "x": head_x,
            "y": head_y,
            "w": head_width,
            "h": head_height,
            "shape_type": "ROUND_RECTANGLE",
            "fill_color": "#FFC1E3",
            "outline_color": "#212121",
            "outline_width": 1,
        }
    )

    ear_width = 18
    ear_height = 24
    ops.extend(
        [
            {
                "type": "shape",
                "id": gen_id("ear_left"),
                "x": head_x + 10,
                "y": head_y - ear_height + 6,
                "w": ear_width,
                "h": ear_height,
                "shape_type": "TRIANGLE",
                "fill_color": "#FFC1E3",
                "outline_color": "#212121",
                "outline_width": 0.6,
            },
            {
                "type": "shape",
                "id": gen_id("ear_right"),
                "x": head_x + head_width - 10 - ear_width,
                "y": head_y - ear_height + 6,
                "w": ear_width,
                "h": ear_height,
                "shape_type": "TRIANGLE",
                "fill_color": "#FFC1E3",
                "outline_color": "#212121",
                "outline_width": 0.6,
            },
        ]
    )

    eye_w = 14
    eye_h = 16
    eye_y = head_y + 28
    eye_spacing = 22
    left_eye_x = head_x + 18
    right_eye_x = left_eye_x + eye_w + eye_spacing
    for idx, eye_x in enumerate((left_eye_x, right_eye_x)):
        ops.append(
            {
                "type": "shape",
                "id": gen_id(f"eye_{idx}"),
                "x": eye_x,
                "y": eye_y,
                "w": eye_w,
                "h": eye_h,
                "shape_type": "ELLIPSE",
                "fill_color": "#FFFFFF",
                "outline_color": "#212121",
                "outline_width": 0.6,
            }
        )
        pupil_x = eye_x + eye_w / 2 - 3
        pupil_y = eye_y + eye_h / 2 - 4
        ops.append(
            {
                "type": "shape",
                "id": gen_id(f"pupil_{idx}"),
                "x": pupil_x,
                "y": pupil_y,
                "w": 6,
                "h": 8,
                "shape_type": "ELLIPSE",
                "fill_color": "#212121",
            }
        )

    nose_width = 14
    nose_height = 8
    nose_x = head_x + (head_width - nose_width) / 2
    nose_y = eye_y + eye_h + 4
    ops.append(
        {
            "type": "shape",
            "id": gen_id("nose"),
            "x": nose_x,
            "y": nose_y,
            "w": nose_width,
            "h": nose_height,
            "shape_type": "ELLIPSE",
            "fill_color": "#EF5350",
        }
    )

    whisker_offset = 6
    whisker_length = 38
    whisker_spacing = 5
    center_y = nose_y + nose_height / 2
    for side in ("left", "right"):
        direction = -1 if side == "left" else 1
        start_x = nose_x + nose_width / 2
        for idx in range(3):
            y = center_y + (idx - 1) * whisker_spacing
            x = start_x if side == "right" else start_x - whisker_length
            w = whisker_length if side == "right" else whisker_length
            ops.append(
                {
                    "type": "line",
                    "id": gen_id(f"whisker_{side}_{idx}"),
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": 0.5,
                    "category": "STRAIGHT",
                    "line_color": "#212121",
                    "line_weight": 1,
                }
            )

    paw_y = body_top + stripe_height * len(stripe_colors) + 6
    paw_width = 28
    paw_height = 12
    paw_color = "#7C4DFF"
    ops.extend(
        [
            {
                "type": "shape",
                "id": gen_id("paw_left"),
                "x": body_left + 8,
                "y": paw_y,
                "w": paw_width,
                "h": paw_height,
                "shape_type": "ROUND_RECTANGLE",
                "fill_color": paw_color,
                "outline_color": "#212121",
                "outline_width": 0.7,
            },
            {
                "type": "shape",
                "id": gen_id("paw_right"),
                "x": body_left + body_width - paw_width - 8,
                "y": paw_y,
                "w": paw_width,
                "h": paw_height,
                "shape_type": "ROUND_RECTANGLE",
                "fill_color": paw_color,
                "outline_color": "#212121",
                "outline_width": 0.7,
            },
        ]
    )

    return ops


def main():
    cfg = load_config()
    client = SlideClient(cfg["presentation_id"], cfg["slide_index"], cfg["host"], cfg["port"])
    slide = client.read_slide()
    cat_ids = [el["objectId"] for el in slide.get("elements", []) if el["objectId"].startswith("cat_")]
    if cat_ids:
        client.delete_objects(cat_ids)
    operations = build_cat_operations()
    client.batch_draw(operations)


if __name__ == "__main__":
    main()
