#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging												## System module
log = logging.getLogger(__name__)

from random import randint									## System module
from datetime import datetime								## System module
from pytz import timezone									## pip install pytz

import Functions.basicData as bd							## Own module
import Functions.eventsFunctions as ef						## Own module
import Functions.message as ms                              ## Own module


# Command /birthdayList
def birthdayList(bot, update, args=None):
    bd.startWithCommand(bot, update, args)

    eventList = ef.birthdayListFunction(args=args)

    if(eventList is None or eventList == {} or eventList == [] or eventList == ""):
        bot.sendMessage(chat_id=bd.chat_id, text=ms.noBirthdaySaved)

    elif(eventList==1):
       bot.sendMessage(chat_id=bd.chat_id, text=ms.dateUnknown)

    else:
        formatedEventList = ''
        lap = 1
        for event in eventList:
            formatedEventList += (str(lap) + '. ' + event['summary'].split('|')[0] + ': ' + event['summary'].split('|')[2] +
            '-' + event['start']['date'].split("-")[1] + '-' + event['start']['date'].split("-")[2] + '\n')
            lap += 1
        if bd.user_id == bd.chatIDDeveloper:
            bot.sendMessage(chat_id=bd.chat_id, text=formatedEventList)
        else:
            if(bd.chat_id != bd.user_id):
                bot.sendMessage(chat_id=bd.chat_id, text=ms.groupListUser)
            else:
                bot.sendMessage(chat_id=bd.chat_id, text=formatedEventList)

# Command /removeB
def birthdayRemove(bot, update, args=None):
    bd.startWithCommand(bot, update, args)

    if bd.user_id != bd.chatIDDeveloper:
        bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])

    else:
        if not ef.birthdayCheckFunction(str(''.join(args))):
            bot.sendMessage(chat_id=bd.chat_id,
            text=ms.removeFailNotUser.replace("$args1", str(''.join(args))))

        else:
            result = ef.birthdayRemoveFunction(args=args)
            if(result is None or result == {} or result == [] or result == ""):
                bot.sendMessage(chat_id=bd.chat_id,
                text=ms.removeFailNotUser.replace("$args1", str(''.join(args))))

            elif(result==1):
                bot.sendMessage(chat_id=bd.chat_id, text=ms.formatErrorRemoveB)

            else:
                bot.sendMessage(chat_id=bd.chat_id,
                text=ms.removeBirthdayDone.replace("$args1", str(''.join(args))))

# Command /birthday
def birthdayAdd(bot, update, args=None):
    bd.startWithCommand(bot, update, args)

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
            bot.sendMessage(chat_id=bd.chat_id,
            text=ms.newBirthdayAdded.replace("$args1", bd.username).replace("$args2", ' '.join(args)))


# Command /eventList
def eventList(bot, update, args=None):
    bd.startWithCommand(bot, update, args)

    eventList = ef.eventListFunction(args=args)

    if(eventList is None or eventList == {} or eventList == [] or eventList == ""):
        bot.sendMessage(chat_id=bd.chat_id, text=ms.noEventSaved)

    elif(eventList==1):
       bot.sendMessage(chat_id=bd.chat_id, text=ms.dateUnknown)

    else:
        formatedEventList = ''
        lap = 1
        for event in eventList:
            date = timezone('UTC').localize(datetime.strptime(event['start']['dateTime'], '%Y-%m-%dT%H:%M:%SZ')).astimezone(timezone('Europe/Madrid')).strftime("%d-%m-%Y %H:%M")
            formatedEventList += (str(lap) + '. ' + event['summary'] + ': ' + date +
            '\nMore Info: /info_' + event['id'] + '\n\n')
            lap += 1
        if bd.user_id == bd.chatIDDeveloper:
            bot.sendMessage(chat_id=bd.chat_id, text=formatedEventList)
        else:
            if(bd.chat_id != bd.user_id):
                bot.sendMessage(chat_id=bd.chat_id, text=ms.groupListUser)
            else:
                bot.sendMessage(chat_id=bd.chat_id, text=formatedEventList)

