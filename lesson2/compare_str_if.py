'''
Практика: Сравнение строк
Написать функцию, которая принимает на вход две строки
Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
Если строки одинаковые, вернуть 1
Если строки разные и первая длиннее, вернуть 2
Если строки разные и вторая строка 'learn', возвращает 3
Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты
'''


def get_user_str(str_number):
    # get str from user
    try:
        entered_str = input(
            f'Введите, пожалуйста, строку номер {str_number}: ')
        return entered_str
    # Question for Mary: what could be wrong?
    # I can't imagine what problems there might be
    except KeyboardInterrupt:
        print('Прервано пользователем')
        return 'Не выполнено'


def compare_two_str(string1, string2):
    if type(string1) != str or type(string2) != str:
        return 0
    else:
        if string1 == string2:
            return 1
        elif string1 > string2:
            return 2
        elif string1 != string2 and string2 == 'learn':
            return 3
        else:
            return None


if __name__ == "__main__":
    while input('Для начала работы нажмите Enter/ для завершения работы введите "хватит": ') != 'хватит':
        str1 = get_user_str(1)
        str2 = get_user_str(2)
        print(compare_two_str(str1, str2))
