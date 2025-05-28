# Для чего используются множества?

print('Удаление дубликатов')
L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))
# {1, 2, 3, 4, 5}
L = list(set(L))
print(L)  # Удаление дубликатов
# [1, 2, 3, 4, 5]
print(list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])))  # Но порядок может измениться
# ['yy', 'aa', 'cc', 'dd', 'xx']

print('\nВыделение различий')
print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))  # Найти различия в списках
# {3, 7}
print(set('abcdefg') - set('abdghij'))  # Найти различия в строках
# {'c', 'f', 'e'}
print(set('spam') - set(['h', 'a', 'm']))  # Найти различия, разнородные типы
# {'s', 'p'}
print(set(dir(bytes)) - set(dir(bytearray)))
# {'__bytes__', '__getnewargs__'}
print(set(dir(bytearray)) - set(dir(bytes)))
# {'copy', '__alloc__', '__imul__', 'extend', 'reverse', 'remove', '__iadd__', '__delitem__', '__release_buffer__', 'append', 'insert', 'pop', 'clear', '__setitem__'}

print('\nПроверка на равенство, нейтральное к порядку')
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)  # В последовательностях порядок имеет значение
# False
print(set(L1) == set(L2))  # Проверка на равенство, нейтральное к порядку
# True
print(sorted(L1) == sorted(L2))  # Похожая проверка, но результаты упорядочены
# True
print('spam' == 'asmp', set('spam') == set('asmp'), sorted('spam') == sorted('asmp'))
# False True True
