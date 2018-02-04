#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging												## System module
log = logging.getLogger(__name__)

from datetime import datetime, timedelta					## System module
from random import randint									## System module
from pytz import timezone									## pip install pytz

import Functions.basicData as bd							## Own module
import Functions.eventsFunctions as ef						## Own module
import Functions.message as ms								## Own module


def birthdayReminder(bot, job):

	eventList = ef.birthdayListFunction(args=[datetime.now().strftime('%d-%m-%Y')])

	if not(eventList is None or eventList == {} or eventList == [] or eventList == "" or eventList==1):
		for event in eventList:
			bot.sendMessage(chat_id=bd.chatIDDeveloper,
				text=ms.birthdayGreetings[randint(0, len(ms.birthdayGreetings)-1)].replace("$args1", event['summary'].split('|')[0]).replace("$args2", str(int(datetime.now().strftime('%Y'))-int(event['summary'].split('|')[2]))))
			bot.sendMessage(chat_id=bd.chatIDCoreDumped,
				text=ms.birthdayGreetings[randint(0, len(ms.birthdayGreetings)-1)].replace("$args1", event['summary'].split('|')[0]).replace("$args2", str(int(datetime.now().strftime('%Y'))-int(event['summary'].split('|')[2]))))


def eventReminder(bot, job):

	if job.context['weekly']:
		eventList = ef.eventListFunction(args=[datetime.now().strftime('%d-%m-%Y')+'|'+(datetime.now()+timedelta(days=7)).strftime('%d-%m-%Y')])
		eventMessage = ms.eventsReminderWeekly
	elif job.context['daily']:
		eventList = ef.eventListFunction(args=[datetime.now().strftime('%d-%m-%Y')])
		eventMessage = ms.eventsReminderDaily
	elif job.context['hourly']:
		eventList = []
		dateTemp = datetime.now()+timedelta(minutes=60)
		eventListTemp = ef.eventListFunction(args=[dateTemp.strftime('%d-%m-%Y %H:%M')+' +00:01'])
		for event in eventListTemp:
			if event['start']['dateTime'] == timezone('Europe/Madrid').localize(dateTemp).astimezone(timezone('UTC')).strftime('%Y-%m-%dT%H:%M:%SZ'):
				eventList.append(event)
		eventMessage = ms.eventsReminderHourly
	else:
		eventList = []
		dateTemp = datetime.now()
		eventListTemp = ef.eventListFunction(args=[dateTemp.strftime('%d-%m-%Y %H:%M')+' +00:01'])
		for event in eventListTemp:
			if event['start']['dateTime'] == timezone('Europe/Madrid').localize(dateTemp).astimezone(timezone('UTC')).strftime('%Y-%m-%dT%H:%M:%SZ'):
				eventList.append(event)
		eventMessage = ms.eventsReminderStart

	if not(eventList is None or eventList == {} or eventList == [] or eventList == "" or eventList==1):
		eventTempMessage = ''
		for event in eventList:
			date = timezone('UTC').localize(datetime.strptime(event['start']['dateTime'], '%Y-%m-%dT%H:%M:%SZ')).astimezone(timezone('Europe/Madrid')).strftime("%d-%m-%Y %H:%M")
			eventTempMessage += ms.eventReminder.replace('$args1', '"'+event['summary']+'"').replace('$args2', date).replace('$args3', '/info_' + event['id']) + '\n\n'

		bot.sendMessage(chat_id=bd.chatIDDeveloper, text=eventMessage.replace('$args1', eventTempMessage))
		bot.sendMessage(chat_id=bd.chatIDCoreDumped, text=eventMessage.replace('$args1', eventTempMessage))


log.info('Reminder Module Loaded.')
