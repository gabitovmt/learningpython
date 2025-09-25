# Расширение yield from из Python 3.3

def both(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i

print(list(both(5)))
# [0, 1, 2, 3, 4, 0, 1, 4, 9, 16]


def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))

print(list(both(5)))
# [0, 1, 2, 3, 4, 0, 1, 4, 9, 16]

print(' : '.join(str(i) for i in both(5)))
# 0 : 1 : 2 : 3 : 4 : 0 : 1 : 4 : 9 : 16
