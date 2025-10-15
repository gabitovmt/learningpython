import dir1.dir2.mod # Первая операция импортирования выполняет инициализационные файлы
# dir1 init
# dir2 init
# in mod.py

import dir1.dir2.mod # Последующие операции импортирования не выполняют

print('-' * 80)
import importlib
print(importlib.reload(dir1))
# dir1 init
# <module 'dir1' from 'C:\\Projects\\MyProjects\\learningpython\\src\\learning_python\\ch24\\dir1\\__init__.py'>

print('-' * 80)
print(dir1)
# <module 'dir1' from 'C:\\Projects\\MyProjects\\learningpython\\src\\learning_python\\ch24\\dir1\\__init__.py'>
print(dir1.dir2)
# <module 'dir1.dir2' from 'C:\\Projects\\MyProjects\\learningpython\\src\\learning_python\\ch24\\dir1\\dir2\\__init__.py'>
print(dir1.dir2.mod)
# <module 'dir1.dir2.mod' from 'C:\\Projects\\MyProjects\\learningpython\\src\\learning_python\\ch24\\dir1\\dir2\\mod.py'>

print('-' * 80)
print(dir1.x, dir1.dir2.y, dir1.dir2.mod.z)
# 1 2 3

print('-' * 80)
# print(dir2.mod)   NameError
# print(mod.z)      NameError

from dir1.dir2 import mod   # Путь записывается только здесь
print(mod.z) # 3

from dir1.dir2.mod import z
print(z) # 3

import dir1.dir2.mod as mod # Использовать более короткое имя
print(mod.z) # 3

from dir1.dir2.mod import z as modz # То же самое, если имена конфликтуют
print(modz) # 3
