#!/bin/python3
import requests
import time

BASE_URL = 'https://intra.epitech.eu/'


def get_epitech_event(EPITECH_AUTH):
    url = BASE_URL + EPITECH_AUTH + '/planning/load?format=json&start='
    r_json = requests.get(url + time.strftime("%Y-%m-%d")).json()
    activities_registered = []
    for i in r_json:
        if ('event_registered' in i and i['event_registered'] is not False) or (
                'status_manager' in i and i['status_manager'] is not None):
            if 'status_manager' in i and i['status_manager'] is not None:
                i['acti_title'] = f"[ORG] {i['acti_title']}"
            activities_registered.append(i)
    return activities_registered


def get_epitech_modules(EPITECH_AUTH):
    url = BASE_URL + EPITECH_AUTH + '/course/filter?format=json'
    r_json = requests.get(url).json()
    modules_registered = []
    for i in r_json:
        if 'status' in i and i['status'] == 'ongoing' and i['title'][:2] != 'B0':
            modules_registered.append(i)
    return modules_registered


def get_module_projects(EPITECH_AUTH, module):
    url = BASE_URL + EPITECH_AUTH + '/module/' + str(module['scolaryear']) + '/' + module['code'] + '/' \
          + module['codeinstance'] + '/?format=json'
    r_json = requests.get(url).json()
    projects = []
    if 'activites' not in r_json:
        return projects
    for i in r_json['activites']:
        if 'is_projet' in i and i['is_projet'] is True and \
                'type_title' in i and i['type_title'] in ['Project', 'Mini-project']:
            projects.append(i)
    return projects


def get_epitech_projects(EPITECH_AUTH):
    modules = get_epitech_modules(EPITECH_AUTH)
    projects = []
    for i in modules:
        projects += get_module_projects(EPITECH_AUTH, i)
    return projects
