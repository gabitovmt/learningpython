D = {'eggs': 3, 'spam': 2, 'ham': 1}
del D['eggs']  # Удаление элемента
print(D)
# {'spam': 2, 'ham': 1}

D['brunch'] = 'Bacon'  # Добавление элемента
print(D)
# {'spam': 2, 'ham': 1, 'brunch': 'Bacon'}

print('\nkeys(), values(), items()')
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(D.keys())  # Итератор ключей
# dict_keys(['spam', 'ham', 'eggs'])
print(D.values())  # Итератор значений
# dict_values([2, 1, 3])
print(D.items())  # Итератор ключ-значений
# dict_items([('spam', 2), ('ham', 1), ('eggs', 3)])

print('\nupdate()')
D = {'a': 1, 'b': 2}
D.update({'b': 3, 'c': 4})
print(D)
# {'a': 1, 'b': 3, 'c': 4}

print('\nget()')
D = {}
print(D.get('a'))
print(D.get('a', 10))
# D['a'] KeyError