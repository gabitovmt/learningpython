L = [1, 2]
L.extend([3, 4, 5])  # Добавление в конец списка
print(L)
# [1, 2, 3, 4, 5]

print(L.pop())  # Удаление и возврат последнего элемента (по умолчанию: -1)
# 5

L.reverse()  # Метод обращения списка на месте
print(L)
# [4, 3, 2, 1]
print(list(reversed(L)))  # Встроенная функция обращения списка с результатом (итератор)
# [1, 2, 3, 4]

L = [1, 2, 3]
print(L.pop(1))
# 2
print(L)
# [1, 3]

print('\nЕщё методы')
L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))  # Индекс объекта (поиск)
# 1
L.insert(1, 'toast')  # Вставка в позицию
print(L)
# ['spam', 'toast', 'eggs', 'ham']
L.remove('eggs')
print(L)
# ['spam', 'toast', 'ham']
print(L.pop(1))  # Удаление по позиции
# toast
print(L)
# ['spam', 'ham']
print(L.count('spam'))  # Кол-во вхождений
# 1

print('\nОператор del')
L = ['spam', 'eggs', 'ham', 'toast']
del L[0]  # Удаление одного элемента
print(L)
# ['eggs', 'ham', 'toast']
del L[1:]  # Удаление целой секции
print(L)
# ['eggs']
