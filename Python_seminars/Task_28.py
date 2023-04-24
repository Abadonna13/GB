# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4
def sumab(one_mem,sec_mem):
    if sec_mem == 0:
        return one_mem
    return sumab(one_mem+1,sec_mem-1)

one_mem = int(input("Введите А: "))
sec_mem = int(input("Введите В: "))
print(sumab(one_mem,sec_mem))