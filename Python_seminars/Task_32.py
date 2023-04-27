# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min = 6
# max = 10
# Вывод: [1, 9, 13, 14, 19]

from random import randint

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
m = []
ind = []
n = int(input('Введите количество элементов в массиве (N): '))
min_number = int(input('Введите нижнний предел (min (от -10 до 10)): '))
max_number = int(input('Введите верхний предел  (max (от -10 до 10)): '))
for i in range(n):
    m.append(randint(-10, 10))
    if min_number <= m[i] <= max_number:
        ind.append(i)
print(m)
print(ind)