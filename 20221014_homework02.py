# Задача 0002

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

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
print(f'Список из {size_array} случайных чисел: {array}', end=' ')

result_array = []
i = 0
j = len(array) - 1
while i <= j:
    result_array.append(array[i] * array[j])
    i += 1
    j -= 1
print(f' =>  {result_array}')
