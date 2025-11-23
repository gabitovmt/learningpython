# Классы генерируют множество объектов экземпляров

# Определить объект класса
class FirstClass:
    # Определить методы класса
    def setdata(self, value):
        # self - это экземпляр
        self.data = value

    def display(self):
        # self.data для каждого экземпляра
        print(self.data)


# Создать два экземпляра
x = FirstClass()
y = FirstClass()

# Вызвать методы: self - это x
x.setdata('King Arthur')
# Выполняется FirstClass.setdata(y, 3.14159)
y.setdata(3.14159)

# self.data отличается в каждом экземпляре
x.display()
# Выполняется FirstClass.display()
y.display()

# Можно получать/устанавливать атрибуты
x.data = "New value"
# И за пределами класса тоже
x.display()

# Здесь можно также устанавливать новые атрибуты!
x.anothername = 'spam'
