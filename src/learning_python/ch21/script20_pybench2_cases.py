# coding=utf-8
"""
pybench_cases.py: запускает pybench на наборе версий Python и операторов. Выбирайте режимы путём редактирования этого
сценария либо использования аргументов командной строки (в sys.argv): например, запускайте
C:\\python27\\python pybench_cases.py, чтобы протестировать только одну версию Python из перечисленных в stmts,
pybench_cases.py -a для тестирования всех версий Python и py -3 pybench_cases.py -a -t для трассировки
командных строк.
"""

import pybench2, sys

pythons = [  # (Python 3?, путь)
    (1, r'C:\devprograms\python\Python313\python'),
    (0, r'C:\devprograms\python\Python27\python'),
    (1, r'C:\devprograms\python\pypy3.11\pypy'),
]

stmts = [  # (количество, повторения, настройка, оператор)
    (0, 0, "", "[x ** 2 for x in range(1000)]"),
    (0, 0, "", "res=[]\nfor x in range(1000): res.append(x ** 2)"),
    (0, 0, "def f(x):\n\treturn x", "[f(x) for x in 'spam' * 2500]"),
    (0, 0, "def f(x):\n\treturn x", "res=[]\nfor x in 'spam' * 2500:\n\tres.append(f(x))"),
    (0, 0, "L = [1, 2, 3, 4, 5]", "for i in range(len(L)): L[i] += 1"),
    (0, 0, "L = [1, 2, 3, 4, 5]", "i=0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1")
]

tracecmd = '-t' in sys.argv  # -t: трассировать командные строки?
pythons = pythons if '-a' in sys.argv else None  # -a: все версии Python в списке, иначе одну?

pybench2.runner(stmts, pythons, tracecmd)
