# Настройка поведения за счёт создания подклассов

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: {}, {}]'.format(self.name, self.pay)


# Определение подкласса Person. Наследование атрибутов Person
class Manager(Person):
    # Переопределение с целью настройки
    def giveRaise(self, percent, bonus=.10):
        # Плохой способ: вырезание и вставка
        self.pay = int(self.pay * (1 + percent + bonus))


class Manager(Person):
    # Переопределение с целью настройки
    def giveRaise(self, percent, bonus=.10):
        # Хороший способ: расширение исходной версии
        Person.giveRaise(self, percent + bonus)
