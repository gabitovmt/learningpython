# Файл timer.py
"""
Любительские инструменты для измерения времени выполнения вызовов функций.
Определяют суммарное время, лучшее время и лучшее суммарное время.
"""

import time


def total(reps, func, *pargs, **kargs):
    """
    Суммарное время выполнения функции func() reps раз.
    Возвращает (суммарное время, последний результат).
    """

    # range в 2.X возвращает список, т.е. накладные расходы. Поэтому вынесен за пределы измерения времени
    repslist = list(range(reps))
    ret = None

    start = time.time()
    for _ in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.time() - start

    return elapsed, ret


def bestof(reps, func, *pargs, **kargs):
    """
    Самая быстрая функция func() среди reps запусков.
    Возвращает (лучшее время, последний результат).
    """
    best = 2 ** 32  # 136 лет представляет достаточным
    ret = None

    for _ in range(reps):  # Использование range при измерении времени не учитывается
        start = time.time()
        ret = func(*pargs, **kargs)
        elapsed = time.time() - start
        if elapsed < best: best = elapsed

    return best, ret


def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Лучшее суммарное время:
    (лучшее время из reps1 запусков (суммарное время reps2 запусков func)).
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)


print(total(100_000, pow, 2, 1000)[0])
# 0.027516603469848633
print(total(100_000, str.upper, 'spam')[0])
# 0.0030770301818847656
print(bestof(100_000, pow, 2, 1000)[0])
# 0.0
print(bestof(100_000, str.upper, 'spam')[0])
# 0.0
print(bestof(50, total, 1000, str.upper, 'spam'))
# (3.504753112792969e-05, (3.123283386230469e-05, 'SPAM'))
print(bestoftotal(50, 1000, str.upper, 'spam'))
# (3.4809112548828125e-05, (3.0279159545898438e-05, 'SPAM'))
print(min(total(1000, str.upper, 'spam') for i in range(50)))
# (3.0279159545898438e-05, 'SPAM')
