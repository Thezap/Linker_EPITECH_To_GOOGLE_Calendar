# Linker_EPITECH_To_GOOGLE_Calendar
Link your Epitech calendar to your Google calendar.

# Installation:

## Basics
- Clone this repository.
- Create a `config.json` file with the following content:

```json
{
    "CALENDAR_ID": "",
    "EPITECH_AUTH": ""
}
```

## Configuration
### Authentications
#### Add your Epitech autologin ID.

This ID can be found on https://intra.epitech.eu/admin/autolog.

You need to copy-paste `auth-XXXX` in the `config.json` file for the `EPITECH_AUTH` key.

#### Add your Calendar ID.

First things first, you can create an Epitech sub-calendar. This step is not mandatory, but creating a sub-calendar improves your general calendar clarity and its organisation.
To do so, create a new calendar by clicking on this menu:
![New Calendar](https://i.imgur.com/GWeeuUF.png)

Then, select the `Settings and sharing` menu option for this sub-calendar:
![Settings and sharing](https://s24454.pcdn.co/wp-content/uploads/2015/10/Capture.jpg)

Press `Ctrl+F`, search for `Calendar ID` in the page and copy-paste the address `XXXX@group.calendar.google.com` in the `config.json` file for the `CALENDAR_ID` key.


In the end, your configuration file should look like this:
```json
{
    "CALENDAR_ID": "XXXX@group.calendar.google.com",
    "EPITECH_AUTH": "auth-XXXX"
}
```

### APIs configuration

Go to https://developers.google.com/calendar/quickstart/python and click on "Enable the Google Calendar API". Create a project and download the client configuration. The `credentials.json` must be located in the program directory.

Run `sudo pip install --upgrade google-api-python-client oauth2client` to install the Google API library.

Run `python3 main.py` to execute the program. *You will need to connect to your Google account the first time.*

Your `tree` should look like this:

```
$ tree
.
├── calendar_craller.py
├── calendar.log
├── config.json
├── credentials.json
├── main.py
├── parser.py
├── README.md
└── token.json

1 directory, 10 files
```

# Notes
You can setup a crontab to synchronise your Epitech calendar regularly. (https://crontab.guru)
