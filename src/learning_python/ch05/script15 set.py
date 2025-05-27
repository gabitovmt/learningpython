# Литералы множеств

print({})  # {}
print(set())  # set()
print(type({}))  # <class 'dict'>

S = set()
print(S)  # set()
S.add(1)
print(S)  # {1}

F = frozenset({1, 2, 3})
print(F)  # frozenset({1, 2, 3})
