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

import birthdayManager as bm								## Own module
import message as ms										## Own module

## Debug chat_id
chatIDDeveloper = 372406715
## Chat_id from group you what to announce events greetings
chatIDCoreDumped = -1001088278003


## Usefull Variables
message = None
username = None
chat_id = None
user_id = None


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

def startWithCommand(bot, update, args=['']):
	global message
	global username
	global chat_id
	global user_id

	if update.message == None:
		message = update.edited_message
	else:
		message = update.message

	username = message.from_user.name
	chat_id = message.chat.id
	user_id = message.from_user.id
	bot.sendMessage(chat_id=chatIDDeveloper, text=message.text.split(' ')[0] + ' ' + ' '.join(args) + ' --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")


#Command /startB or /helpB
def startB(bot, update):
	startWithCommand(bot, update)

	bot.sendMessage(chat_id=chat_id, text=ms.helpOrStart)

#Command /birthday
def addBirthday(bot, update, args=None):
	startWithCommand(bot, update, args=args)

	if args is None or args == '' or args == [] or not validate(args[0]):
		bot.sendMessage(chat_id=chat_id, text=ms.formatErrorBirthday)

	elif bm.checkBirthday(str(user_id)):
		bot.sendMessage(chat_id=chat_id, text=ms.askForDelete)

	else:
		if bm.addBirthday(username, args[0], str(user_id)):
			bot.sendMessage(chat_id=chat_id, text=ms.newBirthdayAdded.replace("$args1", username).replace("$args2", args[0]))

		else:
			bot.sendMessage(chat_id=chatIDDeveloper, text=ms.errorExecCommandAdmin.replace("$args1", message.text.split(' ')[0]).replace("$args2", str(args))
				.replace("$args3", username).replace("$args4", str(chat_id)).replace("$args4", str(user_id)))
			bot.sendMessage(chat_id=chat_id, text=ms.errorExecCommandUser)


#Command /event
def addEvent(bot, update, args=None):
	startWithCommand(bot, update, args=args)



#Command /removeB or /deleteB
def removeB(bot, update, args=None):
	startWithCommand(bot, update, args=args)

	if user_id == chatIDDeveloper:
		if (args is not None and args != '' and args != []):
			if bm.checkBirthday(args[0]):
				# Convert username to user_id
				if args[0][0:1] == "@":
					for key, value in bm.listBirthday().items():
						if value.split(":")[0] == args[0]:
							args[0]=key
				# Get username
				name = dict(bm.listBirthday()).get(args[0])
				if bm.removeBirthday(args[0]):
					bot.sendMessage(chat_id=chat_id, text=ms.removeBirthdayDone.replace("$args1", name.split(":")[0]))

				else:
					bot.sendMessage(chat_id=chatIDDeveloper, text=ms.errorExecCommandAdmin.replace("$args1", message.text.split(' ')[0]).replace("$args2", str(args))
						.replace("$args3", username).replace("$args4", str(chat_id)).replace("$args4", str(user_id)))
					bot.sendMessage(chat_id=chat_id, text=ms.errorExecCommandUser)

			else:
				bot.sendMessage(chat_id=chat_id, text=ms.removeFailNotUser.replace("$args1", args[0]))

		else:
			bot.sendMessage(chat_id=chat_id, text=ms.formatErrorRemove)

	else:
		bot.sendMessage(chat_id=chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])


# Command /listB or /eventsB
def listB(bot, update, args=None):
	startWithCommand(bot, update, args=args)

	birthdaylist = bm.listBirthday()
	if birthdaylist is not None:
		if user_id == chatIDDeveloper:
			if(args==None or args == '' or args == [] or args[0] != str(True)):
				i=0
				newbirthdayString = ""
				while(i<len(birthdaylist)):
					newbirthdayString += (str(i+1) + ". " + list(birthdaylist.values())[i].split(":")[0] + "  --->	" + list(birthdaylist.values())[i].split(":")[1] + "\n")
					i+=1
				birthdaylist = newbirthdayString

			bot.sendMessage(chat_id=chat_id, text=birthdaylist)

		else:
			if(chat_id != user_id):
				bot.sendMessage(chat_id=chat_id, text=ms.groupListUser)
			else:
				i=0
				newbirthdayString = ""
				while(i<len(birthdaylist)):
					newbirthdayString += (str(i+1) + ". " + list(birthdaylist.values())[i].split(":")[0] + "  --->	" + list(birthdaylist.values())[i].split(":")[1] + "\n")
					i+=1
				birthdaylist = newbirthdayString
				bot.sendMessage(chat_id=user_id, text=birthdaylist)
	else:
		bot.sendMessage(chat_id=chat_id, text=ms.noBirthdaySaved)


