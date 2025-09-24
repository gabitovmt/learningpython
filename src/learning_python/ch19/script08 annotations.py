# Аннотации функций в Python 3.X

def func(a, b, c):
    return a + b + c
print(func(1, 2, 3)) # 6

def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c
print(func(1, 2, 3)) # 6
print(func.__annotations__) # {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}

# Обработка аннотаций
def func(a: 'spam', b, c: 99):
    return a + b + c
print(func(1, 2, 3)) # 6
print(func.__annotations__) # {'a': 'spam', 'c': 99}
for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])
# a => spam
# c => 99

def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c
print(func(1, 2, 3)) # 6
print(func()) # 15 (все стандартные значения)
print(func(1, c=10)) # 16
print(func.__annotations__) # {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}

# Пробелы необязательны
def func(a: 'spam'=4, b:(1,10)=5, c:float=6) -> int:
    return a + b + c
print(func(1, 2)) # 9
print(func.__annotations__) # {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}
