import psycopg2

def Create_Table():
    cn=psycopg2.connect("dbname='mystore' user='postgres' password='password' host='localhost' port='5432'")
    cr=cn.cursor()
    cr.execute("CREATE TABLE IF NOT EXISTS mystore(item TEXT, quantity INTEGER, price REAL)")
    cn.commit()
    cn.close()

def Insert(item, quantity, price):
    cn=psycopg2.connect("dbname='mystore' user='postgres' password='password' host='localhost' port='5432'")
    cr=cn.cursor()
    cr.execute("INSERT INTO mystore VALUES (%s,%s,%s)", (item, quantity, price))
    cn.commit()
    cn.close()

def View():
    cn=psycopg2.connect("dbname='mystore' user='postgres' password='password' host='localhost' port='5432'")
    cr=cn.cursor()
    cr.execute("SELECT * FROM mystore")
    rows=cr.fetchall()
    cn.close()
    for i in rows:
        print(i)

def Update(quantity, price, item):
    cn=psycopg2.connect("dbname='mystore' user='postgres' password='password' host='localhost' port='5432'")
    cr=cn.cursor()
    cr.execute("UPDATE mystore SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    cn.commit()
    cn.close()

def Delete(item):
    cn=psycopg2.connect("dbname='mystore' user='postgres' password='password' host='localhost' port='5432'")
    cr=cn.cursor()
    cr.execute("DELETE FROM mystore WHERE item=%s", (item,))
    cn.commit()
    cn.close()
