# Хранение собственных объектов Python: модуль pickle

import pickle

D = {'a': 1, 'b': 2, 'c': 3}
F = open('datafile.pkl', 'wb')
pickle.dump(D, F)  # Сохранение любого объекта в файл с помощью pickle
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)  # Загрузка любого объекта из файла
print(E)
# {'a': 1, 'b': 2, 'c': 3}
