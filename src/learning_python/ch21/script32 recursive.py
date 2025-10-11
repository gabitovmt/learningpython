# Упражнения части IV. Рекурсивные функции

def countdown(n):
    if n > 0:
        print(n, end=' ')
        countdown(n - 1)
    else:
        print('stop')


def countdown1(n):
    [print(i, end=' ') for i in range(n, 0, -1)]
    print('stop')


def countdown2(n):
    list(map(lambda x: print(x, end=' '), range(n, 0, -1)))
    print('stop')


def countdown3(n):
    list(print(i, end=' ') for i in range(n, 0, -1))
    print('stop')


countdown(5)
countdown1(5)
countdown2(5)
countdown3(5)
