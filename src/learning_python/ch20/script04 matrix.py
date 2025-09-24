# Списковые включения и матрицы

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

print(M[1]) # Строка 2
# [4, 5, 6]
print(M[1][2]) # Строка 2, элемент 3
# 6

# Столбец 2
print([row[1] for row in M])
# [2, 5, 8]
print([M[row][1] for row in (0, 1, 2)]) # Использование смещений
# [2, 5, 8]

# Диагонали
print([M[i][i] for i in range(len(M))])
# [1, 5, 9]
print([M[i][len(M)-1-i] for i in range(len(M))])
# [3, 5, 7]

print('-' * 80)

L = [[1, 2, 3], [4, 5, 6]]
for i in range(len(L)):
    for j in range(len(L[i])): # Обновление на месте
        L[i][j] += 10
print(L)
# [[11, 12, 13], [14, 15, 16]]

# Присваивание M для сохранения нового значения
print([col + 10 for row in M for col in row])
# [11, 12, 13, 14, 15, 16, 17, 18, 19]
print([[col + 10 for col in row] for row in M])
# [[11, 12, 13], [14, 15, 16], [17, 18, 19]]

res = []
for row in M:       # Эквиваленты в виде операторов
    for col in row: # Отступ для частей, находящихся дальше справа
        res.append(col + 10)
print(res)
# [11, 12, 13, 14, 15, 16, 17, 18, 19]

res = []
for row in M:
    tmp = []    # Вложенное слева включение начинает новый список
    for col in row:
        tmp.append(col + 10)
    res.append(tmp)
print(res)
# [[11, 12, 13], [14, 15, 16], [17, 18, 19]]

print('-' * 80)

print(M)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(N)
# [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])
# [2, 4, 6, 12, 15, 18, 28, 32, 36]
print([[M[row][col] * N[row][col] for col in range(3)] for row in range(3)])
# [[2, 4, 6], [12, 15, 18], [28, 32, 36]]

print('-' * 80)

res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)
print(res)
# [[2, 4, 6], [12, 15, 18], [28, 32, 36]]

res = [[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)]
print(res)
# [[2, 4, 6], [12, 15, 18], [28, 32, 36]]

res = []
for (row1, row2) in zip(M, N):
    tmp = []
    for (col1, col2) in zip(row1, row2):
        tmp.append(col1 * col2)
    res.append(tmp)
print(res)
# [[2, 4, 6], [12, 15, 18], [28, 32, 36]]
