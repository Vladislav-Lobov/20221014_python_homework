# Задача 0001

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import sys
from random import randint

try:
    size_array = int(input('Введите размер списка элементов: '))
except ValueError:
    print('Допускаются только натуральные числа. Программа завершает работу... ')
    sys.exit()
if size_array < 1:
    print('Допускаются только положительные числа. Программа завершает работу... ')
    sys.exit()

array = [randint(-9, 9) for i in range(size_array)]
print(f'Список из {size_array} случайных чисел: {array}')
odd_array = [array[i] for i in range(1, len(array), 2)]
print(f'Элементы нечётных индексов: {odd_array}')
sum = sum(odd_array)

print(f'Сумма элементов нечётных индексов: {sum}')
