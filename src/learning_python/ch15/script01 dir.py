# Список переменных в области видимости вызывающего кода
print(dir())

o = 'abc'
# Список атрибутов объекта
print(dir(o))

# Список атрибутов встроенного типа dict
print(dir(dict))

import sys
# Список атрибутов импортированного модуля sys
print(dir(sys))

print(f'Количество имён в sys {len(dir(sys))}')
print(f'Количество имён в sys без __ {len([x for x in dir(sys) if not x.startswith('__')])}')
print(f'Количество имён в sys без _ {len([x for x in dir(sys) if not x.startswith('_')])}')

print([a for a in dir([]) if not a.startswith('_')])
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print([a for a in dir({}) if not a.startswith('_')])
# ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
print([a for a in dir(()) if not a.startswith('_')])
# ['count', 'index']
