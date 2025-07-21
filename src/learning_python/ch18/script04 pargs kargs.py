# Примеры произвольного количества аргументов

# Заголовки: сбор аргументов
def f1(*args): print(args)

f1()
# ()
f1(1)
# (1,)
f1(1, 2, 3, 4)
# (1, 2, 3, 4)

def f2(**args): print(args)

f2()
# {}
f2(a=1, b=2)
# {'a': 1, 'b': 2}

def f3(a, *pargs, **kargs): print(a, pargs, kargs)

f3(1, 2, 3, x=1, y=2)
# 1 (2, 3), {'x': 1, 'y': 2}


# Вызовы: распаковка аргументов
def func(a, b, c, d): print(a, b, c, d)
args = (1, 2, 3, 4)
func(*args)
# 1 2 3 4

args = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
func(**args)
# 1 2 3 4

func(*(1, 2), **{'d': 4, 'c': 3})
func(1, *(2, 3), **{'d': 4})
func(1, c=3, *(2,), **{'d': 4})
func(1, *(2, 3), d=4)
func(1, *(2,), c=3, **{'d': 4})


# Обобщённое применение функций
def tracer(func, *pargs, **kargs):  # Принимает произвольные аргументы
    print('calling:', func.__name__)
    return func(*pargs, **kargs)  # Передаёт произвольные аргументы

def func(a, b, c, d):
    return a + b + c + d

print(tracer(func, 1, 2, c=3, d=4))
# calling: func
# 10
