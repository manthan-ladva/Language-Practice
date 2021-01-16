import psycopg2 #---------------------Use "%s" in place of "?". ? is for sqlite3 and %s is for psycopg2.
#------------------ Always pass arguments in single quote ('_')  <~ like this
def Create_Table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def Insert(item, quantity, price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

"""
In view function, It is viewed in python terminal not in database, If Database is connected.
If it is fetchall() function then following example is used

or

If Fetchall() function will not be used then any variable will not be declared for it
Specially in case of not using fetchall function, The database will not be closed. Otherwise Error will generate
{{{{{It is used only for the view of database in python not in SQL}}}}}
"""
def View():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    for i in rows:
        print(i)

def Delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def Update(quantity, price, item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

View()
