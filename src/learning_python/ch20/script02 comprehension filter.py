# Добавление проверок и вложенных циклов: filter

print([x for x in range(5) if x % 2 == 0])
# [0, 2, 4]
print(list(filter(lambda x: x % 2 == 0, range(5))))
# [0, 2, 4]

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)
print(res)
# [0, 2, 4]

# filter() и map()
print([x ** 2 for x in range(10) if x % 2 == 0])
# [0, 4, 16, 36, 64]
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10)))))
# [0, 4, 16, 36, 64]
