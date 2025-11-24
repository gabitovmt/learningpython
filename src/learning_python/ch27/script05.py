# Классы или словари

def example1():
    # Запись на основе кортежа
    rec = ('Bob', 40.5, ['dev', 'mgr'])

    print(rec[0])


def example2():
    # Запись на основе словаря
    rec = {}
    rec['name'] = 'Bob'
    rec['age'] = 40.5
    rec['jobs'] = ['dev', 'mgr']

    print(rec['name'])


def example3():
    # Запись на основе класса
    class rec: pass

    rec.name = 'Bob'
    rec.age = 40.5
    rec.jobs = ['dev', 'mgr']

    print(rec.name)


def example4():
    # Записи на основе экземпляров
    class rec: pass

    pers1 = rec()
    pers1.name = 'Bob'
    pers1.age = 40.5
    pers1.jobs = ['dev', 'mgr']

    pers2 = rec()
    pers2.name = 'Sue'
    pers2.jobs = ['dev', 'cto']

    print(pers1.name, pers2.name)


def example5():
    # Класс = данные + логика
    class Person:
        def __init__(self, name, jobs, age=None):
            self.name = name
            self.jobs = jobs
            self.age = age

        def info(self):
            return (self.name, self.jobs)

    # Вызовы конструктора
    rec1 = Person('Bob', ['dev', 'mgr'], 40.5)
    rec2 = Person('Sue', ['dev', 'cto'])

    print(rec1.jobs, rec2.info())


example1()
example2()
example3()
example4()
example5()
