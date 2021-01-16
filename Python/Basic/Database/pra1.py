import sqlite3

def Create_Table():
    cn=sqlite3.connect("data.db")
    cr=cn.cursor()
    cr.execute("CREATE TABLE IF NOT EXISTS mystore(item TEXT, quantity INTEGER, price REAL)")
    cn.commit()
    cn.close()

def Insert(item, quantity, price):
    cn=sqlite3.connect("data.db")
    cr=cn.cursor()
    cr.execute("INSERT INTO mystore VALUES (?,?,?)", (item, quantity, price))
    cn.commit()
    cn.close()

def View():
    cn=sqlite3.connect("data.db")
    cr=cn.cursor()
    cr.execute("SELECT * FROM mystore")
    #rows=cr.fetchall()
    cn.close()
    for i in cr:
        print(i)

def Update(quantity, price, item):
    cn=sqlite3.connect("data.db")
    cr=cn.cursor()
    cr.execute("UPDATE mystore SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    cn.commit()
    cn.close()

def Delete(item):
    cn=sqlite3.connect("data.db")
    cr=cn.cursor()
    cr.execute("DELETE FROM mystore WHERE item=?", (item,))
    cn.commit()
    cn.close()

View()
print("\n")
