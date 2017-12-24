#!/usr/bin/env python
# -*- coding: utf-8 -*-


## Debug chat_id
chatIDDeveloper = 372406715
## Chat_id from group you what to announce events greetings
chatIDCoreDumped = -1001088278003

## Usefull Variables
message = None
username = None
chat_id = None
user_id = None


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


print("BasicData Module Loaded")
