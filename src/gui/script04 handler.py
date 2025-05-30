# Обработка событий

import tkinter as tk

root = tk.Tk()
root.geometry('300x300')


def on_button_click():
    print('Кнопка нажата!')


btn1 = tk.Button(root, text='Нажми на меня!', command=on_button_click)
btn1.pack()


def on_click(event):
    print(event)


btn2 = tk.Button(root, text='Click left button')
btn2.pack()
btn2.bind('<Button-1>', on_click)  # щелчок ЛКМ

btn3 = tk.Button(root, text='Click middle button')
btn3.pack()
btn3.bind('<Button-2>', on_click)  # щелчок СКМ

btn4 = tk.Button(root, text='Click right button')
btn4.pack()
btn4.bind('<Button-3>', on_click)  # щелчок ПКМ

entry1 = tk.Entry(root)
entry1.pack()
entry1.bind('<KeyPress>', on_click)  # нажатие клавиши на клавиатуре

entry2 = tk.Entry(root)
entry2.pack()
entry2.bind('<KeyRelease>', on_click)  # отпускание клавиши на клавиатуре

root.mainloop()
