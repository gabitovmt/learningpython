# Выбор элементов из итерируемых объектов: filter

print(list(range(-5, 5)))
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
print(list(filter((lambda x: x > 0), range(-5, 5))))
# [1, 2, 3, 4]

# Операторный эквивалент
res = []
for x in range(-5, 5):
    if x > 0:
        res.append(x)
print(res)
# [1, 2, 3, 4]

# Списковое включение эквивалент
print([x for x in range(-5, 5) if x > 0])
# [1, 2, 3, 4]
