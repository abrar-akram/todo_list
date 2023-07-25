import sqlite3


def insertUsers(firstName,lastName,email):
    conn=sqlite3.connect("users.db")

    c=conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users (
              firstName text,
              lastName text,
              emailId text UNIQUE 
    )""")

    c.execute("INSERT INTO users VALUES (?,?,?)",(firstName,lastName,email))
          
    conn.commit()

    conn.close() 

#showAll()    