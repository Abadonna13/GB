# Задача №41. Решение в группах Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число
# N — количество элементов в массиве  Далее записаны N чисел — элементы массива. Массив состоит из
# целых чисел.
# Ввод: 5                   5
#       1 2 3 4 5           1 5 1 5 1
# Вывод: 0                      2

a = [int(x) for x in input("Числа множества через пробел").split()]
count = 0
if len(a) > 3:
    for i in range(2, len(a)-1):
        if a[i - 1] < a[i] < a[i + 1]:
            count += 1
    print(count)
print("Недостаточно элементов массива")




