# coding=utf-8
from recur1 import X    # Нормально: имя X уже присвоено
from recur1 import Y    # Ошибка: имя Y пока не существует
print(X, Y)
