import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO tasks (task_title, task_describe) VALUES (?, ?)",
               ('First Task', 'Content for the first task')
               )

cursor.execute("INSERT INTO tasks (task_title, task_describe) VALUES (?, ?)",
               ('Second Task', 'Content for the second task')
               )

connection.commit()
connection.close()
