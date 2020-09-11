'''
Установите модуль ephem
Добавьте в бота команду /planet, которая будет принимать на вход название
планеты на английском, например /planet Mars
В функции-обработчике команды из update.message.text получите
название планеты (подсказка: используйте .split())
При помощи условного оператора if и ephem.constellation
научите бота отвечать, в каком созвездии сегодня находится планета.
'''

import logging
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

import config


logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet_dialogue(update, context):
    date_now = datetime.date.today().strftime("%y/%m/%d")
    planet_for_search = ephem.Planet
    planet_name = update.message.text.split('/planet')[1].lower().strip()
    # Search planet in planet list
    if planet_name == 'mercury':
        planet_for_search = ephem.Mercury()
    elif planet_name == 'venus':
        planet_for_search = ephem.Venus()
    elif planet_name == 'earth':
        update.message.reply_text(
            'We are on Earth, from our point of view, we are not in a constellation')
        return
    elif planet_name == 'mars':
        planet_for_search = ephem.Mars()
    elif planet_name == 'jupiter':
        planet_for_search = ephem.Jupiter()
    elif planet_name == 'saturn':
        planet_for_search = ephem.Saturn()
    elif planet_name == 'uranus':
        planet_for_search = ephem.Uranus()
    elif planet_name == 'neptune':
        planet_for_search = ephem.Neptune()
    else:
        update.message.reply_text('Planet not found')
        return
    planet_for_search.compute(date_now)
    constellation_text = ', '.join(ephem.constellation(planet_for_search))
    update.message.reply_text(
        'This planet is now in constellations ' + constellation_text)


def main():
    mybot = Updater(token=config.TELEGRAM_BOT_ID, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('Start', greet_user))
    dp.add_handler(CommandHandler('Planet', planet_dialogue))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
