# Упражнения части IV. Вычисление факториалов
import math
import operator
from functools import reduce


def fact1(n):
    if n == 1:
        return 1
    else:
        return n * fact1(n - 1)


def fact2(n):
    return reduce(operator.mul, range(n, 0, -1))


def fact3(n):
    r = 1
    for i in range(n, 0, -1):
        r *= i
    return r


def fact4(n):
    return math.factorial(n)

print(fact1(6))
print(fact2(6))
print(fact3(6))
print(fact4(6))


def fact1(n):
    return 1 if n == 1 else n * fact1(n - 1)
