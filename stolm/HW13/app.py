import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM tasks WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        task_title = request.form['task_title']
        task_describe = request.form['task_describe']

        if not task_title:
            flash('Title is required!')
        else:
            emoji = ""
            if "buy" in task_title.lower():
                emoji += "🛒"
            else:
                emoji += "📄"
            task_title = emoji+task_title
            conn = get_db_connection()
            conn.execute('INSERT INTO tasks (task_title, task_describe) VALUES (?, ?)',
                         (task_title, task_describe))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    if request.method == 'POST':
        task_title = request.form['task_title']
        task_describe = request.form['task_describe']

        if not task_title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE tasks SET task_title = ?, task_describe = ?'
                         ' WHERE id = ?',
                         (task_title, task_describe, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    task = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(task['task_title']))
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
