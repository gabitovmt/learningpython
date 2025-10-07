# coding=utf-8
"""
pybench_cases.py: запускает pybench на наборе версий Python и операторов. Выбирайте режимы путём редактирования этого
сценария либо использования аргументов командной строки (в sys.argv): например, запускайте
C:\\python27\\python pybench_cases.py, чтобы протестировать только одну версию Python из перечисленных в stmts,
pybench_cases.py -a для тестирования всех версий Python и py -3 pybench_cases.py -a -t для трассировки
командных строк.
"""

import pybench, sys

pythons = [  # (Python 3?, путь)
    (1, r'C:\devprograms\python\Python313\python'),
    (0, r'C:\devprograms\python\Python27\python'),
    (1, r'C:\devprograms\python\pypy3.11\pypy'),
]

stmts = [  # (количество, повторения, оператор)
    (0, 0, "[x ** 2 for x in range(1000)]"),  # Итерации
    (0, 0, "res=[]\nfor x in range(1000): res.append(x ** 2)"),  # \n = несколько операторов
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),  # \n\t = отступ
    (0, 0, "list(x ** 2 for x in range(1000))"),  # $ = list или ''
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),  # Строковые операции
    (0, 0, "s = '?'\nfor i in range(10000): s += '?'")
]

tracecmd = '-t' in sys.argv  # -t: трассировать командные строки?
pythons = pythons if '-a' in sys.argv else None  # -a: все версии Python в списке, иначе одну?

pybench.runner(stmts, pythons, tracecmd)
