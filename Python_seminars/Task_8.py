# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите N: "))
m = int(input("Введите M: "))
k = int(input("Введите K: "))
if k <= n*m and (k % n == 0 or k % m ==0):
    print(f"{n} {m} {k} -> yes")
else:
    print(f"{n} {m} {k} -> no")
