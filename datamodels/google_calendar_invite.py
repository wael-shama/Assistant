# {
#     'summary': 'Event summary',
#     'location': 'Event location',
#     'description': 'Event description',
#     'start': {
#         'dateTime': 'Event start time in ISO 8601 format',
#         'timeZone': 'Time zone in which the event starts'
#     },
#     'end': {
#         'dateTime': 'Event end time in ISO 8601 format',
#         'timeZone': 'Time zone in which the event ends'
#     },
#     'reminders': {
#         'useDefault': True/False, # whether to use the default reminders for the calendar
#         'overrides': [
#             {
#                 'method': 'popup',
#                 'minutes': 'Number of minutes before the event to trigger the reminder'
#             },
#             # additional reminder overrides can be included here
#         ]
#     },
#     'attendees': [
#         {
#             'email': 'Attendee email address',
#             'responseStatus': 'Attendee response status (optional)',
#             'optional': True/False, # whether the attendee is optional (optional)
#             'organizer': True/False, # whether the attendee is the organizer (optional)
#             'self': True/False # whether the attendee is the user (optional)
#         },
#         # additional attendees can be included here
#     ],
#     'recurrence': [
#         'Recurrence rule in RFC 5545 format',
#         # additional recurrence rules can be included here
#     ],
#     'colorId': 'Color ID for the event (optional)',
#     'transparency': 'Event transparency (optional)',
#     'visibility': 'Event visibility (optional)',
#     'locationId': 'ID of the location where the event takes place (optional)',
#     'originalStartTime': {
#         'dateTime': 'Event start time in ISO 8601 format',
#         'timeZone': 'Time zone in which the event starts'
#     }
# }

import google_calendar as calendar

event = {
    'summary': 'Team Meeting',
    'location': '123 Main St, Anytown USA',
    'description': 'Discuss project status and upcoming tasks',
    'start': {
        'dateTime': '2023-05-10T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': '2023-05-10T10:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
    'attendees': [
        {'email': 'attendee1@example.com'},
        {'email': 'attendee2@example.com'},
    ],
    'reminders': {
        'useDefault': True
    },
}

calendar.create_event(event)