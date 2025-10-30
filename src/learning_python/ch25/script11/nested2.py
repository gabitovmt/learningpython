from nested1 import X, printer  # копировать имена
X = 88      # изменяет только X в этом модуле
printer()   # X в nested1 по-прежнему 99
