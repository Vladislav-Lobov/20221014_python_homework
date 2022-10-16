# Задача 0003

# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.2

import sys
from random import uniform

try:
    size_array = int(input('Введите размер списка элементов: '))
except ValueError:
    print('Допускаются только натуральные числа. Программа завершает работу... ')
    sys.exit()
if size_array < 1:
    print('Допускаются только положительные числа. Программа завершает работу... ')
    sys.exit()

array = [round(uniform(0, 9), 2) for i in range(size_array)]
print(f'Список из {size_array} случайных чисел: {array}')

fract_array = [round(i % 1, 2) for i in array]
print(f'Список из дробных частей: {fract_array}')

max = fract_array[0]
min = fract_array[0]
for i in fract_array:
    if i < min:
        min = i
    if i > max:
        max = i

print(f'Максимум дробной части элементов {max}')
print(f'Минимум дробной части элементов {min}')
print(f'Разница равна: {max - min}')
