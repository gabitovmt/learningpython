import pybench2

pythons = [
    (1, r'C:\devprograms\python\Python313\python'),
    (0, r'C:\devprograms\python\Python27\python'),
    (1, r'C:\devprograms\python\pypy3.11\pypy'),
]

stmts = [
    (0, 0, 'from math import sqrt', 'for i in range(1000): sqrt(i)'),
    (0, 0, '', 'for i in range(1000): i ** .5'),
    (0, 0, '', 'for i in range(1000): pow(i, .5)')
]

pybench2.runner(stmts, pythons)

# 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)]
# --------------------------------------------------------------------------------
# ['for i in range(1000): sqrt(i)']
# C:\devprograms\python\Python313\python
# 	1000 loops, best of 5: 32.7 usec per loop
# C:\devprograms\python\Python27\python
# 	1000 loops, best of 5: 35.3 usec per loop
# C:\devprograms\python\pypy3.11\pypy
# 	WARNING: timeit is a very unreliable tool. use pyperf or something else for real measurements
# pypy.exe -m pip install pyperf
# pypy.exe -m pyperf timeit -n '1000' -r '5' -s 'from math import sqrt' 'for i in range(1000): sqrt(i)'
# ------------------------------------------------------------
# 1000 loops, average of 5: 4.15 +- 0.344 usec per loop (using standard deviation)
# --------------------------------------------------------------------------------
# ['for i in range(1000): i ** .5']
# C:\devprograms\python\Python313\python
# 	1000 loops, best of 5: 54.8 usec per loop
# C:\devprograms\python\Python27\python
# 	1000 loops, best of 5: 68 usec per loop
# C:\devprograms\python\pypy3.11\pypy
# 	WARNING: timeit is a very unreliable tool. use pyperf or something else for real measurements
# pypy.exe -m pip install pyperf
# pypy.exe -m pyperf timeit -n '1000' -r '5' -s '' 'for i in range(1000): i ** .5'
# ------------------------------------------------------------
# 1000 loops, average of 5: 33.4 +- 0.829 usec per loop (using standard deviation)
# --------------------------------------------------------------------------------
# ['for i in range(1000): pow(i, .5)']
# C:\devprograms\python\Python313\python
# 	1000 loops, best of 5: 62 usec per loop
# C:\devprograms\python\Python27\python
# 	1000 loops, best of 5: 89 usec per loop
# C:\devprograms\python\pypy3.11\pypy
# 	WARNING: timeit is a very unreliable tool. use pyperf or something else for real measurements
# pypy.exe -m pip install pyperf
# pypy.exe -m pyperf timeit -n '1000' -r '5' -s '' 'for i in range(1000): pow(i, .5)'
# ------------------------------------------------------------
# 1000 loops, average of 5: 34 +- 0.909 usec per loop (using standard deviation)
