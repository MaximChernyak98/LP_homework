# Задание 1
lst = [3, 5, 7, 9, 10.5]
print(lst)
lst.append('Python')
print(len(lst))

print(lst[0])
print(lst[-1])
print(lst[1:4])
del lst[-1]

# Задание 2
dct = {'city': 'Москва', 'temperature': '20'}
print(dct['city'])
dct['temperature'] = str(int(dct['temperature']) - 5)
print(dct)

# Задание 3
print('country' in dct)
print(dct.get('contry', 'Россия'))
dct['date'] = '27.05.2019'
print(len(dct))
