# Для чего используется выражение lambda?

L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

for f in L:
    print(f(2))
# 4
# 8
# 16
print(L[0](3))
# 9


def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4
L = [f1, f2, f3]

for f in L:
    print(f(2))
# 4
# 8
# 16
print(L[0](3))
# 9


print('Переключатели для множественного ветвления: окончание')
key = 'got'
x = {'already': (lambda: 2 + 2),
     'got': (lambda: 2 * 4),
     'one': (lambda: 2 ** 6)}[key]()
print(x) # 8

def f1(): return 2 + 2
def f2(): return 2 * 4
def f3(): return 2 ** 6
key = 'one'
x = {'already': f1, 'got': f2, 'one': f3}[key]()
print(x) # 64
