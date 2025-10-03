# Альтернативные версии модуля для измерения времени
"""
total(spam, 1, 2, a=3, b=4, _reps=1000) вызывает и хронометрирует spam(1, 2, a=3, b=4) _reps раз и возвращает
суммарное время для всех прогонов с финальным результатом.

best_of(spam, 1, 2, a=3, b=4, _reps=5) запускает тест лучшего из N в попытке избавиться от влияния колебаний
загрузки системы и возвращает лучшее время среди _reps тестов.

best_of_total(spam, 1, 2, a=3, b=4, _reps1=5, _reps=1000) запускает тест лучшего суммарного времени, который берёт
лучший из _reps1 прогонов (суммарного времени _reps прогонов);
"""

import time, sys

if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    repslist = list(range(_reps)) if sys.version_info[0] >= 3 else range(_reps)

    ret = None
    start = timer()
    for _ in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start

    return elapsed, ret


def best_of(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 5)
    best = 2 ** 32
    ret = None

    for _ in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed

    return best, ret


def best_of_total(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1', 5)

    return min(total(func, *pargs, **kargs) for _ in range(_reps1))
