# Задача 0004

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

import sys

try:
    number = int(input('Введите целое положительное число '))
except ValueError:
    print('Допускаются только натуральные числа. Программа завершает работу... ')
    sys.exit()
if number < 1:
    print('Допускаются только положительные числа. Программа завершает работу... ')
    sys.exit()


def get_bin(number):
    while number != 0:
        binary = number % 2
        yield str(binary)
        number = number // 2


print(f'{number} --->', end=' ')
print(''.join(list(get_bin(number))[::-1]))
