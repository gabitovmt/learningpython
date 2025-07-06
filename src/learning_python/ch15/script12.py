# Упражнения части III

# 4.
def f1():
    L = [1, 2, 4, 8, 16, 32, 64]
    X = 5
    found = False
    i = 0
    while not found and i < len(L):
        if 2 ** X == L[i]:
            found = True
        else:
            i = i + 1
    if found:
        print('at index', i)
    else:
        print(X, 'not found')

def f2():
    L = [1, 2, 4, 8, 16, 32, 64]
    X = 5
    i = 0
    while i < len(L):
        if 2 ** X == L[i]:
            print('at index', i)
            break
        i = i + 1
    else:
        print(X, 'not found')


def f3():
    L = [1, 2, 4, 8, 16, 32, 64]
    X = 5
    for i, x in enumerate(L):
        if 2 ** X == x:
            print('at index', i)
            break
    else:
        print(X, 'not found')


def f4():
    L = []
    for i in range(6):
        L.append(2 ** i)
    X = 5
    for i, x in enumerate(L):
        if 2 ** X == x:
            print('at index', i)
            break
    else:
        print(X, 'not found')


def f5():
    L = []
    for i in range(6):
        L.append(2 ** i)
    X = 5
    f = 2 ** X
    if f in L:
        for i, x in enumerate(L):
            if f == x:
                print('at index', i)
    else:
        print(X, 'not found')


def f6():
    L = [2 ** x for x in range(6)]
    X = 5
    f = 2 ** X
    for i, x in enumerate(L):
        if f == x:
            print('at index', i)
            break
    else:
        print(X, 'not found')

def f7():
    L = [2 ** x for x in range(6)]
    X = 5
    f = 2 ** X
    if f in L:
        print('at index', L.index(f))
    else:
        print(X, 'not found')


f1()
f2()
f3()
f4()
f5()
f6()
f7()
