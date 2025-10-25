from unders import *  # Загружает только имена без подчёркиваний

print(a, c)
# 1 3
# _b    NameError: name '_b' is not defined

import unders  # Но другие импортёры получают все имена
print(unders._b)
# 2
