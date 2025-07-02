# Расширенное присваивание последовательностей в циклах for в Python 3.X
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]: print(a, b, c)
# 1 [2, 3] 4
# 5 [6, 7] 8

# Вложенные циклы for
items = ['aaa', 111, (4, 5), 2.01]  # Набор объектов
tests = [(4, 5), 3.14]  # Ключи для поиска

for key in tests:  # Для всех ключей
    for item in items:  # Для всех элементов
        if item == key:  # Проверка на совпадение
            print(key, 'was found')  # Ключ найден
            break
    else:
        print(key, 'not found!')  # Ключ не найден
# (4, 5) was found
# 3.14 not found!

# Более простой вариант
for key in tests:
    print(key, 'was found' if key in items else 'not found!')
# (4, 5) was found
# 3.14 not found!

seq1 = 'spam'
seq2 = 'scam'
print([x for x in seq1 if x in seq2])
# (4, 5) was found
# 3.14 not found!
