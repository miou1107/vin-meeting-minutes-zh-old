"""One-time authorization for the user's company Gmail and Calendar.

Usage: workspace_auth.py          (pip3 install google-auth-oauthlib first)

Opens Google's consent page in the default browser; the user picks their own @fontrip.com account and
clicks Allow ($MINUTES_OWNER, if set, is offered as the account to pick).
Scopes: read mail (transcripts mailed to the user), send mail (the minutes), read calendars (meeting
time, room, attendees), create events (the next meeting's invite), read the company directory (look up a
colleague's address by name). The OAuth client in ~/.fontrends/google-credentials.json must come from a
Cloud project with the Gmail API, Google Calendar API and People API enabled. The token goes to
~/.fontrends/google-token-workspace.json, separate from the Drive token, and is never printed.
"""
import json
import os
import sys
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT = Path.home() / '.fontrends' / 'google-credentials.json'
TOKEN = Path.home() / '.fontrends' / 'google-token-workspace.json'
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/calendar.readonly',
          'https://www.googleapis.com/auth/calendar.events',
          'https://www.googleapis.com/auth/directory.readonly']


def main():
    if not CLIENT.exists():
        sys.exit(f'STOP: {CLIENT} is missing. Put your own Google Cloud OAuth client (desktop app) there first.')
    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT), SCOPES)
    hint = {'login_hint': os.environ['MINUTES_OWNER']} if os.environ.get('MINUTES_OWNER') else {}
    creds = flow.run_local_server(port=0, open_browser=True, prompt='consent',
                                  authorization_prompt_message='opening the consent page...', **hint)
    fd = os.open(TOKEN, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'w') as fh:
        fh.write(json.dumps({'refresh_token': creds.refresh_token, 'scopes': SCOPES}))
    os.chmod(TOKEN, 0o600)                         # also when the file already existed with wider rights
    print('saved; scopes:', ', '.join(s.rsplit('/', 1)[1] for s in creds.scopes or SCOPES))


if __name__ == '__main__':
    main()
