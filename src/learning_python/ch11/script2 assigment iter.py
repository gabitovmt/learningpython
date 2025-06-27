# Использование срезов
string = 'SPAM'
a, b, c = string[0], string[1], string[2:]  # Индексация и нарезание
print(a, b, c)
# S P AM

a, b, c = list(string[:2]) + [string[2:]]  # Нарезание и конкатенация
print(a, b, c)
# S P AM

a, b = string[:2]  # То же самое, но проще
c = string[2:]
print(a, b, c)
# S P AM

(a, b), c = string[:2], string[2:]  # Выложенные последовательности
print(a, b, c)
# S P AM

# Присваивание серии целых чисел набору переменных
red, green, blue = range(3)
print(red, green, blue)
# 0 1 2

# Циклы
L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)
# 1 [2, 3, 4]
# 2 [3, 4]
# 3 [4]
# 4 []
