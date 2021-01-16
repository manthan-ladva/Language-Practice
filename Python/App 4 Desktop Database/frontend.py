#--------------------------------------------------------------Importing Library and File----------------------------------------------
from tkinter import *
import backend

#--------------------------------------------------------------Functions----------------------------------------------
def get_selected_row(event):
    try:
        global selected_row
        index=list1.curselection()[0]
        selected_row=list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
        e4.delete(0, END)
        e4.insert(END, selected_row[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0, END)
    for r in backend.view():
        list1.insert(END, r)

def search_command():
    list1.delete(0, END)
    for r in backend.search(title_text.get(), author_text.get(), year_text.get(), price_text.get()):
        list1.insert(END, r)

def add_command():
    list1.delete(0, END)
    backend.insert(title_text.get(), author_text.get(), year_text.get(), price_text.get())
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), price_text.get()))

def delete_command():
    try:
        backend.delete(selected_row[0])
    except:
        pass

def update_command():
    try:
        backend.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), price_text.get())
    except:
        pass

#--------------------------------------------------------------Main Loop----------------------------------------------
windows = Tk()

#--------------------------------------------------------------Name of the Application----------------------------------------------
windows.wm_title("Books Store")

#--------------------------------------------------------------Labels And Entries----------------------------------------------
title_text= StringVar()
l1 = Label(windows, text='Title')
l1.grid(row=0, column=0)
e1 = Entry(windows, textvariable= title_text)
e1.grid(row=0, column=1)

author_text= StringVar()
l2 = Label(windows, text='Author')
l2.grid(row=1, column=0)
e2 = Entry(windows, textvariable=author_text)
e2.grid(row=1, column=1)

year_text= StringVar()
l3 = Label(windows, text='Year')
l3.grid(row=0, column=3)
e3 = Entry(windows, textvariable=year_text)
e3.grid(row=0, column=4)

price_text= StringVar()
l4 = Label(windows, text='Price')
l4.grid(row=1, column=3)
e4 = Entry(windows, textvariable=price_text)
e4.grid(row=1, column=4)

#--------------------------------------------------------------ListBox & ScrollBox----------------------------------------------
list1 = Listbox(windows, height=10, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

s1= Scrollbar(windows)
s1.grid(row=2, column=2, rowspan=7)

#--------------------------------------------------------------Configuration----------------------------------------------
list1.configure(yscrollcommand=s1.set)
s1.configure(command=list1.yview)

#--------------------------------------------------------------Binding----------------------------------------------
list1.bind('<<ListboxSelect>>', get_selected_row)

#--------------------------------------------------------------Buttons----------------------------------------------
b1=Button(windows, text='View All', width=14, command=view_command)
b1.grid(row=2, column=4)

b2=Button(windows, text='Search', width=14, command=search_command)
b2.grid(row=3, column=4)

b3=Button(windows, text='Add Entry', width=14, command=add_command)
b3.grid(row=4, column=4)

b4=Button(windows, text='Update', width=14, command=update_command)
b4.grid(row=5, column=4)

b5=Button(windows, text='Delete', width=14, command=delete_command)
b5.grid(row=6, column=4)

b6=Button(windows, text='Close', width=14, command=windows.destroy)
b6.grid(row=7, column=4)

windows.mainloop()
