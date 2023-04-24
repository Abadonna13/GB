# Задача 22: Даны два неупорядоченных набора целых чисел (может быть,
# с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами
# элементы множеств.


# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
set_1 = set()
set_2 = set()
# list_1 = list()
a = [int(x) for x in input("Числа 1 множества через пробел").split()]
print(a)
k = set(a)
print(k)
for i in k:
    set_1.add(i)
print(set_1)
b = [int(x) for x in input("Числа 2 множества через пробел").split()]
print(b)
k1 = set(b)
print(k1)
for i in k1:
    set_2.add(i)
print(set_2)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')