# Command /removeE
def eventRemove(bot, update, args=None):
    bd.startWithCommand(bot, update, args)

    if bd.user_id != bd.chatIDDeveloper:
        bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])

    else:
        if not ef.eventCheckFunction(str(''.join(args))):
            bot.sendMessage(chat_id=bd.chat_id,
            text=ms.removeFailNotEvent.replace("$args1", str(''.join(args))))

        else:
            result = ef.eventRemoveFunction(args=args)
            if(result is None or result == {} or result == [] or result == ""):
                bot.sendMessage(chat_id=bd.chat_id,
                text=ms.removeFailNotEvent.replace("$args1", str(''.join(args))))

            elif(result==1):
                bot.sendMessage(chat_id=bd.chat_id, text=ms.formatErrorRemoveE)

            else:
                bot.sendMessage(chat_id=bd.chat_id,
                text=ms.removeEventDone.replace("$args1", str(''.join(args))))

# Command /event
def eventAdd(bot, update, args=None):
    bd.startWithCommand(bot, update, args)

    if bd.user_id != bd.chatIDDeveloper:
        bot.sendMessage(chat_id=bd.chat_id, text=ms.notAdmin[randint(0, len(ms.notAdmin)-1)])

    else:
        result = ef.eventAddFunction(args=args, data=(bd.username+'|/|'+str(bd.user_id)))
        if(result is None or result == {} or result == [] or result == ""):
            bot.sendMessage(chat_id=bd.chat_id, text=ms.formatErrorEvent)

        elif(result==1):
            bot.sendMessage(chat_id=bd.chat_id, text=ms.formatErrorEvent)

        else:
            date = timezone('UTC').localize(datetime.strptime(result['start']['dateTime'], '%Y-%m-%dT%H:%M:%SZ')).astimezone(timezone('Europe/Madrid')).strftime("%d-%m-%Y %H:%M")
            bot.sendMessage(chat_id=bd.chat_id, text=ms.newEventAdded.replace("$args1", result['summary']).replace("$args2", date))


# Internal Command /info_***
def eventInfo(bot, update, groups=None):
    bd.startWithCommand(bot, update, groups)

    event = ef.eventInfoFunction(bd.message.text.split(' ')[0][6:])

    if(not event or event is None or event == {} or event == [] or event == ""):
        bot.sendMessage(chat_id=bd.chat_id, text=ms.eventNotFound)

    else:
        log.info(event)
        eventDescription = ms.eventDescription
        eventDescription = eventDescription.replace("$args1", event['summary'])
        date = timezone('UTC').localize(datetime.strptime(event['start']['dateTime'], '%Y-%m-%dT%H:%M:%SZ')).astimezone(timezone('Europe/Madrid')).strftime("%d-%m-%Y %H:%M")
        eventDescription = eventDescription.replace("$args2", date)
        if(event['description'].split('/&/')[0].split('|/|')[1].strip()) != "":
            eventDescription = eventDescription.replace("$args3", event['description'].split('/&/')[0].split('|/|')[1])
        else:
            eventDescription = eventDescription.replace("$args3", "(No definido)")
        if(event['description'].split('/&/')[0].split('|/|')[0].strip() != ""):
            eventDescription = eventDescription.replace("$args4", event['description'].split('/&/')[0].split('|/|')[0])
        else:
            eventDescription = eventDescription.replace("$args4", "(No definido)")
        if(event['description'].split('/&/')[0].split('|/|')[2].strip() != ""):
            eventDescription = eventDescription.replace("$args5", event['description'].split('/&/')[0].split('|/|')[2])
        else:
            eventDescription = eventDescription.replace("$args5", "(No definido)")
        eventDescription = eventDescription.replace("$args6", event['id'])

        bot.sendMessage(chat_id=bd.chat_id, text=eventDescription)



log.info('EventsCommands Module Loaded.')
