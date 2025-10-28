# Прямые вызовы загрузки модуля

modname = 'string'
string = __import__(modname)
print(string)
# <module 'string' from 'C:\\DevPrograms\\Python\\Python313\\Lib\\string.py'>

import importlib
string = importlib.import_module(modname)
print(string)
# <module 'string' from 'C:\\DevPrograms\\Python\\Python313\\Lib\\string.py'>