# Command /restartB or /rebootB
def restartB(bot, update):
	startWithCommand(bot, update)

	if user_id == chatIDDeveloper:
		bot.sendMessage(chat_id=chat_id, text=ms.restarting)
		call("./startBot.sh " + str(getpid()), shell=True)

	else:
		bot.sendMessage(chat_id=chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])


# Command /stopB
def stopB(bot, update):
	startWithCommand(bot, update)

	if user_id == chatIDDeveloper:
		bot.sendMessage(chat_id=chat_id, text=ms.stopping)
		_exit(1)

	else:
		bot.sendMessage(chat_id=chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])


# Command /updateB
def updateB(bot, update):
	startWithCommand(bot, update)

	if user_id == chatIDDeveloper:
		bot.sendMessage(chat_id=chatIDDeveloper, text=ms.updating)
		call("wget -qP /$HOME/BirthdayBot/ https://api.github.com/repos/javigines/BirthdayBot-CoreDumped/tarball/master", shell=True)
		call("tar -xzf /$HOME/BirthdayBot/master -C $HOME", shell=True)
		call("rm -f /$HOME/BirthdayBot/master*", shell=True)
		call("cp -rf $HOME/javigines-BirthdayBot-CoreDumped-*/* $HOME/BirthdayBot/ ", shell=True)
		call("rm -rf $HOME/javigines-BirthdayBot-CoreDumped-*/", shell=True)
		bot.sendMessage(chat_id=chatIDDeveloper, text=ms.updateDone)

	else:
		bot.sendMessage(chat_id=chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])

# Leave the group /leaveB
def leaveGroup(bot, update):
	startWithCommand(bot, update)

	if user_id == chatIDDeveloper and update.effective_chat != None and update.effective_chat.type != "private":
		bot.sendMessage(chat_id=chat_id, text=ms.leaving)
		updater.bot.getChat(chat_id=chat_id).leave()

	else:
		bot.sendMessage(chat_id=chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])


# Changelog command /changelog
def changelogB(bot, update):
	startWithCommand(bot, update)


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
start_handler = CommandHandler(list(['startB','helpb']), startB, pass_args=False, allow_edited=True)
dispatcher.add_handler(start_handler)
addB_handler = CommandHandler('birthday', addBirthday, pass_args=True, allow_edited=True)
dispatcher.add_handler(addB_handler)
event_handler = CommandHandler('event', addEvent, pass_args=True, allow_edited=True)
dispatcher.add_handler(event_handler)
remove_handler = CommandHandler(list(['removeB','deleteB']), removeB, pass_args=True, allow_edited=True)
dispatcher.add_handler(remove_handler)
list_handler = CommandHandler(list(['listB','eventsB']), listB, pass_args=True, allow_edited=True)
dispatcher.add_handler(list_handler)
restart_handler = CommandHandler(list(['restartB','rebootB']), restartB, pass_args=False, allow_edited=True)
dispatcher.add_handler(restart_handler)
stop_handler = CommandHandler('stopB', stopB, pass_args=False, allow_edited=True)
dispatcher.add_handler(stop_handler)
leave_handler = CommandHandler('leaveB', leaveGroup, pass_args=False, allow_edited=True)
dispatcher.add_handler(leave_handler)
update_handler = CommandHandler('updateB', updateB, pass_args=False, allow_edited=True)
dispatcher.add_handler(update_handler)
changelog_handler = CommandHandler('changelogB', changelogB, pass_args=False, allow_edited=True)
dispatcher.add_handler(changelog_handler)


schedule.every().day.at("08:00").do(happybirthday,False)
schedule.every().day.at("20:00").do(happybirthday,True)


updater.start_polling(timeout=30)
print("MainBot Completly Loaded.\nBot Working...")
updater.bot.sendMessage(chat_id=chatIDDeveloper, text="Bot Iniciado")

try:
	while 1:
		schedule.run_pending()
		sleep(1)
except (KeyboardInterrupt, TypeError):
	print("Exception")
finally:
	updater.idle()
	print("\nBot Stoped\nShuting down...")
