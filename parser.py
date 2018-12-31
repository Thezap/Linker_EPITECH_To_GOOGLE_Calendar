#!/bin/python3
import requests
import time

def get_epitech_activity(EPITECH_AUTH):
    p = 'https://intra.epitech.eu/' + EPITECH_AUTH + '/planning/load?format=json&start='
    r = requests.get(p + time.strftime("%Y-%m-%d"))
    r_json = r.json()
    modul_resgister = []
    for i in r_json:
        if i['event_registered'] is not False:
            modul_resgister.append(i)
    return modul_resgister
