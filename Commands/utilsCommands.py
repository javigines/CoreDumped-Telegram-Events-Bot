#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging												## System module
log = logging.getLogger(__name__)

from subprocess import call									## System module
import os													## System module
from platform import system									## System module
from random import randint									## System module

import Functions.basicData as bd							## Own module
import Functions.message as ms								## Own module


# Command /updateP (Private)
def updateP(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		if system() == "Linux":
			try:
				bot.sendMessage(chat_id=bd.chatIDDeveloper, text=ms.updating)
				call("wget -qP /$HOME/BirthdayBot/ https://api.github.com/repos/javigines/EventsBot-CoreDumped/tarball/master", shell=True)
				call("tar -xzf /$HOME/BirthdayBot/master -C $HOME", shell=True)
				call("rm -f /$HOME/BirthdayBot/master*", shell=True)
				call("cp -rf $HOME/javigines-EventsBot-CoreDumped-*/* $HOME/BirthdayBot/ ", shell=True)
				call("rm -rf $HOME/javigines-EventsBot-CoreDumped-*/", shell=True)

				bot.sendMessage(chat_id=bd.chatIDDeveloper, text=ms.updateDone, reply_to_message_id=bd.message.message_id)
			except Exception as e:
				log.error(str(e))
				bot.sendMessage(chat_id=bd.chat_id, text=ms.errorExecCommandUser, reply_to_message_id=bd.message.message_id)

		else:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.updateWrongOS, reply_to_message_id=bd.message.message_id)


	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)


# Changelog command /speakP
def speakP(bot, update, args):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		try:
			bot.sendMessage(chat_id=args[0], text=' '.join(args).split('|')[1])
			bot.sendMessage(chat_id=bd.chat_id, text=ms.messageSend, reply_to_message_id=bd.message.message_id)
		except Exception as e:
			log.error(str(e))
			bot.sendMessage(chat_id=bd.chat_id, text=ms.incorrectChatId, reply_to_message_id=bd.message.message_id)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)


# Download file command /downloadp (Private)
def downloadP(bot, update, args):
	bd.startWithCommand(bot, update, args)

	if bd.user_id == bd.chatIDDeveloper:
		try:
			if args == "" or args == None or args == [] or args == {}:
				bot.sendMessage(chat_id=bd.chat_id, text=ms.downloadNoArgs, reply_to_message_id=bd.message.message_id)
			else:
				bot.sendMessage(chat_id=bd.chat_id, text=ms.downloadInProgress)
				fileDocument = open("".join(args), mode="rb")
				bot.sendDocument(chat_id=bd.chatIDDeveloper, document=fileDocument, reply_to_message_id=bd.message.message_id)
				fileDocument.close()
				bot.sendMessage(chat_id=bd.chat_id, text=ms.downloadComplete)
		except Exception as e:
			log.error(str(e))
			bot.sendMessage(chat_id=bd.chat_id, text=ms.errorExecCommandUser, reply_to_message_id=bd.message.message_id)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)


# Clear log File command /clearLogP (Private)
def clearLogP(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		try:
			with open(logging.getLoggerClass().root.handlers[0].baseFilename, "w"):
				pass
			bot.sendMessage(chat_id=bd.chat_id, text=ms.clearlogComplete)
			log.info("Log Clean By User")
		except Exception as e:
			log.error(str(e))
			bot.sendMessage(chat_id=bd.chat_id, text=ms.errorExecCommandUser, reply_to_message_id=bd.message.message_id)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)


log.info('UtilsCommands Module Loaded.')
