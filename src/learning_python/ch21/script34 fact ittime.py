# Упражнения части IV. Вычисление факториалов
import pybench2

pythons = [
    (1, r'C:\devprograms\python\Python313\python'),
    (0, r'C:\devprograms\python\Python27\python'),
    (1, r'C:\devprograms\python\pypy3.11\pypy'),
]

stmts = [
    (0, 0, 'import sys\nsys.setrecursionlimit(2000)\ndef fact1(n):\n\treturn 1 if n == 1 else n * fact1(n - 1)', 'fact1(1000)'),
    (0, 0, 'from functools import reduce\nfrom operator import mul\ndef fact2(n):\n\treturn reduce(mul, range(n, 0, -1))', 'fact2(1000)'),
    (0, 0, 'def fact3(n):\n\tr = 1\n\tfor i in range(n, 0, -1): r *= i\n\treturn r', 'fact3(1000)'),
    (0, 0, 'from math import factorial\ndef fact4(n):\n\treturn factorial(n)', 'fact4(1000)')
]

pybench2.runner(stmts, pythons)


# 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)]
# --------------------------------------------------------------------------------
# ['fact1(1000)']
# C:\devprograms\python\Python313\python
# 	1000 loops, best of 5: 160 usec per loop
# C:\devprograms\python\Python27\python
# 	1000 loops, best of 5: 184 usec per loop
# C:\devprograms\python\pypy3.11\pypy
# 	WARNING: timeit is a very unreliable tool. use pyperf or something else for real measurements
# pypy.exe -m pip install pyperf
# pypy.exe -m pyperf timeit -n '1000' -r '5' -s 'import sys' -s 'sys.setrecursionlimit(2000)' -s 'def fact1(n):' -s '    return 1 if n == 1 else n * fact1(n - 1)' 'fact1(1000)'
# ------------------------------------------------------------
# 1000 loops, average of 5: 86.2 +- 3.46 usec per loop (using standard deviation)
# --------------------------------------------------------------------------------
# ['fact2(1000)']
# C:\devprograms\python\Python313\python
# 	1000 loops, best of 5: 130 usec per loop
# C:\devprograms\python\Python27\python
# 	1000 loops, best of 5: 148 usec per loop
# C:\devprograms\python\pypy3.11\pypy
# 	WARNING: timeit is a very unreliable tool. use pyperf or something else for real measurements
# pypy.exe -m pip install pyperf
# pypy.exe -m pyperf timeit -n '1000' -r '5' -s 'from functools import reduce' -s 'from operator import mul' -s 'def fact2(n):' -s '    return reduce(mul, range(n, 0, -1))' 'fact2(1000)'
# ------------------------------------------------------------
# 1000 loops, average of 5: 73.6 +- 1.26 usec per loop (using standard deviation)
# --------------------------------------------------------------------------------
# ['fact3(1000)']
# C:\devprograms\python\Python313\python
# 	1000 loops, best of 5: 127 usec per loop
# C:\devprograms\python\Python27\python
# 	1000 loops, best of 5: 150 usec per loop
# C:\devprograms\python\pypy3.11\pypy
# 	WARNING: timeit is a very unreliable tool. use pyperf or something else for real measurements
# pypy.exe -m pip install pyperf
# pypy.exe -m pyperf timeit -n '1000' -r '5' -s 'def fact3(n):' -s '    r = 1' -s '    for i in range(n, 0, -1): r *= i' -s '    return r' 'fact3(1000)'
# ------------------------------------------------------------
# 1000 loops, average of 5: 72.1 +- 0.87 usec per loop (using standard deviation)
# --------------------------------------------------------------------------------
# ['fact4(1000)']
# C:\devprograms\python\Python313\python
# 	1000 loops, best of 5: 17.6 usec per loop
# C:\devprograms\python\Python27\python
# 	1000 loops, best of 5: 121 usec per loop
# C:\devprograms\python\pypy3.11\pypy
# 	WARNING: timeit is a very unreliable tool. use pyperf or something else for real measurements
# pypy.exe -m pip install pyperf
# pypy.exe -m pyperf timeit -n '1000' -r '5' -s 'from math import factorial' -s 'def fact4(n):' -s '    return factorial(n)' 'fact4(1000)'
# ------------------------------------------------------------
# 1000 loops, average of 5: 27.2 +- 14.5 usec per loop (using standard deviation)
