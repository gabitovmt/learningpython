# Эмуляция zip и map

S1 = 'abc'
S2 = 'xyz123'

print(list(zip(S1, S2)))
# [('a', 'x'), ('b', 'y'), ('c', 'z')]
# zip объединяет элементы в пары, усекает до самого короткого

print(list(zip([-2, -1, 0, 1, 2])))
# [(-2,), (-1,), (0,), (1,), (2,)]
# Единственная последовательность: 1-арные кортежи

print(list(zip([1, 2, 3], [2, 3, 4, 5])))
# [(1, 2), (2, 3), (3, 4)]
# N последовательностей: N-арные кортежи

# map передаёт объединённые в пары элементов функции, усекает
print(list(map(abs, [-2, -1, 0, 1, 2])))
# [2, 1, 0, 1, 2]
# Единственная последовательность: 1-арная функция

print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))
# [1, 8, 81]
# N последовательностей: N-арная функция, Python 3.X

# map и zip принимают произвольные итерируемые объекты
print(list(map(lambda x, y: x + y, open('myfile.txt'), open('myfile.txt'))))
# ['aaa\naaa\n', 'bbb\nbbb\n', 'ccc\nccc\n']
print([x + y for (x, y) in zip(open('myfile.txt'), open('myfile.txt'))])
# ['aaa\naaa\n', 'bbb\nbbb\n', 'ccc\nccc\n']


# Аналог map(func, seqs...) на основе zip
print('-' * 80)
def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

print(mymap(abs, [-2, -1, 0, 1, 2]))
# [2, 1, 0, 1, 2]
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))
# [1, 8, 81]


# Использование спискового включения
def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

print(mymap(abs, [-2, -1, 0, 1, 2]))
# [2, 1, 0, 1, 2]
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))
# [1, 8, 81]


# Использование генераторов: yield и (...)
def mymap(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)

print(list(mymap(abs, [-2, -1, 0, 1, 2])))
# [2, 1, 0, 1, 2]
print(list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])))
# [1, 8, 81]


# Аналоги zip(seqs...) и map(None, seqs...) из Python 2.X
print('-' * 80)
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res

print(myzip(S1, S2))
# [('a', 'x'), ('b', 'y'), ('c', 'z')]
print(mymapPad(S1, S2))
# [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]
print(mymapPad(S1, S2, pad=99))
# [('a', 'x'), ('b', 'y'), ('c', 'z'), (99, '1'), (99, '2'), (99, '3')]

# Применение генераторов: yield
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)

def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)

print(list(myzip(S1, S2)))
# [('a', 'x'), ('b', 'y'), ('c', 'z')]
print(list(mymapPad(S1, S2)))
# [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]
print(list(mymapPad(S1, S2, pad=99)))
# [('a', 'x'), ('b', 'y'), ('c', 'z'), (99, '1'), (99, '2'), (99, '3')]

# Альтернативная реализация с использованием длин
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]

def mymapPad(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]

print(myzip(S1, S2))
# [('a', 'x'), ('b', 'y'), ('c', 'z')]
print(mymapPad(S1, S2))
# [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]
print(mymapPad(S1, S2, pad=99))
# [('a', 'x'), ('b', 'y'), ('c', 'z'), (99, '1'), (99, '2'), (99, '3')]

# Применение генераторов
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

print(list(myzip(S1, S2)))
# [('a', 'x'), ('b', 'y'), ('c', 'z')]
