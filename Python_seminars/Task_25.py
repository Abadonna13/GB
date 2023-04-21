# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

strr = 'a a a b c a a d c d d'
lst = strr.split()
print(lst)
d = {}
#print(d.get)
out_str = ''
for i in lst:
    if i not in d:
        out_str += i + ' '
    else:
        out_str += i + '_' + str(d[i]) + ' '
d[i] = d.get(i, 0)
d[i] += 1

print(d)
print(out_str)