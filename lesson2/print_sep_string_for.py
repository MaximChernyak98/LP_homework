'''
Цикл
Ввести с клавиатуры строку.
Вывести эту же строку вертикально: по одному символу на строку консоли.
'''


def make_str_vertical():
    string = input('Введите строку для переворота: ')
    for char in string:
        print(char)


if __name__ == "__main__":
    make_str_vertical()
