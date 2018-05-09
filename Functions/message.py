#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A library that provides functionality to the @CoreDumped_EventsBot
# Copyright (C) 2017-2018
# Javier Gines Sanchez <software@javisite.com>
#

import logging  # System module
log = logging.getLogger(__name__)


# Command /help or /start
helpOrStart = ('Las funciones y comandos del bot son los siguiente:\n\n' +
               '/birthday 23/01/1997 - _Añade tu cumpleaños al bot._\n' +
               '/birthdayList (january|18/01/2017|2017)) - _Listado de todos los cumpleaños o de los que se encuentren en la fecha._\n' +
               '/changelog - _Últimos cambios en actualizaciones del bot._\n' +
               '/eventList (january|18/01/2017|2017) - _Listado de todos los eventos o de los que se encuentren en la fecha._\n' +
               '/help - _Esta ayuda._\n' +
               '\n' +
               'Other Commands\n' +
               '/changelog - _Por si tienes interés, aquí tienes los últimos cambios realizados._\n' +
               '/contact - _¿Quieres contactar con el desarrollador? Escribe tu mensaje para que se lo envie._\n' +
               '\n' +
               'Todos los parámetros entre paréntesis son opcionales. En el caso de usarlos, no incluir el paréntesis.\n'
               )

helpOrStartAdmin = ('Las funciones y comandos del bot son los siguiente:\n\n' +
                    '/birthday 23/01/1997 - _Añade tu cumpleaños al bot._\n' +
                    '/birthdayList (january|18/01/2017|2017)) - _Listado de todos los cumpleaños o de los que se encuentren en la fecha._\n' +
                    '/changelog - _Últimos cambios en actualizaciones del bot._\n' +
                    '/eventList (january|18/01/2017|2017) - _Listado de todos los eventos o de los que se encuentren en la fecha._\n' +
                    '/help - _Esta ayuda._\n' +
                    '\n' +
                    'Other Commands\n' +
                    '/changelog - _Por si tienes interés, aquí tienes los últimos cambios realizados._\n' +
                    '/contact - _¿Quieres contactar con el desarrollador? Escribe tu mensaje para que se lo envie._\n' +
                    '\n' +
                    'Admin Events Commands\n' +
                    '/event Título del Evento | Fecha del Evento con Hora y Duración. Formato:(17/06/2017 18:45 +04:30) | (Impartido por) | (Descripción del Evento) | (Precio del Evento)\n' +
                    '- _En el comando /event campos opcionales no usados dejarlos en blanco pero con los separadores |._\n' +
                    '/removeB @Peter - _Borra el cumpleaños de la persona definida._\n' +
                    '/leave - _Si me encuentro en un grupo, lo abandono._\n' +
                    '\n' +
                    'Admin General Commands\n' +
                    '/restartP - _Reinicia el Bot._\n' +
                    '/stopP - _Detiene el Bot._\n' +
                    '/updateP - _Actualiza el Bot desde el repositorio original de GitHub._\n' +
                    '/downloadP File - _Descarga un archivo de servidor del Bot._\n' +
                    '/getLogP - _Descarga el log del Bot._\n' +
                    '/clearLogP - _Elimina el archivo de log el Bot._\n' +
                    '/publiP - _Spam del Bot._\n' +
                    '\n' +
                    'Todos los parámetros entre paréntesis son opcionales. En el caso de usarlos, no incluir el paréntesis.\n'
                    )

#Command /restartB
restartWrongOS = "El bot tiene que estar corriendo sobre Linux para usar esta opción."
restarting = "Reiniciando..."

#Command /stopB
stopping = "Deteniendo..."

#Command /updateB
updateWrongOS = "El bot tiene que estar corriendo sobre Linux para usar esta opción."
updating = "Actualizando..."
updateDone = 'Actualización completa. Reinicia para aplicar.'

# Command /leave
leaving = "Hasta Siempre..."
notGroupLeave = "Este chat no permite el comando /leave"

# Command /changelogB
changelogMessage = '$args1 $args2 \nPara ver el changelog completo:\nhttps://goo.gl/eHrop3'
groupChangelogUser = 'No queremos aburrir a la gente con el listado de cambios, ¿por qué no me lo preguntas por privado mejor?'

# Command /speak & /contact
contactMessage = 'El usuario $args1 ($args2) te ha enviado un mensaje:\n$args3'
contactNoMessage = "Es necesario incluir un mensaje seguido del comando."
messageSend = 'Mensaje enviado.'
incorrectChatId = 'El chat_id indicado no es válido o no tengo acceso a él.'

# Command /downloadp
downloadNoArgs = "Es necesario introducir argumentos para realizar la descarga"
downloadInProgress = "Enviando Archivo..."
downloadComplete = "Archivo enviado."

