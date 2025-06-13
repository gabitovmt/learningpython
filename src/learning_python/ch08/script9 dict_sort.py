D = {'c': 3, 'b': 2, 'a': 1}
Ks = list(D.keys())
Ks.sort()
print(Ks)
# ['a', 'b', 'c']

# 2ой способ
print(sorted(D.keys()))
# ['a', 'b', 'c']
print(sorted(D))
# ['a', 'b', 'c']