"""scopetest: тестовый модуль для области видимости"""
v = 6


def f(x):
    """f: тестовая функция"""
    print("global: ", list(globals().keys()))
    print("entry local: ", locals())
    y = x
    w = v
    print("exit local: ", locals().keys())


