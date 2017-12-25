#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import logging												## System module
log = logging.getLogger(__name__)

import httplib2
import os

from apiclient import discovery
from oauth2client import client, tools
from oauth2client.file import Storage

from datetime import datetime

import Functions.message as ms

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar CoreDumpedBot'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-manager.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def getService():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    return service


def getCalendars():

    service = getService()

    return service.calendarList().list().execute()["items"]

def checkCalendar(calendarData, calendarParam):

    calendarList = getCalendars()

    for calendar in calendarList:
        if calendarData in calendar[calendarParam]:
            return calendar
    return False

def createCalendar(calendarSettings):

    service = getService()

    if not checkCalendar(calendarSettings["summary"], "summary"):
        return service.calendars().insert(body=calendarSettings).execute()
    return False

def removeCalendar(calendarID):

    service = getService()

    if calendarID == "primary":
        service.calendars().clear(calendarId=calendarID).execute()
        return True
    else:
        if checkCalendar(calendarSettings.id):
            service.calendars().delete(calendarId=calendarID).execute()
            return True
    return False



def getEvents(calendarId, dateMin=None, dateMax=None):

    service = getService()

    if dateMin is None and dateMax is None:
        return service.events().list(calendarId=calendarId).execute()["items"]
    else:
        return service.events().list(calendarId=calendarId, timeMin=dateMin, timeMax=dateMax).execute()["items"]

def checkEvent(eventId, calendarId):

    service = getService()

    eventList = getEvents(calendarId)

    for event in eventList:
        if eventId in event["id"]:
            return event

    return False

#event {dateStart:"dd/mm/AAAA XX:XX:XX", name="Evento X", repeat:1, reminder={20,120}}
#repeat: 0=Never, 1=Daily, 2=Weekly, 3=Monthly, 4=Yearly  // reminder=time in sec before date
def createEvent(event, calendarId):

    service = getService()

    #datetimeEventStart = datetime.strptime(event['dateStart'], "%d/%m/%Y %H/%M/%S")
    #datetimeEventEnd = datetime.strptime(event['dateEnd'], "%d/%m/%Y %H/%M/%S")

    calendarList = getCalendars()

    if checkCalendar(calendarId, 'id'):
        return service.events().insert(calendarId=calendarId, body=event).execute()
    else:
        return ms.calendarAddNotCalendarId

def removeEvent(eventId, calendarId):

    service = getService()
    if checkCalendar(calendarId, 'id'):
        if checkEvent(eventId, calendarId):
            return service.events().delete(calendarId=calendarId, eventId=eventId).execute()
        else:
            return ms.eventNotFound
    else:
        return ms.calendarNotFound


log.info('GoogleCalendarQuickFunctions Module Loaded.')
