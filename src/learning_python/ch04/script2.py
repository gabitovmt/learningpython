# Строки
S = 'Spam'

print(len(S))
print(S[0])
print(S[1])
print(S[-1])
print(S[-2])
print('-' * 10)

print(S[1:3])
print(S[1:])
print(S[0:3])
print(S[:3])
print(S[:-1])
print(S[:])
print('-' * 10)

print(S + 'xyz')
print(S * 3)
S = 'z' + S[1:]
print(S)
print('-' * 10)

S = 'shrubbery'
L = list(S)
print(L)
L[1] = 'c'
print(''.join(L))
print('-' * 10)

B = bytearray(b'spam')
B.extend(b'eggs')
print(B)
print(B.decode())