# EventsBot-CoreDumped
Coredumped Events Telegram Bot

Needed Python Modules:

	Telegram Official Python Bot Api:
	pip3 install python-telegram-bot

	Google Calendar Api Module (+ Fix warning with newer oauth2client module):
	pip3 install --upgrade google-api-python-client
	pip3 uninstall -y oauth2client
	pip3 install oauth2client==3.0.0

	Timezones:
	pip3 install pytz


Needed extra file "token.txt" in main bot directory with bot token Key on first line

To start the bot with the script startBot.sh you need to have installed screen package (apt-get install screen)
