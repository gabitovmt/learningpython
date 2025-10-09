# Функции без операторов return

def proc(x):
    print(x)    # Отсутствие return означает возвращение None

x = proc('testing 123...')
# testins 123...
print(x)
# None


list = [1, 2, 3]
list = list.append(4)   # append - это "процедура"
print(list)             # append изменяет список на месте
# None
