# lambda

def func(x, y, z): return x + y + z
print(func(2, 3, 4))
# 9

f = lambda x, y, z: x + y + z
print(f(2, 3, 4))
# 9

x = (lambda a='fee', b='fie', c='foe': a + b + c)
print(x('wee'))
# weefiefoe

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x) # title из области видимости объемлющего def
    return action

act = knights()
msg = act('robin')
print(msg)
# Sir robin
print(act)
# <function knights.<locals>.<lambda> at 0x00000212BA340D60>
