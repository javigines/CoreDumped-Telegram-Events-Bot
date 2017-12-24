#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call									## System module
from sys import argv										## System module
from os import _exit, getpid								## System module
import logging												## System module
from random import randint									## System module
from time import gmtime, sleep, strftime					## System module
from datetime import datetime								## System module

import schedule												## pip install schedule
from telegram.ext import Updater, CommandHandler			## pip install python-telegram-bot

import Functions.basicData as bd
import Commands.basicCommands as bc
import Commands.eventsCommands as ec

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)

# Usefull for /restartB
if(len(argv)>1):
	sleep(2)
	call("kill -9 " + str(argv[1]), shell=True)
	sleep(2)

# Validate date format
def validate(date_text):
	try:
		return datetime.strptime(date_text, '%d/%m/%Y')
	except:
		return False

# Greetings or reminder
def happybirthday(before):
	data = bm.nextBirthday(before)
	i=0;
	if data is not None:
		while i<len(data):
			if not before:
				birthdaySentences = ms.birthdayGreetings

			else:
				birthdaySentences = ms.birthdayReminder

			updater.bot.sendMessage(chat_id=chatIDDeveloper,
			 text=birthdaySentences[randint(0, len(birthdaySentences)-1)].replace("$args1", data[i].split(":")[1]).replace("$args2", str(int(strftime('%Y', gmtime()))-int(data[i].split(":")[2]))))
			updater.bot.sendMessage(chat_id=chatIDCoreDumped,
			 text=birthdaySentences[randint(0, len(birthdaySentences)-1)].replace("$args1", data[i].split(":")[1]).replace("$args2", str(int(strftime('%Y', gmtime()))-int(data[i].split(":")[2]))))
			i+=1




token_file = open("token.txt", 'r')
token = token_file.readline()
token_file.close()

updater = Updater(token, workers=200)
dispatcher = updater.dispatcher

# Initialize "Command" handlers
# Basic Commands
start_handler = CommandHandler(list(['start','help']), bc.start, pass_args=False, allow_edited=True)
dispatcher.add_handler(start_handler)
restart_handler = CommandHandler(list(['restartB','rebootB']), bc.restartB, pass_args=False, allow_edited=True)
dispatcher.add_handler(restart_handler)
stop_handler = CommandHandler('stopB', bc.stopB, pass_args=False, allow_edited=True)
dispatcher.add_handler(stop_handler)
leave_handler = CommandHandler('leaveB', bc.leaveGroup, pass_args=False, allow_edited=True)
dispatcher.add_handler(leave_handler)
update_handler = CommandHandler('updateB', bc.updateB, pass_args=False, allow_edited=True)
dispatcher.add_handler(update_handler)
changelog_handler = CommandHandler('changelog', bc.changelogB, pass_args=False, allow_edited=True)
dispatcher.add_handler(changelog_handler)
speak_handler = CommandHandler('speak', bc.speak, pass_args=True, allow_edited=True)
dispatcher.add_handler(speak_handler)

addB_handler = CommandHandler('birthday', ec.birthdayAdd, pass_args=True, allow_edited=True)
dispatcher.add_handler(addB_handler)
remove_handler = CommandHandler(list(['removeB','deleteB']), ec.birthdayRemove, pass_args=True, allow_edited=True)
dispatcher.add_handler(remove_handler)
list_handler = CommandHandler(list(['listB','eventsB']), ec.birthdayList, pass_args=True, allow_edited=True)
dispatcher.add_handler(list_handler)
event_handler = CommandHandler('event', ec.birthdayAdd, pass_args=True, allow_edited=True)
dispatcher.add_handler(event_handler)

schedule.every().day.at("08:00").do(happybirthday,False)
schedule.every().day.at("20:00").do(happybirthday,True)


updater.start_polling(timeout=30)
print("MainBot Completly Loaded.\nBot Working...")
updater.bot.sendMessage(chat_id=bd.chatIDDeveloper, text="Bot Iniciado")

try:
	while 1:
		schedule.run_pending()
		sleep(1)
except (KeyboardInterrupt, TypeError):
	print("Exception")
finally:
	updater.idle()
	print("\nBot Stoped\nShuting down...")
