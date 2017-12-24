#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from random import randint

import Functions.basicData as bd
import Functions.eventsFunctions as ef
import Functions.message as ms

def birthdayReminder(bot, job):

	eventList = ef.birthdayListFunction(args=[datetime.now().strftime('%d-%m-%Y')])

	if not(eventList is None or eventList == {} or eventList == [] or eventList == "" or eventList==1):
		for event in eventList:
			bot.sendMessage(chat_id=bd.chatIDDeveloper,
				text=ms.birthdayGreetings[randint(0, len(ms.birthdayGreetings)-1)].replace("$args1", event['summary'].split('|')[0]).replace("$args2", str(int(datetime.now().strftime('%Y'))-int(event['summary'].split('|')[2]))))
			bot.sendMessage(chat_id=bd.chatIDCoreDumped,
				text=ms.birthdayGreetings[randint(0, len(ms.birthdayGreetings)-1)].replace("$args1", event['summary'].split('|')[0]).replace("$args2", str(int(datetime.now().strftime('%Y'))-int(event['summary'].split('|')[2]))))
