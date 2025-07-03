# Другие итерационные контексты
# map(), zip(), enumerate(), filter(), reduce(), sorted(), reversed()

print(list('abc'))
# ['a', 'b', 'c']
print(tuple('abc'))
# ('a', 'b', 'c')
print('&&'.join('abc'))
# a&&b&&c
a, b, c = 'abc'
print(a, b, c)
# a b c
a, *b = 'abc'
print(a, b)
# a ['b', 'c']
print('a' in 'abc')
# True
print('d' in 'abc')
# False
L = [1, 2, 3, 4]
L[1:3] = 'abc'
print(L)
# [1, 'a', 'b', 'c', 4]
L = [11]
L.extend('abc')
print(L)
# [11, 'a', 'b', 'c']

# Расширенный синтаксис включений
L = ['foo', 'bar', 'baz']
S = {line for line in L if line[0] == 'b'}
print(S)
# {'bar', 'baz'}
D = {i: line for i, line in enumerate(L) if line[0] == 'b'}
print(D)
# {1: 'bar', 2: 'baz'}

# Генераторы
L = list((line.upper() for line in 'abc'))
print(L)
# ['A', 'B', 'C']

print(sum([3, 2, 4, 1, 5, 0]))
# 15
print(any(['spam', '', 'ni']))
# True
print(all(['spam', '', 'ni']))
# False
print(max([3, 2, 5, 1, 4]))
# 5
print(min([3, 2, 5, 1, 4]))
# 1

# Функция
def f(a, b, c, d):
    print(a, b, c, d, sep='&')

f(1, 2, 3, 4)
# 1&2&3&4
f(*[1, 2, 3, 4])
# 1&2&3&4

X = (1, 2)
Y = (3, 4)
print(list(zip(X, Y)))
# [(1, 3), (2, 4)]
A, B = zip(*zip(X, Y))
print(A, B)
# (1, 2) (3, 4)
