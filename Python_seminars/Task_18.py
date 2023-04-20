# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
#     5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

n = int(input('Введите количество элементов в массиве (N): '))
r = 0
m = []
for i in range(n):
    m.append(randint(0, 30))
    if m[i] > r:
        r = m[i]
print(m)
x = int(input('Введите искомое число (X): '))

for i in m:
    if i > x:
        if i - x < r:
            ymax = i
            ymin = -1
            r = i - x
        elif i - x == r:
            ymax = i

    elif i < x:
        if x - i < r:
            ymin = i
            ymax = -1
            r = x - i
        elif x - i == r:
            ymin = i
    else:
        ymin = i
        ymax = -1
        break
if ymin == -1:
    print(f"Самый близкий по величине элемент к заданному числу X: {ymax}")
elif ymax == -1:
    print(f"Самый близкий по величине элемент к заданному числу X: {ymin}")
else:
    print(f"Самые близкие по величине элементы к заданному числу X: {ymin} и {ymax}")

