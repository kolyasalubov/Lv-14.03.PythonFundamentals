from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from init_db import Session, Post
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


def get_db_connection() -> Session:
    """
    Returns a SQLAlchemy session object connected to the database.
    """
    session = Session()
    return session


def get_post(post_id: int) -> Post:
    """
    Returns a blog post with the given ID
    :param post_id: The ID of the blog post to retrieve.
    :return: post (Post):  The blog post object with the given ID.
    :raise:  404 error if the post with the given ID doesn't exist.
    """
    conn = get_db_connection()
    query = conn.query(Post).filter(Post.id == post_id)
    post = query.first()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/')
def index():
    """
    Renders the index page which displays all the posts.
    :return: A template with the index page displaying all the posts.
    """
    conn = get_db_connection()
    query = conn.query(Post)
    posts = query.all()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    """
    Renders the about page.
    :return: A template with the about page.
    """
    return render_template('about.html')


@app.route('/<int:post_id>')
def post(post_id: int):
    """
    Displays a blog post based on the given post_id
    :param post_id: The ID of the blog post to be displayed.
    :return: The HTML content of the blog post page.
    """
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    """
    Renders a form to create a new blog post and handles the submission
    of the form to create the post in the database.
    :return: The HTML content of the blog post page.
    """
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            new_post = Post(created=datetime.now().strftime("%d-%m-%y %H:%M:%S"),
                            title=title,
                            content=content)
            conn.add(new_post)
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id: int):
    """
    Render a form to edit the post with the given ID,
    or update the post if the form is submitted
    :param id: The ID of the post to edit.
    :raise: HTTPException: If no post with the given ID is found.
    :return: A Flask response with the rendered HTML for the edit page.
    """
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            update_post = conn.query(Post).filter_by(id=id).first()
            update_post.created = datetime.now().strftime("%d-%m-%y %H:%M:%S")
            update_post.title = title
            update_post.content = content
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id: int):
    """
    Deletes a post with the given id from the database
    and redirects the user to the homepage
    :param id: The ID of the post to be deleted.
    :return: A redirect response to the homepage.
    """
    post = get_post(id)
    conn = get_db_connection()
    delete_post = conn.query(Post).filter_by(id=id).first()
    conn.delete(delete_post)
    conn.commit()
    conn.close()
    flash(f'"{post.title}" was successfully deleted!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5002)
