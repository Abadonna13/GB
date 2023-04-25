# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт
# на круглой грядке, причём кусты высажены только по окружности. Таким образом,
# у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном
# файле грядки.

n = int(input("Введите количество кустов N: "))
plod = []
for i in range(n):
    plod.append(int(input(f"Введите количество ягод на кусте {i}:")))
plod_count = []
for i in range(len(plod)):
    plod_count.append(plod[i-2]+plod[i-1]+plod[i])
print(max(plod_count))