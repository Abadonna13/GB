# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых
# не превосходит k. Программа получает на вход одно натуральное число k, не
# превосходящее 10^5. Программа должна вывести все пары дружественных чисел,
# каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).

# Ввод:
# 300
# Вывод:
# 220 284

# import math
# def sum_of_divisors(n):
#     s = 1
#     i = 2
#     j = n
#     j_sqrt = math.isqrt(j)
#     while i <= j_sqrt:
#         if j % i == 0:
#             f = 1
#             m = 1
#             while j % i == 0:
#                 j //= i
#                 m *= i
#                 f += m
#             j_sqrt = math.isqrt(j)
#             s *= f
#         i += 1
#     if j > 1:
#         s *= j + 1
#     return s
#
#
# def sum_of_proper_divisors(n):
#     return sum_of_divisors(n) - n
#
# k = int(input("Введите k: "))
# for i in range(1, k):
#     j = sum_of_proper_divisors(i)
#     if i < j <= k and i == sum_of_proper_divisors(j):
#         print(i, j)

def getSum(value):
    res = 1 + (0 if int(value ** 0.5) ** 2 != value else int(value ** 0.5))
    for i in range(2, int(value ** 0.5)):
        if value % i == 0:
            res += i + value // i
    return res


k = int(input("Введите k: "))
for i in range(10, k):
    sum1 = getSum(i)
    # if sum1 > i:
    sum2 = getSum(sum1)
    if sum2 == i and sum1 != sum2 and sum1 < sum2:
        print(sum1, i)
