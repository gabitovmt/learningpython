var = 99  # Глобальная переменная == атрибут модуля


def local():
    var = 0  # Изменение локальной переменной


def glob1():
    global var  # Объявление глобальной переменной (нормальное)
    var += 1


def glob2():
    import thismod  # Импортирование самого себя
    thismod.var += 1  # Изменение глобальной переменной


def glob3():
    import sys  # Импортирование системной таблицы
    glob = sys.modules['thismod']  # Получение объекта модуля (либо использовать __name__)
    glob.var += 1


def test():
    print(var)
    # 99
    local()
    glob1()
    glob2()
    glob3()
    print(var)
    # 102
