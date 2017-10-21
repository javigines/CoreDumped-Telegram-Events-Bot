#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess                                               ## System module
import sys
import os                                                       ## System module
import datetime                                                 ## System module
import logging                                                  ## System module
import time                                                     ## System module
from random import randint                                      ## System module
from time import gmtime, strftime                               ## System module

import schedule                                                 ## pip install schedule
from telegram.ext import Updater, CommandHandler                ## pip install python-telegram-bot

import birthdayManager as bm                                    ## Own module

## Debug chat_id
chatIDDeveloper = 372406715
## Chat_id from group you what to announce birthday greetings
chatIDCoreDumped = -1001088278003

finish = False
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.WARNING)

# Usefull for /restart
if(len(sys.argv)>1):
    subprocess.call("kill -9 " + str(sys.argv[1]), shell=True)
    time.sleep(3)

# Validate date format
def validate(date_text):
    try:
        return datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except:
        return False

#Command /start
def start(bot, update):
    username = update.message.from_user.name
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
    
    bot.sendMessage(chat_id=chatIDDeveloper, text='/start --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")
    bot.sendMessage(chat_id=chat_id, text='Para añadir tu cumpleaños escribe:\n/add 23/01/1997')

#Command /add
def add(bot, update, args=None):
    username = update.message.from_user.name
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id


    if args is None or not validate(args[0]):
        bot.sendMessage(chat_id=chat_id, text='No me estás enviando tu cumpleaños bien.\nEl formato es: "dd/mm/AAAA\n\n')
        
    elif bm.checkBirthday(username):
        bot.sendMessage(chat_id=chat_id, text='Ya he guardado tu cumpleaños.\nPide a @javigines que lo borre si no es correcto.')
        
    else:
        if bm.addBirthday(username, args[0]):
            bot.sendMessage(chat_id=chatIDDeveloper, text='/add '+ args[0] + ' --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")
            bot.sendMessage(chat_id=chat_id, text='Perfecto, he guardado tu cumple ' + username + ' en la fecha: '+ args[0])
            
        else:
            bot.sendMessage(chat_id=chatIDDeveloper, text='Error al ejecutar /add '+ str(args) + ' --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")
            bot.sendMessage(chat_id=chat_id, text='Ha ocurrido un error y se ha informado de él.')



#Command /remove
def remove(bot, update, args=None):
    username = update.message.from_user.name
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
	
    bot.sendMessage(chat_id=chatIDDeveloper, text='/remove --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")
    if chat_id == chatIDDeveloper:
        if (args is not None and args != '' and args != []):
            if bm.checkBirthday(args[0]):
                if bm.removeBirthday(args[0]):
                    bot.sendMessage(chat_id=chat_id, text='Cumpleaños de ' + args[0] + ' borrado correctamente.')
                    
                else:
                    bot.sendMessage(chat_id=chatIDDeveloper, text='Error al ejecutar /remove '+ str(args) + ' --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")
                    bot.sendMessage(chat_id=chat_id, text='Ha ocurrido un error y se ha informado de él')

            else:
                bot.sendMessage(chat_id=chat_id, text='No tengo el cumpleaños de ' + args[0] + ' en mi agenda.')

        else:
            bot.sendMessage(chat_id=chat_id, text='No has introducido /remove correctamente.')

    else:
        bot.sendMessage(chat_id=chat_id, text='No intentes borrar lo que no debes.')


# Command /list
def list(bot, update):
    username = update.message.from_user.name
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
    
    bot.sendMessage(chat_id=chatIDDeveloper, text='/list --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")
    if user_id == chatIDDeveloper:
        birthdaylist = bm.listBirthday()
        if birthdaylist is not None:
            bot.sendMessage(chat_id=chat_id, text=birthdaylist)
            
        else:
            bot.sendMessage(chat_id=chat_id, text="No tengo ningún cumpleaños guardado.")

    else:
        bot.sendMessage(chat_id=chat_id, text='Sorry, comando solo para admins del bot.')


# Command /restart
def restart(bot, update):
    username = update.message.from_user.name
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id

    bot.sendMessage(chat_id=chatIDDeveloper, text='/restart --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")
    if user_id == chatIDDeveloper:
        subprocess.call("python3.6 mainBot.py " + str(os.getpid()), shell=True)
#       subprocess.call(['exit'])

    else:
        bot.sendMessage(chat_id=chat_id, text='Estás tocando algo que no debes, huye mientras puedas, es una amenaza.')
        

# Command /stop
def stop(bot, update):
    username = update.message.from_user.name
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id

    bot.sendMessage(chat_id=chatIDDeveloper, text='/stop --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")
    if user_id == chatIDDeveloper:
        os._exit(1)

    else:
        bot.sendMessage(chat_id=chat_id, text='Estás tocando algo que no debes, huye mientras puedas, es una advertencia')
        


# Greetings or reminder 
def happybirthday(before):
    data = bm.nextBirthday(before)
    i=0;

    if data is not None:
        while i<len(data):
            if not before:
                birthdaySentences = ["Felicidades " + data[i].split(":")[0] + ", cabron@, eres un puto año más viejo. ",
                                    "Hueles un poco mal pero te felicito el cumpleaños " + data[i].split(":")[0] + ".",
                                    "Es tu Chachi cumple " + data[i].split(":")[0] + ", muchas felicidades de tu amigo el bot :)",
                                    "Pues no tienes mal aspecto para tus " + str(int(strftime('%Y', gmtime()))-int(data[i].split(":")[1]))+ " años " + data[i].split(":")[0],
                                    "Feliz cumpleaños " + data[i].split(":")[0] + " y sonrie mientras tengas todos los dientes.",
                                    "Te felicito " + data[i].split(":")[0] + " porque me han programado, si no ni eso.",
                                    "<FileNotFoundError: [Errno 2] No such file or directory: 'felicitaciones.txt' for " + data[i].split(":")[0],
                                    "Que cumplas muchos más " + data[i].split(":")[0] + " pero por favor un poco más rápido, que se me está haciendo muy largo.",
                                    "Que ni se te pase por la cabeza que estoy feliz porque cumplas un años más pero felicidades " + data[i].split(":")[0]
                                     ]

            else:
                birthdaySentences = ["Mañana parece que es el cumpleaños del desgra... del guap@ de " + data[i].split(":")[0],
                                    "Parece que vosotros los humanos teneis que felicitar mañana a " + data[i].split(":")[0],
                                    "El cab*** que me programó me obliga a recordaros el cumpleaños de " + data[i].split(":")[0],
                                    "Con un poco de suerte os mataré a todos antes de mañana...\n Pero por si acaso mañana es el cumpleaños de " + data[i].split(":")[0],
                                    "Ir mirando frases en google para felicitar a " + data[i].split(":")[0] + ", que mañana es su cumple.",
                                    "/ask Mañana es el cumple de " + data[i].split(":")[0] + " ?"
                                     ]
            
            updater.bot.sendMessage(chat_id=chatIDDeveloper, text=birthdaySentences[randint(0, len(birthdaySentences)-1)])
            updater.bot.sendMessage(chat_id=chatIDCoreDumped, text=birthdaySentences[randint(0, len(birthdaySentences)-1)])
            i+=1




token_file = open("token.txt", 'r')
token = token_file.readline()
token_file.close()

updater = Updater(token, workers=200)
dispatcher = updater.dispatcher

# Initialize "Command" handlers
start_handler = CommandHandler('start', start, pass_args=False)
dispatcher.add_handler(start_handler)
addB_handler = CommandHandler('add', add, pass_args=True)
dispatcher.add_handler(addB_handler)
remove_handler = CommandHandler('remove', remove, pass_args=True)
dispatcher.add_handler(remove_handler)
list_handler = CommandHandler('list', list, pass_args=False)
dispatcher.add_handler(list_handler)
restart_handler = CommandHandler('restart', restart, pass_args=False)
dispatcher.add_handler(restart_handler)
stop_handler = CommandHandler('stop', stop, pass_args=False)
dispatcher.add_handler(stop_handler)



schedule.every().day.at("08:00").do(happybirthday,False)
schedule.every().day.at("12:00").do(happybirthday,False)
schedule.every().day.at("12:00").do(happybirthday,True)


updater.start_polling(timeout=30)
print("mainBot Completly Loaded.\nBot Working...")
updater.bot.sendMessage(chat_id=chatIDDeveloper, text="Bot Iniciado")

try:
    while not finish:
        schedule.run_pending()
        time.sleep(1)
except (KeyboardInterrupt, TypeError):
    print("Exception")
finally:
    updater.idle()
    print("\nBot Stoped\nShuting down...")
