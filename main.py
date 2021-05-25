#!/bin/python3

import epitech_calendar_parser as parser
import calendar_craller
import json
import sys


def remove_duplicate(epitech, google):
    r_list = []
    for i in epitech:
        if ('codeevent' in i and i['codeevent'] not in google) \
                or ('codeacti' in i and 'codeevent' not in i and i['codeacti'] not in google):
            r_list.append(i)
    return r_list


def main():
    sys.stdout = open('calendar.log', 'a')
    j = json.load(open("config.json"))
    CALENDAR_ID = j['CALENDAR_ID']
    EPITECH_AUTH = j['EPITECH_AUTH']
    if "http" in EPITECH_AUTH:
        print("Check your Epitech Token\nShould be auth-xxx\n", file=sys.stderr)
        exit(1)
    epitech_activities_list = parser.get_epitech_event(EPITECH_AUTH)
    if j['GetModules']:
        epitech_activities_list += parser.get_epitech_projects(EPITECH_AUTH)
    calendar_activity = calendar_craller.get_google_event_list(CALENDAR_ID)
    r_list = remove_duplicate(epitech_activities_list, calendar_activity)
    for i in r_list:
        calendar_craller.create_event(i, CALENDAR_ID)
    print(str(len(r_list)) + " elements add to calendar")


if __name__ == '__main__':
    main()
