#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging												## System module
import os
logging.basicConfig(filename=os.path.dirname(os.path.abspath(__file__)) + os.sep+'/.logs/logCoreBot.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info(('-'*30)+' Bot Starting '+('-'*30))

from subprocess import call									## System module
from sys import argv										## System module
from time import sleep										## System module
from datetime import datetime, time							## System module

from telegram.ext import Updater, CommandHandler, RegexHandler, JobQueue	## pip install python-telegram-bot

import Functions.basicData as bd
import Functions.reminder as rmr
import Commands.basicCommands as bc
import Commands.eventsCommands as ec


# Usefull for /restartB
if(len(argv)>1):
	sleep(2)
	call("kill -9 " + str(argv[1]), shell=True)
	logging.info('Bot restarting complete.')
	sleep(2)


token_file = open("token.txt", 'r')
token = token_file.readline()
token_file.close()

updater = Updater(token, workers=200)
dispatcher = updater.dispatcher

# Initialize "Command" handlers
# Basic Commands
start_handler = CommandHandler(list(['start','help']), bc.start, pass_args=False, allow_edited=True)
dispatcher.add_handler(start_handler)
restart_handler = CommandHandler(list(['restartP','rebootP']), bc.restartB, pass_args=False, allow_edited=True)
dispatcher.add_handler(restart_handler)
stop_handler = CommandHandler('stopP', bc.stopB, pass_args=False, allow_edited=True)
dispatcher.add_handler(stop_handler)
leave_handler = CommandHandler('leave', bc.leaveGroup, pass_args=False, allow_edited=True)
dispatcher.add_handler(leave_handler)
update_handler = CommandHandler('updateP', bc.updateB, pass_args=False, allow_edited=True)
dispatcher.add_handler(update_handler)
changelog_handler = CommandHandler('changelog', bc.changelogB, pass_args=False, allow_edited=True)
dispatcher.add_handler(changelog_handler)
speak_handler = CommandHandler('speak', bc.speak, pass_args=True, allow_edited=True)
dispatcher.add_handler(speak_handler)
logging.info('Basic commands loaded correctly.')

# EventsFunctions Commands
addB_handler = CommandHandler('birthday', ec.birthdayAdd, pass_args=True, allow_edited=True)
dispatcher.add_handler(addB_handler)
remove_handler = CommandHandler(list(['removeB','deleteB']), ec.birthdayRemove, pass_args=True, allow_edited=True)
dispatcher.add_handler(remove_handler)
birthdayList_handler = CommandHandler('birthdayList', ec.birthdayList, pass_args=True, allow_edited=True)
dispatcher.add_handler(birthdayList_handler)
event_handler = CommandHandler('event', ec.eventAdd, pass_args=True, allow_edited=True)
dispatcher.add_handler(event_handler)
event_handler = CommandHandler(list(['removeE','deleteE']), ec.eventRemove, pass_args=True, allow_edited=True)
dispatcher.add_handler(event_handler)
eventList_handler = CommandHandler('eventList', ec.eventList, pass_args=True, allow_edited=True)
dispatcher.add_handler(eventList_handler)
eventInfo_handler = RegexHandler('\/info_*', ec.eventInfo, pass_groups=True)
dispatcher.add_handler(eventInfo_handler)
logging.info('Events commands loaded correctly.')


#Jobs (Scheduler)
job_queue = JobQueue(updater.bot)
job_queue.run_daily(rmr.birthdayReminder, time(hour=8, minute=00, second=00), name='birthdayReminderJob')
job_queue.run_daily(rmr.eventReminder, time(hour=20, minute=00, second=00), name='eventWeeklyReminderJob', context={'weekly':True}, days=(6,))
job_queue.run_daily(rmr.eventReminder, time(hour=19, minute=53, second=00), name='eventDailyReminderJob', context={'weekly':False})
job_queue.start()
logging.info('Jobs loaded correctly.')


updater.start_polling(timeout=30)

logging.info('MainBot Completly Loaded.')
logging.info('Bot Working.')
updater.bot.sendMessage(chat_id=bd.chatIDDeveloper, text="Bot Iniciado")

updater.idle()
