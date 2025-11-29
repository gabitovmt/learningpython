# Добавление настройки поведения в подкласс

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


class Manager(Person):
    # Переопределить на этом уровне
    def giveRaise(self, percent, bonus=.10):
        # Вызвать версию из Person
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100_000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    # Создать экземпляр Manager: __init__
    tom = Manager('Tom Jones', 'mgr', 50000)
    # Выполняется специальная версия
    tom.giveRaise(.10)
    # Выполняется унаследованный метод
    print(tom.lastName())
    # Выполняется унаследованный __repr__
    print(tom)

    print('--All three--')
    # Обработать объекты обобщённым образом
    for obj in (bob, sue, tom):
        # Выполнить метод giveRaise этого объекта
        obj.giveRaise(.10)
        # Выполнить общий метод __repr__
        print(obj)
