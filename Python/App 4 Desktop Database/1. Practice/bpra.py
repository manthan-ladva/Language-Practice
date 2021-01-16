import sqlite3

def Create():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mystore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, address TEXT, year INTEGER, price REAL)")
    con.commit()
    con.close()

def Insert(title, author, address, year, price):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("INSERT INTO mystore VALUES (NULL,?,?,?,?,?)", (title, author, address, year, price))
    con.commit()
    con.close()

def View():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM mystore")
    rows=cur.fetchall()
    con.close()
    for i in rows:
        print(i)
    return rows

def Search(title, author, address, year, price):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM mystore WHERE title=? OR author=? OR address=? OR year=? OR price=?", (title, author, address, year, price))
    rows=cur.fetchall()
    con.close()
    for i in rows:
        print(i)
    return rows

def Delete(id): #-----------------Delete <~ is used to delete the whole row
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("DELETE FROM mystore WHERE id=?", (id,))
    con.commit()
    con.close()

def Update(id, title, author, address, year, price):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("UPDATE mystore SET title=?, author=?, address=?, year=?, price=? WHERE id=?", (title, author, address, year, price, id))
    con.commit()
    con.close()

Create()
#Insert('Swami', 'A1', 1800, 110)
#View()
#elete(2)
#View()
