# Атрибуты функций

def func(a):
    b = 'spam'
    return b * a

print(func)
# <function func at 0x000002321F2C3240>
func.count = 0
func.count += 1
print(func.count)
# 1

func.handles = 'Button-Press'
print(func.handles)
# Button-Press

print(dir(func)[-5:])
# ['__str__', '__subclasshook__', '__type_params__', 'count', 'handles']
