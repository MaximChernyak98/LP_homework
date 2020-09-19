'''
Перепишите функцию discounted(price, discount, max_discount=20)
из урока про функции так, чтобы она перехватывала исключения,
когда переданы некорректные аргументы (например, строки вместо чисел).
'''


def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        print('Введены некорректные числа')
    except TypeError:
        print('Введены некорректные данные')


if __name__ == "__main__":
    print(discounted([1, 1], [1, 1]))
