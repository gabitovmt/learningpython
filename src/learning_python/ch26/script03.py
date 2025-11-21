# Полиморфизм и классы

# Универсальный суперкласс
class Employee:
    def computeSalary(self):
        return 'Employee.computeSalary()'
    def giveRaise(self): ...
    def promote(self): ...
    def retire(self): ...

# Специализированный подкласс
class Engineer(Employee):
    # Что-то специальное
    def computeSalary(self):
        return 'Engineer.computeSalary()'

# Стандартное поведение
bob = Employee()
# Стандартное поведение
sue = Employee()
# Специальный расчёт заработной платы
tom = Engineer()

# Составной объект
company = [bob, sue, tom]
for emp in company:
    # Выполнить версию для данного объекта: стандартную или специальную
    print(emp.computeSalary())
# Employee.computeSalary()
# Employee.computeSalary()
# Engineer.computeSalary()
