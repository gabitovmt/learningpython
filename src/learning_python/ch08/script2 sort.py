# Списки. Сортировка
L = ['abc', 'ABD', 'aBe']
L.sort() # Сортировка со смешанным регистром символов
print(L)
# ['ABD', 'aBe', 'abc']
L.sort(key=str.casefold) # Приведение к нижнему регистру
print(L)
# ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True) # Изменение порядка сортировки
print(L)
# ['aBe', 'ABD', 'abc']

L = [1, 'a']
# L.sort() TypeError

print('sorted()')
L = [3, 1, 2]
print(sorted(L)) # [1, 2, 3]
print(L) # [3, 1, 2]

L = ['abc', 'ABD', 'aBe']
print(sorted(L, key=str.lower, reverse=True))
# ['aBe', 'ABD', 'abc']
print(sorted([x.lower() for x in L])) # Отличается!
# ['abc', 'abd', 'abe']