# Итерируемые объекты других встроенных объектов
D = {'a': 1, 'b': 2, 'c': 3}
I = iter(D)
print(next(I))
print(next(I))
print(next(I))

# Словари сами являются итерируемыми объектами
for key in D:
    print(key, D[key])

R = range(5)
print(R) # В Python 3.X диапазоны являются итерируемыми объектами
I = iter(R)
print(next(I))
