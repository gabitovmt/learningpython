# Генерация смещений и элементов: enumerate

S = 'spam'
offset = 0
for item in S:
    print(f'{item} appears at offset {offset}')
    offset += 1
# s appears at offset 0
# p appears at offset 1
# a appears at offset 2
# m appears at offset 3

for offset, item in enumerate(S):
    print(f'{item} appears at offset {offset}')
# s appears at offset 0
# p appears at offset 1
# a appears at offset 2
# m appears at offset 3

E = enumerate(S)
print(E)
# <enumerate object at 0x00000288790D72E0>
print(next(E))
# (0, 's')
print(next(E))
# (1, 'p')
print(next(E))
# (2, 'a')
