def four():
    x = 0
    while x < 4:
        print('in generator, x =', x)
        yield x
        x += 1


for i in four():
    print(i)


def subgen(x):
    for i in range(x):
        yield i


def gen(y):
    yield from subgen(y)


for q in gen(6):
    print(q)

print(2 in four())
print(5 in four())
