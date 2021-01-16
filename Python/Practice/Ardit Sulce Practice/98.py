from tkinter import *

windows = Tk()

file = open("98gui.txt", 'a+')

def add():
    file.write(user_value.get() + '\n')
    entry.delete(0, END)

def save():
    global file
    file.close()
    file = open("98gui.txt", 'a+')

def close():
    file.close()
    windows.destroy()

user_value = StringVar()
entry = Entry(windows, textvariable = user_value)
entry.grid(row = 0, column = 0)

button_add = Button(windows, text = "Add Line", command = add)
button_add.grid(row = 0, column = 1)

button_save = Button(windows, text = "Save Line", command = save)
button_save.grid(row = 0, column = 2)

button_close = Button(windows, text = "Save & Close", command = close)
button_close.grid(row = 0, column = 3)

windows.mainloop()
