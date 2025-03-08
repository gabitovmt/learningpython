# Множества

X = set('spam')
Y = {'h', 'a', 'm'}
print(X, Y)
print(X & Y)  # пересечение
print(X | Y)  # объединение
print(X - Y)  # разность
print(X > Y)  # надмножество
print({n ** 2 for n in [1, 2, 3, 4]})  # Включения множеств. 3.Х и 2.7

print(list(set([1, 2, 1, 3, 1])))  # фильтрация дубликатов
print(set('spam') - set('ham'))  # нахождение разностей в коллекциях
print(set('spam') == set('asmp'))  # нейтральная к порядку проверка равенства

print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])
