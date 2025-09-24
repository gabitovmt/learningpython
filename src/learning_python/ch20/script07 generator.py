# Для чего используются генераторные функции?

def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res

for x in buildsquares(5): print(x, end=' : ')
print()
# 0 : 1 : 4 : 9 : 16 :

for x in [n ** 2 for n in range(5)]:
    print(x, end=' : ')
print()
# 0 : 1 : 4 : 9 : 16 :

for x in map(lambda n: n ** 2, range(5)):
    print(x, end=' : ')
print()
# 0 : 1 : 4 : 9 : 16 :

def ups(line):
    for sub in line.split(','):     # Генератор подстрок
        yield sub.upper()
print(tuple(ups('aaa,bbb,ccc')))    # Все итерационные контексты
# ('AAA', 'BBB', 'CCC')

print({i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))})
# {0: 'AAA', 1: 'BBB', 2: 'CCC'}
