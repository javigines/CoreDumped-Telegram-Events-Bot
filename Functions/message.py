#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging												## System module
log = logging.getLogger(__name__)


# Command /help or /start
helpOrStart = 'Para añadir tu cumpleaños escribe:\n/birthday 23/01/1997'

#Command /restartB
restarting = "Reiniciando..."

#Command /stopB
stopping = "Deteniendo..."

#Command /updateB
updating = "Actualizando..."
updateDone = 'Actualización completa. Reinicia para aplicar.'

# Command /leaveB
leaving = "Hasta Siempre..."

# Command /changelogB
groupChangelogUser = 'No queremos aburrir a la gente con el listado de cambios, ¿por qué no me lo preguntas por privado mejor?'
changelog = ('Versión 1.0.2\n\n(WIP)')

# Command /speak
messageSend = 'Mensaje enviado.'
incorrectChatId = 'El chat_id indicado no es válido o no tengo acceso a él.'

# General Messages
errorExecCommandAdmin = 'Error al ejecutar $args1 $args2 --> $args3 (chat_id: $args4 , user_id: $args5 )'
errorExecCommandUser = 'Ha ocurrido un error y se ha informado de él.'
notAdmin = ['No intentes hacer lo que no debes.',
            'Estás tocando algo que no debes, huye mientras puedas, es una amenaza.']



# Command /eventList && /birthdayList
groupListUser = "Pídeme el listado por privado para evitar hacer spam aquí.\n\n@CoreDumped_EventsBot"
noBirthdaySaved = "No tengo ningún cumpleaños guardado."
noEventSaved = "No tengo ningún evento guardado."

# Command /birthday
notDate = 'Tienes que escribir una fecha.'
formatErrorBirthday = 'No me estás enviando tu cumpleaños bien.\nEl formato es: "dd/mm/AAAA\n\n'
askForDelete = 'Ya he guardado tu cumpleaños.\nPide a @javigines que lo borre si no es correcto.'
newBirthdayAdded = 'Perfecto, he guardado tu cumple $args1 en la fecha: $args2'
notValidBirthday = 'Cumpleaños no válido.'

# Command /event
notDateTitle = 'Tienes que escribir un título y una fecha.'
formatErrorEvent = ('No me estás enviando el nuevo evento bien. El formato es:\n'+
                    '\n/event Título del Evento | Fecha del Evento con Hora y Duración (17/06/2017 18:45 +04:30) | Impartido por(Opcional) | Descripción del Evento (Opcional) | Precio del Evento (Opcional)\n\n'+
                    'Campos opcionales no usados dejarlos en blanco pero con los separadores |')
newEventAdded = 'Perfecto, he guardado el evento $args1 en la fecha: $args2'

# Command /deleteB or /removeB
removeBirthdayDone = 'Cumpleaños de $args1 borrado correctamente.'
removeFailNotUser = 'No tengo el cumpleaños de $args1 en mi agenda.'
formatErrorRemoveB = 'No has introducido /removeB correctamente.'

# Command /deleteE or /removeE
removeEventDone = 'Evento $args1 borrado correctamente.'
removeFailNotEvent = 'No tengo el evento $args1 en mi calendario.'
formatErrorRemoveE = 'No has introducido /removeE correctamente.'


# Command /info_***
eventDescription = ("El evento $args1 se celebrará el día $args2\n" +
                    "Descripción: $args3\nImpartido por: $args4\n\nPrecio: $args5\n\nId Evento: $args6")

# Greetings Birthday
birthdayGreetings = ["Felicidades $args1, cabron@, eres un puto año más viejo. ",
                    "Hueles un poco mal pero te felicito el cumpleaños $args1.",
                    "Es tu Chachi cumple $args1, muchas felicidades de tu amigo el bot :)",
                    "Pues no tienes mal aspecto para tus $args2 años $args1",
                    "Feliz cumpleaños $args1 y sonrie mientras tengas todos los dientes.",
                    "Te felicito $args1 porque me han programado, si no ni eso.",
                    "<FileNotFoundError: [Errno 2] No such file or directory: 'felicitaciones.txt' for $args1",
                    "Que cumplas muchos más $args1 pero por favor un poco más rápido, que se me está haciendo muy largo.",
                    "Que ni se te pase por la cabeza que estoy feliz porque cumplas un años más pero felicidades $args1"
                     ]

# Events reminder
eventsReminderWeekly = 'El listado de eventos de esta próxima semana es:\n\n$args1'
eventsReminderDaily = 'El listado de eventos del día de hoy es:\n\n$args1'
eventReminder = 'Evento: $args1\nFecha: $args2\nMore Info: $args3'



#General Calendar/Event
calendarNotFound= "No se ha encontrado el calendario."
eventNotFound = "No se ha encontrado el evento."
dateUnknown = "No se reconoce la fecha que has enviado."


#CalendarAdd
calendarAddNotCalendarId = "El ID del calendario no existe en tu lista de calendarios"


log.info('Message Module Loaded.')
