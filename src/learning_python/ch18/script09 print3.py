#!python
"""
Эмулирует большую часть функции print из Python 3.X для применения в Python 2.X (и Python 3.X).
Сигнатура вызова: print3(*args, sep=' ', end='\n', file=sys.stdout)
"""

import sys

def print3(*args, **kargs):
    sep = kargs.get('sep', ' ')
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print3(1, 2, 3)
print(1, 2, 3, sep='')
print3(1, 2, 3, sep='...')
print3(1, [2], (3,), sep='...')
print3(4, 5, 6, sep='', end='')
print(7, 8, 9)
print3()
print3(1, 2, 3, sep='??', end='.\n', file=sys.stderr)
# 1 2 3
# 123
# 1...2...3
# 1...[2]...(3,)
# 4567 8 9
#
# 1??2??3.


"Использование аргументов с передачей только по ключевым словам Python 3.X"

def print3(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


# print3(99, name='bob')
# TypeError: print3() got an unexpected keyword argument 'name'


"Использование удаления ключевых аргументов Python 2.X/3.X со стандартными значениями"

def print3(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs:
        raise TypeError('extra keywords: %s' % kargs)

    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


# print3(99, name='bob')
# TypeError: extra keywords: {'name': 'bob'}
