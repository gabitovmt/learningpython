# Файл timer.py
"""
Любительские инструменты для измерения времени выполнения вызовов функций.
Определяют суммарное время, лучшее время и лучшее суммарное время.
Python 3.8+.
"""

import time


def total(reps, func, *pargs, **kargs):
    """
    Суммарное время выполнения функции func() reps раз.
    Возвращает (суммарное время, последний результат).
    """

    ret = None

    start = time.perf_counter()
    for _ in range(reps):
        ret = func(*pargs, **kargs)
    elapsed = time.perf_counter() - start

    return elapsed, ret


def best_of(reps, func, *pargs, **kargs):
    """
    Самая быстрая функция func() среди reps запусков.
    Возвращает (лучшее время, последний результат).
    """

    best = 2 ** 32  # 136 лет представляет достаточным
    ret = None

    for _ in range(reps):  # Использование range при измерении времени не учитывается
        start = time.perf_counter()
        ret = func(*pargs, **kargs)
        elapsed = time.perf_counter() - start
        if elapsed < best: best = elapsed

    return best, ret


def best_of_total(reps1, reps2, func, *pargs, **kargs):
    """
    Лучшее суммарное время:
    (лучшее время из reps1 запусков (суммарное время reps2 запусков func)).
    """

    return best_of(reps1, total, reps2, func, *pargs, **kargs)
