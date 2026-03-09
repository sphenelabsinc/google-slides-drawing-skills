import json
import os
from pprint import pprint

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/presentations",
    "https://www.googleapis.com/auth/drive.metadata.readonly"
]


def load_config():
    with open("config.json") as f:
        return json.load(f)


def authenticate():

    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    slides_service = build("slides", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    return slides_service, drive_service


def list_presentations(drive_service):

    print("\n--- Presentations on your account ---")

    results = drive_service.files().list(
        q="mimeType='application/vnd.google-apps.presentation'",
        fields="files(id, name)",
        pageSize=50
    ).execute()

    for f in results.get("files", []):
        print(f"{f['name']}  |  {f['id']}")


def get_presentation(slides_service, presentation_id):

    presentation = slides_service.presentations().get(
        presentationId=presentation_id
    ).execute()

    print("\nPresentation:", presentation.get("title"))

    return presentation


def ensure_slide_exists(slides_service, presentation_id, slide_index):

    presentation = get_presentation(slides_service, presentation_id)

    slides = presentation.get("slides", [])

    if slide_index < len(slides):

        slide = slides[slide_index]

        print(f"\nUsing existing slide index {slide_index}")
        return slide

    print("\nSlide index does not exist — creating new slide")

    requests = [{
        "createSlide": {
            "insertionIndex": slide_index,
            "slideLayoutReference": {
                "predefinedLayout": "BLANK"
            }
        }
    }]

    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={"requests": requests}
    ).execute()

    presentation = get_presentation(slides_service, presentation_id)

    return presentation["slides"][slide_index]


def print_slide_contents(slide):

    print("\n--- Current Slide Elements ---")

    elements = slide.get("pageElements", [])

    if not elements:
        print("Slide is empty")
        return

    for e in elements:

        obj_id = e.get("objectId")

        print(f"\nElement ID: {obj_id}")

        if "shape" in e:

            text_elements = e["shape"].get("text", {}).get("textElements", [])

            text = ""

            for t in text_elements:
                if "textRun" in t:
                    text += t["textRun"]["content"]

            print("Type: Shape/Text")
            print("Text:", text.strip())

        elif "image" in e:

            print("Type: Image")

        else:

            print("Type: Other")


def draw_shape(slides_service, presentation_id, slide_id):

    shape_id = "ai_shape_box"

    print("\nDrawing shape on slide...")

    requests = [

        {
            "createShape": {
                "objectId": shape_id,
                "shapeType": "RECTANGLE",
                "elementProperties": {
                    "pageObjectId": slide_id,
                    "size": {
                        "height": {"magnitude": 200, "unit": "PT"},
                        "width": {"magnitude": 400, "unit": "PT"}
                    },
                    "transform": {
                        "scaleX": 1,
                        "scaleY": 1,
                        "translateX": 100,
                        "translateY": 100,
                        "unit": "PT"
                    }
                }
            }
        },

        {
            "insertText": {
                "objectId": shape_id,
                "text": "AI generated drawing"
            }
        }

    ]

    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={"requests": requests}
    ).execute()

    print("Shape drawn.")


def main():

    config = load_config()

    presentation_id = config["presentation_id"]
    slide_index = config["slide_index"]

    slides_service, drive_service = authenticate()

    list_presentations(drive_service)

    slide = ensure_slide_exists(
        slides_service,
        presentation_id,
        slide_index
    )

    slide_id = slide["objectId"]

    print("\nSlide Object ID:", slide_id)

    print_slide_contents(slide)

    draw_shape(slides_service, presentation_id, slide_id)


if __name__ == "__main__":
    main()