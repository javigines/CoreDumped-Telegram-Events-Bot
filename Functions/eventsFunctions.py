#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Functions.googleCalendarQuickFunctions as gc
from datetime import datetime, timedelta

def translateStringToDatetime(date):

    try:
        if(date.lower() in ["january","enero"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=1),
                "dateEnd" = datetime.now().replace(day=31, month=1)
                }
                return finaldate
        elif(date.lower() in ["february","febrero"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=2),
                "dateEnd" = datetime.now().replace(day=28, month=2)
                }
                return finaldate
        elif(date.lower() in ["march","marzo"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=3),
                "dateEnd" = datetime.now().replace(day=31, month=3)
                }
                return finaldate
        elif(date.lower() in ["april","abril"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=4),
                "dateEnd" = datetime.now().replace(day=30, month=4)
                }
                return finaldate
        elif(date.lower() in ["may","mayo"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=5),
                "dateEnd" = datetime.now().replace(day=31, month=5)
                }
                return finaldate
        elif(date.lower() in ["june","junio"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=6),
                "dateEnd" = datetime.now().replace(day=30, month=6)
                }
                return finaldate
        elif(date.lower() in ["july","julio"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=7),
                "dateEnd" = datetime.now().replace(day=31, month=7)
                }
                return finaldate
        elif(date.lower() in ["august","agosto"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=8),
                "dateEnd" = datetime.now().replace(day=31, month=8)
                }
                return finaldate
        elif(date.lower() in ["september","septiembre"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=9),
                "dateEnd" = datetime.now().replace(day=30, month=9)
                }
                return finaldate
        elif(date.lower() in ["october","octubre"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=10),
                "dateEnd" = datetime.now().replace(day=31, month=10)
            }
            return finaldate
        elif(date.lower() in ["november","noviembre"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=11),
                "dateEnd" = datetime.now().replace(day=30, month=11)
            }
            return finaldate
        elif(date.lower() in ["december","diciembre"]):
            finaldate = {
                "dateStart" = datetime.now().replace(day=1, month=12),
                "dateEnd" = datetime.now().replace(day=31, month=12)
            }
            return finaldate

        elif(len(date)==4):
            date = int(date)
            if date >1899 and date < 3000:
                return {"dateStart" = datetime.now().replace(day=1, month=1, year=date),
                        "dateEnd" = datetime.now().replace(day=31, month=12, year=date)
                        }

        elif(len(date.split("-"))==3 or len(date.split("/"))==3 or
            len(date.split("."))==3):
            date = "/".join(date.split("."))
            date = "/".join(date.split("-"))
            return {"dateStart" = datetime.strptime(date, '%d/%m/%Y'),
                    "dateEnd" = datetime.strptime(date, '%d/%m/%Y') + timedelta(seconds=86399)
                    }
        return {"dateStart" = None, "dateEnd" = None}

    except:
        return {"dateStart" = None, "dateEnd" = None}


def birthdayListFunction(args=None):
    calendar = gc.checkCalendar("birtdaysCalendar", "summary")

    if not calendar:
        newCalendar = {
        "summary" = "birthdaysCalendar"
        }
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
        eventList = gc.getEvents(calendar['id'], date["dateStart"], date["dateEnd"])

    return eventList

def birthdayAddFunction(args):
    calendar = gc.checkCalendar("birtdaysCalendar", "summary")

    if not calendar:
        newCalendar = {
        "summary" = "birthdaysCalendar"
        }
        calendar = gc.createCalendar(newCalendar)


    if args is None or args == '' or args == []:
        return None
    else:
        date = translateStringToDatetime(date=''.join(args))
        if(date['dateStart']==None or date['dateEnd']==None):
            return 1

        event = {
          'start': {
            'dateTime': date['dateStart'],
            'timeZone': 'Europe/Madrid',
          },
          'end': {
            'dateTime': date['dateEnd'],
            'timeZone': 'Europe/Madrid',
          },
          'recurrence': [
            'RRULE:FREQ=YEARLY;'
          ],
        }

        return gc.createEvent(event=event, calendarId=calendar['id'])
