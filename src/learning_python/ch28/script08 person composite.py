# Делегирование объектов

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


class Manager:
    def __init__(self, name, pay):
        # Внедрить объект Person
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        # Перехватить и делегировать
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        # Делегировать все остальные атрибуты
        return getattr(self.person, attr)

    def __repr__(self):
        # Снова должен быть перегружен (3.X)
        return str(self.person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100_000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
