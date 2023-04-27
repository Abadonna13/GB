# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел. Все числа списка находятся
# на разных строках.
# Ввод:
# 1 2 3 2 3
#
# Вывод:
# 2
from random import randint
def randomList(n):
    s = []
    for i in range(n):
        s.append(randint(1,9))
    return s

x = randomList(int(input("Введите размер первого массива: ")))
#x = [4, 3, 9, 1, 9, 4, 3, 9, 4, 4, 7, 2, 6, 4, 6, 4, 9, 2, 4, 5]
print(x)
x.sort()
print(x)
count = 0
i=0
while i <= (len(x)-2):
    j = i + 1
    while x[i] == x[j]:
        j += 1
        if j > len(x)-1:
            count = count + (j - i) // 2
            i = j
            break
    count = count + (j-i)//2
    i = j
print(count)
