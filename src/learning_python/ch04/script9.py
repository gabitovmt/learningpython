# Словари
print('Операции над отображениями')
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D['food'])

D['quantity'] += 1
print(D)

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
print(D)

bob1 = dict(name='Bob', job='dev', age=40)
print(bob1)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

print('\nВложения')
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
print(rec['name'])
print(rec['name']['last'])
rec['jobs'].append('janitor')
print(rec)

print('\nНедостающие ключи: проверки if')
D = {'a': 1, 'b': 2, 'c': 3}
print(D)
D['e'] = 99
print(D)
# D['f']  KeyError
print('f' in D)
if not 'f' in D:
    print('missing')

print('\nСортировка ключей: циклы for')
D = {'a': 1, 'b': 2, 'c': 3}
Ks = list(D.keys())
Ks.sort()
for key in Ks:
    print(key, '=>', D[key])

for c in 'spam':
    print(c.upper())

print('\nИтерация и оптимизация')
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)
squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)
print(squares)
