import sqlite3

connection = sqlite3.connect('database2.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO datas (password, username) VALUES (?, ?)",
            ('123', 'qweqwe@gmail.com')
            )

connection.commit()
connection.close()
