# Генераторные выражения: итерируемые объекты встречаются с включениями

print([x ** 2 for x in range(4)])   # Списковое включение: строит список
# [0, 1, 4, 9]
print((x ** 2 for x in range(4)))   # Генераторное выражение: создаёт итерируемый объект
# <generator object <genexpr> at 0x00000235D56AB2A0>
print(list(x ** 2 for x in range(4)))   # Эквивалентность списковому включению
# [0, 1, 4, 9]

print('-' * 80)
G = (x ** 2 for x in range(4))
print(iter(G) is G)
print(next(G))
print(next(G))
print(next(G))
print(next(G))
try:
    print(next(G))
except StopIteration:
    print('StopIteration')
print(G)

print('-' * 80)
for num in (x ** 2 for x in range(4)):  # Автоматически вызывает next()
    print('%s, %s' % (num, num / 2.0))
# 0, 0.0
# 1, 0.5
# 4, 2.0
# 9, 4.5

print(''.join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))
# AAABBBCCC
a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
print((a, c))
# ('aaa\n', 'ccc\n')

print(sum(x ** 2 for x in range(4)))    # Круглые скобки необязательные
# 14
print(sorted(x ** 2 for x in range(4))) # Круглые скобки необязательные
# [0, 1, 4, 9]
print(sorted((x ** 2 for x in range(4)), reverse=True)) # Круглые скобки обязательны
# [9, 4, 1, 0]
