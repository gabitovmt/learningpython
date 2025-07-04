# Итерируемые объекты map, zip, filter
M = map(abs, (-1, 0, 1))
print(next(M))
# 1
print(next(M))
# 0
print(next(M))
# 1
for x in M: print(x) # Итератор map теперь пуст, только один проход

# zip аналогично

F = filter(bool, ['spam', '', 'ni'])
print(F)
# <filter object at 0x0000026385D9A620>
print(list(F))
# ['spam', 'ni']