# Command /clearLogP
clearlogComplete = "Archivo de log borrado."

# Command /publip
spamMessage = [
    'Buenos días, soy el magnífico bot de Eventos de CoreDumped.\nQue tal si tú, sucio humano (que no tienes amigos), me introduces... (;D) tu cumpleaños con el comando /birthday para tener al menos mi felicitación ese día.']

# General Messages
errorExecCommandAdmin = 'Error al ejecutar $args1'
errorExecCommandUser = 'Ha ocurrido un error y se ha informado de él.'
userNotAuthorizedCommand = "Un usuario esta intentando usar un comando no autorizado:\n$args1"
notAdmin = ['No intentes hacer lo que no debes.',
            'Estás tocando algo que no debes, huye mientras puedas, es una amenaza.']


# Command /eventList && /birthdayList
groupListUser = "Pídeme el listado por privado para evitar hacer spam aquí.\n\n@CoreDumped_EventsBot"
noBirthdaySaved = "No tengo ningún cumpleaños guardado."
noEventSaved = "No tengo ningún evento guardado."
restrictBirthday = "Esta función esta restrigida a los usuarios pertenecientes a CoreDumped."

# Command /birthday
notDate = 'Tienes que escribir una fecha.'
formatErrorBirthday = 'No me estás enviando tu cumpleaños bien.\nEl formato es: "dd/mm/AAAA\n\n'
askForDelete = 'Ya tengo guardado tu cumpleaños.\nPide a @javigines o a un admin que lo borre si deseas cambiarlo.'
newBirthdayAdded = 'Perfecto, he guardado tu cumple $args1 en la fecha: $args2'
notValidBirthday = 'Cumpleaños no válido.'

# Command /event
notDateTitle = 'Tienes que escribir un título y una fecha.'
formatErrorEvent = ('No me estás enviando el nuevo evento bien. El formato es:\n' +
                    '\n/event Título del Evento | Fecha del Evento con Hora y Duración (17/06/2017 18:45 +04:30) | Impartido por(Opcional) | Descripción del Evento (Opcional) | Precio del Evento (Opcional)\n\n' +
                    'Campos opcionales no usados dejarlos en blanco pero con los separadores |')
newEventAdded = 'Perfecto, he guardado el evento $args1 en la fecha: $args2'

# Command /removeE_***
removeBirthdayDone = 'Cumpleaños de $args1 borrado correctamente.'
removeFailNotUser = 'No tengo el cumpleaños de $args1 en mi agenda.'
formatErrorRemoveB = 'No has introducido /removeB correctamente.'

# Command /deleteE or /removeE
removeEventDone = 'Evento $args1 borrado correctamente.'
removeFailNotEvent = 'No tengo el evento $args1 en mi calendario.'
formatErrorRemoveE = 'No has introducido /removeE correctamente.'


# Command /info_***
eventDescription = ("El evento $args1 se celebrará el día $args2\n" +
                    "Descripción: $args3\nImpartido por: $args4\n\nPrecio: $args5\n\n$args6\n$args7")

# Greetings Birthday
birthdayGreetings = ["Felicidades $args1, cabron@, eres un puto año más viejo. ",
                     "Hueles un poco mal pero te felicito el cumpleaños $args1.",
                     "Es tu Chachi cumple $args1, muchas felicidades de tu amigo el bot :)",
                     "Pues no tienes mal aspecto para tus \"Error Undefined Age\" años $args1",
                     "Feliz cumpleaños $args1 y sonrie mientras tengas todos los dientes.",
                     "Te felicito $args1 porque me han programado, si no ni eso.",
                     "<FileNotFoundError: [Errno 2] No such file or directory: 'frasesdemierdaparafelicitar.txt' for $args1",
                     "Que cumplas muchos más $args1 pero por favor un poco más rápido, que se me está haciendo muy largo.",
                     "Que ni se te pase por la cabeza que estoy feliz porque cumplas un año más, pero felicidades $args1"
                     ]

# Events reminder
eventsReminderWeekly = 'El listado de eventos de esta próxima semana es:\n\n$args1'
eventsReminderDaily = 'El listado de eventos del día de hoy es:\n\n$args1'
eventsReminderHourly = 'Falta una hora para que empiece\n\n$args1\n¿Estás preparado?'
eventsReminderStart = 'Acaba de empezar\n\n$args1\nSi no estás ya en él, estás tardando.'
eventReminder = 'Evento: $args1\nFecha: $args2\nMore Info: $args3'


# General Calendar/Event
calendarNotFound = "No se ha encontrado el calendario."
eventNotFound = "No se ha encontrado el evento."
dateUnknown = "No se reconoce la fecha que has enviado."


# CalendarAdd
calendarAddNotCalendarId = "El ID del calendario no existe en tu lista de calendarios"


log.info('Message Module Loaded.')
