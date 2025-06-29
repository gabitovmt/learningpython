# Циклы for
# Базовое использование
for x in ['spam', 'eggs', 'ham']:
    print(x, end=' ')
print()
# spam eggs ham

sum = 0
for x in [1, 2, 3, 4]:
    sum += x
print(sum)
# 10

prod = 1
for item in [1, 2, 3, 4]: prod *= item
print(prod)
# 24

# Другие типы данных
S = 'lumberjack'
T = ('and', "I'm", 'okay')
for x in S: print(x, end=' ')  # Итерация по строке
print()
# l u m b e r j a c k
for x in T: print(x, end=' ')  # Итерация по кортежу
print()
# and I'm okay

# Присваивание кортежей в циклах for
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)
# 1 2
# 3 4
# 5 6
