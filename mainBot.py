#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging																## System module
import os
logFile= os.path.dirname(os.path.abspath(__file__)) + os.sep+'/.logs/logCoreBot.log'
try:
	logging.basicConfig(
	filename=logFile,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO
	)
except Exception as e:
	print("Se ha generado la siguiente excepción:\n\n"+str(e)+"\n\nCorrijala para ejecutar el programa.")
	os._exit(1)

logging.info(('-'*30)+' Bot Starting '+('-'*30))
logging.getLogger('googleapiclient.discovery').setLevel(logging.WARNING)

from subprocess import call													## System module
from sys import argv														## System module
from time import sleep														## System module
# Usefull for /restartB
if(len(argv)>1):
	sleep(2)
	call("kill -9 " + str(argv[1]), shell=True)
	logging.info('Bot restarting complete.')
	sleep(2)

from datetime import datetime, time, timedelta								## System module

from telegram.ext import Updater, CommandHandler, RegexHandler, JobQueue	## pip install python-telegram-bot

import Functions.basicData as bd											## Own module
import Functions.reminder as rmr											## Own module
import Commands.basicCommands as bc											## Own module
import Commands.utilsCommands as uc											## Own module
import Commands.eventsCommands as ec										## Own module

try:
	token_file = open("token.txt", 'r')
except Exception as e:
	print("Se ha generado la siguiente excepción:\n\n"+str(e)+"\n\nCorrijala para ejecutar el programa.")
	os._exit(1)

bc.logFile = logFile
token = token_file.readline()
token_file.close()

updater = Updater(token, workers=200)
dispatcher = updater.dispatcher
dispatcher.add_error_handler(bd.basicErrorTelegramHandler)


# Initialize "Command" handlers
# Basic Commands
start_handler = CommandHandler(list(['start','help']), bc.start, pass_args=False, allow_edited=True)
dispatcher.add_handler(start_handler)
restart_handler = CommandHandler(list(['restartP','rebootP']), bc.restartP, pass_args=False, allow_edited=True)
dispatcher.add_handler(restart_handler)
stop_handler = CommandHandler('stopP', bc.stopP, pass_args=False, allow_edited=True)
dispatcher.add_handler(stop_handler)
leave_handler = CommandHandler('leave', bc.leaveGroup, pass_args=False, allow_edited=True)
dispatcher.add_handler(leave_handler)
changelog_handler = CommandHandler('changelog', bc.changelog, pass_args=False, allow_edited=True)
dispatcher.add_handler(changelog_handler)
contact_handler = CommandHandler('contact', bc.contact, pass_args=True, allow_edited=True)
dispatcher.add_handler(contact_handler)
logging.info('Basic commands loaded correctly.')

# Utils Commands
update_handler = CommandHandler('updateP', uc.updateP, pass_args=False, allow_edited=True)
dispatcher.add_handler(update_handler)
speak_handler = CommandHandler('speakP', uc.speakP, pass_args=True, allow_edited=True)
dispatcher.add_handler(speak_handler)
download_handler = CommandHandler('downloadP', uc.downloadP, pass_args=True, allow_edited=True)
dispatcher.add_handler(download_handler)
clearLog_handler = CommandHandler('clearlogP', uc.clearLogP, allow_edited=True)
dispatcher.add_handler(clearLog_handler)
publiP_handler = CommandHandler('publiP', uc.publiP, allow_edited=True)
dispatcher.add_handler(publiP_handler)
logging.info('Utils commands loaded correctly.')

# Events Commands
birthdayList_handler = CommandHandler('birthdayList', ec.birthdayList, pass_args=True, allow_edited=True)
dispatcher.add_handler(birthdayList_handler)
remove_handler = CommandHandler(list(['removeB','deleteB']), ec.birthdayRemove, pass_args=True, allow_edited=True)
dispatcher.add_handler(remove_handler)
addB_handler = CommandHandler('birthday', ec.birthdayAdd, pass_args=True, allow_edited=True)
dispatcher.add_handler(addB_handler)
eventList_handler = CommandHandler('eventList', ec.eventList, pass_args=True, allow_edited=True)
dispatcher.add_handler(eventList_handler)
eventRemove_handler = RegexHandler('\/removeE_*', ec.eventRemove, pass_groups=True)
dispatcher.add_handler(eventRemove_handler)
event_handler = CommandHandler('event', ec.eventAdd, pass_args=True, allow_edited=True)
dispatcher.add_handler(event_handler)
eventInfo_handler = RegexHandler('\/info_*', ec.eventInfo, pass_groups=True)
dispatcher.add_handler(eventInfo_handler)
logging.info('Events commands loaded correctly.')


#Jobs (Scheduler)
job_queue = JobQueue(updater.bot)
job_queue.run_daily(rmr.birthdayReminder, time(hour=8, minute=0, second=0), name='birthdayReminderJob')
job_queue.run_daily(rmr.eventReminder, time(hour=20, minute=0, second=0), name='eventWeeklyReminderJob', context={'monthly':False,'weekly':True,'daily':False,'hourly':False}, days=(6,))
job_queue.run_daily(rmr.eventReminder, time(hour=8, minute=0, second=0), name='eventDailyReminderJob', context={'monthly':False,'weekly':False,'daily':True,'hourly':False})
job_queue.run_repeating(rmr.eventReminder, interval=60, first=(datetime.now().replace(second=0,microsecond=0) + timedelta(minutes=1)),name='eventHourlyReminderJob', context={'monthly':False,'weekly':False,'daily':False,'hourly':True})
job_queue.run_repeating(rmr.eventReminder, interval=60, first=(datetime.now().replace(second=0,microsecond=0) + timedelta(minutes=1)), name='eventNowReminderJob', context={'monthly':False,'weekly':False,'daily':False,'hourly':False})
job_queue.start()
logging.info('Jobs loaded correctly.')


updater.start_polling(timeout=30)

logging.info('MainBot Completly Loaded.')
logging.info('Bot Working.')
updater.bot.sendMessage(chat_id=bd.chatIDDeveloper, text="Bot Iniciado")

updater.idle()
