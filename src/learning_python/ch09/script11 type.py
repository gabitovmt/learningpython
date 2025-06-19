# Объекты type

print(type([1]) == type([])) # Сравнение с типом другого списка
# True
print(type([1]) == list) # Сравнение с именем спискового типа
# True
print(isinstance([1], list)) # Проверка, список ли это или его настройка
# True
import types # Модуль Types содержит имена для других типов
def f(): pass
print(type(f) == types.FunctionType)
# True