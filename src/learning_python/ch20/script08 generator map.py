# Генераторные выражения или map

# [1, 2, 3, 4]
print(list(map(abs, (-1, -2, 3, 4))))           # Отображает функцию на кортеж
print(list(abs(x) for x in (-1, -2, 3, 4)))     # Генераторное выражение

# [2, 4, 6, 8]
print(list(map(lambda x: x * 2, (1, 2, 3, 4)))) # Случай не функции
print(list(x * 2 for x in (1, 2, 3, 4)))        # Проще как генератор?

line = 'aaa,bbb,ccc'
# AAABBBCCC
print(''.join([x.upper() for x in line.split(',')]))    # Создаёт бессмысленный список
print(''.join(x.upper() for x in line.split(',')))      # Генерирует результаты
print(''.join(map(str.upper, line.split(','))))         # Генерирует результаты

# aaaaaabbbbbbcccccc
print(''.join(x * 2 for x in line.split(',')))      # Проще как генератор?
print(''.join(map(lambda x: x * 2, line.split(','))))

# [2, 4, 6, 8]
print([x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]])        # Вложенные включения
print(list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))))     # Вложенные отображения
print(list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4))))    # Вложенные отображения

import math
print(list(map(math.sqrt, (x ** 2 for x in range(4)))))     # Вложенные комбинации
# [0.0, 1.0, 2.0, 3.0]

# Вложение пришло в упадок?
# [1, 0, 1]
print(list(map(abs, map(abs, map(abs, (-1, 0, 1))))))
print(list(abs(x) for x in (abs(x) for x in (abs(x) for x in (-1, 0, 1)))))

print('-' * 80)
print(list(abs(x) * 2 for x in (-1, -2, 3, 4)))     # Эквиваленты без вложения
# [2, 4, 6, 8]
print(list(math.sqrt(x ** 2) for x in range(4)))    # Плоский часто лучше
# [0.0, 1.0, 2.0, 3.0]
print(list(abs(x) for x in (-1, 0, 1)))
# [1, 0, 1]
