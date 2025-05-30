import tkinter as tk

root = tk.Tk()
root.title('Моё первое приложение Tkinter')
root.geometry('800x600')

# Добавить виджет Label
label = tk.Label(root, text='Hello, Tkinter!')
label.pack()

# Запустить цикл событий Tkinter
root.mainloop()