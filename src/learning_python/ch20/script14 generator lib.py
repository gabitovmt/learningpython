# Генераторы и библиотечные средства: инструменты прохода по каталогам

import os

for (root, subs, files) in os.walk('.'):
    for name in files:
        if name.endswith('.txt'):
            print(root, name)
# . myfile.txt

G = os.walk('.')
print(iter(G) is G) # Однопроходный итератор

I = iter(G)
print(next(I))
# ('.', [], ['myfile.txt', 'script01 list comprehension.py', 'script02 comprehension filter.py', ...
try:
    print(next(I))
except StopIteration:
    print('StopIteration')


# Генераторы и применение функций
def f(a, b, c): print('%s, %s, and %s' % (a, b, c))

print('-'* 80)
f(0, 1, 2)  # Нормальные позиционные аргументы
# 0, 1, and 2
f(*range(3))         # Распаковка значений range
# 0, 1, and 2
f(*(i for i in range(3)))   # Распаковка значений генераторного выражения
# 0, 1, and 2

D = dict(a='Bob', b='dev', c=40.5)
print(D)    # {'a': 'Bob', 'b': 'dev', 'c': 40.5}

f(a='Bob', b='dev', c=40.5)     # Нормальные ключевые аргументы
# Bob, dev, and 40.5
f(**D)      # Распаковка словаря: ключ=значение
# Bob, dev, and 40.5
f(*D)       # Распаковка итератора ключей
# a, b, and c
f(*D.values()) # Распаковка итератора представления
# Bob, dev, and 40.5
