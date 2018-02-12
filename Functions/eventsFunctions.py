#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging												## System module
log = logging.getLogger(__name__)

from datetime import datetime, timedelta					## System module
from sys import exc_info
from pytz import timezone									## pip install pytz

import Functions.googleCalendarQuickFunctions as gc			## Own module


def translateStringToDatetime(date):
	finaldate = {}
	try:
#		Date only Month
		if(date.lower() in ["january","enero"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=1)
			finaldate["dateEnd"] = datetime.now().replace(day=31, month=1)

			return finaldate
		elif(date.lower() in ["february","febrero"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=2)
			finaldate["dateEnd"] = datetime.now().replace(day=28, month=2)

			return finaldate
		elif(date.lower() in ["march","marzo"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=3)
			finaldate["dateEnd"] = datetime.now().replace(day=31, month=3)

			return finaldate
		elif(date.lower() in ["april","abril"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=4)
			finaldate["dateEnd"] = datetime.now().replace(day=30, month=4)

			return finaldate
		elif(date.lower() in ["may","mayo"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=5)
			finaldate["dateEnd"] = datetime.now().replace(day=31, month=5)

			return finaldate
		elif(date.lower() in ["june","junio"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=6)
			finaldate["dateEnd"] = datetime.now().replace(day=30, month=6)

			return finaldate
		elif(date.lower() in ["july","julio"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=7)
			finaldate["dateEnd"] = datetime.now().replace(day=31, month=7)

			return finaldate
		elif(date.lower() in ["august","agosto"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=8)
			finaldate["dateEnd"] = datetime.now().replace(day=31, month=8)

			return finaldate
		elif(date.lower() in ["september","septiembre"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=9)
			finaldate["dateEnd"] = datetime.now().replace(day=30, month=9)

			return finaldate
		elif(date.lower() in ["october","octubre"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=10)
			finaldate["dateEnd"] = datetime.now().replace(day=31, month=10)

			return finaldate
		elif(date.lower() in ["november","noviembre"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=11)
			finaldate["dateEnd"] = datetime.now().replace(day=30, month=11)

			return finaldate
		elif(date.lower() in ["december","diciembre"]):
			finaldate["dateStart"] = datetime.now().replace(day=1, month=12)
			finaldate["dateEnd"] = datetime.now().replace(day=31, month=12)

			return finaldate

#		Date only Year
		elif(len(date)==4):
			date = int(date)
			if date >1899 and date < 3000:
				finaldate["dateStart"] = datetime.now().replace(day=1, month=1, year=date)
				finaldate["dateEnd"] = datetime.now().replace(day=31, month=12, year=date)

				return finaldate

#		Date Complete with Duration
		elif(len(date.split(" "))==3):
			dateTemp = None
			time = None
			duration = None

			if '.' in date.split(" ")[0]:
				dateTemp = "/".join(date.split(" ")[0].split("."))
			elif '-' in date.split(" ")[0]:
				dateTemp = "/".join(date.split(" ")[0].split("-"))
			else:
				dateTemp = date.split(" ")[0]

			if '.' in date.split(" ")[1]:
				time = ":".join(date.split(" ")[1].split("."))
			elif '-' in date.split(" ")[1]:
				time = ":".join(date.split(" ")[1].split("-"))
			else:
				time = date.split(" ")[1]

			if '.' in date.split(" ")[2]:
				duration = int(date.split(" ")[2].replace('+','').split(".")[0])*60 + int(date.split(" ")[2].split(".")[1])
			elif '-' in date.split(" ")[2]:
				duration = int(date.split(" ")[2].replace('+','').split("-")[0])*60 + int(date.split(" ")[2].split("-")[1])
			elif ':' in date.split(" ")[2]:
				duration = int(date.split(" ")[2].replace('+','').split(":")[0])*60 + int(date.split(" ")[2].split(":")[1])

			finaldate["dateStart"] = datetime.strptime(dateTemp+' '+time, '%d/%m/%Y %H:%M')
			finaldate["dateEnd"] = (datetime.strptime(dateTemp+' '+time, '%d/%m/%Y %H:%M') + timedelta(minutes=duration))

			return finaldate

#		Date without Time
		elif(len(date.split(" "))==1 and (len(date.split("-"))==3 or len(date.split("/"))==3 or
			len(date.split("."))==3)):
			date = "/".join(date.split("."))
			date = "/".join(date.split("-"))
			finaldate["dateStart"] = datetime.strptime(date, '%d/%m/%Y')
			finaldate["dateEnd"] = datetime.strptime(date, '%d/%m/%Y') + timedelta(days=1)

			return finaldate

#		No more combination if not Return Date Unknown
		finaldate["dateStart"] = None
		finaldate["dateEnd"] = None

		return finaldate

	except Exception as e:
		log.error(str(e)+ " - Line "+ str(exc_info()[2].tb_lineno))
		finaldate["dateStart"] = None
		finaldate["dateEnd"] = None

		return finaldate


def birthdayListFunction(args=None):
	calendar = gc.checkCalendar("birthdaysCalendar", "summary")

	if not calendar:
		newCalendar = {}
		newCalendar["summary"] = "birthdaysCalendar"

		calendar = gc.createCalendar(newCalendar)
		return None

	if args is None or args == '' or args == []:
		eventList = gc.getEvents(calendar['id'])
	else:
		if(''.join(args).find("|") != -1):
			date["dateStart"] = translateStringToDatetime(date=''.join(args).split("|")[0])["dateStart"]
			date["dateEnd"] = translateStringToDatetime(date=''.join(args).split("|")[1])["dateStart"]
		else:
			date = translateStringToDatetime(date=''.join(args))

		if(date['dateStart']==None or date['dateEnd']==None):
			return 1

		eventList = gc.getEvents(calendar['id'], date["dateStart"].strftime("%Y-%m-%dT%XZ"), date["dateEnd"].strftime("%Y-%m-%dT%XZ"))
	return eventList

def birthdayCheckFunction(user_id):
	eventList = birthdayListFunction()

	for event in eventList:
		if user_id in event['summary']:
			return True
	return False

def birthdayRemoveFunction(args):
	calendar = gc.checkCalendar("birthdaysCalendar", "summary")

	if not calendar:
		newCalendar = {}
		newCalendar["summary"] = "birthdaysCalendar"

		calendar = gc.createCalendar(newCalendar)
		return None


	if args is None or args == '' or args == []:
		return 1
	else:
		eventList = gc.getEvents(calendar['id'])
		for event in eventList:
			if ''.join(args) in event['summary']:
				gc.removeEvent(event['id'].split("_")[0], calendar['id'])
				return 200

def birthdayAddFunction(args, summary):
	calendar = gc.checkCalendar("birthdaysCalendar", "summary")

	if not calendar:
		newCalendar = {}
		newCalendar["summary"] = "birthdaysCalendar"

		calendar = gc.createCalendar(newCalendar)


	if args is None or args == '' or args == []:
		return None
	else:
		date = translateStringToDatetime(date=''.join(args))
		if(date['dateStart']==None or date['dateEnd']==None):
			return 1
		if ((datetime.now().year - date['dateStart'].year) < 0 or (datetime.now().year - date['dateStart'].year) > 120 or
			(date['dateEnd'] - date['dateStart']).total_seconds() != 86400):
			return 2

		event = {
		'summary': summary+'|'+date['dateStart'].strftime("%Y"),
		'start': {
			'date': date['dateStart'].strftime("%Y-%m-%d"),
			'timeZone': 'Europe/Madrid',
			},
		'end': {
			'date': date['dateEnd'].strftime("%Y-%m-%d"),
			'timeZone': 'Europe/Madrid',
			},
		'recurrence': [
			'RRULE:FREQ=YEARLY;'
			],
		}

		return gc.createEvent(event=event, calendarId=calendar['id'])


def eventListFunction(args=None):
	date = {"dateStart":None, "dateEnd":None}
	calendar = gc.checkCalendar("eventsCalendar", "summary")

	if not calendar:
		newCalendar = {}
		newCalendar["summary"] = "eventsCalendar"

		calendar = gc.createCalendar(newCalendar)
		return None

	if args is None or args == '' or args == []:
		eventList = gc.getEvents(calendar['id'])
	else:
		if(''.join(args).find("|") != -1):
			date["dateStart"] = translateStringToDatetime(date=''.join(args).split("|")[0])["dateStart"]
			date["dateEnd"] = translateStringToDatetime(date=''.join(args).split("|")[1])["dateStart"]
		else:
			date = translateStringToDatetime(date=''.join(args))

		if(date['dateStart']==None or date['dateEnd']==None):
			return 1


		eventList = gc.getEvents(calendar['id'], timezone('Europe/Madrid').localize(date["dateStart"]).astimezone(timezone('UTC')).strftime("%Y-%m-%dT%XZ"),
		 timezone('Europe/Madrid').localize(date["dateEnd"]).astimezone(timezone('UTC')).strftime("%Y-%m-%dT%XZ"))
	return eventList

def eventCheckFunction(event_id):
	calendar = gc.checkCalendar("eventsCalendar", "summary")

	if not calendar:
		newCalendar = {}
		newCalendar["summary"] = "eventsCalendar"

		calendar = gc.createCalendar(newCalendar)
		return False

	return gc.checkEvent(eventId=event_id, calendarId=calendar['id'])

def eventRemoveFunction(args):
	calendar = gc.checkCalendar("eventsCalendar", "summary")

	if not calendar:
		newCalendar = {}
		newCalendar["summary"] = "eventsCalendar"

		calendar = gc.createCalendar(newCalendar)
		return None


	if args is None or args == '' or args == []:
		return 1
	else:
		gc.removeEvent(''.join(args), calendar['id'])
		return 200

def eventAddFunction(args, data):
	calendar = gc.checkCalendar("eventsCalendar", "summary")

	if not calendar:
		newCalendar = {}
		newCalendar["summary"] = "eventsCalendar"

		calendar = gc.createCalendar(newCalendar)


	if ((args is None) or (args == '') or (args == []) or (len((' '.join(args)).split('|'))!=5) or
	(' '.join(args).split('|')[0].strip() == "") or (' '.join(args).split('|')[1].strip() == "")):
		return None
	else:
		date = translateStringToDatetime(date=(' '.join(args)).split('|')[1].strip())

		if(date['dateStart']==None or date['dateEnd']==None):
			return 1

		event = {
		'summary': (' '.join(args)).split('|')[0],
		'description': '|/|'.join((' '.join(args)).split('|')[2:]) + '/&/' + data,
		'start': {
			'dateTime': date['dateStart'].astimezone(timezone('UTC')).strftime("%Y-%m-%dT%XZ"),
			},
		'end': {
			'dateTime': date['dateEnd'].astimezone(timezone('UTC')).strftime("%Y-%m-%dT%XZ"),
			},
		}

		return gc.createEvent(event=event, calendarId=calendar['id'])


def eventInfoFunction(eventId):
	calendar = gc.checkCalendar("eventsCalendar", "summary")

	if not calendar:
		newCalendar = {}
		newCalendar["summary"] = "eventsCalendar"

		calendar = gc.createCalendar(newCalendar)
		return None

	return gc.checkEvent(eventId, calendar['id'])


log.info('EventsFunctions Module Loaded.')
