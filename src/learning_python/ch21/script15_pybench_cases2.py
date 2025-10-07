# coding=utf-8
import pybench, sys

pythons = [
    (1, r'C:\devprograms\python\Python313\python'),
    (1, r'C:\devprograms\python\pypy3.11\pypy'),
]

stmts = [
    # Использовать вызовы функций: map выигрывает
    (0, 0, "[ord(x) for x in 'spam' * 2500]"),
    (0, 0, "res=[]\nfor x in 'spam' * 2500: res.append(ord(x))"),
    (0, 0, "$listif3(map(ord, 'spam' * 2500))"),
    (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
    # Множества и словари
    (0, 0, "{x ** 2 for x in range(1000)}"),
    (0, 0, "s=set()\nfor x in range(1000): s.add(x ** 2)"),
    (0, 0, "{x: x ** 2 for x in range(1000)}"),
    (0, 0, "d={}\nfor x in range(1000): d[x] = x ** 2"),
    # Патологический случай: 301030 цифр
    (1, 1, "import sys\nsys.set_int_max_str_digits(400000)\nlen(str(2**1_000))") # На этот раз PyPy проигрывает
]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None

pybench.runner(stmts, pythons, tracecmd)
