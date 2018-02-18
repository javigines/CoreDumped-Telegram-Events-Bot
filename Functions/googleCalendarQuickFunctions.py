#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A library that provides functionality to the @CoreDumped_EventsBot
# Copyright (C) 2017-2018
# Javier Gines Sanchez <software@javisite.com>
#

import logging												## System module
log = logging.getLogger(__name__)

import os                                                   ## System module
from datetime import datetime								## System module

import httplib2												## pip install google-api-python-client
from apiclient import discovery                             ## pip install google-api-python-client
from oauth2client import client, tools						## pip install google-api-python-client
from oauth2client.file import Storage						## pip install google-api-python-client

import Functions.message as ms                              ## Own module



# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar CoreDumpedBot'
flags = tools.argparser.parse_args('--auth_host_name localhost --noauth_local_webserver --logging_level ERROR'.split())


def get_credentials():
	home_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep
	credential_dir = os.path.join(home_dir, '.credentials')
	if not os.path.exists(credential_dir):
		os.makedirs(credential_dir)
	credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')

	store = Storage(credential_path)
	credentials = store.get()
	if not credentials or credentials.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
		flow.user_agent = APPLICATION_NAME
		if flags:
			credentials = tools.run_flow(flow, store, flags)
		else:
			credentials = tools.run(flow, store)
		log.info('Storing credentials to ' + credential_path)
	return credentials



def getService():
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('calendar', 'v3', http=http, cache_discovery=False)
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
		return service.events().list(calendarId=calendarId, timeMin=datetime(year=datetime.now().year, month=1, day=1).strftime('%Y-%m-%dT00:00:00Z'), timeMax=datetime(year=datetime.now().year+1, month=1, day=1).strftime('%Y-%m-%dT00:00:00Z'), orderBy="startTime", singleEvents=True, maxResults=2500).execute()["items"]
	else:
		return service.events().list(calendarId=calendarId, timeMin=dateMin, timeMax=dateMax, orderBy="startTime", singleEvents=True, maxResults=2500).execute()["items"]

def checkEvent(eventId, calendarId):

	service = getService()

	eventList = getEvents(calendarId=calendarId, dateMin="1950-1-1T00:00:00Z", dateMax="2050-1-1T00:00:00Z")

	for event in eventList:
		if eventId in event["id"]:
			return event

	return False

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
