import sqlite3

class Database:
    def __init__(self): #----------------(__init__) is a constructor which is called by itself
        self.con=sqlite3.connect("books.db")
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, price REAL)")
        self.con.commit()

    def insert(self, title='NULL', author='NULL', year='NULL', price='NULL'):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, price))
        self.con.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        for i in rows:
            z = print(i)
        return rows

    def search(self, title="", author="", year="", price=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR price=?", (title, author, year, price))
        rows=self.cur.fetchall()
        for i in rows:
            z = print(i)
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.con.commit()

    def update(self, id, title, author, year, price):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, price=? WHERE id=?", (title, author, year, price, id))
        self.con.commit()

    def __del__(self):
        self.con.close()

#view()
