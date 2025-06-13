print('Отображение значений на ключи')
table = {1975: 'Holy Grail',
         1979: 'Life of Brain',
         1983: 'The Meaning of Life'}
for year in table:
    print(str(year) + '\t' + table[year])

V = 'Life of Brain'
print([key for (key, value) in table.items() if value == V])
print([key for key in table if table[key] == V])

print('\nИспользование словарей для имитации гибких списков: целочисленные ключи')
D = {}
D[99] = 'spam'
print(D[99])
# spam
print(D)
# {99: 'spam'}

print('\nИспользование словарей для разряжённых структур данных: ключи в форме кортежей')
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
X = 2; Y = 3; Z = 4
print(Matrix[(X, Y, Z)])
# 88
print(Matrix)
# {(2, 3, 4): 88, (7, 8, 9): 99}

print('\ndict.fromkeys()')
print(dict.fromkeys(['a', 'b'], 0))
# {'a': 0, 'b': 0}