# Списки

print('Операции над последовательностями')
L = [123, 'spam', 1.23]
print(len(L))
print(L[0])
print(L[:-1])
print(L + [4, 5, 6])
print(L * 2)
print(L)

print('Операции, специфичные для типа')
L.append('NI')
print(L)
print(L.pop(2))
print(L)

M = ['bb', 'aa', 'cc']
M.sort()
print(M)
M.reverse()
print(M)

print('Контроль границ')
# L[99]         Index Error
# L[99] = 1     Index Error

print('Вложение')
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(M)
print(M[1])
print(M[1][2])