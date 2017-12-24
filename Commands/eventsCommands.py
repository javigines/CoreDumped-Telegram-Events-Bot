#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Functions.basicData as bd
import Functions.eventsFunctions as ef
import Functions.message as ms

def birthdayList(bot, update, args=None):
    bd.startWithCommand(bot, update)

    eventList = ef.birthdayListFunction(args=args)

    if(eventList is None or eventList == {} or
     eventList == [] or eventList == ""):
 		bot.sendMessage(chat_id=bd.chat_id, text=ms.noBirthdaySaved)
        
    elif(eventList==1):
       bot.sendMessage(chat_id=bd.chat_id, text=ms.dateUnknown)

    else:
        #TODO Manejar listado devuelto
        print(eventList)

def birthdayCheck(bot, update, args=None):
    bd.startWithCommand(bot, update)

    eventList = ef.birthdayListFunction()



def birhdayRemove(bot, update, args=None):
    bd.startWithCommand(bot, update)


def birthdayAdd(bot, update, args=None):
    bd.startWithCommand(bot, update)




def eventList(bot, update):
    bd.startWithCommand(bot, update)


def eventCheck(bot, update):
    bd.startWithCommand(bot, update)


def eventRemove(bot, update):
    bd.startWithCommand(bot, update)


def eventAdd(bot, update):
    bd.startWithCommand(bot, update)
