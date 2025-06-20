D = {'a': 1, 'b': 2, 'c': 3}
K = D.keys()
V = D.values()
# Представление поддерживает тот же порядок, что и словарь
print(list(K), list(V))
# ['a', 'b', 'c'] [1, 2, 3]

del D['b']
print(list(K), list(V))
# ['a', 'c'] [1, 3]

print('\nПредставление ключей подобны множествам')
print(K | {'x': 4})
# {'c', 'x', 'a'}
print(K | {'x'})
# {'c', 'x', 'a'}

# V | {'x': 4} TypeError
# V | {'x':4}.values() TypeError
print('-' * 80)

D = {'a': 1, 'b': 2, 'c': 3}
print(D.keys() & D.keys())  # Пересечение представлений ключей
# {'b', 'c', 'a'}
print(D.keys() & {'b'})  # Пересечение представления ключей и множества
# {'b'}
print(D.keys() & {'b': 1})  # Пересечение представления ключей и словаря
# {'b'}
print(D.keys() | {'b', 'c', 'd'})  # Объединение представления ключей и множества
# {'c', 'a', 'b', 'd'}

print('\nПредставления элементов подобны множествам, если они хешируемы, (содержат только неизменяемые объекты)')
D = {'a': 1}
print(list(D.items()))
# [('a', 1)]
print(D.items() | D.keys())  # Объединение представления и представления
# {('a', 1), 'a'}
print(D.items() | D)  # Словарь трактуется так же, как его ключи
# {('a', 1), 'a'}
print(D.items() | {('c', 3), ('d', 4)})  # Множество пар "ключ/значение"
# {('d', 4), ('c', 3), ('a', 1)}
print(dict(D.items() | {('c', 3), ('d', 4)}))  # Словарь также принимает итерируемые множества
# {'c': 3, 'a': 1, 'd': 4}
