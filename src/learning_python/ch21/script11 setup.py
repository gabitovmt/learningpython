# Настройка теста находится в области видимости самого теста

from timeit import repeat

print(min(repeat(
    number=1000, repeat=3,
    setup='from min3 import min3\nvals=list(range(1000))',
    stmt='min3(*vals)'
)))
# 0.009984900243580341

print(min(repeat(
    number=1000, repeat=3,
    setup='from min3 import min3\nimport random\nvals=[random.random() for i in range(1000)]',
    stmt='min3(*vals)'
)))
# 0.11281519988551736
