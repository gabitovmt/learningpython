# Списковые включения
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
col2 = [row[1] for row in M]
print(col2)  # [2, 5, 8]
print(M)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('-' * 10)

print([row[1] + 1 for row in M])  # [3, 6, 9]
print([row[1] for row in M if row[1] % 2 == 0])  # [2, 8]
print('-' * 10)

diag = [M[i][i] for i in [0, 1, 2]]
print(diag)  # [1, 5, 9]
doubles = [c * 2 for c in 'spam']
print(doubles)  # ['ss', 'pp', 'aa', 'mm']
print('-' * 10)

print(list(range(4)))  # [0, 1, 2, 3]
print(list(range(-6, 7, 2)))  # от -6 до +6 с шагом 2
print([[x ** 2, x ** 3] for x in range(4)])  # [[0, 0], [1, 1], [4, 8], [9, 27]]
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])  # [[2, 1.0, 4], [4, 2.0, 8], [6, 3.0, 12]]
print('-' * 10)

print('Генераторы')
G = (sum(row) for row in M)  # Создать генератор сумм элементов в строках
print(next(G))  # 6
print(next(G))  # 15
print(next(G))  # 24
print('-' * 10)

print(list(map(sum, M)))  # [6, 15, 24]
print('-' * 10)

print({sum(row) for row in M})  # {24, 6, 15} - множество
print({i: sum(M[i]) for i in range(3)})  # {0: 6, 1: 15, 2: 24} - таблица ключей/значений
print([ord(x) for x in 'spaam'])  # [115, 112, 97, 97, 109] - список порядковых чисел для символов
print({ord(x) for x in 'spaam'})  # {112, 97, 115, 109}
