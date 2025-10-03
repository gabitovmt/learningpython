import src.learning_python.timer3 as timer

reps = 10_000
reps_range = range(reps)


def dict_for_loop():
    res = {}
    for x in reps_range:
        res[x] = abs(x)
    return res


def dict_comp():
    return {x: abs(x) for x in reps_range}


def set_for_loop():
    res = set()
    for x in reps_range:
        res.add(abs(x))
    return res


def set_comp():
    return {x for x in reps_range}


for test in (dict_for_loop, dict_comp):
    (total, result) = timer.best_of_total(test, _reps1=5, _reps=1000)
    print('%-13s: %.5f => %s' % (test.__name__, total, str(result)[:100]))

for test in (set_for_loop, set_comp):
    (total, result) = timer.best_of_total(test, _reps1=5, _reps=1000)
    print('%-13s: %.5f => %s' % (test.__name__, total, str(result)[:100]))
