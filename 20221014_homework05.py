# Задача 0005

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import sys

try:
    number = int(input('Введите целое положительное число '))
except ValueError:
    print('Допускаются только натуральные числа. Программа завершает работу... ')
    sys.exit()
if number < 1:
    print('Допускаются только положительные числа. Программа завершает работу... ')
    sys.exit()


def get_positive(n):
    count = 1
    while count <= n:
        if count == 1 or count == 2:
            a = 1
            b = 1
        else:
            tmp = b
            b = a + b
            a = tmp
        yield b
        count += 1


pos_array = list(get_positive(number))

j = 1
neg_array = [i * (-1) ** (j := j + 1) for i in pos_array]
neg_array = neg_array[::-1]

result_array = neg_array + [0] + pos_array
print(f'Для k={number} список равен: {result_array}')
