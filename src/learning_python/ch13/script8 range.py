# Циклы с подсчётом: range
print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))
# [0, 1, 2, 3, 4] [2, 3, 4] [0, 2, 4, 6, 8]
print(list(range(-5, 5)))
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
print(list(range(5, -5, -1)))
# [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

for i in range(3):
    print(i, 'Pythons')
# 0 Pythons
# 1 Pythons
# 2 Pythons

# Просмотр последовательностей: while и range или for
X = 'spam'

# Простая итерация
for item in X: print(item, end=' ')
print()

# Итерация в цикле while
i = 0
while i < len(X):
    print(X[i], end=' ')
    i += 1
print()

# Ручная итерация посредством range/len
for i in range(len(X)): print(X[i], end=' ')
print()

# Тасование последовательностей: range и len
S = 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')
# pams amsp mspa spam
print()

L = [1, 2, 3]
for i in range(len(L)):
    X = L[i:] + L[:i]
    print(X, end=' ')
print()
# [1, 2, 3] [2, 3, 1] [3, 1, 2]

# Неполный обход: range или срезы
S = 'abcdefghijk'
for i in range(0, len(S), 2): print(S[i], end=' ')
# a c e g i k
print()

for c in S[::2]: print(c, end=' ')
# a c e g i k
print()
