# Доп. задача на полиндром

word = input('Введите слово: ')
print(len(word) // 2)

def pol (word, i, flag):
    if i < 0:
        return flag
    else:
        print(i, word[i], word[- i - 1])
        if word[i] != word[- i - 1]:
            flag = False
        return pol(word, i - 1, flag)

if pol(word, len(word) // 2 - 1, True):
    print('Это полиндром!')
else:
    print('Это не полиндром!')