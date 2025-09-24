# Комбинирование элементов из итерируемых объектов: reduce
from functools import reduce

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))
# 10
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))
# 24

# Операторный эквивалент
L = [1, 2, 3, 4]
res = L[0]
for x in L[1:]:
    res = res + x
print(res)
# 10

def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally
print(myreduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
# 15
print(myreduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
# 120

# Использование модуля operator
import operator

print(reduce(operator.add, [2, 4, 6]))
# 12
print(reduce(lambda x, y: x + y, [2, 4, 6]))
# 12
