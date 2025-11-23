# Простейший в мире класс Python

# Объект пустого пространства имён
class rec: pass

# Просто объект с атрибутами
rec.name = 'Bob'
rec.age = 40

# Подобен структуре C или записи Pascal
print(rec.name)
# Bob

# Экземпляры наследуют имена класса
x = rec()
y = rec()
# name хранится только в классе
print(x.name, y.name)
# Bob Bob

# Но присваивание изменяет только x
x.name = 'Sue'
print(rec.name, x.name, y.name)
# Bob Sue Bob

# Python 3.13
print(list(rec.__dict__))
# ['__module__', '__firstlineno__', '__static_attributes__', '__dict__', '__weakref__', '__doc__', 'name', 'age']
print(list(name for name in rec.__dict__ if not name.startswith('__')))
# ['name', 'age']
print(list(x.__dict__))
# ['name', 'age']
print(list(y.__dict__))
# ['name']

# Представленные здесь атрибуты являются ключами dict
print(x.name, x.__dict__['name'])
# Sue Sue
# Но извлечение атрибута проверяет также классы
print(x.age)
# 40
# Индексирование словаря не производит поиск в иерархии наследования
# print(x.__dict__['age'])
# KeyError: 'age'

# Связь экземпляра с классом
print(x.__class__)
# <class '__main__.rec'>

# Связь с суперклассами
print(rec.__bases__)
# (<class 'object'>,)

def uppername(obj):
    # По-прежнему необходим аргумент self (obj)
    return obj.name.upper()

# Вызов как простой функции
print(uppername(x))
# SUE

# Теперь это метод класса!
rec.method = uppername
# Запустить метод для обработки x
print(x.method())
# SUE
# То же самое, но передать y для self
print(y.method())
# BOB
# Можно вызывать через экземпляр или класс
print(rec.method(x))
# SUE
