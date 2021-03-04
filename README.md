# Linker_EPITECH_To_GOOGLE_Calendar
Link your Epitech calendar to your Google calendar.

# Installation:

## Basics
- Clone this repository.
- Create a `config.json` file with the following content:

```json
{
    "CALENDAR_ID": "",
    "EPITECH_AUTH": "",
    "GetModules": false
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

![New Calendar](https://i.imgur.com/THXXkR0.png)

Then, select the `Settings and sharing` menu option for this sub-calendar:

![Settings and sharing](https://i.imgur.com/mvFQdWB.jpg)

Press `Ctrl+F`, search for `Calendar ID` in the page and copy-paste the address `XXXX@group.calendar.google.com` in the `config.json` file for the `CALENDAR_ID` key.

#### Specify your getter preference

If you want to retrieve modules' timeline in addition of projects' one, replace `false` by `true` in the `config.json` file for the `GetModules` key.

In the end, your configuration file should look like this:
```json
{
    "CALENDAR_ID": "XXXX@group.calendar.google.com",
    "EPITECH_AUTH": "auth-XXXX",
    "GetModules": false
}
```

### APIs configuration

Go to https://developers.google.com/calendar/quickstart/python and click on "Enable the Google Calendar API". Create a project and download the client configuration. The `credentials.json` must be located in the program directory.

Run `sudo pip3 install --upgrade google-api-python-client oauth2client` to install the Google API library, and `sudo pip3 install -r requirements.txt` to install all other dependencies.

If you do not have access to an internet browser (e.g., in a server context) run `python3 main.py --noauth_local_webserver` otherwise run `python3 main.py` to execute the program. *You will need to connect to your Google account the first time.*

# Notes
You can setup a crontab to synchronise your Epitech calendar regularly. (https://crontab.guru)
