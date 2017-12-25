#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging												## System module
log = logging.getLogger(__name__)

import Functions.googleCalendarQuickFunctions as gc
from datetime import datetime, timedelta


def translateStringToDatetime(date):
    finaldate = {}
    try:
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

        elif(len(date)==4):
            date = int(date)
            if date >1899 and date < 3000:
                finaldate["dateStart"] = datetime.now().replace(day=1, month=1, year=date)
                finaldate["dateEnd"] = datetime.now().replace(day=31, month=12, year=date)

                return finaldate

        elif(len(date.split("-"))==3 or len(date.split("/"))==3 or
            len(date.split("."))==3):
            date = "/".join(date.split("."))
            date = "/".join(date.split("-"))
            finaldate["dateStart"] = datetime.strptime(date, '%d/%m/%Y')
            finaldate["dateEnd"] = datetime.strptime(date, '%d/%m/%Y') + timedelta(days=1)

            return finaldate

        finaldate["dateStart"] = None
        finaldate["dateEnd"] = None

        return finaldate

    except:
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
                gc.removeEvent(event['id'], calendar['id'])
                return 200


log.info('EventsFunctions Module Loaded.')
