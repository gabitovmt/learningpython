# Присваивание кортежей в циклах for
D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(f'{key} = {D[key]}')  # Использование итерации по ключам словаря и индексации
# a = 1
# b = 2
# c = 3

print(list(D.items()))
# [('a', 1), ('b', 2), ('c', 3)]

for key, value in D.items():
    print(f'{key} = {value}')  # Итерация сразу по ключам и значениям
# a = 1
# b = 2
# c = 3

T = [(1, 2), (3, 4), (5, 6)]
for both in T:
    a, b = both # Эквивалент в виде присваивания вручную
    print(a, b)
# 1 2
# 3 4
# 5 6

((a, b), c) = ((1, 2), 3) # Работает также и для вложенных последовательностей
print(a, b, c)
# 1 2 3

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)
# 1 2 3
# 4 5 6

for ((a, b), c) in [((1, 2), 3), ['XY', 6]]: print(a, b, c)
# 1 2 3
# X Y 6
