# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

coin = list()
c_orel = 0
c_reshka = 0
n = int(input("Введите количество монет: "))
for i in range(n):
    coin.append(int(input(f"Введите сторону для монеты {i+1} 1 - орел или 0 - решка: ")))
    if coin[i] == 0:
        c_reshka += 1
    else:
        c_orel += 1
if c_orel > c_reshka:
    print(f"{coin} Количество монет, которые нужно перевернуть -> {c_reshka}")
else:
    print(f"{coin} Количество монет, которые нужно перевернуть -> {c_orel}")