# Расширенный синтаксис включений для множеств и словарей

print([x * x for x in range(10) if x % 2 == 0])     # Списки упорядочиваются
# [0, 4, 16, 36, 64]
print({x * x for x in range(10) if x % 2 == 0})     # Но множества - нет
# {0, 64, 4, 36, 16}
print({x: x * x for x in range(10) if x % 2 == 0})  # Ключи словаря тоже не упорядочиваются
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

print('-' * 80)
print([x + y for x in [1, 2, 3] for y in [4, 5, 6]])    # Списки сохраняют дубликаты
# [5, 6, 7, 6, 7, 8, 7, 8, 9]
print({x + y for x in [1, 2, 3] for y in [4, 5, 6]})    # Но множества - нет
# {5, 6, 7, 8, 9}
print({x: y for x in [1, 2, 3] for y in [4, 5, 6]})     # Ключи словаря тоже не сохраняют дубликаты
# {1: 6, 2: 6, 3: 6}

print('-' * 80)
print({x + y for x in 'ab' for y in 'cd'})
# {'ad', 'ac', 'bc', 'bd'}
print({x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'})
# {'ac': (97, 99), 'ad': (97, 100), 'bc': (98, 99), 'bd': (98, 100)}
print({k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'})
# {'spamspam', 'sausagesausage'}
print({k.upper(): k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'})
# {'SPAM': 'spamspam', 'SAUSAGE': 'sausagesausage'}
