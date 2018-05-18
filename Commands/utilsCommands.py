#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A library that provides functionality to the @CoreDumped_EventsBot
# Copyright (C) 2017-2018
# Javier Gines Sanchez <software@javisite.com>
#


import logging  # System module
log = logging.getLogger(__name__)

from subprocess import call  # System module
import os  # System module
from platform import system  # System module
from sys import exc_info
from random import randint  # System module

import Functions.basicData as bd  # Own module
import Functions.message as ms  # Own module


# Command /updateP (Private)
def updateP(bot, update):
    bd.startWithCommand(bot, update)

    if bd.user_id in bd.chat_id_authorized:
        if system() == "Linux":
            try:
                bot.sendMessage(chat_id=bd.chat_id_authorized[1], text=ms.updating)
                call("wget -qP /$HOME/EventsBot/ https://api.github.com/repos/javigines/EventsBot-CoreDumped/tarball/master", shell=True)
                call("tar -xzf /$HOME/EventsBot/master -C $HOME", shell=True)
                call("rm -f /$HOME/EventsBot/master*", shell=True)
                call("cp -rf $HOME/javigines-EventsBot-CoreDumped-*/* $HOME/EventsBot/ ", shell=True)
                call("rm -rf $HOME/javigines-EventsBot-CoreDumped-*/", shell=True)

                bot.sendMessage(chat_id=bd.chat_id_authorized[1], text=ms.updateDone)
            except Exception as e:
                bd.exceptionHandler(bot, update, __name__, e)

        else:
            bot.sendMessage(chat_id=bd.chat_id, text=ms.updateWrongOS, reply_to_message_id=bd.message.message_id)

    else:
        bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(
            0, len(ms.notAdmin) - 1)], reply_to_message_id=bd.message.message_id)


# Download file command /downloadp (Private)
def downloadP(bot, update, args):
    bd.startWithCommand(bot, update, args)

    if bd.user_id in bd.chat_id_authorized[:2]:
        try:
            if args == "" or args == None or args == [] or args == {}:
                bot.sendMessage(chat_id=bd.chat_id, text=ms.downloadNoArgs, reply_to_message_id=bd.message.message_id)
            else:
                bot.sendMessage(chat_id=bd.chat_id, text=ms.downloadInProgress)
                fileDocument = open("".join(args), mode="rb")
                bot.sendDocument(chat_id=bd.chat_id_authorized[1], document=fileDocument,
                                 reply_to_message_id=bd.message.message_id)
                fileDocument.close()
                bot.sendMessage(chat_id=bd.chat_id, text=ms.downloadComplete)
        except Exception as e:
            bd.exceptionHandler(bot, update, __name__, e, args)

    else:
        bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(
            0, len(ms.notAdmin) - 1)], reply_to_message_id=bd.message.message_id)

# Send Log File /getLogP (Private)


def getLogP(bot, update):
    bd.startWithCommand(bot, update)

    if bd.user_id in bd.chat_id_authorized:
        try:
            bot.sendMessage(chat_id=bd.chat_id, text=ms.downloadInProgress, reply_to_message_id=bd.message.message_id)
            fileLog = open(logging.getLoggerClass().root.handlers[0].baseFilename, "rb")
            bot.sendDocument(chat_id=bd.chat_id_authorized[1],
                             document=fileLog)
            fileLog.close()
            bot.sendMessage(chat_id=bd.chat_id, text=ms.downloadComplete, reply_to_message_id=bd.message.message_id)
            log.info("Log Download By User")
        except Exception as e:
            bd.exceptionHandler(bot, update, __name__, e)

    else:
        bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(
            0, len(ms.notAdmin) - 1)], reply_to_message_id=bd.message.message_id)


# Clear log File command /clearLogP (Private)
def clearLogP(bot, update):
    bd.startWithCommand(bot, update)

    if bd.user_id in bd.chat_id_authorized:
        try:
            getLogP(bot, update)
            with open(logging.getLoggerClass().root.handlers[0].baseFilename, "w"):
                pass
            bot.sendMessage(chat_id=bd.chat_id, text=ms.clearlogComplete, reply_to_message_id=bd.message.message_id)
            log.info("Log Clean By User")
        except Exception as e:
            bd.exceptionHandler(bot, update, __name__, e)

    else:
        bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(
            0, len(ms.notAdmin) - 1)], reply_to_message_id=bd.message.message_id)


# Send spam (like a boss) command /publip (Private)
def publiP(bot, update):
    bd.startWithCommand(bot, update)

    if bd.user_id in bd.chat_id_authorized:
        try:
            bot.sendMessage(chat_id=bd.chat_id, text=ms.spamMessage[randint(
                0, len(ms.spamMessage) - 1)], reply_to_message_id=bd.message.message_id)
        except Exception as e:
            bd.exceptionHandler(bot, update, __name__, e)

    else:
        bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(
            0, len(ms.notAdmin) - 1)], reply_to_message_id=bd.message.message_id)


log.info('UtilsCommands Module Loaded.')
