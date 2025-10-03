"""
Используется в точности как script04_timer2.py, но для получения более простого кода применяет аргументы с передачей
только по ключевым словам и стандартными значениями Python 3.X.
"""

import time, sys

if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(func, *pargs, _reps=1000, **kargs):
    ret = None
    start = timer()
    for _ in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timer() - start

    return elapsed, ret


def best_of(func, *pargs, _reps=5, **kargs):
    best = 2 ** 32
    ret = None

    for _ in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed

    return best, ret


def best_of_total(func, *pargs, _reps1=5, **kargs):
    return min(total(func, *pargs, **kargs) for _ in range(_reps1))
