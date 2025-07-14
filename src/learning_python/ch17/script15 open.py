# Настройка open

import builtins

def makeopen(id):
    original = builtins.open
    def custom(*pargs, **kwargs):
        print('Custom open call %r' % id, pargs, kwargs)
        return original(*pargs, **kwargs)
    builtins.open = custom


F = open('text.txt', encoding='utf-8')  # Вызов встроенной функции open в builtins
print(F.read())
# Текст ...

makeopen('spam')  # Специальная версия open вызывает встроенную версию open
F = open('text.txt', encoding='utf-8')
# Custom open call 'spam' ('text.txt',) {'encoding': 'utf-8'}
print(F.read())
# Текст ...

makeopen('eggs')  # Вложенные настроенные версии тоже работают!
F = open('text.txt', encoding='utf-8')  # Из-за того, что каждая сохраняет собственное состояние
# Custom open call 'eggs' ('text.txt',) {'encoding': 'utf-8'}
# Custom open call 'spam' ('text.txt',) {'encoding': 'utf-8'}
print(F.read())
# Текст ...
