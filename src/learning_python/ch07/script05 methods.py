# Методы строковых и байтовых объектов
import string

print('s.join()')
print(''.join(str(x) for x in range(7)))  # 0123456
print('-'.join('abc'))  # a-b-c

print('\ns.ljust()')
print('spam'.ljust(3, '-'))  # spam
print('spam'.ljust(6, '-'))  # spam--

print('\ns.lower()')
print('123Spam'.lower())  # 123spam

print('\ns.lstrip()')
print('   abc   '.lstrip())  # 'abc   '
print('banana'.lstrip('abc'))  # nana

print('\ns.partition()')
print('banana'.partition('a'))  # ('b', 'a', 'nana')
print('banana'.partition('x'))  # ('banana', '', '')

print('\ns.removeprefix()')
print('TestHook'.removeprefix('Test'))  # Hook
print('BaseTestCase'.removeprefix('Test'))  # BaseTestCase

print('\ns.removesuffix()')
print('MiscTests'.removesuffix('Tests'))  # Misc
print('TmpDirMixin'.removesuffix('Tests'))  # TmpDirMixin

print('\ns.replace()')
print('banana'.replace('na', 'me'))  # bameme
print('banana'.replace('na', 'me', 1))  # bamena

print('\ns.rfind()')
print('banana'.rfind('na'))  # 4

print('\ns.rindex()')
print('banana'.rindex('na'))  # 4

print('\ns.rjust()')
print('spam'.rjust(6, '+'))  # ++spam

print('\ns.rstrip()')
print('banana'.rstrip('abc'))  # banan

print('\ns.rpartition()')
print('banana'.rpartition('na'))  # ('bana', 'na', '')

print('\ns.rsplit()')
print('four score and seven years'.rsplit(None, 3))  # ['four score', 'and', 'seven', 'years']

print('\ns.split()')
print('four score and seven years'.split(None, 3))  # ['four', 'score', 'and', 'seven years']
print('a   b'.split())  # ['a', 'b']
print('a   b'.split(' '))  # ['a', '', '', 'b']
