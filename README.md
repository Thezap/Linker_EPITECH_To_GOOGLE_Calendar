# Linker_EPITECH_To_GOOGLE_Calendar
Link Epitech calendar to google calendar

# Usage :

Create a config.json with this template

```
{
    "CALENDAR_ID":"",
    "EPITECH_AUTH":""
}
```

Go to https://developers.google.com/calendar/quickstart/python and click on "Enable the google calendar API". Create a project and download client configuration.

Copy the credentials.json on this folder.

Launch `python3 main.py`, connect your google account and now the script is ready.

You can it in a crontab to fetch event at regular time.