# Google Slides + Drive Setup

This project uses the Google Slides and Drive APIs, and `test.py` runs a quick smoke test once you have the credentials configured locally.

## Prerequisites
1. Python 3.10+ (or the version your virtual environment uses).
2. The dependencies listed in `requirements.txt` (`google-auth`, `google-auth-oauthlib`, `google-api-python-client`, etc.).
3. A Google Cloud project that you control and can configure.

## Step-by-step credential setup
1. Open the Google Cloud Console and select or create the project you will use for this repo.
2. Configure the OAuth consent screen first: choose *External* (for a personal Gmail account), fill in the required fields, and save. After it is configured, add your testing Gmail address as a *Test user* so you can skip verification.
3. Enable both of these APIs in the same project: the **Google Slides API** and the **Google Drive API**.
4. Still in the same project, create an **OAuth 2.0 Client ID** credential. Choose “Desktop app” (or “Other”) because `test.py` uses the installed app flow. Download the resulting `credentials.json` and drop it in the project root, replacing any placeholder file already there.
5. Leave `token.json` in place (or let the script generate it) so future runs reuse the stored tokens; the file is created after the first successful login.

## Local configuration
1. (Optional) Customize `config.json` with the `presentation_id` and `slide_index` you want `test.py` to target.
2. Install dependencies from the repo root:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Verifying the environment
Run `python test.py` from the repo root. The script will:
1. Prompt you to authenticate via a browser window and persist the credentials into `token.json`.
2. List presentation files in your Drive so you can confirm access.
3. Draw a rectangle on the configured slide to prove the Slides API is writable.

If the script succeeds without errors, the Google credentials and APIs are set up correctly.
