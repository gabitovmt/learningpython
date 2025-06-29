# Тернарное выражение if/else

A = 't' if 'spam' else 'f'
print(A)
# t
A = 't' if '' else 'f'
print(A)
# f

A = (('spam' and 't') or 'f') # ((X and Y) or Z), здесь Y должен быть истинным
print(A)
# t
A = (('' and 't') or 'f')
print(A)
# f

# A = [Z, Y][bool(X)],
# не то же самое, что тернарное выражение, потому что python не будет предпринимать укороченную оценку
A = ['f', 't'][bool('spam')]
print(A)
# t
A = ['f', 't'][bool('')]
print(A)
# f
