from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = 'Привет, {}! Ты написал «{}»'.format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

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

def wordcount(bot, update):
    symbols = ["-", "=", "_", "\"", "?", "!", "."]
    user_phrase = update.message.text
    for symbol in symbols:
        user_phrase = user_phrase.replace(symbol,"")
    user_phrase = user_phrase.strip().split(" ")
    user_phrase = user_phrase[1:]

    if user_phrase:
        count_words = len(user_phrase)
        if count_words == 1:
            reply_wordcount = "В вашей фразе {} слово.".format(count_words)
        if count_words > 1 < 4:
            reply_wordcount = "В вашей фразе {} слова.".format(count_words)
        if count_words >= 5: 
            reply_wordcount = "В вашей фразе {} слов.".format(count_words)

    else:
        reply_wordcount = "Почему ничего нет?"
    
    update.message.reply_text(reply_wordcount)

def start_calc(bot,update):
    expression = update.message.text
    if expression[-1] == "=":
        calculate(bot,update)
    else:
        return talk_to_me(bot,update)

def calculate(bot,update):
    user_phrase = update.message.text
    user_phrase = user_phrase.replace("=","")

    if "+" in user_phrase:
        user_phrase = user_phrase.split("+")
        calculation = float(user_phrase[0]) + float(user_phrase[1])

    if "-" in user_phrase:
        user_phrase = user_phrase.split("-")
        calculation = float(user_phrase[0]) - float(user_phrase[1])

    if "/" in user_phrase:
        user_phrase = user_phrase.split("/")
        calculation = round(float(user_phrase[0]) / float(user_phrase[1]), 2)

    if "*" in user_phrase:
        calculation = float(user_phrase[0]) * float(user_phrase[1])

    update.message.reply_text(calculation)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, start_calc))
#    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_ephem))
    dp.add_handler(CommandHandler("wordcount", wordcount))


    mybot.start_polling()
    mybot.idle()


main()