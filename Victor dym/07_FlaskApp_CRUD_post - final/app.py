import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import hashlib

def get_db_connection():
    conn = sqlite3.connect('database2.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def decode_hashed_id(hashed_id):
    for i in range(1, 1000):
        test_id = str(i)
        test_hash = hashlib.sha256(test_id.encode()).hexdigest()
        if test_hash == hashed_id:
            return i
    raise ValueError("Invalid hashed_id")

def get_data(data_id):
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM datas WHERE id = ?', (data_id,)).fetchone()
    conn.close()
    if data is None:
        abort(404)
    return data


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')



@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


@app.route('/about')
def about():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('about.html', posts=posts)



@app.route('/register', methods=['GET', 'POST'])
def register():
    conn = get_db_connection()
    datas = conn.execute('SELECT * FROM datas').fetchall()
    conn.close()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO datas (username, password) VALUES (?, ?)',
                         (username, password))
            conn.commit()
            conn.close()
            conn = get_db_connection()
            user = conn.execute('SELECT id FROM datas WHERE username = ? AND password = ?', (username, password)).fetchone()
            conn.close()

            if user is not None:
                hashed_user_id = hashlib.sha256(str(user[0]).encode()).hexdigest()
                return redirect(url_for('user_profile', hashed_id=hashed_user_id))

            else:
                flash('Invalid username or password')

    return render_template('login.html')





@app.route('/user/<string:hashed_id>')
def user_profile(hashed_id):
    user_id = decode_hashed_id(hashed_id)
    user = get_data(user_id)
    return render_template('user.html', user=user)



@app.route('/login', methods=['GET', 'POST'])
def act_login():

    if request.method == 'POST':
        username_login = request.form['username_login']
        password_login = request.form['password_login']

        if not username_login:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            user = conn.execute('SELECT id FROM datas WHERE username = ? AND password = ?',
                                (username_login, password_login)).fetchone()

            conn.close()
            if user != None:
                hashed_user_id = hashlib.sha256(str(user[0]).encode()).hexdigest()
                return redirect(url_for('user_profile', hashed_id=hashed_user_id))
    return render_template('act_login.html')



if __name__ == '__main__':
    app.run(debug=True, port=5001)