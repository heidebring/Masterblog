from flask import Flask, redirect, render_template, request, url_for
from helper import (
    add_new_post,
    delete_blog_post,
    get_post_by_id,
    load_json,
    update_blog_post,
)

app = Flask(__name__)


FILE_PATH = "blog_posts.json"


@app.route("/")
def index():
    """Route for root page with all blog posts"""

    try:
        blog_posts = load_json(FILE_PATH)
    except Exception as error:
        app.logger.exception(f"Error occured: {error}")
        return ("Internal Server Error", 500)
    else:
        return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Route for adding a new blog post"""

    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")
        try:
            add_new_post(title, author, content, FILE_PATH)
            return redirect("/")
        except Exception as error:
            app.logger.exception(f"Error occured: {error}")
            return ("Internal Server Error", 500)
    return render_template("add.html")


@app.route("/delete/<int:post_id>")
def delete(post_id):
    """Route for deleting a post by id"""

    try:
        delete_blog_post(post_id, FILE_PATH)
        return redirect("/")
    except Exception as error:
        app.logger.exception(f"Error occured: {error}")
        return ("Internal Server Error", 500)


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """Route for updating a post by id"""

    try:
        post = get_post_by_id(post_id, FILE_PATH)
        if post is None:
            return "Post not found", 404

        if request.method == "POST":
            title = request.form.get("title")
            author = request.form.get("author")
            content = request.form.get("content")
            update_blog_post(post_id, title, author, content, FILE_PATH)
            return redirect("/")
    except Exception as error:
        app.logger.exception(f"Error occured: {error}")
        return ("Internal Server Error", 500)

    return render_template("update.html", post=post)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
