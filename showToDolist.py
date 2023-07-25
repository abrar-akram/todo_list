import sqlite3


def showTodoList(email):
    conn=sqlite3.connect("users.db")

    c=conn.cursor()

    c.execute("SELECT rowid,todoItem FROM todoList WHERE emailId = ?",(email,))

    print(c.fetchall())
          
    conn.commit()

    conn.close() 
