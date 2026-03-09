import json
import socket

from authentication import ensure_credentials

try:
    from server.slides_api import SlidesAPI
    from server.slide_reader import read_slide
    from server.batch_planner import execute_batch
except ImportError:
    from slides_api import SlidesAPI
    from slide_reader import read_slide
    from batch_planner import execute_batch


HOST = "127.0.0.1"
PORT = 8765
BUFFER_SIZE = 131072


def _get_slide(api, presentation_id, slide_index):
    presentation = api.get_presentation(presentation_id)
    slides = presentation.get("slides", [])
    if slide_index >= len(slides):
        raise IndexError("slide_index is out of bounds for the presentation")
    return presentation, slides[slide_index]


def handle_command(api, cmd):
    tool = cmd.get("tool")

    if tool == "read_slide":
        return read_slide(api, cmd)

    if tool == "batch_draw":
        return execute_batch(api, cmd)

    if tool == "duplicate_slide":
        presentation_id = cmd["presentation_id"]
        slide_index = cmd["slide_index"]
        _, slide = _get_slide(api, presentation_id, slide_index)
        return {"status": "ok", "response": api.duplicate_slide(presentation_id, slide["objectId"])}

    if tool == "delete_objects":
        presentation_id = cmd["presentation_id"]
        object_ids = cmd["object_ids"]
        requests = [{"deleteObject": {"objectId": oid}} for oid in object_ids]
        if not requests:
            return {"status": "ok", "message": "no objects to delete"}
        return {"status": "ok", "response": api.batch_update(presentation_id, requests)}

    if tool == "clear_slide":
        presentation_id = cmd["presentation_id"]
        slide_index = cmd["slide_index"]
        _, slide = _get_slide(api, presentation_id, slide_index)
        requests = [
            {"deleteObject": {"objectId": element["objectId"]}}
            for element in slide.get("pageElements", [])
            if element.get("objectId")
        ]
        if not requests:
            return {"status": "ok", "message": "slide already empty"}
        return {"status": "ok", "response": api.batch_update(presentation_id, requests)}

    return {"status": "error", "message": f"unknown tool '{tool}'"}


def run():
    ensure_credentials()
    api = SlidesAPI()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST, PORT))
        server_sock.listen()
        print("Slides skill server running on", HOST, PORT)

        while True:
            conn, addr = server_sock.accept()
            with conn:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    continue

                try:
                    cmd = json.loads(data.decode("utf-8"))
                    response = handle_command(api, cmd)
                except Exception as exc:
                    response = {
                        "status": "error",
                        "message": str(exc),
                    }

                conn.sendall(json.dumps(response).encode("utf-8"))


if __name__ == "__main__":
    run()
