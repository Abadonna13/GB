# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в
# массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
#
#     5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

n = int(input('Введите количество элементов в массиве (N): '))
x = int(input('Введите искомое число (X): '))
count = 0
m = []
for i in range(n):
    m.append(randint(0, 30))
    if m[i] == x:
        count += 1
print(m)
print(f" -> {count}")