# Упражнения части IV. Итерации и включения
import math

values = [2, 4, 9, 16, 25]


def forLoop(l):
    res = []
    for x in l:
        res.append(math.sqrt(x))
    return res


def comp(l):
    return [math.sqrt(x) for x in l]


def mapFunc(l):
    return list(map(lambda x: math.sqrt(x), l))

def gen(l):
    return list(math.sqrt(x) for x in l)


print(forLoop(values))
print(comp(values))
print(mapFunc(values))
print(gen(values))
