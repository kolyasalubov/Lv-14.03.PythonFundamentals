import sqlite3



def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn


def get_all_posts():
    conn = get_db_connection()
    allposts = conn.execute('SELECT * FROM posts',
                        ).fetchall()
    conn.close()
    return allposts

print(get_all_posts())    