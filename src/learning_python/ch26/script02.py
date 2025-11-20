# Перегрузка операций

class C2: ...
class C3: ...

class C1(C2, C3):
    # Установка name при конструировании
    def __init__(self, who):
        self.name = who

# Установка I1.name в 'bob'
I1 = C1('bob')
# Установка I2.name в 'sue'
I2 = C1('sue')

# Выводит 'bob'
print(I1.name)
