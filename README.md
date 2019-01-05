# Linker_EPITECH_To_GOOGLE_Calendar
Link Epitech calendar to Google calendar

# Usage :

Create a config.json with this template

```
{
    "CALENDAR_ID":"",
    "EPITECH_AUTH":""
}
```
For the `EPITECH_AUTH`, go to https://intra.epitech.eu/admin/autolog and copy the auth code starting by `auth-`.

To get your `CALENDAR_ID`, follow this documentation : https://docs.simplecalendar.io/find-google-calendar-id/


Go to https://developers.google.com/calendar/quickstart/python and click on "Enable the google calendar API". Create a project and download client configuration.

Copy the credentials.json on this folder.

Run `sudo pip install --upgrade google-api-python-client oauth2client` to install the google api library.

Launch `python3 main.py` and connect your Google account
Your Google Calendar should be updated with the epitech one.

You can set a crontab to fetch event at regular time (https://crontab.guru/).
