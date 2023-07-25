import sqlite3


def removeTodoItem(id):
    conn=sqlite3.connect("users.db")

    c=conn.cursor()

    c.execute("DELETE FROM todoList where rowid=?",(id,))

    print('Item with id ',id,' removed')
          
    conn.commit()

    conn.close() 