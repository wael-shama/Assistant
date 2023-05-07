"""

This code defines a `GoogleCalendar` class that can be used to interact with the Google Calendar API in an object-oriented manner. 

The class has two methods:

1. `get_events`: This method fetches events from the user's primary calendar for the specified time range. It takes two optional arguments, `time_min` and `time_max`, which are `datetime.datetime` objects representing the minimum and maximum times of events to retrieve. If these arguments are not provided, the method will retrieve events for the current day.

2. `create_event`: This method creates a new event on the user's primary calendar. It takes several arguments, including `start_time`, `end_time`, `summary`, `location`, `description`, and `attendees`, which are used to set the properties of the event. The `start_time` and `end_time` arguments should be `datetime.datetime` objects representing the start and end times of the event, respectively. The `summary`, `location`, and `description` arguments should be strings representing the summary, location, and description of the event, respectively. The `attendees` argument should be a list of email addresses representing the attendees of the event. If this argument is not provided, the event will be created without any attendees. 

This code also includes the necessary imports and set up for authentication with the Google Calendar API using the OAuth2 flow and `google-auth` and `google-api-python-client` packages. The authentication credentials are stored in a local file named `token.pickle`, which is created during the authentication process.

"""
import datetime
import pytz
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
import config

class GoogleCalendar:
    def __init__(self):
        # Set up the credentials
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_config(config.CALENDAR_CLIENT_CONFIG, ['https://www.googleapis.com/auth/calendar.events'])
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        # Build the API client
        self.service = build('calendar', 'v3', credentials=creds)

    def get_events(self, time_min=None, time_max=None):
        """
        Fetches events from the user's primary calendar for the specified time range.

        :param time_min: The minimum time of events to retrieve.
        :type time_min: datetime.datetime
        :param time_max: The maximum time of events to retrieve.
        :type time_max: datetime.datetime
        :return: A list of events.
        :rtype: list
        """
        if not time_min:
            time_min = datetime.datetime.utcnow()
        if not time_max:
            time_max = time_min + datetime.timedelta(days=1)
        time_min = time_min.astimezone(pytz.UTC).isoformat()
        time_max = time_max.astimezone(pytz.UTC).isoformat()

        events_result = self.service.events().list(calendarId='primary', timeMin=time_min, timeMax=time_max, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        return events

    def create_event(self, start_time, end_time, summary, location=None, description=None, attendees=None):
        """
        Creates a new event on the user's primary calendar.

        :param start_time: The start time of the event.
        :type start_time: datetime.datetime
        :param end_time: The end time of the event.
        :type end_time: datetime.datetime
        :param summary: The summary or title of the event.
        :type summary: str
        :param location: The location of the event.
        :type location: str
        :param description: The description of the event.
        :type description: str
        :param attendees: The list of attendees for the event.
        :type attendees: list
        :return: The newly created event.
        :rtype: dict
        """
        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': start_time.astimezone(pytz.UTC).isoformat(),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': end_time.astimezone(pytz.UTC).isoformat(),
                'timeZone': 'UTC',
            },
        }
        if attendees:
            event['attendees'] = [{'email': email} for email in attendees]

        created_event = self.service.events().insert(calendarId='primary', body=event).execute()

        return created_event
