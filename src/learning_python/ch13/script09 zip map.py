# Параллельные обходы: zip и map
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
print(zip(L1, L2))
# <zip object at 0x0000024E6B7080C0>
print(list(zip(L1, L2))) # list() требуется в Python 3.X, но не в Python 2.X
# [(1, 5), (2, 6), (3, 7), (4, 8)]

for x, y in zip(L1, L2):
    print(f'{x} {y} -- {x+y}')
# 1 5 -- 6
# 2 6 -- 8
# 3 7 -- 10
# 4 8 -- 12

T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
print(list(zip(T1, T2, T3)))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

S1 = 'abc'
S2 = 'xyz123'
print(list(zip(S1, S2))) # Усекает по длине более короткой строки
# [('a', 'x'), ('b', 'y'), ('c', 'z')]

# Эквивалентность map
print(map(lambda x, y: x+y, S1, S2))
# <map object at 0x000001900F7E7130>
print(list(map(lambda x, y: x+y, S1, S2))) # Усекает по длине короткой строки
# ['ax', 'by', 'cz']

print(list(map(ord, 'spam')))
# [115, 112, 97, 109]

# Создание словарей с помощью zip
keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
print(list(zip(keys, vals)))
# [('spam', 1), ('eggs', 3), ('toast', 5)]
D = {}
for k, v in zip(keys, vals):
    D[k] = v
print(D)
# {'spam': 1, 'eggs': 3, 'toast': 5}

# 2.2+
D = dict(zip(keys, vals))
print(D)
# {'spam': 1, 'eggs': 3, 'toast': 5}

# Списковые включения
print({k: v for k, v in zip(keys, vals)})
# {'spam': 1, 'eggs': 3, 'toast': 5}
