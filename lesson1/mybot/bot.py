import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import config

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(token=config.TELEGRAM_BOT_ID, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('Start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()