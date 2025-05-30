# Менеджеры геометрии

import tkinter as tk


# Pack. Упорядочивает виджеты внутри их родительского контейнера, расширяя или сжимая их, чтобы заполнить доступное
# пространство. Виджеты могут быть расположены выше, ниже, слева или справа друг от друга

def pack():
    label1 = tk.Label(root, text='Label 1')
    label1.pack(side=tk.TOP)

    label2 = tk.Label(root, text='Label 2')
    label2.pack(side=tk.LEFT)

    label3 = tk.Label(root, text='Label 3')
    label3.pack(side=tk.RIGHT)


# Grid. Организует виджеты в структуру, подобную таблице, с помощью строк и столбцов. Он обеспечивает больший контроль
# над макетом и подходит для создания сложных и гибких пользовательских интерфейсов

def grid():
    label1 = tk.Label(root, text='Label 1')
    label1.grid(row=0, column=0)

    label2 = tk.Label(root, text='Label 2')
    label2.grid(row=0, column=1)

    label3 = tk.Label(root, text='Label 3')
    label3.grid(row=1, column=0)


root = tk.Tk()
root.geometry('300x300')


# Place. Позволяет позиционировать виджеты по определённым координатам внутри их родительского контейнера с помощью
# абсолютного или относительного позиционирования. Менеджер даёт точный контроль над размещением виджетов,
# но может не подойти для сложных макетов или отзывчивых дизайнов, т.к. требует ручной настройки при изменении размера
# окна

def place():
    label1 = tk.Label(root, text='Label 1')
    label1.place(x=10, y=10)

    label2 = tk.Label(root, text='Label 2')
    label2.place(x=100, y=10)

    label3 = tk.Label(root, text='Label 3')
    label3.place(x=10, y=50)


place()

root.mainloop()
