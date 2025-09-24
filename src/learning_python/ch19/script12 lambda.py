# Области видимости: выражения lambda также могут быть вложенными

def action(x):
    return (lambda y: x + y)
act = action(99)
print(act)
# <function action.<locals>.<lambda> at 0x000001B7A2F99440>
print(act(2))
# 101

action = (lambda x: (lambda y: x + y))
act = action(99)
print(act(3))
# 102

print(((lambda x: (lambda y: x + y))(99))(4))
# 103
