'''
Создать список из десяти целых чисел.
Вывести на экран каждое число, увеличенное на 1.
'''


def print_list():
    lst = range(5, 15)
    for i in lst:
        print(i+1)


if __name__ == "__main__":
    print_list()
