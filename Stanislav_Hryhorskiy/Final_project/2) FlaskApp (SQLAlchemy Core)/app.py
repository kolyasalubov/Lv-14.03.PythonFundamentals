from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from init_db_new import engine, posts_table
from sqlalchemy import insert, select, update, delete
from datetime import datetime


def get_db_connection():
    conn = engine.connect()
    return conn


def get_post(post_id: int):
    conn = get_db_connection()
    query = select(posts_table).where(posts_table.c.id == post_id)
    post = conn.execute(query).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"


@app.route('/')
def index():
    conn = get_db_connection()
    query = select(posts_table)
    posts = conn.execute(query).fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if not title:
            flash("Title is required!")
        else:
            conn = get_db_connection()
            new_post = {"created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "title": title,
                        "content": content}
            conn.execute(insert(posts_table).values(new_post))
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("create.html")


@app.route("/<int:id>/edit", methods=("GET", "POST"))
def edit(id: int):
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if not title:
            flash("Title is required!")
        else:
            conn = get_db_connection()
            update_post = {"created": datetime.now().strftime("%y-%m-%d %H:%M:%S"),
                           "title": title,
                           "content": content}
            update_statement = update(posts_table).where(posts_table.c.id == id).values(update_post)
            conn.execute(update_statement)
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("edit.html", post=post)


@app.route("/<int:id>/delete", methods=("POST",))
def delete(id: int):
    post = get_post(id)
    conn = get_db_connection()
    delete_statement = delete(posts_table).where(posts_table.c.id == id)
    conn.execute(delete_statement)
    conn.commit()
    conn.close()
    flash(f"{post['title']} was successfully deleted")
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True, port=5003)
