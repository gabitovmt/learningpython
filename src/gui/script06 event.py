# Обработка событий по иерархии

import tkinter as tk


def on_key_press_parent(event):
    print('Обработчик события нажатия родительской клавиши')


def on_key_press_child(event):
    print('Обработчик события нажатия дочерней клавиши')
    return 'break'


root = tk.Tk()
root.geometry('300x300')

frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame)
entry.pack()
entry.bind('<KeyPress>', on_key_press_child)

frame.bind('<KeyPress>', on_key_press_parent)

root.mainloop()
