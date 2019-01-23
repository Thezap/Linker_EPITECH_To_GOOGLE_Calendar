#!/bin/python3
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time

SCOPES = 'https://www.googleapis.com/auth/calendar'

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))


def format_codeevent(description):
    desc = description.split()[0]
    if desc[0] != '#':
        return
    if desc[1:11] != "codeevent=":
        return
    return desc[11:]


def get_google_event_list(CALENDAR_ID):
    event_list = []

    page_token = None
    while True:
        events = service.events().list(calendarId=CALENDAR_ID,
                                       pageToken=page_token).execute()
        for event in events['items']:
            if 'description' in event:
                desc = format_codeevent(event['description'])
                if desc is not None:
                    event_list.append(desc)
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return event_list


def make_description(codeevent):
    return "#codeevent=" + codeevent


def format_time(h):
    t = time.strptime(h, "%Y-%m-%d %H:%M:%S")
    return time.strftime("%Y-%m-%dT%H:%M:%S", t)


def creat_event(event_param, CALENDAR_ID):
    event = {
        "end": {
            "dateTime": format_time(event_param['end']),
            "timeZone": "Europe/Paris"
        },
        "start": {
            "dateTime": format_time(event_param['start']),
            "timeZone": "Europe/Paris"
        },
        "summary": event_param['acti_title'],
        "location": event_param['room']['code'],
        "description": make_description(event_param['codeevent'])
    }
    print(event)
    print(service.events().insert(calendarId=CALENDAR_ID,
                                  body=event).execute())
