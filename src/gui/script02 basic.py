import tkinter as tk

root = tk.Tk()
root.title('Моё первое приложение Tkinter')
root.geometry('800x600')

# Виджеты

# Label
label = tk.Label(root, text='Hello, Tkinter!')
label.pack()


# Button
def on_click():
    print('Кнопка нажата')


button = tk.Button(root, text='Click me!', command=on_click)
button.pack()

# Entry
entry = tk.Entry(root)
entry.pack()

# Text
text = tk.Text(root)
text.pack()

# CheckButton
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, variable=check_var)
checkbutton.pack()

# Radiobutton
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text='Option 1', value='option1', variable=radio_var)
radio2 = tk.Radiobutton(root, text='Option 2', value='option2', variable=radio_var)
radio1.pack()
radio2.pack()

# Scale
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

root.mainloop()
