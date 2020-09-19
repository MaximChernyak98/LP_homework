'''
Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”,
пока он не ответит “Хорошо”
Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!",
"Что делаешь?": "Программирую"} и так далее
Доработайте ask_user() так, чтобы когда пользователь вводил вопрос
который есть в словаре, программа давала ему соответствующий ответ.
'''
answer_dict = {"Как дела": "Хорошо!",
               "Что делаешь?": "Программирую",
               "Это": "Спарта"}


def ask_user_1():
    while True:
        try:
            answer = input('Как дела?\n')
            if answer == 'Хорошо':
                print('Ну и славно')
                break
            else:
                default_answer = "Не могу тебе ничего ответить"
                print(f'{answer_dict.get(answer, default_answer)}\n')
        except KeyboardInterrupt:
            # Question to Mary: keyboard interrupt didn't work from IDE, but work
            # from command line - it's all right?
            print('Пока!')


if __name__ == "__main__":
    ask_user_1()
