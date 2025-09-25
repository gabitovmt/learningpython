# Генераторные выражения или filter

line = 'aa bbb c'

# aabbb
print(''.join(x for x in line.split() if len(x) > 1))   # Генератор с конструкцией if
print(''.join(filter(lambda x: len(x) > 1, line.split())))  # Подобный вызов filter

# map & filter
# AABBB
print(''.join(x.upper() for x in line.split() if len(x) > 1))
print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))

# Операторный эквивалент
res = ''
for x in line.split():
    if len(x) > 1:
        res += x.upper()
print(res)
