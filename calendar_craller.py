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


def format_code_epitech(description):
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
                desc = format_code_epitech(event['description'])
                if desc is not None:
                    event_list.append(desc)
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return event_list


def make_description(codeevent):
    return '#codeevent=' + codeevent


def format_time(h):
    t = time.strptime(h, '%Y-%m-%d %H:%M:%S')
    return time.strftime('%Y-%m-%dT%H:%M:%S', t)


def format_time_all_day(h):
    t = time.strptime(h, '%Y-%m-%d %H:%M:%S')
    return time.strftime('%Y-%m-%d', t)


def create_event_project(event_param, CALENDAR_ID):
    event = {
        "end": {
            "date": format_time_all_day(event_param['end']),
            "timeZone": "Europe/Paris"
        },
        "start": {
            "date": format_time_all_day(event_param['start']),
            "timeZone": "Europe/Paris"
        },
        "summary": event_param['title'] + ' | ' + event_param['module_title'],
        "description": make_description(event_param['codeacti']),
        'transparency': 'transparent',
    }
    print(event)
    print(service.events().insert(calendarId=CALENDAR_ID,
                                  body=event).execute())


def create_event(event_param, CALENDAR_ID):
    if 'is_projet' in event_param:
        create_event_project(event_param, CALENDAR_ID)
        return
    if 'rdv_group_registered' not in event_param or event_param['rdv_group_registered'] is None:
        en = format_time(event_param['end'])
        st = format_time(event_param['start'])
    else:
        a = event_param['rdv_group_registered'].split('|')
        en = format_time(a[1])
        st = format_time(a[0])
    summary = event_param['acti_title'] if ('acti_title' in event_param) and \
                                           (event_param['acti_title'] is not None) else 'No title'
    location = event_param['room']['code'] if ('room' in event_param) and \
                                              (event_param['room'] is not None) and \
                                              ('code' in event_param['room']) and \
                                              (event_param['room']['code'] is not None) else ''
    event = {
        "end": {
            "dateTime": en,
            "timeZone": "Europe/Paris"
        },
        "start": {
            "dateTime": st,
            "timeZone": "Europe/Paris"
        },
        "summary": summary,
        "location": location,
        "description": make_description(event_param['codeevent'])
    }
    print(event)
    print(service.events().insert(calendarId=CALENDAR_ID,
                                  body=event).execute())
