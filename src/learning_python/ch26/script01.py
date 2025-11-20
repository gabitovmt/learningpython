# Создание деревьев классов

# Создание объектов суперклассов
class C2: ...
class C3: ...


# Создание и связывание класса C1
class C1(C2, C3):
    # Присваивание name: C1.setname
    def setname(self, who):
        # self является либо I1, либо I2
        self.name = who

# Создание двух экземпляров
I1 = C1()
I2 = C1()
# Установка I1.name в 'bob'
I1.setname('bob')
# Установка I2.name в 'sue'
I2.setname('sue')

# Выводит 'bob'
print(I1.name)
