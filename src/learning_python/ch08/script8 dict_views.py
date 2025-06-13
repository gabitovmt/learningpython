D = {'a': 1, 'b': 2, 'c': 3}
K = D.keys()
V = D.values()
# Представление поддерживает тот же порядок, что и словарь
print(list(K), list(V))
# ['a', 'b', 'c'] [1, 2, 3]

del D['b']
print(list(K), list(V))
# ['a', 'c'] [1, 3]
