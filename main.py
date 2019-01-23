#!/bin/python3

import parser
import calendar_craller
import json
import sys


def remove_doublon(epitech, google):
    r_list = []
    for i in epitech:
        if i['codeevent'] not in google:
            r_list.append(i)
    return r_list


def main():
    sys.stdout = open('calendar.log', 'w')
    j = json.load(open("config.json"))
    CALENDAR_ID = j['CALENDAR_ID']
    EPITECH_AUTH = j['EPITECH_AUTH']
    module_liste = parser.get_epitech_activity(EPITECH_AUTH)
    calendar_activity = calendar_craller.get_google_event_list(CALENDAR_ID)
    r_list = remove_doublon(module_liste, calendar_activity)
    for i in r_list:
        calendar_craller.creat_event(i, CALENDAR_ID)
    print(str(len(r_list)) + " elements add to calendar")


if __name__ == '__main__':
    main()
