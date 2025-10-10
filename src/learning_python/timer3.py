"""
Любительские инструменты для измерения времени выполнения вызовов функций.
Определяют суммарное время, лучшее время и лучшее суммарное время.
Python 3.8+.
"""

import time


def total(func, *pargs, _reps=1000, **kargs):
    ret = None

    start = time.perf_counter()
    for _ in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = time.perf_counter() - start

    return elapsed, ret


def best_of(func, *pargs, _reps=5, **kargs):
    best = 2 ** 32
    ret = None

    for _ in range(_reps):
        start = time.perf_counter()
        ret = func(*pargs, **kargs)
        elapsed = time.perf_counter() - start
        if elapsed < best: best = elapsed

    return best, ret


def best_of_total(func, *pargs, _reps1=5, **kargs):
    return min(total(func, *pargs, **kargs) for _ in range(_reps1))
