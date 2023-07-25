import sqlite3


def showAll():
    conn=sqlite3.connect("users.db")

    c=conn.cursor()

    c.execute("SELECT * FROM users")

    print(c.fetchall())
          
    conn.commit()

    conn.close() 

#showAll()    