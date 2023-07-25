import sqlite3


def insertToDoItem(email,todoItem):
    conn=sqlite3.connect("users.db")

    c=conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS todoList (
              emailId text,
              todoItem text
    )""")

    c.execute("SELECT * FROM users where emailId = ?", (email,)) 

    data=c.fetchall()

    if (len(data)):
        c.execute("INSERT INTO todoList VALUES (?,?)",(email, todoItem))
        print('To do item added')
    else:
        print("Username doesn't exist")

          
    conn.commit()
    conn.close() 

 