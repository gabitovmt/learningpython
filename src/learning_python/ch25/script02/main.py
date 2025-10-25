from alls import *

print(a, _c)
# 1 3
# b     NameError: name 'b' is not defined


from alls import a, b, _c, _d   # Но другие импортёры получают все имена
print(a, b, _c, _d)
# 1 2 3 4


import alls
print(alls.a, alls.b, alls._c, alls._d)
# 1 2 3 4
