# coding=utf-8
from . import m1
def somefunc():
    m1.somefunc()
    print('m2.somefunc')
if __name__ == '__main__':
    somefunc()  # Код самотестирования или режима использования как сценария верхнего уровня
