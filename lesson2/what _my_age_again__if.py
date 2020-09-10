'''
Практика: Возраст
Попросить пользователя ввести возраст при помощи input и положить результат в переменную
Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: учиться в детском саду, школе, ВУЗе или работать
Вызвать функцию, передав ей возраст пользователя, и положить результат работы функции в переменную
Вывести содержимое переменной на экран
'''


def get_user_age():
    # get age from user
    try:
        entered_age = int(input('Введите, пожалуйста, свой возвраст: '))
        if entered_age < 0:
            print('Введите возраст в виде целого положительного числа')
            return 'Не выполнено'
    except Exception:
        print('Проверьте ввод, что-то пошло не так')
        return 'Не выполнено'

    # search instruction for entered age
    if entered_age <= 3:
        age_instuction = 'Сидим с мамой/папой/бабушкой дома'
    elif entered_age <= 7:
        age_instuction = 'Можно идти в сад'
    elif entered_age <= 17:
        age_instuction = 'Ходим в школу'
    elif entered_age <= 21:
        age_instuction = 'Можно идти в ВУЗ(или техникум, или просто искать себя)'
    elif entered_age <= 65:
        age_instuction = 'Работаем, продолжаем искать себя'
    else:
        age_instuction = 'Доживаем:)'
    return age_instuction


if __name__ == "__main__":
    result = get_user_age()
    print(result)
