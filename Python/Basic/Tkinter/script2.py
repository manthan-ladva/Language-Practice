from tkinter import *

windows = Tk()

def converter():
    grams= float(e2_value.get())*1000
    pounds= float(e2_value.get())*2.20462
    ounces= float(e2_value.get())*35.274
    
    t1.insert(END, str(grams) + ' Grams\n')
    t2.insert(END, str(pounds) + ' Pounds\n')
    t3.insert(END, str(ounces) + ' Ounces\n')

b1=Button(windows, text='Convert', command=converter)
b1.grid(row=0, column=3)

e2_value=StringVar()
e2=Entry(windows, textvariable=e2_value)
e2.grid(row=0, column=1)

e1=Label(windows, text="Kg = ")
e1.grid(row=0, column=0)


t1=Text(windows, height=1, width=20)
t1.grid(row=1, column=0)

t2=Text(windows, height=1, width=20)
t2.grid(row=1, column=1)

t3=Text(windows, height=1, width=20)
t3.grid(row=1, column=2)

windows=mainloop()
