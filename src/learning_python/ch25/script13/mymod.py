#!python
# coding=utf-8
"""
mymod.py: подсчитывает количество строки и символов в файле
"""

def countlines(name):
    """Количество строк"""
    return len(open(name).readlines())

def countchars(name):
    """Количество символов"""
    return len(open(name).read())

def test(name):
    """(кол-во строк, кол-во символов)"""
    return countlines(name), countchars(name)

if __name__ == '__main__':
    print(test('mymod.py'))
