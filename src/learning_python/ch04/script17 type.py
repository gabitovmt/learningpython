# Типы

L = [1,2,3]
print(type(L))
print(type(type(L)))

if type(L) == type([]): # Проверка типа при необходимости
    print('yes')

if type(L) == list: # Использование имени типа
    print('yes')

if isinstance(L, list): # объектно-ориентированная проверка
    print('yes')