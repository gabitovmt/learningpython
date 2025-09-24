# Списковые включения или map

print(ord('s'))
# 115

res = []
for x in 'spam':
    res.append(ord(x))
print(res)
# [115, 112, 97, 109]

res = list(map(ord, 'spam'))
print(res)
# [115, 112, 97, 109]

res = [ord(x) for x in 'spam']
print(res)
# [115, 112, 97, 109]

# Можем применять произвольное выражение, не только функцию
print([x ** 2 for x in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# map работает только с функцией
print(list(map(lambda x: x ** 2, range(10))))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
