from script02 import SecondClass

# Классы могут перехватывать операции Python
print('-' * 80)

# Унаследован от SecondClass
class ThirdClass(SecondClass):
    # Вызывается для ThirdClass(value)
    def __init__(self, value):
        self.data = value

    # Вызывается для self + other
    def __add__(self, other):
        return ThirdClass(self.data + other)

    # Вызывается для print(self), str()
    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    # Изменение на месте: именованный метод
    def mul (self, other):
        self.data *= other


# Вызывается __init__
a = ThirdClass('abc')
# Вызывается унаследованный метод
a.display()

# __str__: возвращает отображаемую строку
print(a)

# __add__: создаёт новый экземпляр
b = a + 'xyz'
# b имеет все методы класса ThirdClass
b.display()

# __str__: возвращает отображаемую строку
print(b)

# mul: изменяет экземпляр на месте
a.mul(3)
print(a)
