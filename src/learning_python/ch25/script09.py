# Импортирование модулей по строкам с именами

# import 'string'
# SyntaxError

x = 'string'
# import x
# ModuleNotFoundError: No module named 'x'

modname = 'string'
exec('import ' + modname)   # Выполнение строки кода
print(string)
# <module 'string' from 'C:\\DevPrograms\\Python\\Python313\\Lib\\string.py'>
