def format_price(price):
    try:
        price_int = int(price)
    except ValueError:
        price_int = 0
        print('неверный тип данных, введите целое число')
    return f'Цена: {price_int} руб.'


result_price = format_price(56.24)
print(result_price)
