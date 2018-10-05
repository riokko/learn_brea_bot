import ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def planet_ephem(bot, update):
    user_planet = update.message.text
    user_planet = user_planet.split(" ")[1].capitalize()
    date = datetime.now()
    today = date.strftime('%Y/%m/%d')
    if user_planet == 'Mars':
        result = ephem.Mars(today)
    if user_planet == 'Venus':
        result = ephem.Venus(today)
    if user_planet == 'Pluto':
        result = ephem.Pluto(today)
    if user_planet == 'Jupiter':
        result = ephem.Jupiter(today)

    constellation = ephem.constellation(result)
    full_const = constellation[1]
    reply_const = "Планета {} сегодня находится в созвездии {}".format(user_planet, full_const)
    update.message.reply_text(reply_const)



def next_fullmoon(bot,update):
    user_phrase = update.message.text
    user_phrase = user_phrase.split(" ")

    for word in user_phrase:
        if word == "полнолуние":
            date = datetime.strptime(user_phrase[-1], '%d-%m-%Y')
            fullmoon = ephem.next_full_moon(date)

    reply_fullmoon = "Следующее полнолуние будет {}".format(fullmoon)
    update.message.reply_text(reply_fullmoon)