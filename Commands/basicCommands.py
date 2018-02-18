#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A library that provides functionality to the @CoreDumped_EventsBot
# Copyright (C) 2017-2018
# Javier Gines Sanchez <software@javisite.com>
#

import logging												## System module
log = logging.getLogger(__name__)

from subprocess import call									## System module
from os import _exit, getpid								## System module
from sys import exc_info									## System module
from platform import system									## System module
from random import randint									## System module

import Functions.basicData as bd							## Own module
import Functions.message as ms								## Own module


#Command /start or /help
def start(bot, update):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.helpOrStart, reply_to_message_id=bd.message.message_id, disable_web_page_preview=True, parse_mode="MARKDOWN")


# Command /restartP or /rebootP (Private)
def restartP(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		if system() == "Linux":
			try:
				bot.sendMessage(chat_id=bd.chat_id, text=ms.restarting, reply_to_message_id=bd.message.message_id)
				call("./startBot.sh " + str(getpid()), shell=True)
			except Exception as e:
				bd.exceptionHandler(bot, update, __name__, e)

		else:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.restartWrongOS, reply_to_message_id=bd.message.message_id)
	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)
		bd.userNotAuthorizedMessage(bot, update)


# Command /stopP (Private)
def stopP(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		try:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.stopping, reply_to_message_id=bd.message.message_id)
			_exit(1)
		except Exception as e:
			bd.exceptionHandler(bot, update, __name__, e)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)
		bd.userNotAuthorizedMessage(bot, update)


# Leave the group /leave
def leaveGroup(bot, update):
	bd.startWithCommand(bot, update)

	if update.effective_chat != None and update.effective_chat.type != "private":
		admin = False

		if bd.message.chat.all_members_are_administrators:
			admin = True
		else:
			for adminMember in bd.message.chat.get_administrators():
				if adminMember['user']['id'] is bd.user_id:
					admin = True

		if bd.user_id == bd.chatIDDeveloper or admin:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.leaving, reply_to_message_id=bd.message.message_id)
			bot.getChat(chat_id=bd.chat_id).leave()
		else:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)], reply_to_message_id=bd.message.message_id)
			bd.userNotAuthorizedMessage(bot, update)
	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notGroupLeave, reply_to_message_id=bd.message.message_id)


# Changelog command /changelog
def changelog(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper or bd.user_id == bd.chat_id:
		try:
			changelogStr = ""
			changelog = open("CHANGELOG.md", mode="r")
			changelogTemp = changelog.read()
			changelog.close()
			changelogTemp = ms.changelogMessage.replace('$args1', "## [" + changelogTemp.split("## [")[2]).replace('$args2', "## ["+ changelogTemp.split("## [")[1])
			changelogTemp = changelogTemp.split("\n")
			for line in changelogTemp:
				if "###" in line:
					line = line.replace("###", "_")+ "_"
				if "##" in line:
					line = line.replace("##", "*") + "*"
				changelogStr += line + "\n"
			bot.sendMessage(chat_id=bd.chat_id, text=changelogStr, reply_to_message_id=bd.message.message_id, parse_mode="MARKDOWN")
		except Exception as e:
			bd.exceptionHandler(bot, update, __name__, e)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.groupChangelogUser, reply_to_message_id=bd.message.message_id)


# Changelog command /contact
def contact(bot, update, args):
	bd.startWithCommand(bot, update)

	if args is None or args == '' or args == []:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.contactNoMessage, reply_to_message_id=bd.message.message_id)

	else:
		bot.sendMessage(chat_id=bd.chatIDDeveloper, text=ms.contactMessage.replace('$args1', bd.username).replace('$args2', str(bd.user_id)).replace('$args3', ' '.join(args)))
		bot.sendMessage(chat_id=bd.chat_id, text=ms.messageSend, reply_to_message_id=bd.message.message_id)


log.info('BasicCommands Module Loaded.')
