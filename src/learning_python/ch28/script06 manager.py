# Наследование, настройка и расширение

class Person:
    def lastName(self): ...
    def giveRaise(self): ...
    def __repr__(self): ...

# Наследование
class Manager(Person):
    # Настройка
    def giveRaise(self): ...
    # Расширение
    def someThingElse(self): ...

tom = Manager()
# Буквальное наследование
tom.lastName()
# Настроенная версия
tom.giveRaise()
# Метод для расширения
tom.someThingElse()
# Унаследованный перегруженный метод
print(tom)
