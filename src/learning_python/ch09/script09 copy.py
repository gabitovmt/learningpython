# Ссылки или копии

L = [1, 2, 3]
D = {'a': 1, 'b': 2}
A = L[:]
B = D.copy()
A[1] = 'Ni'
B['c'] = 'spam'

print(L, D)
# [1, 2, 3] {'a': 1, 'b': 2}
print(A, B)
# [1, 'Ni', 3] {'a': 1, 'b': 2, 'c': 'spam'}

# Глубокая копия
X = [[1, 2], 3, 4]
import copy
Y = copy.deepcopy(X)
Y[0][1] = 'a'
Y[2] = 'b'
print(X)
# [[1, 2], 3, 4]
print(Y)
# [[1, 'a'], 3, 'b']