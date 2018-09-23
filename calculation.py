from func_hard_calc import calculator, precalculator
from func_word_calc import digits, word_calc
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start_calc(bot,update):
    expression = update.message.text
    if expression[-1] == "=":
        calculate(bot,update)
    elif expression[0:7] == "сколько":
        word_calculation(bot,update)
    else:
        return talk_to_me(bot,update)

def word_calculation(bot,update):
    user_phrase = update.message.text
    user_phrase = word_calc(user_phrase)
    user_phrase = round(calculator(user_phrase), 2)
    update.message.reply_text(user_phrase)

def calculate(bot,update):
    user_phrase = update.message.text
    user_phrase = user_phrase.replace("=","")
    user_phrase = round(calculator(user_phrase), 2)
    update.message.reply_text(user_phrase)
'''
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
'''