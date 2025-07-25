# Примеры ключевых слов и стандартных значений
def f(a, b, c): print(a, b, c)
f(1, 2, 3)  # По позиции
# 1 2 3

# Сопоставление по имени
f(c=3, b=2, a=1)
# 1 2 3

# Сначала позиционные аргументы, потом ключевые
f(1, c=3, b=2)
# 1 2 3

# Стандартные значения
def f(a, b=2, c=3): print(a, b, c)  # a - обязательный, b и c - необязательные

# Использование стандартных значений
f(1)
# 1 2 3
f(a=1)
# 1 2 3

# Переопределение стандартных значений
f(1, 4)
# 1 4 3
f(1, 4, 5)
# 1 4 5

# Выбор стандартных значений
f(1, c=6)
# 1 2 6

# Комбинирование ключевых слов и стандартных значений
def func(spam, eggs, toast=0, ham=0):  # Первые два аргумента обязательны
    print((spam, eggs, toast, ham))

func(1, 2)  # (1, 2, 0, 0)
func(1, ham=1, eggs=0)  # (1, 0, 0, 1)
func(spam=1, eggs=0)  # (1, 0, 0, 0)
func(toast=1, eggs=2, spam=3)  # (3, 2, 1, 0)
func(1, 2, 3, 4)  # (1, 2, 3, 4)
