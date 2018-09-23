import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)
    

def talk_to_me(bot, update):
    user_text = 'Привет, {}! Ты написал «{}»'.format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


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
