from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import *
from calculation import *
from astronomy import *
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

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

if __name__ == '__main__':
    main()