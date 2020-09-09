# Задание 1
def get_summ(one, two, delimiter='&'):

    return f'{str(one).upper()}{delimiter}{str(two).upper()}'


result = get_summ('Learn', 'python')
print(result)
