'''
Напечатайте в консоль даты: вчера, сегодня, месяц назад
Превратите строку "01/01/25 12:10:03.234567" в объект datetime
'''

import datetime as date
import locale


def print_date():

    localw.now = date.datetime.now()
    yesterday = now - date.timedelta(days=1)
    month_ago = now - date.timedelta(days=30)
    print(now)
    print(yesterday)
    print(month_ago)


if __name__ == "__main__":
    print_date()
