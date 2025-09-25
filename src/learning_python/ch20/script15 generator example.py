# Генерация перемешанных последовательностей

# Простые функции
def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res

print(scramble('spam'))
# ['spam', 'pams', 'amsp', 'mspa']


def scramble(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]

print(scramble('spam'))
# ['spam', 'pams', 'amsp', 'mspa']

for x in scramble((1, 2, 3)):
    print(x, end=' ')
print()
# (1, 2, 3) (2, 3, 1) (3, 1, 2)


# Генераторные функции
print('-' * 80)

def scramble(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]     # Генераторная функция
        yield seq                   # Здесь работают присваивания

def scramble(seq):
    for i in range(len(seq)):       # Генераторная функция
        yield seq[i:] + seq[:i]     # Выдача по одному элементу на итерацию

print(list(scramble('spam')))
# ['spam', 'pams', 'amsp', 'mspa']
print(list(scramble((1, 2, 3))))
# [(1, 2, 3), (2, 3, 1), (3, 1, 2)]
for x in scramble((1, 2, 3)):
    print(x, end=' ')
print()
# (1, 2, 3) (2, 3, 1) (3, 1, 2)


# Генераторные выражения
print('-' * 80)

S = 'spam'
G = (S[i:] + S[:i] for i in range(len(S)))   # Эквивалентное генераторное выражение
print(list(G))
# ['spam', 'pams', 'amsp', 'mspa']

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(F(S))
# <generator object <lambda>.<locals>.<genexpr> at 0x00000144B90DC660>

print(list(F(S)))
# ['spam', 'pams', 'amsp', 'mspa']
print(list(F([1, 2, 3])))
# [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
for x in F((1, 2, 3)):
    print(x, end=' ')
print()
# (1, 2, 3) (2, 3, 1) (3, 1, 2)
