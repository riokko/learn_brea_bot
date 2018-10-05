from glob import glob
import logging
from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = 'Привет {}'.format(emo)
    contact_button = KeyboardButton('Контактные данные', request_contact=True)
    location_button = KeyboardButton('Геолокация', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
                        ['Прислать котика', 'Сменить аватарку'],
                        [contact_button, location_button]
                        ])
    update.message.reply_text(text, reply_markup=get_keyboard())

def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = 'Привет, {} {}! Ты написал «{}»'.format(update.message.chat.first_name, emo, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


def change_avatar(bot, update, user_data):
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text('Готово: {}'.format(emo), reply_markup=get_keyboard())


def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Готово: {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())


def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Готово: {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())


def get_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emo']

def get_keyboard():
    contact_button = KeyboardButton('Контактные данные', request_contact=True)
    location_button = KeyboardButton('Геолокация', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
                        ['Прислать котика', 'Сменить аватарку'],
                        [contact_button, location_button]
                        ], resize_keyboard=True
                        )
    return my_keyboard

def wordcount(bot, update, user_data):
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
    
    update.message.reply_text(reply_wordcount, reply_markup=get_keyboard())


def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat_id, photo=open(cat_pic, 'rb'), reply_markup=get_keyboard())
