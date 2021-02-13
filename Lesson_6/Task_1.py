# Задача 3 из Урока 2, требуется перевернуть число.
from sys import getsizeof

num = int(input('Введите число: '))


def byte(*var):
    result = 0
    for v in var:
        result += getsizeof(v)
    return result


# Способ 1
def func1(numb):
    if numb < 10:
        return numb
    else:
        return int(f'{numb % 10}{func1(numb // 10)}')


print(func1(num))
print(f'В первом случае было использовано {byte(num)} байт памяти.')
print('-' * 30)

# Способ 2
res = ''
for number in str(num):
    res = f'{number}{res}'
print(int(res))
print(f'Во втором случае было использовано {byte(num, res)} байт памяти.')
print('-' * 30)

# Способ 3
result = ''
i = 0
lst = []
for a in str(num):
    lst.append(a)
for _ in lst:
    result = f'{lst[i]}{result}'
    i += 1
print(int(result))
print(f'В третьем случае было использовано {byte(num, result, i, lst)} байт памяти.')
print('-' * 30)

# У меня 64-разрядная Windows8, python 3.7.7
# При вводе числа 10, у меня получилось: 28 байт, 79 байт, 203 байта.
# Вариант с рекурсией явно лучше в плане затраченной памяти,
# ведь ему приходится хранить только исходное число, вводимое пользователем.
