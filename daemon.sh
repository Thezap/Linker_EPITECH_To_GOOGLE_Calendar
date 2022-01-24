#!/usr/bin/env bash

while true; do
    python3 main.py --noauth_local_webserver
    if [ $? -eq 0 ] ; then
        echo "CALENDAR UPDATED"
    else
        echo "CALENDAR NOT UPDATED"
    fi
    sleep $SLEEP_TIME
done