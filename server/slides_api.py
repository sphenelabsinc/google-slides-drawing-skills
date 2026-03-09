from googleapiclient.discovery import build

from authentication import ensure_credentials


class SlidesAPI:
    SCOPES = ["https://www.googleapis.com/auth/presentations"]

    def __init__(self, token_path="token.json", credentials_path="credentials.json"):
        self._token_path = token_path
        self._credentials_path = credentials_path
        self.creds = self._load_credentials()
        self.service = build("slides", "v1", credentials=self.creds)

    def _load_credentials(self):
        return ensure_credentials(
            token_path=self._token_path,
            credentials_path=self._credentials_path,
            scopes=self.SCOPES,
        )

    def get_presentation(self, presentation_id):
        return (
            self.service.presentations()
            .get(presentationId=presentation_id)
            .execute()
        )

    def batch_update(self, presentation_id, requests):
        return (
            self.service.presentations()
            .batchUpdate(presentationId=presentation_id, body={"requests": requests})
            .execute()
        )

    def duplicate_slide(self, presentation_id, slide_id):
        return self.batch_update(
            presentation_id,
            [
                {
                    "duplicateObject": {
                        "objectId": slide_id,
                    }
                }
            ],
        )
