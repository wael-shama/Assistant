from datetime import datetime, timedelta
from google_calendar import GoogleCalendar

# create a GoogleCalendar object
calendar = GoogleCalendar()

# fetch events for the current day
events = calendar.get_events()

# print the start time and summary of each event
for event in events:
    start_time = event['start'].get('dateTime', event['start'].get('date'))
    summary = event['summary']
    print(f"{start_time} - {summary}")

# create a new event for tomorrow at 2:00 PM
start_time = datetime.now() + timedelta(days=1)
start_time = start_time.replace(hour=14, minute=0, second=0, microsecond=0)
end_time = start_time + timedelta(hours=1)
summary = "Meeting with John"
location = "Office"
description = "Discuss project progress"
attendees = ["john@example.com"]

calendar.create_event(start_time, end_time, summary, location, description, attendees)
print("Event created successfully!")
