# Формальный синтаксис включений

# [ выражение for цель1 in итерируемый_объект1 if условие1
#             for цель2 in итерируемый_объект2 if условие2
#             for цельN in итерируемый_объектN if условиеN ]

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)
# [100, 200, 300, 101, 201, 301, 102, 202, 302]

res = []
for x in [0, 1, 2]:
    for y in [100, 200, 300]:
        res.append(x + y)
print(res)
# [100, 200, 300, 101, 201, 301, 102, 202, 302]

print([x + y for x in 'spam' for y in 'SPAM'])
# ['sS', 'sP', 'sA', 'sM', 'pS', 'pP', 'pA', 'pM', 'aS', 'aP', 'aA', 'aM', 'mS', 'mP', 'mA', 'mM']

print([x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')])
# ['sP', 'sA', 'mP', 'mA']

print([x + y + z for x in 'spam' if x in 'sm'
                 for y in 'SPAM' if y in ('P', 'A')
                 for z in '123' if z > '1'])
# ['sP2', 'sP3', 'sA2', 'sA3', 'mP2', 'mP3', 'mA2', 'mA3']

print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
# [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))
print(res)
# [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
