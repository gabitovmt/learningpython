# Групповые присваивания
a = b = []
b.append(42)
print(a, b)
# [42] [42]

a, b = [], []
b.append(42)
print(a, b)
# [] [42]

# Дополненные присваивания
x = 1
x += 1
print(x)
# 2

S = 'spam'
S += 'SPAM'
print(S)
# spamSPAM

L = [1, 2]
L += [3, 4]
print(L)
# [1, 2, 3, 4]

L = []
L += 'spam'
print(L)
# ['s', 'p', 'a', 'm']

# L = L + 'spam'
# TypeError