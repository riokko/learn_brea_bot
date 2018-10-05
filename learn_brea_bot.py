from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, Filters

import settings

from astronomy import *
from calculation import *
from handlers import *

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
#    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_ephem, pass_user_data=True))
    dp.add_handler(CommandHandler("wordcount", wordcount, pass_user_data=True))
    dp.add_handler(CommandHandler("fullmoon", next_fullmoon, pass_user_data=True))
    dp.add_handler(CommandHandler("cat", send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Прислать котика)$', send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Сменить аватарку)$', change_avatar, pass_user_data=True))

    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, start_calc, pass_user_data=True))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()