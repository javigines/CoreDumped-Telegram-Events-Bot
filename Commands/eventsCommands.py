#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Functions.basicData as bd
import Functions.eventsFunctions as ef
import Functions.message as ms

def birthdayList(bot, update, args=None):
    bd.startWithCommand(bot, update)

    eventList = ef.birthdayListFunction(args=args)

    if(eventList is None or eventList == {} or eventList == [] or eventList == ""):
     bot.sendMessage(chat_id=bd.chat_id, text=ms.noBirthdaySaved)

    elif(eventList==1):
       bot.sendMessage(chat_id=bd.chat_id, text=ms.dateUnknown)

    else:
        formatedEventList = ''
        lap = 1
        for event in eventList:
            formatedEventList += (str(lap) + '. ' + event['summary'].split('|')[0] + ': ' +
                                    event['start']['date'] + '\n')
            lap += 1
        if bd.user_id == bd.chatIDDeveloper:
            bot.sendMessage(chat_id=bd.chat_id, text=formatedEventList)
        else:
            if(bd.chat_id != bd.user_id):
                bot.sendMessage(chat_id=bd.chat_id, text=ms.groupListUser)
            else:
                bot.sendMessage(chat_id=bd.chat_id, text=formatedEventList)


def birthdayRemove(bot, update, args=None):
    bd.startWithCommand(bot, update)

    if not bd.user_id is bd.chatIDDeveloper:
        bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin)

    if not ef.birthdayCheckFunction(str(''.join(args))):
        bot.sendMessage(chat_id=bd.chat_id, text=ms.removeFailNotUser)

    else:
        result = ef.birthdayRemoveFunction(args=args)
        if(result is None or result == {} or result == [] or result == ""):
            bot.sendMessage(chat_id=bd.chat_id, text=ms.removeFailNotUser)

        elif(result==1):
            bot.sendMessage(chat_id=bd.chat_id, text=ms.formatErrorRemove)

        else:
            bot.sendMessage(chat_id=bd.chat_id, text=ms.removeBirthdayDone)


def birthdayAdd(bot, update, args=None):
    bd.startWithCommand(bot, update)

    if ef.birthdayCheckFunction(str(bd.user_id)):
        bot.sendMessage(chat_id=bd.chat_id, text=ms.askForDelete)

    else:
        result = ef.birthdayAddFunction(args=args, summary=(bd.username+'|'+str(bd.user_id)))
        if(result is None or result == {} or result == [] or result == ""):
            bot.sendMessage(chat_id=bd.chat_id, text=ms.notDate)

        elif(result==1):
            bot.sendMessage(chat_id=bd.chat_id, text=ms.formatErrorBirthday)

        elif(result==2):
            bot.sendMessage(chat_id=bd.chat_id, text=ms.notValidBirthday)

        else:
            bot.sendMessage(chat_id=bd.chat_id, text=ms.newBirthdayAdded)




def eventList(bot, update):
    bd.startWithCommand(bot, update)


def eventCheck(bot, update):
    bd.startWithCommand(bot, update)


def eventRemove(bot, update):
    bd.startWithCommand(bot, update)


def eventAdd(bot, update):
    bd.startWithCommand(bot, update)
