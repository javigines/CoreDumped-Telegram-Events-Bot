#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging												## System module
log = logging.getLogger(__name__)

from subprocess import call									## System module
from os import _exit, getpid								## System module
from random import randint									## System module

import Functions.basicData as bd							## Own module
import Functions.message as ms								## Own module


#Command /start or /help
def start(bot, update):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.helpOrStart, reply_to_message_id=bd.message.message_id)


# Command /restartP or /rebootP (Private)
def restartP(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.restarting, reply_to_message_id=bd.message.message_id)
		call("./startBot.sh " + str(getpid()), shell=True)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)


# Command /stopP (Private)
def stopP(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.stopping, reply_to_message_id=bd.message.message_id)
		_exit(1)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)


# Command /updateP (Private)
def updateP(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		bot.sendMessage(chat_id=bd.chatIDDeveloper, text=ms.updating, reply_to_message_id=bd.message.message_id)
		call("wget -qP /$HOME/BirthdayBot/ https://api.github.com/repos/javigines/EventsBot-CoreDumped/tarball/master", shell=True)
		call("tar -xzf /$HOME/BirthdayBot/master -C $HOME", shell=True)
		call("rm -f /$HOME/BirthdayBot/master*", shell=True)
		call("cp -rf $HOME/javigines-EventsBot-CoreDumped-*/* $HOME/BirthdayBot/ ", shell=True)
		call("rm -rf $HOME/javigines-EventsBot-CoreDumped-*/", shell=True)

		bot.sendMessage(chat_id=bd.chatIDDeveloper, text=ms.updateDone)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)


# Leave the group /leave
def leaveGroup(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper and update.effective_chat != None and update.effective_chat.type != "private":
		bot.sendMessage(chat_id=bd.chat_id, text=ms.leaving, reply_to_message_id=bd.message.message_id)
		bot.getChat(chat_id=bd.chat_id).leave()

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)


# Changelog command /changelog
def changelog(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper or bd.user_id == bd.chat_id:
		changelogStr = ""
		changelog = open("CHANGELOG.md", mode="r")
		changelogTemp = changelog.read()
		changelog.close()
		changelogTemp = "## [" + changelogTemp.split("## [")[2] + "## ["+ changelogTemp.split("## [")[1]+"\n\nPara ver el changelog completo:\nhttps://goo.gl/eHrop3"
		changelogTemp = changelogTemp.split("\n")
		for line in changelogTemp:
			if "###" in line:
				line = line.replace("###", "_")+ "_"
			if "##" in line:
				line = line.replace("##", "*") + "*"
			changelogStr += line + "\n"
		bot.sendMessage(chat_id=bd.chat_id, text=changelogStr, reply_to_message_id=bd.message.message_id, parse_mode="MARKDOWN")

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.groupChangelogUser, reply_to_message_id=bd.message.message_id)


# Changelog command /speak
def speak(bot, update, args):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		try:
			bot.sendMessage(chat_id=args[0], text=' '.join(args).split('|')[1])
			bot.sendMessage(chat_id=bd.chat_id, text=ms.messageSend, reply_to_message_id=bd.message.message_id)
		except:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.incorrectChatId, reply_to_message_id=bd.message.message_id)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)

# Changelog command /contact
def contact(bot, update, args):
	bd.startWithCommand(bot, update)

	try:
		bot.sendMessage(chat_id=bd.chatIDDeveloper, text=ms.contactMessage.replace('$args1', bd.username).replace('$args2', str(bd.user_id)).replace('$args3', ' '.join(args)))
		bot.sendMessage(chat_id=bd.chat_id, text=ms.messageSend, reply_to_message_id=bd.message.message_id)
	except Exception as e:
		log.error(str(e))
		bot.sendMessage(chat_id=bd.chat_id, text=ms.errorExecCommandUser, reply_to_message_id=bd.message.message_id)

# Download file command /downloadp (Private)
def downloadP(bot, update, args):
	bd.startWithCommand(bot, update, args)

	if bd.user_id == bd.chatIDDeveloper:
		try:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.downloadInProgress, reply_to_message_id=bd.message.message_id)
			fileDocument = open("".join(args), mode="rb")
			bot.sendDocument(chat_id=bd.chatIDDeveloper, document=fileDocument, reply_to_message_id=bd.message.message_id)
			fileDocument.close()
			bot.sendMessage(chat_id=bd.chat_id, text=ms.downloadComplete, reply_to_message_id=bd.message.message_id)
		except Exception as e:
			log.error(str(e))
			bot.sendMessage(chat_id=bd.chat_id, text=ms.errorExecCommandUser, reply_to_message_id=bd.message.message_id)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)


log.info('BasicCommands Module Loaded.')
