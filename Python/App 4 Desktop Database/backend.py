import sqlite3

def create():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, price REAL)")
    con.commit()
    con.close()

def insert(title='NULL', author='NULL', year='NULL', price='NULL'):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, price))
    con.commit()
    con.close()

def view():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()
    for i in rows:
        z = print(i)
    return rows

def search(title="", author="", year="", price=""):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR price=?", (title, author, year, price))
    rows=cur.fetchall()
    con.close()
    for i in rows:
        z = print(i)
    return rows

def delete(id):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()

def update(id, title, author, year, price):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, price=? WHERE id=?", (title, author, year, price, id))
    con.commit()
    con.close()

view()
