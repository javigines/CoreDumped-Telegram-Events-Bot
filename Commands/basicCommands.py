#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call									## System module
from os import _exit, getpid								## System module
from random import randint

import Functions.basicData as bd
import Functions.message as ms


#Command /start or /help
def start(bot, update):
    bd.startWithCommand(bot, update)

    bot.sendMessage(chat_id=bd.chat_id, text=ms.helpOrStart)


# Command /restartB or /rebootB
def restartB(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.restarting)
		call("./startBot.sh " + str(getpid()), shell=True)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])


# Command /stopB
def stopB(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.stopping)
		_exit(1)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])


# Command /updateB
def updateB(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper:
		bot.sendMessage(chat_id=bd.chatIDDeveloper, text=ms.updating)
		call("wget -qP /$HOME/BirthdayBot/ https://api.github.com/repos/javigines/EventsBot-CoreDumped/tarball/master", shell=True)
		call("tar -xzf /$HOME/BirthdayBot/master -C $HOME", shell=True)
		call("rm -f /$HOME/BirthdayBot/master*", shell=True)
		call("cp -rf $HOME/javigines-EventsBot-CoreDumped-*/* $HOME/BirthdayBot/ ", shell=True)
		call("rm -rf $HOME/javigines-EventsBot-CoreDumped-*/", shell=True)

		bot.sendMessage(chat_id=bd.chatIDDeveloper, text=ms.updateDone)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])


# Leave the group /leaveB
def leaveGroup(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper and update.effective_chat != None and update.effective_chat.type != "private":
		bot.sendMessage(chat_id=bd.chat_id, text=ms.leaving)
		bot.getChat(chat_id=bd.chat_id).leave()

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])


# Changelog command /changelog
def changelogB(bot, update):
	bd.startWithCommand(bot, update)

	if bd.user_id == bd.chatIDDeveloper or bd.user_id == bd.chat_id:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.changelog)

	else:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.groupChangelogUser)


print("BasicCommands Module Loaded")
