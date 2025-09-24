# Отображение функций на итерируемые объекты: map

counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)
print(updated)
# [11, 12, 13, 14]

def inc(x): return x + 10
print(list(map(inc, counters)))
# [11, 12, 13, 14]

print(list(map((lambda x: x + 3), counters)))
# [4, 5, 6, 7]


print('Использование собственной функции map')
def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res

print(list(map(inc, [1, 2, 3]))) # Встроенная функция является итерируемым объектом
# [11, 12, 13]
print(mymap(inc, [1, 2, 3])) # Наша функция строит список
# [11, 12, 13]


print(pow(3, 4)) # 81
print(list(map(pow, [1, 2, 3], [2, 3, 4])))
# [1, 8, 81]


print('Использование списковых включений')
print(list(map(inc, [1, 2, 3, 4])))
# [11, 12, 13, 14]
print([inc(x) for x in [1, 2, 3, 4]])
# [11, 12, 13, 14]
