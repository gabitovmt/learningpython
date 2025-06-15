# Именованный кортеж

from collections import namedtuple # Импортирование типа расширения

Rec = namedtuple('Rec', ['name', 'age', 'jobs']) # Создание производного класса
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr']) # Запись в виде именованного кортежа
print(bob)
# Rec(name='Bob', age=40.5, jobs=['dev', 'mgr'])

print(bob[0], bob[2]) # Доступ по позиции
# Bob ['dev', 'mgr']
print(bob.name, bob.jobs) # Доступ по атрибуту
# Bob ['dev', 'mgr']

O = bob._asdict() # Форма, похожая на словарь
print(O['name'], O['jobs']) # Доступ также и по ключу
# Bob ['dev', 'mgr']
print(O)
# {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}

print('\nРаспаковывающее присваивание кортежей')
bob = Rec('Bob', 40.5, ['dev', 'mgr'])
name, age, jobs = bob
print(name, age, jobs)
# Bob 40.5 ['dev', 'mgr']

for x in bob: print(x)
# Bob
# 40.5
# ['dev', 'mgr']