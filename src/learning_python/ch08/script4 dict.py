# Словари

print('Создание по ключевым словам')
D = dict(name='Bob', age=40)
print(D)
# {'name': 'Bob', 'age': 40}

print('Создание по парам "ключ-значение"')
D = dict([('name', 'Bob'), ('age', 40)])
print(D)
# {'name': 'Bob', 'age': 40}

print('Создание по упакованным парам "ключ-значение"')
D = dict(zip(['name', 'age'], ['Bob', 40]))
print(D)
# {'name': 'Bob', 'age': 40}

print('Создание из списка ключей')
D = dict.fromkeys(['name', 'age'])
print(D)
# {'name': None, 'age': None}

print('\nПроверка членства')
print('ham' in D)
# False

print('\nСоздание нового списка ключей')
print(list(D.keys()))
# ['name', 'age']