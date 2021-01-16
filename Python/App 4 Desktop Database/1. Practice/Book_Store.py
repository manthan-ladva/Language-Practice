from tkinter import *                                       #Importing Files
import bpra                                                 #Importing Files

def get_selected_row(event):
    try:
        global selected_row
        index=l1.curselection()[0]
        selected_row = l1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
        e4.delete(0, END)
        e4.insert(END, selected_row[4])
        e5.delete(0, END)
        e5.insert(END, selected_row[5])
    except IndexError:
        pass

def view_command():
    l1.delete(0, END)
    for r in bpra.View():
        l1.insert(END, r)

def search_command():
    l1.delete(0, END)
    for r in bpra.Search(title_text.get(), author_text.get(), address_text.get(), year_text.get(), price_text.get()):
        l1.insert(END, r)

def add_command():
    a = title_text.get()
    b = author_text.get()
    c = address_text.get()
    d = year_text.get()
    e = price_text.get()

    if a == str() and b == str() and c == str() and d == int() and e == float():
        pass
    else:
        l1.delete(0, END)
        bpra.Insert(title_text.get(), author_text.get(), address_text.get(), year_text.get(), price_text.get())
        for r in bpra.View():
            l1.insert(END, r)

def delete_command():
    try:
        bpra.Delete(selected_row[0])
        l1.delete(0, END)
        for r in bpra.View():
            l1.insert(END, r)
    except:
        pass

def update_command():
    try:
        bpra.Update(selected_row[0], title_text.get(), author_text.get(), address_text.get(), year_text.get(), price_text.get())
        l1.delete(0, END)
        l1.insert(END, (selected_row[0], title_text.get(), author_text.get(), address_text.get(), year_text.get(), price_text.get()))
    except:
        pass

def clear_command():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    l1.delete(0, END)

windows= Tk()

windows.wm_title("Book Store")

title_text= StringVar()
l1=Label(windows, text='Title')
l1.grid(row=0, column=0)
e1=Entry(windows, textvariable=title_text)
e1.grid(row=0, column=1)

author_text= StringVar()
l2=Label(windows, text='Author')
l2.grid(row=1, column=0)
e2=Entry(windows, textvariable=author_text)
e2.grid(row=1, column=1)

address_text= StringVar()
l3=Label(windows, text='Address')
l3.grid(row=2, column=0)
e3=Entry(windows, textvariable=address_text)
e3.grid(row=2, column=1)

year_text= StringVar()
l4=Label(windows, text='Year')
l4.grid(row=0, column=2)
e4=Entry(windows, textvariable=year_text)
e4.grid(row=0, column=3)

price_text= StringVar()
l5=Label(windows, text='Price')
l5.grid(row=1, column=2)
e5=Entry(windows, textvariable=price_text)
e5.grid(row=1, column=3)


l1=Listbox(windows, height=10, width=35)
l1.grid(row=3, column=0, rowspan=8, columnspan=2)

s1=Scrollbar(windows)
s1.grid(row=3, column=2, rowspan=7)

l1.configure(yscrollcommand=s1.set)
s1.configure(command=l1.yview)


l1.bind("<<ListboxSelect>>", get_selected_row)


b1=Button(windows, text='View All', width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(windows, text='Search', width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(windows, text='Add Entry', width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(windows, text='Update', width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(windows, text='Delete', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(windows, text='Clear', width=12, command=clear_command)
b6.grid(row=7, column=3)

b6=Button(windows, text='Close', width=12, command=windows.destroy)
b6.grid(row=8, column=3)

windows.mainloop()
