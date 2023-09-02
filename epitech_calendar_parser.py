#!/bin/python3
import requests
import time

BASE_URL = 'https://intra.epitech.eu/'


def get_epitech_event(COOKIE):
    url = BASE_URL + '/planning/load?format=json&start='
    r_json = requests.get(url + time.strftime("%Y-%m-%d"), 
    # Add a auth cookie to the request
    cookies={'user': COOKIE}
    ).json()
    activities_registered = []
    for i in r_json:
        if ('event_registered' in i and i['event_registered'] is not False) or (
                'status_manager' in i and i['status_manager'] is not None):
            if 'status_manager' in i and i['status_manager'] is not None:
                i['acti_title'] = f"[ORG] {i['acti_title']}"
            activities_registered.append(i)
    return activities_registered


def get_epitech_modules(COOKIE):
    url = BASE_URL + '/course/filter?format=json'
    r_json = requests.get(url, 
        cookies={'user': COOKIE}
).json()
    modules_registered = []
    for i in r_json:
        if 'status' in i and i['status'] == 'ongoing' and i['title'][:2] != 'B0':
            modules_registered.append(i)
    return modules_registered


def get_module_projects(COOKIE, module):
    url = BASE_URL + '/module/' + str(module['scolaryear']) + '/' + module['code'] + '/' \
          + module['codeinstance'] + '/?format=json'
    r_json = requests.get(url, 
        cookies={'user': COOKIE}
).json()
    projects = []
    if 'activites' not in r_json:
        return projects
    for i in r_json['activites']:
        if 'is_projet' in i and i['is_projet'] is True and \
                'type_title' in i and i['type_title'] in ['Project', 'Mini-project']:
            projects.append(i)
    return projects


def get_epitech_projects(COOKIE):
    modules = get_epitech_modules(COOKIE)
    projects = []
    for i in modules:
        projects += get_module_projects(COOKIE, i)
    return projects
