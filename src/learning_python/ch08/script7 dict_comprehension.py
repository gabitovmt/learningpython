# Включения словарей

print(list(zip(['a', 'b', 'c'], [1, 2, 3])))
# [('a', 1), ('b', 2), ('c', 3)]
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(D)
# {'a': 1, 'b': 2, 'c': 3}

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)
# {'a': 1, 'b': 2, 'c': 3}

D = {x: x ** 2 for x in range(1, 5)}
print(D)
# {1: 1, 2: 4, 3: 9, 4: 16}

D = {c: c * 4 for c in 'SPAM'}
print(D)
# {'S': 'SSSS', 'P': 'PPPP', 'A': 'AAAA', 'M': 'MMMM'}

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)
# {'spam': 'SPAM!', 'eggs': 'EGGS!', 'ham': 'HAM!'}

D = dict.fromkeys(['a', 'b', 'c'], 0)
print(D)
# {'a': 0, 'b': 0, 'c': 0}
D = {k:0 for k in ['a', 'b', 'c']}
print(D)
# {'a': 0, 'b': 0, 'c': 0}

D = dict.fromkeys('spam')
print(D)
# {'s': None, 'p': None, 'a': None, 'm': None}
D = {k: None for k in 'spam'}
print(D)
# {'s': None, 'p': None, 'a': None, 'm': None}