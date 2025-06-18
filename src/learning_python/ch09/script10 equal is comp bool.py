# Сравнения
L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]
print(L1 == L2, L1 is L2)
# True False

S1 = 'spam'
S2 = 'spam'
print(S1 == S2, S1 is S2)
# True True

S1 = 'a longer string'
S2 = 'a longer string'
print(S1 == S2, S1 is S2)
# True True

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print(L1 < L2, L1 == L2, L1 > L2)

D1 = {'a': 1, 'b': 2}
D2 = {'a': 1, 'b': 3}
# print(D1 < D2, D1 > D2) TypeError

print('\nТип bool')
print(bool(1))
# True
print(bool('spam'))
# True
print(bool({}))
# False