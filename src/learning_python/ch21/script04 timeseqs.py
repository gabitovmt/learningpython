"""Проверка относительной скорости итерационных альтернатив."""

import sys, src.learning_python.ch21.script04_timer2 as timer

reps = 10_000
reps_range = range(reps)


def for_loop():
    res = []
    for x in reps_range:
        res.append(abs(x))
    return res


def list_comp():
    return [abs(x) for x in reps_range]


def map_call():
    return list(map(abs, reps_range))


def gen_expr():
    return list(abs(x) for x in reps_range)


def gen_func():
    def gen():
        for x in reps_range:
            yield abs(x)

    return list(gen())


print(sys.version)
print('abs(x)')
for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
    (total, result) = timer.best_of_total(test, _reps1=5, _reps=1000)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, total, result[0], result[-1]))


def for_loop():
    res = []
    for x in reps_range:
        res.append(x + 10)
    return res


def list_comp():
    return [x + 10 for x in reps_range]


def map_call():
    return list(map(lambda x: x + 10, reps_range))


def gen_expr():
    return list(x + 10 for x in reps_range)


def gen_func():
    def gen():
        for x in reps_range:
            yield x + 10

    return list(gen())


print('-' * 80)
print('x + 10')
for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
    (total, result) = timer.best_of_total(test, _reps1=5, _reps=1000)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, total, result[0], result[-1]))
