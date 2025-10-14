import module1  # Получить модуль как единое целое (один или больше)
module1.printer('Hello World')  # Уточнить, чтобы получить имена

from module1 import printer # Копировать переменную (одни или более)
printer('Hello World')  # Уточнение не требуется

from module1 import *   # Копировать все переменные
printer('Hello World')
