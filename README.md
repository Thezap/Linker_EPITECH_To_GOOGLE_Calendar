# Linker_EPITECH_To_GOOGLE_Calendar
Link your Epitech calendar to your Google calendar.

# Installation:

### Basics
- Clone this repository.
- Create a `config.json` file with the following content:

```json
{
    "CALENDAR_ID": "",
    "EPITECH_AUTH": ""
}
```

### Configuration
- `EPITECH_AUTH`: add your Epitech autologin ID.

This ID can be found on https://intra.epitech.eu/admin/autolog.

You need to copy paste `auth-XXXX` into the file.

- `CALENDAR_ID`: add your Calendar ID.

First things first, you can create an Epitech sub-calendar. This step is not mandatory, but creating a sub-calendar improves your general calendar clarity and its organisation.
To do so, create a new calendar by clicking on this menu:
![New Calendar](https://i.imgur.com/GWeeuUF.png)

Then, select the `Settings and sharing` menu option for this sub-calendar:
![Settings and sharing](https://s24454.pcdn.co/wp-content/uploads/2015/10/Capture.jpg)

Search for `Calendar ID` in the page by pressing `Ctrl+F` and copy-paste the address `XXXX@group.calendar.google.com` in the configuration file.

- APIs configuration

Go to https://developers.google.com/calendar/quickstart/python and click on "Enable the Google Calendar API". Create a project and download the client configuration. The `credentials.json` must be located in the program directory.

Run `sudo pip install --upgrade google-api-python-client oauth2client` to install the Google API library.

Run `python3 main.py` once to link your Google account.

You can setup a crontab to update your Epitech calendar regularly. (https://crontab.guru)
