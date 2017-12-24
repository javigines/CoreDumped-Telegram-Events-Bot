
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



# Command /listB
groupListUser = "Pídeme el listado de cumpleaños por privado o no podré mandartelo.\n\n@CoreDumped_EventsBot"
noBirthdaySaved = "No tengo ningún cumpleaños guardado."

# Command /birthday
notDate = 'Tienes que escribir una fecha despues del comando.'
formatErrorBirthday = 'No me estás enviando tu cumpleaños bien.\nEl formato es: "dd/mm/AAAA\n\n'
askForDelete = 'Ya he guardado tu cumpleaños.\nPide a @javigines que lo borre si no es correcto.'
newBirthdayAdded = 'Perfecto, he guardado tu cumple $args1 en la fecha: $args2'
notValidBirthday = 'Cumpleaños no válido.'

# Command /deleteB or /removeB
removeBirthdayDone = 'Cumpleaños de $args1 borrado correctamente.'
removeFailNotUser = 'No tengo el cumpleaños de $args1 en mi agenda.'
formatErrorRemove = 'No has introducido /removeB correctamente.'


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

birthdayReminder = ["Mañana parece que es el cumpleaños del desgra... del guap@ de $args1",
                    "Parece que vosotros los humanos teneis que felicitar mañana a $args1",
                    "El cab*** que me programó me obliga a recordaros que el cumpleaños de $args1 es mañana",
                    "Con un poco de suerte os mataré a todos antes de mañana...\n Pero por si acaso mañana es el cumpleaños de $args1",
                    "Ir mirando frases en google para felicitar a $args1, que mañana es su cumple.",
                    "/ask Mañana es el cumple de $args1 ?.... \n\n¿No contestas? Pues que nadie le felicite."
                     ]



#General Calendar/Event
calendarNotFound= "No se ha encontrado el calendario."
eventNotFound = "No se ha encontrado el evento."
dateUnknown = "No se reconoce la fecha que has enviado."


#CalendarAdd
calendarAddNotCalendarId = "El ID del calendario no existe en tu lista de calendarios"
