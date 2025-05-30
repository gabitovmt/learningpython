# Обработка событий

import tkinter as tk

root = tk.Tk()
root.geometry('800x600')


def on_key_press(event):
    print(f'Нажата клавиша: {event.char}')


def remove_key_press_binging():
    entry.unbind('<KeyPress>')


entry = tk.Entry(root)
entry.pack()
entry.bind('<KeyPress>', on_key_press)

button = tk.Button(root, text='Unbind KeyPress', command=remove_key_press_binging)
button.pack()

root.mainloop()
