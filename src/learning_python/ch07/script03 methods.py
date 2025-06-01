# Методы строковых и байтовых объектов

print('s.capitalize()')
print('hello'.capitalize())  # Hello

print('\ns.casefold()')
print('Hello'.casefold())  # hello

print('\ns.center()')
print('spam'.center(10))  # '   spam   '
print('spam'.center(10, '*'))  # ***spam***
print('spam'.center(1, '*'))  # spam

print('\ns.count()')
print('banana'.count('na'))  # 2
print('banana'.count('na', 4))  # 1
print('banana'.count('na', 0, 4))  # 1

print('\ns.endswith()')
print('spam'.endswith('a'))  # False
print('spam'.endswith('a', 0, -1))  # True
print('spam'.endswith('am'))  # True
print('spam'.endswith('am', -1))  # False
print('spam'.endswith(('am', 'an')))  # True

print('\ns.expandtabs()')
print('a\tb'.expandtabs(2))  # a b
print('ac\tb'.expandtabs(2))  # ac  b
print('a\tb'.expandtabs(4))  # a   b

print('\ns.find()')
print('banana'.find('na'))  # 2
print('banana'.find('na', 1))  # 2
print('banana'.find('na', 3))  # 4
print('banana'.find('na', 0, 4))  # 2
print('banana'.find('na', 0, 2))  # -1

print('\ns.index()')
print('banana'.index('na'))  # 2
# print('banana'.index('naa'))  # ValueError
