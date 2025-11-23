from script01 import FirstClass
from script01 import x

# Классы настраиваются через наследование
print('-' * 80)

# Наследует setdata
class SecondClass(FirstClass):
    # Изменяет display (перегрузка)
    def display(self):
        print('Current value = "%s"' % self.data)


z = SecondClass()
# Находит setdata в FirstClass
z.setdata(42)
# Находит переопределённый метод в SecondClass
z.display()

# x - по-прежнему экземпляр FirstClass
x.display()
