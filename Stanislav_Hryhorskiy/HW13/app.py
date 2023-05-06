from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///database_new.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Posts(db.Model):
    """
    Database class containing post information
    (id, creation time, post title, post text)
    """
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.String(19), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created = self.set_created_at()

    @staticmethod
    def set_created_at():
        """
        A function to display the current time
        in the format %Y-%m-%d %H:%M:%S
        """
        time_now = datetime.now()
        current_date_and_time = time_now.strftime("%Y-%m-%d %H:%M:%S")
        return current_date_and_time


@app.route('/')
def index():
    """
    A function that returns a list of all posts
    on the 'index.html' page
    """
    posts = Posts.query.all()
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    """
    A function that returns information about SportBlog
    on the 'about.html' page
    """
    return render_template('about.html')


@app.route('/<int:post_id>')
def post(post_id: int):
    """
    A function that returns information about post
    with id number 'post_id' on the 'post.html' page
    """
    post = Posts.query.get_or_404(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        else:
            post = Posts(title=title, content=content)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id: int):
    post = Posts.query.get_or_404(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            post.title = title
            post.content = content
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id: int):
    post = Posts.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash(f'"{post.title}" was successfully deleted!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
