def prost(x,z=2):
    if x<2:
        return False
    elif x == 2:
        return True
    elif x % z == 0:
        return False
    elif z * z > x:
        return True
    else:
        return prost(x, z +1)


x = int(input())
print(prost(x))


# def prost (x, z):
#     if z < 2:
#         return True
#     elif x % z == 0:
#         return False
#     else:
#         return prost (x, z - 1)
#
# ch = int(input('Введите число: '))
#
# if prost (ch, ch - 1):
#     print('Простое число')
# else:
#     print('Не простое число')